# 지식 그래프·참고문헌·페이지 서지 정의 → kg_{n}.json / refs_{n}.json / meta_{n}.json
# python3 build/kg_defs.py  (ai-lab-explainer v1.14 O1·O2 형식, optimization_3d_map/build/kg_defs.py와 같은 짜임)
import json, os
B = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://adminmrobo.github.io/hilbert_space_lab/'
DATE = '2026-11-19'

def N(id, type, ko, en, page, anchor, level=1, df=None, fam='representation'):
    n = {"id": id, "type": type, "label": {"ko": ko, "en": en}, "page": page, "anchor": anchor, "level": level,
         "status": "known", "confidence": "high", "coverage": "explained", "family": fam, "domain": ["ai"], "match": []}
    if df: n["definition"] = {"ko": df}
    return n
def E(s, p, o, anchor='#sum'):
    return {"s": s, "p": "lab:" + p, "o": o, "anchor": anchor, "confidence": "high"}

EEA = {"id": "eea_euclid", "type": "graphic", "title": "EUCLIDEAN SPACE 01~10", "author": [{"literal": "eeanimation"}],
       "accessed": {"date-parts": [[2026, 11, 19]]},
       "lab": {"work": "lab:work/eea_euclid", "role": "background", "supports": [], "locs": [],
               "verified": {"title": True, "author": True, "year": False, "url": False},
               "checkedBy": "사용자 제공 이미지에서 옮김. 원 게시물 주소·게시일은 받지 못함",
               "note": "카드 구성과 도표 좌표만 따르고 그림은 새로 그림"}}
CURR = {"id": "moe_curriculum", "type": "report", "title": "고등학교 수학·기하 교육과정", "author": [{"literal": "교육부"}],
        "lab": {"work": "lab:work/moe_curriculum", "role": "background", "supports": [], "locs": [],
                "verified": {"title": True, "author": True, "year": False, "url": False}, "checkedBy": "교과 단원 이름 대조"}}
def ref(id, title, authors, year, extra=None, supports=None):
    r = {"id": id, "type": "article-journal", "title": title, "author": authors, "issued": {"date-parts": [[year]]},
         "lab": {"work": "lab:work/" + id, "role": "background", "supports": supports or [], "locs": [],
                 "verified": {"title": True, "author": True, "year": True, "url": False}, "checkedBy": DATE}}
    if extra: r.update(extra)
    return r

def meta(n, title, num, url, about, based):
    return {"title": title, "series": "유클리드 공간 · 힐베르트 공간", "number": num,
            "creator": [{"name": "안상선", "role": "author", "affiliation": "(주)M-Robo"}],
            "contributor": [{"name": "AI 보조 제작", "role": "assistant"}], "date": DATE, "version": "1.0", "language": ["ko"],
            "license": "", "url": SITE + url, "about": about, "basedOn": based, "educationalLevel": "입문",
            "learningResourceType": "interactive explainer", "registry": "KG_00_registry 0.2",
            "suggestedCitation": "안상선 (2026). " + title + ". 유클리드 공간 · 힐베르트 공간 " + num + ", v1.0."}

# ── e0 오리엔테이션 ──
P = 'e0_orientation'
e0n = [N('lab:concept/coordinate-plane', 'Concept', '좌표평면', 'Coordinate plane', P, '#bag1', 1, '가로·세로 두 축으로 점의 자리를 숫자 두 개로 적는 평면.', 'math'),
       N('lab:concept/pythagorean-theorem', 'Concept', '피타고라스 정리', 'Pythagorean theorem', P, '#bag2', 1, '직각삼각형에서 빗변² = 가로² + 세로².', 'math'),
       N('lab:concept/sine-cosine', 'Concept', 'sin·cos', 'Sine and cosine', P, '#bag3', 1, '단위원 위 점의 세로·가로 좌표. 각도를 길이로 바꾼다.', 'math'),
       N('lab:sim/e0-bag', 'Simulation', '가방 점검 실험 세 개', 'Bag check experiments', P, '#bag', 2),
       N('lab:question/e0-ready', 'Question', '자와 각도기의 방에 들어갈 준비가 됐나?', 'Ready for the ruler rooms?', P, '#top', 1)]
