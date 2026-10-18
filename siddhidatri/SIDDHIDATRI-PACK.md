# सिद्धिदात्री — "आदिशक्ति का प्राकट्य"
### ६०-सेकंड सिनेमाई मास्टर + ३०+३० दो-भाग संस्करण — शूट-रेडी प्रोडक्शन पैक

**लॉगलाइन:** जब ब्रह्मांड मौन हो जाता है, तब बंद कमल से सिद्धिदात्री प्रकट होती हैं — चक्र, गदा, शंख और कमल धारण किए — और कैलाश पर ध्यानमग्न शिव को सिद्धि देकर अर्धनारीश्वर का रहस्य पूर्ण करती हैं; अंत में कृपा समूची पृथ्वी पर उतरती है।

**नोट:** सिद्धिदात्री का एक समान मानवीय जीवनचरित ग्रंथों में नहीं मिलता — इसलिए यह प्रस्तुति पुराणिक महिमा, नवदुर्गा परंपरा और लोकप्रिय अर्धनारीश्वर कथा पर आधारित **प्रतीकात्मक, श्रद्धापूर्ण** चित्रण है। शिव को सिद्धि-प्रदान की कथा बिना किसी हिंसा/विस्फोट के, शांत प्रकाश-प्रवाह के रूप में दिखाई गई है।

---

## तैयार डिलिवरेबल्स (इसी फ़ोल्डर में)

| फ़ाइल | विवरण |
|---|---|
| `siddhidatri_60s.mp4` | **मास्टर** — 1920×1080, 30fps, 60.18s, पूर्ण ऑडियो (वाचन+मंत्र+संगीत) |
| `part1_0-30s.mp4` | वीडियो १ — "आदिशक्ति का प्राकट्य" (0–30s, गोल्डन-फ़ेड आउट) |
| `part2_30-60s.mp4` | वीडियो २ — "सिद्धि, करुणा और अर्धनारीश्वर" (30–60s, फ़ेड-इन) |
| `keyframes/v00…v12` | १३ कीफ़्रेम — image-to-video स्टार्ट-फ़्रेम के रूप में प्रयोग करें |
| `audio/vachan1_hi.mp3` | वाचन १ (स्त्री-स्वर, 13.8s) |
| `audio/vachan2_hi.mp3` | वाचन २ (स्त्री-स्वर, 16.6s) |
| `audio/mantra_stri.mp3` / `mantra_purush.mp3` | अंतिम मंत्र — दो स्वर (मक्स में 0.9s ऑफ़सेट से संयुक्त-प्रतिध्वनि) |
| `build/build_siddhidatri.py` | पूरा रेंडर पाइपलाइन (ffmpeg) — दोबारा बनाने हेतु |

**निरंतरता:** सभी कीफ़्रेम एक ही "मास्टर दर्शन" (`v03`) से एडिट-श्रृंखला द्वारा बने हैं — चेहरा, मुकुट, सिंदूर, लाल-सुनहरी साड़ी, चार भुजाएँ, चक्र-गदा-शंख-कमल, हर दृश्य में समान।

---

## निर्मित समय-रेखा (मास्टर, वास्तविक)

| समय | दृश्य | कीफ़्रेम | कैमरा |
|---|---|---|---|
| 0–5s | अंधकार से ब्रह्मांड; बंद महाकमल | `v00_cosmos` | धीमा push-in |
| 5–10s | पंखुड़ियाँ खुलें; स्वर्ण-प्रकाश से प्राकट्य (चरण→साड़ी→आसन→चेहरा) | `v01_lotus_opens` | push-in |
| 10–15s | चेहरा क्लोज़अप — वास्तविक त्वचा, जीवंत आँखें | `v02_face_cu` | push-in |
| 15–18s | पूर्ण दर्शन — pull-back reveal | `v03_darshan_master` | zoom-out |
| 18–23s | चतुर्भुज-आयुध चाप (चक्र-गदा-शंख-कमल) | `v04_ayudhas` | L→R ऑर्बिट-पैन |
| 23–27s | शांत गरिमामय सिंह, हिमालय | `v05_lion` | pull-back |
| 27–30s | दृष्टि कैमरे की ओर; **नौ किरणें** | `v06_nine_rays` | push-in, गोल्डन होल्ड |
| 30–36s | वही आसन, किरणें धड़कती → कैलाश रूपांतरण; ध्यानमग्न शिव | `v07_kailash_shiva` | push-in |
| 36–42s | कमल से हृदय तक करुणा-प्रकाश प्रवाह | `v08_light_transfer` | push (शिव-पक्ष) |
| 42–48s | स्वर्ण-नील मंडल; **अर्धनारीश्वर** प्रतीकात्मक प्रकट्य | `v09_ardhanarishvara` | pull-back reveal |
| 48–53s | आशीर्वाद मुद्रा; साधक-परिवार, कृपा-प्रकाश | `v10_blessing` | push-in |
| 53–57s | अंतिम शांत मुस्कान; विशाल खिले कमल | `v11_final_smile` | push-in |
| 57–60s | मंत्र-कार्ड: **ॐ देवी सिद्धिदात्र्यै नमः** | `v12` (libass) | स्थिर, गोल्डन फ़ेड |

