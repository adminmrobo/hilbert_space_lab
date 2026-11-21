// 확장 스킬(ai-lab-extend) 블록 끼우기 — build.js가 페이지마다 부른다.
// 조수 수식 상자 순서를 "말로 → 숫자로 → 학교 수학 → 식(접기, 읽는 법) → 바꿔 보면?"으로 바꾸고,
// 실험 바로가기, 박사 대사, AI 판단 코너, 기호 읽는 법을 더한다. 문구는 ext_data.js에 있다.
const DATA = require('./ext_data.js');

const CSS = `
/* ── 확장 스킬 블록 ── */
.jump{display:inline-block;margin-top:10px;font-size:14px;font-weight:700;color:var(--info);text-decoration:none;border-bottom:1px dashed var(--info)}
.am .plainline{background:#fff;border-radius:8px;padding:10px 14px;margin:8px 0;border-left:3px solid var(--terrain)}
.am ol.steps{margin:6px 0 8px;padding-left:24px;display:flex;flex-direction:column;gap:6px;font-variant-numeric:tabular-nums}
.am ol.steps li{background:#fff;border-radius:8px;padding:6px 10px}
.am details.eq,.am details.chg{background:#fff;border:1px solid #f0c9da;border-radius:8px;padding:8px 12px;margin:10px 0}
.am details.eq summary,.am details.chg summary{cursor:pointer;font-weight:700;font-size:14.5px;color:var(--c-asst)}
.wm>*{min-width:0}
.am details.eq{overflow-x:auto}
.am details.eq table{margin-top:8px}
.am details.eq td:nth-child(2){font-size:14px;color:var(--muted)}
.am details.chg p{margin:8px 0 0}
.gloss .rd{font-style:normal;font-size:13px;color:var(--muted)}
.chk{background:var(--panel);border:1px solid var(--rule);border-left:4px solid var(--eye);border-radius:10px;padding:14px 18px;margin:14px 0}
.chk ol{margin:6px 0 0;padding-left:22px;display:flex;flex-direction:column;gap:6px}
#aicheck details.fold ol{display:flex;flex-direction:column;gap:8px;padding-left:22px;margin:10px 0 0}
`;

const esc = s => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

function room(sec, id, d, warn) {
  // 1) 첫 실험 패널에 id, 왜 상자 끝에 바로가기
  const pid = 'pv-' + id;
  if (sec.includes('<div class="panel">')) {
    sec = sec.replace('<div class="panel">', '<div class="panel" id="' + pid + '">');
    sec = sec.replace(/(<div class="why">[\s\S]*?<div class="easy">[\s\S]*?<\/div>)/,
      '$1<a class="jump" href="#' + pid + '">식이 낯설면 아래 실험부터 눌러 보세요 ↓</a>');
  }
  // 2) 조수 수식 상자 재구성
  const m = sec.match(/<div class="am">([\s\S]*?)<div class="ac">([\s\S]*?)<\/div><\/div>/);
  if (!m) { warn.push(id + ': 수식 상자 없음'); return sec; }
  const body = m[1];
  const h4 = body.match(/<h4>[\s\S]*?<\/h4>/)[0];
  const aq = body.match(/<p class="aq">[\s\S]*?<\/p>/)[0];
  const school = body.match(/<span class="lbl">학교 수학으로 보면<\/span>([\s\S]*?)<table>/)[1].trim();
  let table = body.match(/<table>[\s\S]*?<\/table>/)[0];
  const rows = table.match(/<tr><td>[\s\S]*?<\/tr>/g) || [];
  if (rows.length !== d.read.length) warn.push(id + ': 식 조각 ' + rows.length + '줄, 읽는 법 ' + d.read.length + '줄');
  let i = 0;
  table = table.replace('<tr><th>식 조각</th><th>뜻</th></tr>', '<tr><th>식 조각</th><th>읽는 법</th><th>뜻</th></tr>')
    .replace(/<tr><td>([\s\S]*?)<\/td>/g, (s, a) => '<tr><td>' + a + '</td><td>' + (d.read[i++] || '') + '</td>');
  const out = h4 + '\n      ' + aq +
    '\n      <div class="plainline"><span class="lbl">식 없이 말로 먼저</span>' + d.plain + '</div>' +
    '\n      <span class="lbl">숫자로 한 번 해 보기</span><ol class="steps">' + d.steps.map(s => '<li>' + s + '</li>').join('') + '</ol>' +
    '\n      <span class="lbl">학교 수학으로 보면</span>' + school +
    '\n      <details class="eq"><summary>식으로 적으면 — 읽는 법과 함께 (눌러서 펼치기)</summary>' + table + '</details>' +
    (d.change ? '\n      <details class="chg"><summary>숫자를 바꿔 보면? — ' + d.change[0] + '</summary><p>' + d.change[1] + '</p></details>' : '') +
    '\n      <div class="ac">' + m[2] + '</div>';
  sec = sec.replace(m[0], '<div class="am">' + out + '</div>');
  // 3) 한계 앞 추가 블록
  if (d.extra) sec = sec.replace('<div class="lim">', d.extra + '\n  <div class="lim">');
  return sec;
}