e0e = [E('lab:concept/pythagorean-theorem', 'prerequisiteOf', 'lab:concept/euclidean-distance'),
       E('lab:concept/sine-cosine', 'prerequisiteOf', 'lab:concept/inner-product'),
       E('lab:concept/coordinate-plane', 'prerequisiteOf', 'lab:concept/euclidean-space'),
       E('lab:sim/e0-bag', 'demonstratedBy', 'lab:concept/pythagorean-theorem'),
       E('lab:concept/coordinate-plane', 'broader', 'lab:topic/linear-algebra')]
# ── e1 자와 각도기의 방 ──
P = 'e1_ruler_rooms'
e1n = [N('lab:concept/euclidean-space', 'Concept', '유클리드 공간 ℝⁿ', 'Euclidean space', P, '#r1', 1, '숫자 n개로 주소를 적고, 곧은 자와 각도기로 거리·각도를 재는 방.'),
       N('lab:concept/feature-space', 'Concept', '특성 공간', 'Feature space', P, '#r1', 1, '데이터 표의 열을 축으로 삼은 방. 한 행이 점 하나.'),
       N('lab:concept/vector', 'Concept', '화살표(벡터)', 'Vector', P, '#r2', 1, '두 점의 차이. 길이와 방향만 가진 이동.'),
       N('lab:concept/euclidean-distance', 'Concept', '거리', 'Euclidean distance', P, '#r3', 1, '칸마다 차이를 제곱해 더한 뒤 제곱근.'),
       N('lab:concept/inner-product', 'Concept', '겹침 점수(내적)', 'Inner product', P, '#r4', 1, '같은 자리 숫자끼리 곱해서 더한 값. 길이 × 길이 × cos θ.'),
       N('lab:concept/cosine-similarity', 'Concept', '코사인 유사도', 'Cosine similarity', P, '#r4', 1, '겹침 점수를 두 길이로 나눈 값. 1이면 같은 쪽, 0이면 직각.'),
       N('lab:concept/orthonormal-basis', 'Concept', '자 세트(정규직교기저)', 'Orthonormal basis', P, '#r5', 2, '길이 1이고 서로 직각인 자들. 좌표 = 겹침 점수.'),
       N('lab:method/knn', 'Method', '가장 가까운 이웃 찾기(KNN)', 'k-nearest neighbors', P, '#r3', 1, '거리로 가장 가까운 이웃을 골라 답을 정한다.'),
       N('lab:method/one-hot', 'Method', '원-핫 인코딩', 'One-hot encoding', P, '#r5', 1),
       N('lab:claim/distance-any-dim', 'Claim', '칸이 몇 개든 거리 식은 같다(항만 늘어난다)', 'Distance formula holds in any dimension', P, '#r1', 1),
       N('lab:claim/rotation-keeps-length', 'Claim', '자 세트를 돌려도 길이는 그대로', 'Rotating the basis preserves length', P, '#r5', 2),
       N('lab:analogy/table-row-point', 'Analogy', '표의 한 줄 = 방 안의 점 하나', 'Table row as a point', P, '#r1', 1),
       N('lab:analogy/street-vs-straight', 'Analogy', '골목길 거리와 직선거리', 'Street distance vs straight line', P, '#r3', 1),
       N('lab:analogy/taste-table', 'Analogy', '두 사람의 취향표', 'Two taste profiles', P, '#r4', 1),
       N('lab:limitation/angle-drops-size', 'Limitation', '각도는 크기를 버린다', 'Angle ignores magnitude', P, '#r4', 2),
       N('lab:sim/e1-dims', 'Simulation', '칸 수 늘리기 실험', 'Adding dimensions', P, '#r1', 2),
       N('lab:sim/e1-angle', 'Simulation', '겹침 점수와 각도 실험', 'Dot product and angle', P, '#r4', 2),
       N('lab:sim/e1-basis', 'Simulation', '자 세트 돌리기 실험', 'Rotating the basis', P, '#r5', 2),
       N('lab:work/eea_euclid', 'Work', 'eeanimation — EUCLIDEAN SPACE 01~10', 'eeanimation — Euclidean Space', P, '#top', 1)]
