#!/usr/bin/env python3
"""Siddhidatri 60s cinematic assembly: 13 keyframe segments -> xfade -> 1920x1080@30fps
+ devotional audio bed (tanpura drone, temple bells, whoosh, om-swell, sparkle) + narration/mantra.
"""
import subprocess, os, sys
from imageio_ffmpeg import get_ffmpeg_exe

FF = get_ffmpeg_exe()
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # siddhidatri/
KF = os.path.join(ROOT, "keyframes")
AU = os.path.join(ROOT, "audio")
TMP = os.path.join(ROOT, "build", "segs")
ENDCARD = os.path.join(ROOT, "keyframes", "v12_endcard.png")
OUT_VIDEO = os.path.join(ROOT, "build", "video60.mp4")
OUT_AUDIO = os.path.join(ROOT, "build", "audio60.wav")
OUT_FINAL = os.path.join(ROOT, "siddhidatri_60s.mp4")
os.makedirs(TMP, exist_ok=True)

FPS = 30
XFADE = 0.5
# (image, span_seconds, camera params)
SEGMENTS = [
    ("v00_cosmos.png",           5.0, dict(kind="push", zs=1.00, ze=1.09)),
    ("v01_lotus_opens.png",      5.0, dict(kind="push", zs=1.02, ze=1.13, ybias=0.55)),
    ("v02_face_cu.png",          5.0, dict(kind="push", zs=1.05, ze=1.14)),
    ("v03_darshan_master.png",   3.0, dict(kind="push", zs=1.13, ze=1.01)),   # pull-back reveal
    ("v04_ayudhas.png",          5.0, dict(kind="pan",  z=1.06)),             # L->R arc
    ("v05_lion.png",             4.0, dict(kind="push", zs=1.10, ze=1.00)),   # pull-back
    ("v06_nine_rays.png",        3.0, dict(kind="push", zs=1.00, ze=1.07)),
    ("v07_kailash_shiva.png",    6.0, dict(kind="push", zs=1.02, ze=1.11)),
    ("v08_light_transfer.png",   6.0, dict(kind="push", zs=1.03, ze=1.13, xbias=0.6)),
    ("v09_ardhanarishvara.png",  6.0, dict(kind="push", zs=1.12, ze=1.00)),   # pull-back reveal
    ("v10_blessing.png",         5.0, dict(kind="push", zs=1.00, ze=1.09)),
    ("v11_final_smile.png",      4.0, dict(kind="push", zs=1.03, ze=1.13, ybias=0.45)),
    ("v12_endcard.png",          3.0, dict(kind="push", zs=1.00, ze=1.05)),
]

def render_segment(idx, img, span, cam):
    D = int(round((span + XFADE) * FPS))  # +0.5s pad consumed by the crossfade
    if cam["kind"] == "pan":
        zexpr = f"{cam['z']}"
        xexpr = f"(iw-iw/zoom)*on/{D-1}"
    else:
        zexpr = f"min({cam['zs']}+({cam['ze']}-{cam['zs']})*on/{D-1},{cam['ze']})"
        xb = cam.get("xbias", 0.5)
        xexpr = f"(iw-iw/zoom)*{xb}" if xb != 0.5 else "iw/2-(iw/zoom)/2"
    yb = cam.get("ybias", 0.5)
    yexpr = f"(ih-ih/zoom)*{yb}" if yb != 0.5 else "ih/2-(ih/zoom)/2"
    out = os.path.join(TMP, f"seg{idx:02d}.mp4")
    vf = (f"scale=6000:-2:flags=lanczos,"
          f"zoompan=z='{zexpr}':x='{xexpr}':y='{yexpr}':d={D}:s=1920x1080:fps={FPS},"
          f"format=yuv420p")
    cmd = [FF, "-y", "-i", img, "-filter_complex", vf, "-frames:v", str(D),
           "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-r", str(FPS), out]
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"  seg{idx:02d} {os.path.basename(img)} span={span}s frames={D} ok")
    return out

def concat():
    n = len(SEGMENTS)
    inputs = []
    for i in range(n):
        inputs += ["-i", os.path.join(TMP, f"seg{i:02d}.mp4")]
    fc, prev = [], "[0:v]"
    off = float(int(round((SEGMENTS[0][1] + XFADE) * FPS))) / FPS - XFADE  # = span0
    for i in range(1, n):
        out = f"[x{i}]" if i < n - 1 else "[vout]"
        fc.append(f"{prev}[{i}:v]xfade=transition=fade:duration={XFADE}:offset={off:.3f}{out}")
        prev = out
        off += SEGMENTS[i][1]
    fc.append("[vout]eq=saturation=1.05:contrast=1.02,vignette=angle=PI/6,"
              "fade=t=in:st=0:d=0.8,fade=t=out:st=58.8:d=1.2,format=yuv420p[vf]")
    cmd = [FF, "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[vf]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-r", str(FPS), OUT_VIDEO]
    subprocess.run(cmd, check=True, capture_output=True)
    print("video60.mp4 ok, expected dur = 60.0s")

