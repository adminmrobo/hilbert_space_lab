// 힐베르트 공간 편 검산: node code/check_hilbert.js
const H=require('../build/hgeo.js');let bad=0;
function ok(n,g,w,t){t=t==null?0.005:t;const p=typeof w==='string'?g===w:Math.abs(g-w)<=t;if(!p)bad++;console.log((p?'  ok ':'FAIL ')+n+' = '+(typeof g==='number'?+g.toFixed(5):g)+(p?'':' (기대 '+w+')'));}
console.log('1번 방');ok('u+v x',1+3,4);ok('u+v y',2+1,3);
console.log('2번 방');ok('(3,4)·(4,3)',3*4+4*3,24);ok('cos θ',24/25,0.96);ok('각도',Math.acos(0.96)*180/Math.PI,16.26,0.01);
ok('곡선 겹침 φ=0',H.ip(H.f2,H.g2(0),0,1),0.5);ok('곡선 겹침 φ=60°',H.ip(H.f2,H.g2(Math.PI/3),0,1),0.25);ok('곡선 겹침 φ=90°',H.ip(H.f2,H.g2(Math.PI/2),0,1),0);
console.log('3번 방');ok('(3,4)·(−4,3)',3*-4+4*3,0);ok('‖x+y‖²',1+49,50);ok('‖sin πt‖',H.nrm(H.f2,0,1),0.7071,0.0001);
ok('sin πt ⟂ sin 2πt',H.ip(H.ek(1),H.ek(2),0,1),0,1e-6);ok('‖f+g‖² (f=sin πt, g=sin 2πt)',H.integ(t=>(Math.sin(Math.PI*t)+Math.sin(2*Math.PI*t))**2,0,1),1);
console.log('4번 방');ok('‖경사로₁₀ − 계단‖',Math.sqrt(H.integ(t=>(H.ramp(10)(t)-H.step(t))**2,0,1,20000)),H.rampGap(10),0.0005);ok('n=10',H.rampGap(10),0.0913,0.0001);ok('n=100',H.rampGap(100),0.0289,0.0001);
console.log('5번 방');ok('Σ1/k² 10항',H.psum(k=>1/k/k,10),1.5498,0.0001);ok('Σ1/k² 100항',H.psum(k=>1/k/k,100),1.6350,0.0001);ok('π²/6',Math.PI**2/6,1.6449,0.0001);
ok('Σ1/k 10항',H.psum(k=>1/k,10),2.929,0.001);ok('Σ1/k 100항',H.psum(k=>1/k,100),5.187,0.001);ok('∫t²',H.integ(t=>t*t,0,1),1/3);
console.log('6번 방');[0,1,2,3,4].forEach(i=>ok('c'+(i+1),H.ip(H.f6,H.ek(i+1),0,1),H.C6[i],0.0005));ok('‖f‖²',H.ip(H.f6,H.f6,0,1),1.0224,0.0005);
console.log('7번 방');ok('‖x−m‖ m=(1,1,0)',Math.hypot(1,0,3),3.1623,0.0001);
console.log('8번 방');const co=H.coeffs(H.sig8,8);ok('s₁',co.s[0],1.507,0.001);ok('오차 n=1',H.err(H.sig8,co,1),0.7077,0.001);ok('오차 n=3',H.err(H.sig8,co,3),0.2127,0.001);ok('오차 n=5',H.err(H.sig8,co,5),0,0.001);
const cq=H.coeffs(H.sq8,25);[5,25].forEach(n=>{const p=H.partial(cq,n);let mx=-9;for(let i=0;i<=4000;i++)mx=Math.max(mx,p(i/4000*Math.PI));ok('네모파 최고점 n='+n,mx,1.18,0.012);});
console.log('9번 방');ok('∫(3e₁+4e₂)²',H.energy(3,4),25);
console.log('10번 방');ok('커널 σ=0.5 맞힌 수',H.kacc(0.5),32,0);ok('곧은 칸막이 최고',H.lineAcc(),23,0);
console.log('대결');ok('시아(낮은 물결부터) 조각 수',H.duelPlan('low').n,7,0);ok('모아(큰 조각부터) 조각 수',H.duelPlan('big').n,3,0);ok('모아 3조각 에너지 %',H.duelPlan('big').steps[2].e*100,99.07,0.01);
console.log(bad?('\n틀린 곳 '+bad+'개'):'\n모두 맞음');process.exit(bad?1:0);