e1e = [E('lab:concept/feature-space', 'broader', 'lab:concept/euclidean-space', '#r1'),
       E('lab:concept/euclidean-distance', 'partOf', 'lab:concept/euclidean-space', '#r3'),
       E('lab:concept/inner-product', 'partOf', 'lab:concept/euclidean-space', '#r4'),
       E('lab:concept/cosine-similarity', 'derivedFrom', 'lab:concept/inner-product', '#r4'),
       E('lab:concept/vector', 'prerequisiteOf', 'lab:concept/euclidean-distance', '#r2'),
       E('lab:concept/euclidean-distance', 'prerequisiteOf', 'lab:method/knn', '#r3'),
       E('lab:concept/inner-product', 'prerequisiteOf', 'lab:concept/orthonormal-basis', '#r5'),
       E('lab:method/one-hot', 'relatedTo', 'lab:concept/orthonormal-basis', '#r5'),
       E('lab:analogy/table-row-point', 'analogyOf', 'lab:concept/feature-space', '#r1'),
       E('lab:analogy/street-vs-straight', 'analogyOf', 'lab:concept/euclidean-distance', '#r3'),
       E('lab:analogy/taste-table', 'analogyOf', 'lab:concept/cosine-similarity', '#r4'),
       E('lab:concept/cosine-similarity', 'hasLimitation', 'lab:limitation/angle-drops-size', '#r4'),
       E('lab:claim/distance-any-dim', 'supports', 'lab:concept/euclidean-distance', '#r1'),
       E('lab:claim/rotation-keeps-length', 'supports', 'lab:concept/orthonormal-basis', '#r5'),
       E('lab:sim/e1-dims', 'demonstratedBy', 'lab:claim/distance-any-dim', '#r1'),
       E('lab:sim/e1-angle', 'demonstratedBy', 'lab:concept/inner-product', '#r4'),
       E('lab:sim/e1-basis', 'demonstratedBy', 'lab:claim/rotation-keeps-length', '#r5'),
       E('lab:concept/euclidean-space', 'derivedFrom', 'lab:work/eea_euclid', '#top'),
       E('lab:concept/euclidean-space', 'broader', 'lab:topic/linear-algebra'),
       E('lab:method/knn', 'broader', 'lab:topic/knn'),
       E('lab:concept/feature-space', 'broader', 'lab:topic/embedding-space'),
       E('lab:concept/cosine-similarity', 'relatedTo', 'lab:topic/attention-mechanism'),
       E('lab:concept/vector', 'relatedTo', 'lab:topic/word-embedding'),
       E('lab:concept/orthonormal-basis', 'relatedTo', 'lab:topic/pca')]
