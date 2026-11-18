# hilbert_space_lab — 자와 각도기의 방: 유클리드 공간에서 힐베르트 공간까지

연구실 해설 시리즈. 인턴 시아·모아가 박사가 만든 연구실 복도의 방을 하나씩 통과하며, 데이터를 점으로 놓고 거리·각도·그림자로 인공지능·머신러닝을 읽는 법을 배웁니다. 연구실 스킬(ai-lab-explainer-plain, 낮의 연구실·흰 배경)과 [공간 좌표 해설 제작 지침서](docs/SPACE_COORDINATE_GUIDE.md)를 따릅니다.

- 사이트: https://adminmrobo.github.io/hilbert_space_lab/
- 먼저 보면 좋은 시리즈: [좌표축 위의 그릇 — 3D 지도로 본 모델 최적화](https://adminmrobo.github.io/optimization_3d_map/)
- 글 · 안상선 ((주)M-Robo 대표) · [저자 소개](https://adminmrobo.github.io/who_am_i/who_am_i.html)

| 편 | 파일 | 내용 | 대결 |
|---|---|---|---|
| 목차 | `index.html` | 유클리드 공간 · 힐베르트 공간 | — |
| 유클리드 0편 | `e0_orientation.html` | 가방 점검 — 좌표평면·피타고라스·sin·cos, 그릇 시리즈 화살표 대응표, 마지막 점검 3문항 | — |
| 유클리드 ① | `e1_ruler_rooms.html` | 1 n칸 방(특성 공간) · 2 점과 화살표(임베딩) · 3 거리(KNN) · 4 겹침 점수와 각도(코사인 유사도) · 5 자 세트(원-핫·PCA) | — |
| 유클리드 ② | `e2_shadow_rooms.html` | 6 그림자(예측선 긋기·평균) · 7 칸막이(SVM) · 8 움직임(데이터 늘리기) · 9 공(차원의 저주) · 10 단위 맞추기·호와 현 · 복도 끝의 끝없는 방(힐베르트 예고) | 가장 가까운 이웃 찾기 — 시아(단위 그대로) vs 모아(단위 맞춤) → 모아 승 |
| 힐베르트 ① | `h1_arrow_rooms.html` | 입구 방(유클리드 요약) · 1 세 겹 상자 · 2 곡선의 겹침 점수 · 3 길이·거리·직각 · 4 빈틈 없는 방(√2 구멍, 경사로 → 계단) · 5 세 종류의 방(ℝⁿ·ℓ²·L²) | — |
| 힐베르트 ② | `h2_wave_rooms.html` | 6 자 세트 · 7 그림자 · 8 물결 조각(푸리에, 네모파의 튀어나옴) · 9 피타고라스의 확장(파스발) · 10 쓰이는 곳(커널 방 실험) | 곡선 맞히기 — 시아(낮은 물결부터) vs 모아(큰 조각부터) → 모아 승 (3 : 7조각) |

모든 페이지는 단일 HTML(외부 요청은 글꼴 하나)이고, 끝에 지식 색인(`#kg`)과 온톨로지·서지 꾸러미(`#export`)가 있습니다.

## 바탕 자료와 저작권
- eeanimation 인포그래픽 「EUCLIDEAN SPACE 01~10」, 「HILBERT SPACE 01~10」 — 사용자가 제공한 자료입니다. 원본 그림은 이 저장소에 넣지 않았고, 도표는 구도·좌표만 따라 모두 새로 그렸습니다. 원 게시물 주소·게시일은 아직 받지 못해 "미확인"으로 적었습니다.
- 교육부 고등학교 수학·기하 교육과정(단원 이름 대조), Mikolov 외(2013), Cortes·Vapnik(1995), Bellman(1961), Kreyszig(1978), Schölkopf·Smola(2002), Vaswani 외(2017).
- 캐릭터 이름·설정·그림은 저작권자 안상선의 허락 없이 사용할 수 없습니다.

## 폴더
```
.
├─ index.html · e0~e2 (유클리드) · h1_arrow_rooms.html · h2_wave_rooms.html (힐베르트)   완성 페이지 (build/에서 만듦)
├─ build/
│  ├─ idx·e0·e1·e2·h1·h2 .src.html   페이지 원본
│  ├─ common.css · common.js   공용 디자인·모듈 (optimization_3d_map에서 가져와 방 짜임 추가)
│  ├─ plane.js                 2D 좌표평면 도우미 (점 끌기)
│  ├─ geo.js                   유클리드 계산 모듈 (거리·내적·그림자·칸막이·껍질 비율·대결 데이터)
│  ├─ hgeo.js                  힐베르트 계산 모듈 (곡선 내적·경사로·급수·푸리에·파스발·커널·대결)
│  ├─ kg_defs.py → kg_*/refs_*/meta_*.json   지식 색인·서지 정의
│  ├─ kgx.js · backbone.json · sprites96.js   꾸러미 모듈·AI 영역 뼈대·캐릭터 그림
│  └─ build.js                 조립: node build/build.js
├─ code/
│  ├─ check_euclid.js          유클리드 숫자 검산 (node code/check_euclid.js)
│  ├─ check_hilbert.js         힐베르트 숫자 검산 (node code/check_hilbert.js)
│  └─ shot.py                  화면 점검 390·1280px (python3 code/shot.py 파일 390 1280)
└─ docs/
   ├─ SPACE_COORDINATE_GUIDE.md   공간 좌표 해설 제작 지침서 (범용)
   ├─ PLAN_euclidean_space.md     유클리드 편 기획·제작 기록
   ├─ PLAN_hilbert_space.md       힐베르트 편 기획안 v1.4
   └─ COVER_PROMPTS.md            표지 그림 지시문 (유클리드·힐베르트)
```
다시 만들기: `python3 build/kg_defs.py && node build/build.js && node code/check_euclid.js && node code/check_hilbert.js`
