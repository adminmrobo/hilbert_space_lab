# 표지 그림 지시문 — 힐베르트 공간 시리즈 (픽셀풍)

> 기준: 연구실 스킬 18-9·18-14 — 공통 스타일 *16-bit RPG style pixel art* (애니메 일러스트 아님). 캐릭터 고정 외형은 캐릭터 팩 CHAR_lab4 18-4의 영어 묘사를 그대로 씀. 시아·모아가 메인이라 네 식구에 두 인턴을 더해 여섯이 등장.
> 지난판(애니메풍 지시문)은 지침 위반이라 폐기함. 유클리드 편 표지는 euclidean_space_lab 저장소의 IMAGE_PROMPTS.md가 기준이며, 그쪽도 같은 픽셀풍으로 고쳐야 함.

**참고 이미지 (함께 올리기):** 네 식구 기본 그림 4장 + 시아·모아 기본 그림 2장 (GitHub `adminmrobo/fruitfly-lab-expressions`, 여섯 식구 단체 사진 `images/_sheets/lab6_lineup.png`). 목차 표지를 먼저 받아 그림체를 확인한 뒤 나머지에 함께 올린다.
**받은 뒤:** 1600×900 WebP(220KB 이하)로 줄여 `img/{키}.webp`에 넣고, 페이지의 그림판 표지(`data-img`)를 교체, og:image 추가.

## cover_index — index.html — 시리즈 목차

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_index · L (16:9, 1920 이상) |
| 주제 은유 | 끝없이 이어지는 흰 연구실 복도, 번호 없는 문들이 빛 속으로 사라짐 |
| 대체 글 (alt) | 하얀 복도 끝까지 늘어선 문 앞에서 시아와 모아가 출발하고, 네 식구가 배웅하는 표지 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 16비트 RPG 픽셀아트 그림체(굵은 외곽선, 2~3단 명암)로, 첨부한 참고 이미지의 여섯 캐릭터(박사, 조수, 초파리 연구원, 주판봇, 인턴 시아, 인턴 모아)를 같은 외형으로, 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a long bright white laboratory corridor whose rows of doors fade into soft white light at the far end, faint floor grid lines running toward the vanishing point.
All six characters together:
  the doctor (chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie), standing in the middle, one arm raised toward the far end of the corridor;
  the assistant (girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans), beside him holding a clipboard, smiling;
  the fruit fly researcher (anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings), on the left facing right, peeking through a magnifier at the floor grid;
  the abacus robot (boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus), on the right facing left, sliding abacus beads with excitement;
  the black-haired intern (calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron), in front, holding a large transparent ruler, looking down the corridor;
  the beige-haired intern (gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt), in front, holding a protractor and a notebook, smiling.
Visual metaphor of the topic: glowing arrows on the floor that turn into a smooth wave as they go deeper down the corridor.
Composition: the two interns in the center foreground; keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the floor grid where the arrows turn into a wave.
Mood: curious, friendly, the moment before the discovery.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same six characters, same pixel art style and composition. Change only: {고칠 점}. Still no text.`

## cover_h1 — h1_arrow_rooms.html — ① 화살표의 방

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_h1 · L (16:9, 1920 이상) |
| 주제 은유 | 곡선 두 개가 공중에서 겹치고 겹친 부분이 빛남 |
| 대체 글 (alt) | 끝없는 방에서 두 곡선을 겹쳐 보는 시아·모아 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 16비트 RPG 픽셀아트 그림체(굵은 외곽선, 2~3단 명암)로, 첨부한 참고 이미지의 여섯 캐릭터(박사, 조수, 초파리 연구원, 주판봇, 인턴 시아, 인턴 모아)를 같은 외형으로, 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a bright white lab room that seems to extend endlessly, faint grid lines fading into white light.
All six characters together:
  the doctor (chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie), on the right of center pointing at the overlap with a small purple sparkle in his hand;
  the assistant (girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans), looking amazed, notebook in hand;
  the fruit fly researcher (anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings), on the left facing right, holding a measuring tape;
  the abacus robot (boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus), on the right facing left, screen eyes wide with surprise;
  the black-haired intern (calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron), pointing at where the two curves overlap;
  the beige-haired intern (gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt), writing in a notebook that shows small dots lining up toward one point.
Visual metaphor of the topic: two smooth glowing curves (one blue, one teal) floating in the air and overlapping, the overlapping area softly shaded orange; a row of small dots approaching one bright point.
Composition: the two interns in the center foreground; keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the overlapping area of the two curves.
Mood: curious, friendly, the moment before the discovery.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same six characters, same pixel art style and composition. Change only: {고칠 점}. Still no text.`

