# socialking600

## SIDDHIDATRI — आदिशक्ति का प्राकट्य (Navratri Day 9)

A 60-second cinematic devotional AI-film: the universe falls silent, a closed cosmic lotus opens, Devi Siddhidatri manifests (four arms: chakra, gada, shankha, pink lotus), bestows siddhi on a meditating Shiva at Kailash — the Ardhanarishvara mystery — and her grace spreads over devotees. Ends on the mantra "ॐ देवी सिद्धिदात्र्यै नमः".

**Thesis:** No biopic — a reverent, symbolic presentation of her puranic mahima, built on strict character continuity (one master-darshan keyframe seeds every shot; skin, saree, crown, four arms and objects stay identical throughout).

- **`siddhidatri/siddhidatri_60s.mp4`** — the 60s master (1920×1080@30, Hindi narration + mantra + tanpura/bells score)
- **`siddhidatri/part1_0-30s.mp4`** · **`siddhidatri/part2_30-60s.mp4`** — the two-part 30s+30s cut
- **`siddhidatri/keyframes/`** — 13 continuity keyframes (image-to-video start frames)
- **`siddhidatri/audio/`** — narration + separate female/male mantra voices
- **`siddhidatri/SIDDHIDATRI-PACK.md`** — full production pack: shot timeline, audio map, copy-paste Veo/Sora/Kling prompts, negative block, fallback ladder, Suno prompt, posting pack
- **`siddhidatri/build/build_siddhidatri.py`** — full ffmpeg pipeline to re-render everything

## MAHAGAURI — The Stillness That Moved a River

My director's version of the Mata Mahagauri story: a 60-second cinematic AI-film treatment, built as a response/alternative to a spectacle-first cut.

**Thesis:** Her stillness is the action. The camera learns tapas (locked-off for 30s), the river asks her permission (a drop that doesn't land = Peak 2), and the bull kneels to her (she ends by blessing the audience — the loop).

- **`index.html`** — the full interactive treatment site: myth kernel, 3 directorial reversals, Your Cut vs My Cut, 4 keyframes, clickable peak timeline, 13-shot list, re-hook ladder, copy-paste generation prompts (4 × ~15s clips), Suno music map, 90s/3-min expansion, posting pack.
- **`PRODUCTION-PACK.md`** — the offline shoot sheet (shot list, fallback ladder, Suno prompt, posting copy).
- **`images/`** — 4 keyframes to use as image-to-video start frames:
  `keyframe-01-tapas.jpg` · `keyframe-02-river-waits.jpg` · `keyframe-03-mahagauri.jpg` · `keyframe-04-bull-kneels.jpg`

Open `index.html` in any browser, or serve: `python3 -m http.server 8080 --bind 0.0.0.0`