function apply(H, n) {
  const P = DATA[n]; if (!P) return H;
  const warn = [];
  H = H.replace('</head>', '<style>' + CSS + '</style>\n</head>');
  // 방마다
  for (const id of Object.keys(P.rooms)) {
    const re = new RegExp('<section class="sec" id="' + id + '"[\\s\\S]*?</section>');
    const mm = H.match(re); if (!mm) { warn.push(id + ': 방 없음'); continue; }
    H = H.replace(mm[0], () => room(mm[0], id, P.rooms[id], warn));
  }
  // 기호 읽는 법
  for (const [k, v] of Object.entries(P.gloss || {})) {
    const s = '<div><b>' + k + '</b>';
    if (!H.includes(s)) { warn.push('기호 풀이 없음: ' + k); continue; }
    H = H.replace(s, s + ' <i class="rd">(읽기: ' + v + ')</i>');
  }
  // AI 판단 코너 (정리 앞) + 메뉴
  if (P.ai) {
    const sec = '<section class="sec" id="aicheck" aria-labelledby="h-ai"><div class="wrap">\n' +
      '  <h2 id="h-ai"><span class="door e">?</span>AI 판단 코너 — 이 결과, 믿어도 될까? <span class="sub">계산 대신 판단 연습</span></h2>\n' +
      '  <p>계산은 프로그램과 AI가 1초 만에 해 줍니다. 우리에게 필요한 건 결과가 그럴듯한지 알아보는 힘이에요. 주판봇의 보고에서 이상한 곳을 먼저 찾아본 뒤 펼쳐 보세요.</p>\n' +
      '  <div data-dlg="ai"></div>\n' +
      '  <details class="fold"><summary>이상한 곳 확인하기 (눌러서 펼치기)</summary><ol>' + P.ai.check.map(s => '<li>' + s + '</li>').join('') + '</ol></details>\n' +
      '  <p class="muted" style="font-size:13.5px">주판봇의 보고 숫자는 연습용 예시값입니다.</p>\n</div></section>\n\n';
    H = H.replace('<section class="sec" id="sum"', sec + '<section class="sec" id="sum"');
    H = H.replace('<a href="#sum">정리</a>', '<a href="#aicheck">AI 판단</a><a href="#sum">정리</a>');
  }
  // 박사 대사·AI 대화
  const pre = {}; for (const [id, d] of Object.entries(P.rooms)) if (d.doc) pre[id] = d.doc;
  const inj = 'var EXT_PRE=' + JSON.stringify(pre) + ',EXT_SET=' + JSON.stringify(P.ai ? { ai: P.ai.dlg } : {}) +
    ';Object.keys(EXT_PRE).forEach(function(k){if(DLG[k])DLG[k].unshift(EXT_PRE[k]);});Object.keys(EXT_SET).forEach(function(k){DLG[k]=EXT_SET[k];});\n';
  if (!H.includes('U.dialogues(DLG);')) warn.push('대화 연결 지점 없음');
  H = H.replace('U.dialogues(DLG);', inj + 'U.dialogues(DLG);');
  if (warn.length) console.warn('[ext ' + n + '] ' + warn.join(' / '));
  return H;
}
module.exports = { apply };
