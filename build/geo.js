/* geo.js — 유클리드 공간 편 계산 모듈 (브라우저·node 공용)
   모든 숫자는 설명용 예시값. code/check_euclid.js가 페이지 기대값을 다시 계산한다. */
var EG=(function(){
'use strict';
function dot(a,b){var s=0;for(var i=0;i<a.length;i++)s+=a[i]*b[i];return s;}
function norm(a){return Math.sqrt(dot(a,a));}
function sub(a,b){return a.map(function(x,i){return x-b[i];});}
function add(a,b){return a.map(function(x,i){return x+b[i];});}
function mul(a,k){return a.map(function(x){return x*k;});}
function dist(a,b){return norm(sub(a,b));}
function deg(r){return r*180/Math.PI;}
function rad(d){return d*Math.PI/180;}
function angle(a,b){var c=dot(a,b)/(norm(a)*norm(b));return deg(Math.acos(Math.max(-1,Math.min(1,c))));}
function rot(p,th){var c=Math.cos(th),s=Math.sin(th);return [p[0]*c-p[1]*s,p[0]*s+p[1]*c];}

/* 1번 방: 시아·모아의 특성표 (설명용 예시값). 칸이 늘면 항이 하나씩 붙는다 */
var FEAT=[['키(cm)',160,163],['몸무게(kg)',50,54],['나이',25,24],['하루 걸음(천 보)',7,8],['수면(시간)',7,6],['통학(km)',12,10],['커피(잔)',2,1],['독서(권/월)',1,2],['운동(회/주)',2,3],['영화(편/월)',3,3]];
/* 100칸일 때 나머지 90칸의 차이: 시드 고정 0·1·−1 */
function extraDiffs(n){var out=[],s=7;for(var i=0;i<n;i++){s=(s*1103515245+12345)%2147483648;var r=s%5;out.push(r===0?1:r===1?-1:0);}return out;}
function personDiff(n){var d=[];for(var i=0;i<Math.min(n,10);i++)d.push(FEAT[i][2]-FEAT[i][1]);if(n>10)d=d.concat(extraDiffs(n-10));return d;}
function personDist(n){return norm(personDiff(n));}

/* 6번 방: 그림자 */
function project(v,u){var k=dot(v,u)/dot(u,u);return mul(u,k);}
function sse(xs,c){var s=0;xs.forEach(function(x){s+=(x-c)*(x-c);});return s;}
var HEIGHTS=[160,162,164];

/* 7번 방: 칸막이 x₁ + 2x₂ + 2x₃ = 6 */
var PLANE={n:[1,2,2],b:6};
function side(p){return dot(PLANE.n,p)-PLANE.b;}
function planeDist(p){return side(p)/norm(PLANE.n);}

/* 9번 방: 껍질 비율 — 반지름 0.9 안쪽이 차지하는 부피 비율 = 0.9ⁿ */
function inner(n,r){return Math.pow(r==null?0.9:r,n);}
/* 반경 이웃: 시드 고정 점 40개 */
function dots40(){var out=[],s=11;function rnd(){s=(s*16807)%2147483647;return s/2147483647;}for(var i=0;i<40;i++)out.push([rnd()*8-4,rnd()*8-4]);return out;}

/* 10번 방 + 대결: 손님 데이터 (설명용 예시값) */
var KNOWN=[['K1',158,48],['K2',160,72],['K3',170,52],['K4',172,66],['K5',165,60],['K6',178,80],['K7',155,58],['K8',175,50],['K9',168,74]];
var NEWC=[['N1',159,70],['N2',171,51],['N3',166,62],['N4',171,75],['N5',157,50],['N6',169,62]];
function size(w){return w<55?'S':w<68?'M':'L';}
var SPREAD={h:8,w:10};   /* 단위 맞추기: 키 8cm, 몸무게 10kg을 한 칸으로 */
function metric(mode){
  if(mode==='mm')return function(q,k){return Math.hypot((q[1]-k[1])*10,q[2]-k[2]);};
  if(mode==='std')return function(q,k){return Math.hypot((q[1]-k[1])/SPREAD.h,(q[2]-k[2])/SPREAD.w);};
  return function(q,k){return Math.hypot(q[1]-k[1],q[2]-k[2]);};}
function nearest(q,mode,list){var f=metric(mode),best=null,bd=Infinity;(list||KNOWN).forEach(function(k){var d=f(q,k);if(d<bd){bd=d;best=k;}});return {k:best,d:bd};}
function duel(){return NEWC.map(function(q){var a=nearest(q,'mm'),b=nearest(q,'std'),t=size(q[2]);
  return {q:q,truth:t,sia:a.k,siaSize:size(a.k[2]),siaOk:size(a.k[2])===t,moa:b.k,moaSize:size(b.k[2]),moaOk:size(b.k[2])===t};});}
/* 10번 방 미니: 새 손님 Q와 후보 A·B */
var UNITQ=['Q',165,60],UNITC=[['A',163,58],['B',165,66]];

/* 10번 방: 지구 위 두 도시 — 호와 현 */
var R_EARTH=6371;
function arc(th){return R_EARTH*rad(th);}
function chord(th){return 2*R_EARTH*Math.sin(rad(th)/2);}

return {dot:dot,norm:norm,sub:sub,add:add,mul:mul,dist:dist,deg:deg,rad:rad,angle:angle,rot:rot,FEAT:FEAT,personDiff:personDiff,personDist:personDist,
  project:project,sse:sse,HEIGHTS:HEIGHTS,PLANE:PLANE,side:side,planeDist:planeDist,inner:inner,dots40:dots40,
  KNOWN:KNOWN,NEWC:NEWC,size:size,SPREAD:SPREAD,metric:metric,nearest:nearest,duel:duel,UNITQ:UNITQ,UNITC:UNITC,R_EARTH:R_EARTH,arc:arc,chord:chord};
})();
if(typeof module!=='undefined')module.exports=EG;