# ── e2 그림자와 칸막이의 방 ──
P = 'e2_shadow_rooms'
e2n = [N('lab:concept/orthogonal-projection', 'Concept', '그림자(정사영)', 'Orthogonal projection', P, '#r6', 1, '바닥에 똑바로 내린 발. 바닥 위에서 가장 가까운 점.'),
       N('lab:concept/residual', 'Concept', '빗나간 만큼(잔차)', 'Residual', P, '#r6', 1, '정답 − 그림자. 바닥과 직각.'),
       N('lab:method/least-squares', 'Method', '예측선 긋기(최소제곱)', 'Least squares', P, '#r6', 1, '빗나간 거리 제곱 합이 가장 작은 답을 고른다. 예측 = 정답의 그림자.'),
       N('lab:concept/hyperplane', 'Concept', '칸막이(초평면)', 'Hyperplane', P, '#r7', 1, 'n칸 방을 둘로 나누는 한 칸 적은 판. 꽂힌 화살표 n과의 겹침 점수가 일정한 점들.'),
       N('lab:concept/decision-boundary', 'Concept', '결정 경계', 'Decision boundary', P, '#r7', 1),
       N('lab:concept/isometry', 'Concept', '거리를 지키는 움직임(등거리 변환)', 'Isometry', P, '#r8', 2, '밀기·돌리기·뒤집기. 모든 점 사이 거리를 그대로 둔다.'),
       N('lab:concept/ball', 'Concept', '공(반지름 r 안쪽)', 'Ball', P, '#r9', 1),
       N('lab:concept/curse-of-dimensionality', 'Concept', '차원의 저주', 'Curse of dimensionality', P, '#r9', 2, '칸이 많으면 공의 부피가 거의 껍질에 몰려 모두 비슷하게 멀어진다.'),
       N('lab:method/feature-scaling', 'Method', '단위 맞추기(특성 스케일링)', 'Feature scaling', P, '#r10', 1, '열마다 한 칸의 크기를 비슷하게 맞춘 뒤 거리를 잰다.'),
       N('lab:concept/geodesic', 'Concept', '표면을 따라 간 길이(호)', 'Geodesic distance', P, '#r10', 2),
       N('lab:method/data-augmentation', 'Method', '데이터 늘리기', 'Data augmentation', P, '#r8', 1),
       N('lab:claim/mean-is-projection', 'Claim', '평균은 숫자들의 그림자', 'The mean is a projection', P, '#r6', 1),
       N('lab:claim/units-change-neighbor', 'Claim', '단위를 바꾸면 가장 가까운 이웃이 바뀔 수 있다', 'Units can change the nearest neighbour', P, '#r10', 1),
       N('lab:analogy/noon-shadow', 'Analogy', '정오의 막대 그림자', 'Noon shadow', P, '#r6', 1),
       N('lab:analogy/playground-line', 'Analogy', '운동장 가운데 줄', 'Playground dividing line', P, '#r7', 1),
       N('lab:analogy/hollow-balloon', 'Analogy', '속이 빈 100칸 풍선', 'Hollow 100-dimensional balloon', P, '#r9', 1),
       N('lab:limitation/finite-dims', 'Limitation', '칸 수가 정해져 있어야 한다', 'Needs a fixed, finite number of dimensions', P, '#endless', 1),
       N('lab:limitation/straight-ruler', 'Limitation', '곧은 자는 휜 표면에서 짧게 잰다', 'Straight ruler underestimates on curved surfaces', P, '#r10', 2),
       N('lab:concept/hilbert-space', 'Concept', '힐베르트 공간(예고)', 'Hilbert space (preview)', P, '#endless', 2, '자와 각도기는 그대로, 방을 끝없이 넓힌 것.'),
       N('lab:sim/e2-shadow', 'Simulation', '그림자와 그릇 실험', 'Projection and bowl', P, '#r6', 2),
       N('lab:sim/e2-plane', 'Simulation', '칸막이 실험', 'Hyperplane side', P, '#r7', 2),
       N('lab:sim/e2-shell', 'Simulation', '껍질 비율 실험', 'Shell volume ratio', P, '#r9', 2),
       N('lab:sim/e2-duel', 'Simulation', '가장 가까운 이웃 찾기 대결', 'Nearest-neighbour duel', P, '#duel', 2),
       N('lab:question/e2-units', 'Question', '단위가 다른 열을 섞으면 거리는 무엇을 재나?', 'What does distance measure across mixed units?', P, '#duel', 1)]
