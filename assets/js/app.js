(()=>{const d=document,h=d.documentElement,rm=matchMedia('(prefers-reduced-motion: reduce)').matches;h.classList.add('js');
const nav=d.querySelector('.nav'),bt=d.querySelector('.burger');
if(bt){bt.addEventListener('click',()=>{const o=nav.classList.toggle('open');bt.setAttribute('aria-expanded',o)});
d.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');bt.setAttribute('aria-expanded','false');bt.focus()}});
nav.querySelectorAll('.links a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');bt.setAttribute('aria-expanded','false')}))}
// skip intro on any input
const skip=()=>{d.body.classList.add('done');['wheel','touchstart','keydown','pointerdown'].forEach(t=>removeEventListener(t,skip))};
['wheel','touchstart','keydown','pointerdown'].forEach(t=>addEventListener(t,skip,{passive:true,once:true}));setTimeout(skip,1300);
// clock
const c=d.querySelector('[data-clock]');if(c&&!rm){let s=3*3600+7*60+12;const f=n=>String(n).padStart(2,'0');setInterval(()=>{s++;const H=Math.floor(s/3600)%12||12,M=Math.floor(s/60)%60;c.textContent=`${f(H)}:${f(M)}:${f(s%60)} AM`},1000)}else if(c)c.textContent='03:07 AM';
// time codes roll in
if('IntersectionObserver'in window&&!rm){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('roll');io.unobserve(e.target)}}));d.querySelectorAll('section:not(.hero) .tc').forEach(t=>io.observe(t))}
// puddle
const p=d.querySelector('[data-puddle]');if(!p||rm)return;
const disp=d.querySelector('#rip feDisplacementMap'),tb=d.querySelector('#rip feTurbulence');let tk=0;
const onS=()=>{if(tk)return;tk=requestAnimationFrame(()=>{tk=0;const r=p.getBoundingClientRect(),k=Math.max(0,Math.min(1,-r.top/r.height*1.6));disp.setAttribute('scale',(10+k*40).toFixed(1));tb.setAttribute('baseFrequency',`0.008 ${(0.05+k*0.04).toFixed(3)}`)})};
addEventListener('scroll',onS,{passive:true});onS();
p.addEventListener('pointermove',e=>{const r=p.getBoundingClientRect();disp.setAttribute('scale',(20+40*Math.abs(e.clientX-r.left-r.width/2)/r.width*2).toFixed(1))},{passive:true});
})();