def audio():
    tanp = ("aevalsrc='0.055*sin(2*PI*110*t)+0.045*sin(2*PI*164.81*t)+0.05*sin(2*PI*220*t)"
            "+0.018*sin(2*PI*277.18*t)+0.03*sin(2*PI*110.5*t)':s=48000:d=60,"
            "lowpass=f=900,aecho=0.55:0.45:90|180:0.25|0.15[drone]")
    bell = ("aevalsrc='"
            "0.40*(gte(t,24))*exp(-2.3*(t-24))*(sin(2*PI*523.25*t)+0.5*sin(2*PI*783.99*t)+0.25*sin(2*PI*1046.5*t))"
            "+0.28*(gte(t,30))*exp(-2.3*(t-30))*(sin(2*PI*659.25*t)+0.5*sin(2*PI*987.77*t))"
            "+0.42*(gte(t,42))*exp(-2.0*(t-42))*(sin(2*PI*523.25*t)+0.6*sin(2*PI*783.99*t)+0.3*sin(2*PI*1318.51*t))"
            "+0.38*(gte(t,57))*exp(-1.6*(t-57))*(sin(2*PI*392*t)+0.5*sin(2*PI*587.33*t))"
            "':s=48000:d=60,bellespace=0.1,aecho=0.6:0.4:120:0.25[bell]" )
    bell = bell.replace("bellespace=0.1,", "")  # keep it simple
    om = ("aevalsrc='0.085*sin(2*PI*136.1*t)+0.05*sin(2*PI*68.3*t)':s=48000:d=60,"
          "afade=t=in:st=41.5:d=2.0,afade=t=out:st=46.5:d=2.2[om]")
    nz = ("anoisesrc=color=pink:sample_rate=48000:amplitude=0.35:d=60,lowpass=f=520,"
          "afade=t=in:st=26.2:d=1.1,afade=t=out:st=28.4:d=1.4,volume=0.30[nz]")
    spark = ("aevalsrc='0.05*sin(2*PI*1567.98*t)*(0.5+0.5*sin(2*PI*7*t))"
             "+0.04*sin(2*PI*2093.0*t)*(0.5+0.5*sin(2*PI*5.3*t))':s=48000:d=60,"
             "afade=t=in:st=26.8:d=1.2,afade=t=out:st=29.0:d=0.9[spark]")
    v1 = f"[1:a]adelay=2500:all=1,volume=1.15[nv1]"
    v2 = f"[2:a]adelay=32000:all=1,volume=1.15[nv2]"
    v3 = f"[3:a]adelay=54400:all=1,volume=1.0[nv3]"
    v4 = f"[4:a]adelay=55500:all=1,volume=0.95[nv4]"
    mix = ("[drone][bell][om][nz][spark][nv1][nv2][nv3][nv4]"
           "amix=inputs=9:duration=longest:normalize=0,alimiter=limit=0.92,"
           "pan=stereo|c0=c0|c1=c0[aout]")
    inputs = ["-i", OUT_VIDEO,
              "-i", os.path.join(AU, "vachan1_hi.mp3"),
              "-i", os.path.join(AU, "vachan2_hi.mp3"),
              "-i", os.path.join(AU, "mantra_stri.mp3"),
              "-i", os.path.join(AU, "mantra_purush.mp3")]
    fc = ";".join([tanp, bell, om, nz, spark, v1, v2, v3, v4, mix])
    subprocess.run([FF, "-y", *inputs, "-filter_complex", fc, "-map", "[aout]",
                    "-c:a", "pcm_s16le", "-ar", "48000", OUT_AUDIO],
                   check=True, capture_output=True)
    print("audio60.wav ok")

def mux():
    subprocess.run([FF, "-y", "-i", OUT_VIDEO, "-i", OUT_AUDIO,
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-movflags", "+faststart", "-shortest", OUT_FINAL],
                   check=True, capture_output=True)
    print("FINAL:", OUT_FINAL)

def endcard():
    """Blurred v11 background + mantra text burned via libass (correct Devanagari shaping)."""
    from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
    src = Image.open(os.path.join(KF, "v11_final_smile.png")).convert("RGB").resize((1920, 1080), Image.LANCZOS)
    bg = src.filter(ImageFilter.GaussianBlur(26))
    bg = ImageEnhance.Brightness(bg).enhance(0.52)
    d = ImageDraw.Draw(bg)
    for y in range(1080):  # gentle bottom darkening
        a = int(110 * max(0, (y - 600)) / 480)
        d.line([(0, y), (1920, y)], fill=(6, 5, 12))
    tmp_bg = os.path.join(TMP, "endcard_bg.png")
    bg.save(tmp_bg)
    ass = os.path.join(ROOT, "build", "endcard.ass")
    subprocess.run([FF, "-y", "-loop", "1", "-i", tmp_bg,
                    "-vf", f"subtitles=filename={ass}:fontsdir={os.path.join(ROOT, 'assets')}",
                    "-t", "3.5", "-r", str(FPS), "-frames:v", "105",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                    os.path.join(TMP, "seg12.mp4")], check=True, capture_output=True)
    print("endcard seg12 ok (libass)")

if __name__ == "__main__":
    steps = sys.argv[1:] or ["endcard", "segments", "concat", "audio", "mux"]
    if "endcard" in steps: endcard()
    if "segments" in steps:
        for i, (img, span, cam) in enumerate(SEGMENTS):
            if img == "v12_endcard.png":
                continue  # seg12 built by endcard() via libass
            render_segment(i, os.path.join(KF, img), span, cam)
    if "concat" in steps: concat()
    if "audio" in steps: audio()
    if "mux" in steps: mux()