e2e = [E('lab:concept/residual', 'partOf', 'lab:concept/orthogonal-projection', '#r6'),
       E('lab:method/least-squares', 'derivedFrom', 'lab:concept/orthogonal-projection', '#r6'),
       E('lab:claim/mean-is-projection', 'supports', 'lab:method/least-squares', '#r6'),
       E('lab:concept/hyperplane', 'derivedFrom', 'lab:concept/inner-product', '#r7'),
       E('lab:concept/decision-boundary', 'broader', 'lab:concept/hyperplane', '#r7'),
       E('lab:concept/isometry', 'relatedTo', 'lab:concept/orthonormal-basis', '#r8'),
       E('lab:method/data-augmentation', 'relatedTo', 'lab:concept/isometry', '#r8'),
       E('lab:concept/curse-of-dimensionality', 'relatedTo', 'lab:concept/ball', '#r9'),
       E('lab:method/feature-scaling', 'solves', 'lab:question/e2-units', '#r10'),
       E('lab:claim/units-change-neighbor', 'supports', 'lab:method/feature-scaling', '#r10'),
       E('lab:analogy/noon-shadow', 'analogyOf', 'lab:concept/orthogonal-projection', '#r6'),
       E('lab:analogy/playground-line', 'analogyOf', 'lab:concept/hyperplane', '#r7'),
       E('lab:analogy/hollow-balloon', 'analogyOf', 'lab:concept/curse-of-dimensionality', '#r9'),
       E('lab:concept/euclidean-space', 'hasLimitation', 'lab:limitation/finite-dims', '#endless'),
       E('lab:concept/euclidean-distance', 'hasLimitation', 'lab:limitation/straight-ruler', '#r10'),
       E('lab:limitation/finite-dims', 'addressedBy', 'lab:concept/hilbert-space', '#endless'),
       E('lab:sim/e2-shadow', 'demonstratedBy', 'lab:claim/mean-is-projection', '#r6'),
       E('lab:sim/e2-plane', 'demonstratedBy', 'lab:concept/hyperplane', '#r7'),
       E('lab:sim/e2-shell', 'demonstratedBy', 'lab:concept/curse-of-dimensionality', '#r9'),
       E('lab:sim/e2-duel', 'demonstratedBy', 'lab:claim/units-change-neighbor', '#duel'),
       E('lab:method/least-squares', 'broader', 'lab:topic/linear-regression'),
       E('lab:concept/decision-boundary', 'relatedTo', 'lab:topic/svm'),
       E('lab:concept/decision-boundary', 'relatedTo', 'lab:topic/logistic-regression'),
       E('lab:method/data-augmentation', 'broader', 'lab:topic/data-augmentation'),
       E('lab:method/feature-scaling', 'broader', 'lab:topic/feature-engineering'),
       E('lab:concept/curse-of-dimensionality', 'relatedTo', 'lab:topic/knn'),
       E('lab:concept/orthogonal-projection', 'broader', 'lab:topic/linear-algebra')]


# ── h1 화살표의 방 ──
P = 'h1_arrow_rooms'
h1n = [N('lab:concept/hilbert-space', 'Concept', '힐베르트 공간', 'Hilbert space', P, '#r1', 1, '겹침 점수(내적)가 있고 빈틈이 없는(완비) 방.'),
       N('lab:concept/vector-space', 'Concept', '벡터 공간', 'Vector space', P, '#r1', 1, '더하고 늘릴 수 있는 방.'),
       N('lab:concept/inner-product-space', 'Concept', '내적 공간', 'Inner-product space', P, '#r1', 1),
       N('lab:concept/function-inner-product', 'Concept', '곡선의 겹침 점수', 'Inner product of functions', P, '#r2', 1, '같은 시각끼리 곱해서 넓이(정적분).'),
       N('lab:concept/norm', 'Concept', '길이(노름)', 'Norm', P, '#r3', 1),
       N('lab:concept/orthogonality', 'Concept', '직각(직교)', 'Orthogonality', P, '#r3', 1, '겹침 점수 0.'),
       N('lab:concept/cauchy-sequence', 'Concept', '코시 수열', 'Cauchy sequence', P, '#r4', 2),
       N('lab:concept/completeness', 'Concept', '빈틈 없음(완비성)', 'Completeness', P, '#r4', 2, '점점 모이는 수열의 목적지가 방 안에 있다.'),
       N('lab:concept/l2-sequence', 'Concept', '끝없는 목록 방 ℓ²', 'ℓ² space', P, '#r5', 2),
       N('lab:concept/l2-function', 'Concept', '곡선 방 L²', 'L² space', P, '#r5', 2),
       N('lab:claim/ramp-to-step', 'Claim', '매끈한 곡선만 있는 방은 빈틈이 있다(경사로 → 계단)', 'Continuous functions are not complete in L² norm', P, '#r4', 2),
       N('lab:claim/inv-sqrt-not-l2', 'Claim', '1/√k 목록은 ℓ²에 들어오지 못한다', '1/√k is not square-summable', P, '#r5', 2),
       N('lab:analogy/three-boxes', 'Analogy', '세 겹 상자', 'Three nested boxes', P, '#r1', 1),
       N('lab:analogy/mood-graphs', 'Analogy', '두 사람의 하루 기분 그래프', 'Two daily mood curves', P, '#r2', 1),
       N('lab:analogy/root2-hole', 'Analogy', '√2라는 구멍', 'The √2 hole in the rationals', P, '#r4', 1),
       N('lab:sim/h1-overlap', 'Simulation', '곡선 겹침 실험', 'Function overlap', P, '#r2', 2),
       N('lab:sim/h1-ramp', 'Simulation', '경사로 → 계단 실험', 'Ramp to step', P, '#r4', 2),
       N('lab:sim/h1-series', 'Simulation', '두 목록의 제곱 합 실험', 'Square sums of two sequences', P, '#r5', 2),
       N('lab:work/eea_hilbert', 'Work', 'eeanimation — HILBERT SPACE 01~10', 'eeanimation — Hilbert Space', P, '#top', 1)]