## cover_h2 — h2_wave_rooms.html — ② 곡선을 쪼개는 방

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_h2 · L (16:9, 1920 이상) |
| 주제 은유 | 곡선 하나가 여러 가는 물결 빛줄기로 나뉨, 옆에 세기 막대 |
| 대체 글 (alt) | 큰 투명 판 위 곡선이 물결 조각들로 갈라지고, 시아·모아가 조각을 고르는 대결 직전 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 16비트 RPG 픽셀아트 그림체(굵은 외곽선, 2~3단 명암)로, 첨부한 참고 이미지의 여섯 캐릭터(박사, 조수, 초파리 연구원, 주판봇, 인턴 시아, 인턴 모아)를 같은 외형으로, 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a white lab room with a large transparent board standing in the center.
All six characters together:
  the doctor (chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie), standing behind the board like a host;
  the assistant (girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans), in the middle raising a small referee flag;
  the fruit fly researcher (anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings), on the left facing right, cheering from the audience side;
  the abacus robot (boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus), on the right facing left, counting bars on its abacus;
  the black-haired intern (calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron), stacking thin waves in order from the smallest;
  the beige-haired intern (gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt), holding a magnifier over the tallest bar.
Visual metaphor of the topic: one wavy teal curve on the board splitting into several thin colored sine waves like layers of light, with a small bar chart of wave strengths beside it.
Composition: the two interns in the center foreground; keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the tallest bar of the bar chart.
Mood: curious, friendly, the moment before the discovery.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same six characters, same pixel art style and composition. Change only: {고칠 점}. Still no text.`

## cover_h3 — h3_practice_rooms.html — ③ 실전, 네 개의 작업실

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_h3 · L (16:9, 1920 이상) |
| 주제 은유 | 네 작업실 문(물결, 기울어진 화살표, 그림자, 휘어진 곡선) |
| 대체 글 (alt) | 출장 가방을 든 시아·모아가 작업실 네 곳의 문 앞에 선 장면 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 16비트 RPG 픽셀아트 그림체(굵은 외곽선, 2~3단 명암)로, 첨부한 참고 이미지의 여섯 캐릭터(박사, 조수, 초파리 연구원, 주판봇, 인턴 시아, 인턴 모아)를 같은 외형으로, 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a bright white hallway with four small workshop doors side by side, each door decorated with a simple glowing symbol: a sound wave, a tilted arrow inside a quarter circle, an arrow casting a shadow onto a floor, and a smooth U-shaped curve through dots.
All six characters together:
  the doctor (chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie), handing over a small travel map;
  the assistant (girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans), waving goodbye with a smile;
  the fruit fly researcher (anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings), on the left facing right, carrying a small toolbox;
  the abacus robot (boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus), on the right facing left, wearing a tiny travel cap;
  the black-haired intern (calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron), holding a small suitcase, looking at the first door;
  the beige-haired intern (gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt), holding a checklist, pointing at the fourth door.
Visual metaphor of the topic: four doors, four ways the same light ray is used.
Composition: the two interns in the center foreground; keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the four door symbols.
Mood: curious, friendly, the moment before the discovery.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same six characters, same pixel art style and composition. Change only: {고칠 점}. Still no text.`