**ऑडियो मैप:** तानपुरा-ड्रोन (A2/E/A) पूरे 60s · वाचन १ @ 2.5s · शंख-स्पर्श घंटी @ 24s · वायु-संक्रमण @ 26–30s (कैलाश बदलाव) · झंकार @ 30s · "ॐ" सुर-तरंग (136.1Hz) @ 41.5–48.7s (अर्धनारीश्वर) · महाघंटी @ 42s · वाचन २ @ 32s · मंत्र (स्त्री+पुरुष प्रतिध्वनि) @ 54.4s · अंतिम घंटी @ 57s · फ़ेड 58.8–60s

---

## जनरेशन प्रॉम्प्ट — 4 क्लिप (Veo / Sora / Kling / Runway)

हर क्लिप के आरंभ में यह **कैरेक्टर-ब्लॉक** शब्दशः जोड़ें:

> **Character block (constant):** Devi Siddhidatri — serene, compassionate, radiant HUMAN face, ultra-realistic skin with visible pores and natural texture (never plastic, waxy or glossy), large calm dark eyes, long deep-black gently wavy hair, red sindoor and ornate golden crown, rich red-and-gold silk saree, EXACTLY FOUR arms holding a golden chakra, a golden mace, a white conch and a fully bloomed pink lotus, seated in padmasana on a giant pink lotus, soft golden halo, calm dignified lion. Indian temple architecture, starry Himalayan sky, drifting lotus petals, warm golden volumetric light, ultra-realistic cinematic film, slow dignified motion, no text, no watermark.

**Clip A (0–15s, `v00` से `v02`):** Total darkness; a deep-blue star-filled cosmos fades in with slow galaxies and golden light particles. Camera drifts slowly toward ONE vast closed pink lotus on dark mirror-calm water. Petals slowly unfurl; soft golden light blooms from within; the goddess manifests through the glow — feet first, red silk, lotus seat, four arms, finally her serene human face. Cut closer: extreme close-up of her face, real skin texture, living eyes, deep maternal peace.

**Clip B (15–30s, `v03` से `v06`):** Slow pull-back from her face reveals the full darshan — lotus throne, halo, temple pillars, misty Himalayan peaks. The camera glides in a gentle arc across her four hands: spinning chakra radiating mild light, golden mace, nacre conch, dewy pink lotus. Behind her a golden lion appears, calm and dignified, never aggressive, golden dust and petals floating. She slowly raises her gaze to camera; nine soft golden beams fan out behind her; the scene settles into still golden light.

**Clip C (30–45s, `v07`–`v08`):** Continuity from the same throne: the nine rays pulse gently; the environment transforms into snow-clad Mount Kailash before dawn — blue sky, light mist, drifting snowflakes. Lord Shiva sits motionless in meditation before her, ash-smeared, crescent moon in his jata hair, serene ascetic presence. Her compassionate gaze falls on him; from the pink lotus in her hand a soft golden-pink stream of light flows quietly into his heart — a peaceful, symbolic bestowal of siddhi. No violence, no explosion; only calm light.

**Clip D (45–60s, `v09` से `v12`):** A balanced mandala of intertwined golden and deep-blue light forms around them; the two luminous figures gently merge into ONE symbolic Ardhanarishvara — left half goddess (sindoor, crown-half, red-gold silk, pink lotus), right half Shiva (matted locks, crescent, ash, rudraksha), exactly TWO arms, anatomically natural, classical and dignified. Return to Siddhidatri raising her palm in blessing; below, tiny vignettes of devotees meditating at dawn as golden grace spreads over them. Final close-up: her gentle smile, many giant lotuses blooming on dark sacred water, the frame dissolving into warm gold. End on a dark golden card: "ॐ देवी सिद्धिदात्र्यै नमः" (correct Devanagari rendering only).