h1e = [E('lab:concept/inner-product-space', 'broader', 'lab:concept/vector-space', '#r1'), E('lab:concept/hilbert-space', 'broader', 'lab:concept/inner-product-space', '#r1'),
       E('lab:concept/completeness', 'partOf', 'lab:concept/hilbert-space', '#r4'), E('lab:concept/cauchy-sequence', 'prerequisiteOf', 'lab:concept/completeness', '#r4'),
       E('lab:concept/norm', 'derivedFrom', 'lab:concept/function-inner-product', '#r3'), E('lab:concept/orthogonality', 'derivedFrom', 'lab:concept/function-inner-product', '#r3'),
       E('lab:concept/l2-sequence', 'broader', 'lab:concept/hilbert-space', '#r5'), E('lab:concept/l2-function', 'broader', 'lab:concept/hilbert-space', '#r5'),
       E('lab:claim/ramp-to-step', 'supports', 'lab:concept/completeness', '#r4'), E('lab:claim/inv-sqrt-not-l2', 'supports', 'lab:concept/l2-sequence', '#r5'),
       E('lab:analogy/three-boxes', 'analogyOf', 'lab:concept/hilbert-space', '#r1'), E('lab:analogy/mood-graphs', 'analogyOf', 'lab:concept/function-inner-product', '#r2'), E('lab:analogy/root2-hole', 'analogyOf', 'lab:concept/completeness', '#r4'),
       E('lab:sim/h1-overlap', 'demonstratedBy', 'lab:concept/function-inner-product', '#r2'), E('lab:sim/h1-ramp', 'demonstratedBy', 'lab:claim/ramp-to-step', '#r4'), E('lab:sim/h1-series', 'demonstratedBy', 'lab:claim/inv-sqrt-not-l2', '#r5'),
       E('lab:concept/hilbert-space', 'derivedFrom', 'lab:work/eea_hilbert', '#top'), E('lab:concept/hilbert-space', 'broader', 'lab:topic/linear-algebra')]
# ── h2 곡선을 쪼개는 방 ──
P = 'h2_wave_rooms'
h2n = [N('lab:concept/hilbert-basis', 'Concept', '곡선 방의 자 세트(힐베르트 기저)', 'Orthonormal (Hilbert) basis', P, '#r6', 2, '길이 1이고 서로 직각인 곡선들. 좌표 = 겹침 점수.'),
       N('lab:concept/hilbert-projection', 'Concept', '끝없는 방의 그림자', 'Projection theorem', P, '#r7', 2, '닫힌 바닥 위 가장 가까운 점은 하나뿐이고, 빗나간 만큼은 바닥과 직각.'),
       N('lab:concept/fourier-series', 'Concept', '물결 조각(푸리에 급수)', 'Fourier series', P, '#r8', 1, '곡선을 서로 직각인 sin·cos 물결의 합으로.'),
       N('lab:concept/parseval', 'Concept', '피타고라스의 확장(파스발 항등식)', "Parseval's identity", P, '#r9', 1, '곡선의 세기 = 조각 세기의 합.'),
       N('lab:concept/kernel-method', 'Method', '커널 방(RKHS)', 'Kernel methods / RKHS', P, '#r10', 2, '닮음 점수표로 끝없는 방에서 곧게 가른다.'),
       N('lab:concept/gibbs', 'Limitation', '꺾인 곳의 튀어나옴(평균제곱 수렴 ≠ 모든 점 수렴)', 'Gibbs overshoot', P, '#r8', 2),
       N('lab:method/compression', 'Method', '큰 조각만 남기기(압축)', 'Truncation / compression', P, '#duel', 1),
       N('lab:analogy/smoothie', 'Analogy', '스무디를 과일별 컵 수로', 'Smoothie back to fruit cups', P, '#r6', 1),
       N('lab:analogy/choir-parts', 'Analogy', '합창을 파트별로', 'Choir parts', P, '#r8', 1),
       N('lab:analogy/allowance-accounts', 'Analogy', '용돈을 통장에 나눠도 합은 같다', 'Allowance split across accounts', P, '#r9', 1),
       N('lab:claim/kernel-beats-line', 'Claim', '커널 방은 곧은 칸막이가 못 가르는 원 무리를 가른다', 'Kernel separates ring data a line cannot', P, '#r10', 2),
       N('lab:claim/largest-first', 'Claim', '큰 조각부터 고르면 가장 적은 조각으로 세기를 살린다', 'Largest coefficients first is most efficient', P, '#duel', 1),
       N('lab:sim/h2-basis', 'Simulation', '조각 켜기 실험', 'Toggle basis components', P, '#r6', 2),
       N('lab:sim/h2-fourier', 'Simulation', '물결 조각 늘리기 실험', 'Fourier partial sums', P, '#r8', 2),
       N('lab:sim/h2-kernel', 'Simulation', '커널 방 실험', 'RBF kernel classifier', P, '#r10', 2),
       N('lab:sim/h2-duel', 'Simulation', '곡선 맞히기 대결', 'Curve reconstruction duel', P, '#duel', 2)]
