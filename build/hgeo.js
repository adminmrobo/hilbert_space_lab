/* hgeo.js — 힐베르트 공간 편 계산 모듈 (브라우저·node 공용). 모든 숫자는 설명용 예시값.
   code/check_hilbert.js가 페이지 기대값을 다시 계산한다. */
var HG=(function(){
'use strict';
var PI=Math.PI;
/* 심프슨 적분 */
function integ(f,a,b,n){n=n||400;if(n%2)n++;var h=(b-a)/n,s=f(a)+f(b);for(var i=1;i<n;i++)s+=(i%2?4:2)*f(a+i*h);return s*h/3;}
function ip(f,g,a,b){return integ(function(t){return f(t)*g(t);},a,b);}
function nrm(f,a,b){return Math.sqrt(ip(f,f,a,b));}

/* 2번 방: f = sin(πt), g = sin(πt + φ) on [0,1] → 겹침 = ½cos φ */
function f2(t){return Math.sin(PI*t);}
function g2(phi){return function(t){return Math.sin(PI*t+phi);};}

/* 4번 방: 빈틈 — √2로 다가가는 유리수, 계단으로 다가가는 경사로 */
var ROOT2=[1,1.4,1.41,1.414,1.4142,1.41421,1.414213];
function ramp(n){return function(t){return Math.max(0,Math.min(1,n*(t-0.5)+0.5));};}
function step(t){return t>=0.5?1:0;}
function rampGap(n){return Math.sqrt(1/(12*n));}            /* ‖f_n − 계단‖ (손 계산값) */

/* 5번 방: 끝없는 목록 */
function psum(fn,n){var s=0;for(var k=1;k<=n;k++)s+=fn(k);return s;}

/* 6번 방: 곡선 방의 자 세트 e_k(t) = √2 sin(kπt) on [0,1] */
function ek(k){return function(t){return Math.SQRT2*Math.sin(k*PI*t);};}
var C6=[0.8,0.5,0.3,0.18,0.1];
function f6(t){var s=0;for(var k=0;k<C6.length;k++)s+=C6[k]*ek(k+1)(t);return s;}

/* 7번 방: 그림자 3D */
var X7=[2,1,3];

/* 8번 방: 물결 조각 on [0, 2π]. 기저: e0 = 1/√(2π), c_k = cos(kx)/√π, s_k = sin(kx)/√π */
var TWO=2*PI;
function sig8(x){return 0.85*Math.sin(x)+0.35*Math.sin(2*x)-0.15*Math.sin(3*x)+0.12*Math.sin(5*x);}
function sq8(x){x=((x%TWO)+TWO)%TWO;return x<PI?1:-1;}
function basis(kind,k){if(kind==='0')return function(){return 1/Math.sqrt(TWO);};if(kind==='c')return function(x){return Math.cos(k*x)/Math.sqrt(PI);};return function(x){return Math.sin(k*x)/Math.sqrt(PI);};}
function coeffs(f,K){var o={a0:ip(f,basis('0'),0,TWO),c:[],s:[]};for(var k=1;k<=K;k++){o.c.push(ip(f,basis('c',k),0,TWO,800));o.s.push(ip(f,basis('s',k),0,TWO,800));}return o;}
function partial(co,n){return function(x){var v=co.a0*basis('0')(x);for(var k=1;k<=n;k++)v+=co.c[k-1]*basis('c',k)(x)+co.s[k-1]*basis('s',k)(x);return v;};}
function err(f,co,n){var p=partial(co,n);return Math.sqrt(integ(function(x){var d=f(x)-p(x);return d*d;},0,TWO,2000));}

/* 9번 방: 피타고라스 확장. x(t) = a e1(t) + b e2(t) on [0,1] */
function energy(a,b){return integ(function(t){var v=a*ek(1)(t)+b*ek(2)(t);return v*v;},0,1,800);}

/* 10번 방: 커널 방 — 안쪽 원(+) / 바깥 고리(−), 닮음 점수표 exp(−거리²/(2σ²)) */
function ring(){var out=[],s=5;function r(){s=(s*16807)%2147483647;return s/2147483647;}
  for(var i=0;i<14;i++){var a=r()*TWO,d=r()*0.9;out.push([d*Math.cos(a),d*Math.sin(a),1]);}
  for(i=0;i<18;i++){a=r()*TWO;d=1.7+r()*0.8;out.push([d*Math.cos(a),d*Math.sin(a),-1]);}return out;}
var RING=ring();
function kscore(x,y,sig){var s=0;RING.forEach(function(p){var d2=(x-p[0])*(x-p[0])+(y-p[1])*(y-p[1]);s+=p[2]*Math.exp(-d2/(2*sig*sig));});return s;}
function kacc(sig){var ok=0;RING.forEach(function(p){if(Math.sign(kscore(p[0],p[1],sig))===p[2])ok++;});return ok;}
function lineAcc(){var best=0;for(var a=0;a<180;a+=2){var t=a*PI/180,nx=Math.cos(t),ny=Math.sin(t);for(var b=-3;b<=3;b+=0.1){var ok=0;RING.forEach(function(p){if(Math.sign(nx*p[0]+ny*p[1]-b)===p[2])ok++;});best=Math.max(best,ok);}}return best;}

/* 대결: 곡선 맞히기 — 물결 번호 k의 조각 세기 (sin만) */
var DUEL={1:0.3,2:0.1,4:0.9,7:0.4};
function duelSig(x){var s=0;for(var k in DUEL)s+=DUEL[k]*Math.sin(k*x)/Math.sqrt(PI);return s;}
function duelPlan(order){var tot=0,ks=Object.keys(DUEL).map(Number);ks.forEach(function(k){tot+=DUEL[k]*DUEL[k];});
  var seq=order==='low'?[1,2,3,4,5,6,7,8]:ks.slice().sort(function(a,b){return DUEL[b]*DUEL[b]-DUEL[a]*DUEL[a];});
  var acc=0,steps=[];for(var i=0;i<seq.length;i++){var c=DUEL[seq[i]]||0;acc+=c*c;steps.push({k:seq[i],e:acc/tot});if(acc/tot>=0.95)break;}return {steps:steps,n:steps.length,tot:tot};}

return {PI:PI,integ:integ,ip:ip,nrm:nrm,f2:f2,g2:g2,ROOT2:ROOT2,ramp:ramp,step:step,rampGap:rampGap,psum:psum,ek:ek,C6:C6,f6:f6,X7:X7,TWO:TWO,sig8:sig8,sq8:sq8,basis:basis,coeffs:coeffs,partial:partial,err:err,energy:energy,RING:RING,kscore:kscore,kacc:kacc,lineAcc:lineAcc,DUEL:DUEL,duelSig:duelSig,duelPlan:duelPlan};
})();
if(typeof module!=='undefined')module.exports=HG;
