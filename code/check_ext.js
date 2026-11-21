// 확장 블록(ext_data.js)에서 새로 쓴 숫자 검산: node code/check_ext.js
const E=Math.exp,ok=(n,a,b,t=5e-3)=>{const g=Math.abs(a-b)<=t;console.log((g?'  ok ':'  XX ')+n+' = '+a.toFixed(4));if(!g)process.exitCode=1;};
ok('h1 r2 ½cos120°',0.5*Math.cos(2*Math.PI/3),-0.25);
ok('h1 r3 (7,7) 길이²',98,49+49);ok('h1 r3 차이=2×겹침',98-50,2*24);
ok('h1 r4 1/√12000',1/Math.sqrt(12000),0.0091,1e-4);ok('h1 r4 1/√1200',1/Math.sqrt(1200),0.029,1e-3);
let s=0;for(let k=1;k<=3;k++)s+=1/k/k;ok('h1 r5 3항',s,1.361);ok('h1 r5 반씩 줄기',1/(1-1/4),1.3333);
ok('h2 r6 0.1 버림',1.0224-0.01,1.0124,1e-9);
function gm(N){let m=0;for(let i=1;i<20000;i++){let x=i/20000*Math.PI/2,v=0;for(let k=1;k<=N;k+=2)v+=4/Math.PI*Math.sin(k*x)/k;m=Math.max(m,v);}return m}
ok('h2 r8 깁스 100번',gm(101),1.18);ok('h2 r9 16/25',16/25,0.64);ok('h2 r10 e^-0.125',E(-0.125),0.88);ok('h2 r7 √10',Math.sqrt(10),3.16);
ok('h3 r11 0.01π',0.01*Math.PI,0.031);ok('h3 r11 비율',0.01/1.01,0.01);
ok('h3 r13 c=2.5',0.25+0.25+2.25,2.75);ok('h3 r13 (2,3,7) 평균',(2+3+7)/3,4);
ok('h3 r14 e^-0.5/e^-2',E(-0.5)/E(-2),4.5,0.05);
console.log(process.exitCode?'\n틀린 값 있음':'\n모두 맞음');