h2e = [E('lab:concept/hilbert-basis', 'partOf', 'lab:concept/hilbert-space', '#r6'), E('lab:concept/fourier-series', 'broader', 'lab:concept/hilbert-basis', '#r8'),
       E('lab:concept/parseval', 'derivedFrom', 'lab:concept/hilbert-basis', '#r9'), E('lab:concept/hilbert-projection', 'derivedFrom', 'lab:concept/completeness', '#r7'),
       E('lab:concept/fourier-series', 'hasLimitation', 'lab:concept/gibbs', '#r8'), E('lab:method/compression', 'derivedFrom', 'lab:concept/parseval', '#duel'),
       E('lab:claim/largest-first', 'supports', 'lab:method/compression', '#duel'), E('lab:claim/kernel-beats-line', 'supports', 'lab:concept/kernel-method', '#r10'),
       E('lab:analogy/smoothie', 'analogyOf', 'lab:concept/hilbert-basis', '#r6'), E('lab:analogy/choir-parts', 'analogyOf', 'lab:concept/fourier-series', '#r8'), E('lab:analogy/allowance-accounts', 'analogyOf', 'lab:concept/parseval', '#r9'),
       E('lab:sim/h2-basis', 'demonstratedBy', 'lab:concept/hilbert-basis', '#r6'), E('lab:sim/h2-fourier', 'demonstratedBy', 'lab:concept/gibbs', '#r8'), E('lab:sim/h2-kernel', 'demonstratedBy', 'lab:claim/kernel-beats-line', '#r10'), E('lab:sim/h2-duel', 'demonstratedBy', 'lab:claim/largest-first', '#duel'),
       E('lab:concept/kernel-method', 'relatedTo', 'lab:topic/svm'), E('lab:concept/fourier-series', 'relatedTo', 'lab:topic/positional-encoding'), E('lab:concept/parseval', 'relatedTo', 'lab:topic/pca'), E('lab:concept/hilbert-projection', 'relatedTo', 'lab:topic/linear-regression')]
EEH = dict(EEA); EEH = json.loads(json.dumps(EEA)); EEH['id'] = 'eea_hilbert'; EEH['title'] = 'HILBERT SPACE 01~10'; EEH['lab']['work'] = 'lab:work/eea_hilbert'