**Negative block (हर क्लिप में जोड़ें):**
> deformed face, more or fewer than four arms, extra fingers, unnatural anatomy, plastic or waxy or glossy skin, cartoon, doll face, horror, anger, violence, blood, battle, modern clothes, western fantasy outfit, wrong religious symbols, blurry hands, shifting face, changing crown, changing saree colour, objects swapping between hands, aggressive lion, flashy explosions, fast camera shakes, sudden cuts, text, watermark, garbled Devanagari, disrespectful gestures

**फ़ॉलबैक सीढ़ी (क्रम से हटाएँ, केवल विफल क्लिप दोबारा बनाएँ):**
① चतुर्भुज विफल → दो-भुजा रूप (केवल कमल+अभय) ② सिंह विफल → कुहासा + दूर की आकृति/केवल श्वास-ध्वनि ③ अर्धनारीश्वर विफल → दोनों आकृतियों के प्रकाश-मंडल एक-दूसरे में घुलते (विलय-प्रतीक, आकृति नहीं) ④ शिव का चेहरा विफल → पीठ/प्रोफ़ाइल + त्रिशूल-चंद्र रेखा केवल सिल्हूट में।

---

## संगीत (Suno — जैसा-वैसा पेस्ट करें)

> Cinematic devotional ambient, 60 seconds, no lyrics. Deep tanpura drone on A, distant conch-like soft horn at 24s, delicate temple bells, subtle veena phrases, airy shimmer. Structure: warm drone 0–6s, gentle bloom 6–10s, serene peak 10–15s, flowing strings 15–27s, wind transition 27–30s, colder Kailash palette 30–36s, warm light stream 36–42s, big soft bell + Om-like low drone swell 42–48s, blessing warmth 48–53s, tender resolution 53–57s, single deep bell and fade 57–60s. Emotional arc: mystery → revelation → compassion → union → grace. Not EDM, no beat drops, no chanting of names.

(इस रेंडर में संगीत ffmpeg-संश्लेषित है: तानपुरा-ड्रोन, घंटी-विसर्जन, "ॐ"-सुर, हवा-संक्रमण। Suno ट्रैक मिलने पर `build/build_siddhidatri.py` के audio() में बदलें।)

---

## स्थानीय पुनः-रेंडर

```bash
cd siddhidatri/build
pip install imageio-ffmpeg pillow   # एक बार
python3 build_siddhidatri.py        # endcard → segments → concat → audio → mux
```

---

## पोस्टिंग पैक

- **थंबनेल:** `keyframes/v06_nine_rays.png` (नौ किरणें + सीधा दर्शन) — या `v02_face_cu.png` चेहरा-क्लोज़। ≤3 शब्द: **"सिद्धियाँ की सिद्धि"**
- **शीर्षक:** सिद्धिदात्री माता: जब ब्रह्मांड मौन हुआ | नवरात्रि नौवाँ दिन 🙏 | 60 सेकंड में दिव्य दर्शन
- **कैप्शन हुक:** "ब्रह्मांड की हर शक्ति मौन थी… तब खुला वह कमल, जिसमें सिद्धियाँ बसती हैं। शिव को सिद्धि देने वाली — माँ सिद्धिदात्री। नवरात्रि नौवाँ दिन 🌺 कमेंट में लिखें: ॐ देवी सिद्धिदात्र्यै नमः"
- **पिन कमेंट:** "माता के चारों हाथों का अर्थ जानते हैं? चक्र, गदा, शंख, कमल — चारों मिलकर 'पूर्णता' बनते हैं। आपका पसंदीदा कौन-सा? 🪷"
- **अवधि:** नवमी सुबह 5–7 बजे IST। 16:9 पोस्ट करें, 9:16 के लिए केंद्र 56% सुरक्षित रखें (दोनों 30s भाग Reels/Shorts के लिए तैयार हैं)।
- **लूप-ट्रिक:** Reels पर part2 का अंत (गोल्डन फ़ेड) → part1 का आरंभ (अंधकार से तारे) — अगले नवरात्र में पुनःप्रसारण हेतु लूप।

---

## शास्त्रीय संदर्भ (साइट/विवरण हेतु)

नवदुर्गा का नौवाँ स्वरूप; चतुर्भुज — चक्र, गदा, शंख, कमल; कमलासन; कुछ परंपराओं में सिंह-वाहन; शिव को सिद्धियाँ प्रदान कर अर्धनारीश्वर रूप की लोकप्रिय कथा। सभी दृश्य श्रद्धापूर्ण प्रतीकात्मक चित्रण — कोई मानवीय जीवनचरित दावा नहीं।