pages = {
 'e0': (e0n, e0e, [EEA, CURR], meta('e0', '유클리드 공간 0편 가방 점검 — 좌표평면·피타고라스·sin·cos', '0', 'e0_orientation.html', ['lab:concept/coordinate-plane', 'lab:concept/pythagorean-theorem'], ['moe_curriculum'])),
 'e1': (e1n, e1e, [EEA, CURR, ref('mikolov2013', 'Efficient Estimation of Word Representations in Vector Space', [{"family": "Mikolov", "given": "Tomas"}, {"family": "Chen", "given": "Kai"}, {"family": "Corrado", "given": "Greg"}, {"family": "Dean", "given": "Jeffrey"}], 2013, {"type": "paper-conference", "URL": "https://arxiv.org/abs/1301.3781"}, ['lab:concept/vector'])],
        meta('e1', '유클리드 공간 ① 자와 각도기의 방 — 점·이동·거리·각도·자 세트', '1', 'e1_ruler_rooms.html', ['lab:concept/euclidean-space', 'lab:concept/inner-product'], ['eea_euclid', 'moe_curriculum'])),
 'h1': (h1n, h1e, [EEH, CURR, ref('kreyszig1978', 'Introductory Functional Analysis with Applications', [{"family": "Kreyszig", "given": "Erwin"}], 1978, {"type": "book", "publisher": "Wiley"}, ['lab:concept/hilbert-space'])],
        meta('h1', '힐베르트 공간 ① 화살표의 방 — 끝없는 방에서도 자와 각도기를 쓰려면', '3', 'h1_arrow_rooms.html', ['lab:concept/hilbert-space', 'lab:concept/completeness'], ['eea_hilbert', 'moe_curriculum'])),
 'h2': (h2n, h2e, [EEH, CURR, ref('scholkopf2002', 'Learning with Kernels', [{"family": "Schölkopf", "given": "Bernhard"}, {"family": "Smola", "given": "Alexander J."}], 2002, {"type": "book", "publisher": "MIT Press"}, ['lab:concept/kernel-method']),
        ref('vaswani2017', 'Attention Is All You Need', [{"family": "Vaswani", "given": "Ashish"}], 2017, {"type": "paper-conference", "URL": "https://arxiv.org/abs/1706.03762"}, ['lab:concept/fourier-series'])],
        meta('h2', '힐베르트 공간 ② 곡선을 쪼개는 방 — 자 세트·그림자·물결 조각·피타고라스의 확장·커널 방', '4', 'h2_wave_rooms.html', ['lab:concept/fourier-series', 'lab:concept/parseval', 'lab:concept/kernel-method'], ['eea_hilbert', 'moe_curriculum'])),
 'e2': (e2n, e2e, [EEA, CURR,
        ref('cortes1995', 'Support-vector networks', [{"family": "Cortes", "given": "Corinna"}, {"family": "Vapnik", "given": "Vladimir"}], 1995, {"container-title": "Machine Learning", "volume": "20", "page": "273-297", "DOI": "10.1007/BF00994018"}, ['lab:concept/hyperplane']),
        ref('bellman1961', 'Adaptive Control Processes: A Guided Tour', [{"family": "Bellman", "given": "Richard"}], 1961, {"type": "book", "publisher": "Princeton University Press"}, ['lab:concept/curse-of-dimensionality'])],
        meta('e2', '유클리드 공간 ② 그림자와 칸막이의 방 — 그림자·칸막이·움직임·공·곧은 자의 한계', '2', 'e2_shadow_rooms.html', ['lab:concept/orthogonal-projection', 'lab:concept/hyperplane', 'lab:method/feature-scaling'], ['eea_euclid', 'moe_curriculum'])),
}
ALL = {}
for k, v in pages.items():
    for n in v[0]: ALL.setdefault(n['id'], n)
for k, (nodes, edges, refs, m) in pages.items():
    have = {n['id'] for n in nodes}
    for e in edges:
        for x in (e['s'], e['o']):
            if x not in have and x in ALL:
                st = dict(ALL[x]); st['anchor'] = ALL[x]['page'] + '.html' + ALL[x]['anchor']; st['coverage'] = 'mentioned'; nodes.append(st); have.add(x)

    page = m['url'].split('/')[-1].replace('.html', '')
    json.dump({"version": "1.3", "page": page, "nodes": nodes, "edges": edges}, open(os.path.join(B, 'kg_%s.json' % k), 'w'), ensure_ascii=False, indent=1)
    json.dump(refs, open(os.path.join(B, 'refs_%s.json' % k), 'w'), ensure_ascii=False, indent=1)
    json.dump(m, open(os.path.join(B, 'meta_%s.json' % k), 'w'), ensure_ascii=False, indent=1)
    print(k, len(nodes), 'nodes', len(edges), 'edges')
