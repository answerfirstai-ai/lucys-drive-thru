(()=>{
const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
// micro: button label feedback
$$('[data-dir]').forEach(a=>a.addEventListener('click',()=>{const l=$('.lbl',a);if(!l)return;const t=l.textContent;l.textContent='Opening Maps…';setTimeout(()=>l.textContent=t,1600)}));
$$('[data-call]').forEach(a=>a.addEventListener('click',()=>{const l=$('.lbl',a);if(!l)return;const t=l.textContent;l.textContent='Calling…';setTimeout(()=>l.textContent=t,1600)}));
// shelf buttons
const sh=$('[data-shelf]');$$('[data-sh]').forEach(b=>b.addEventListener('click',()=>sh&&sh.scrollBy({left:+b.dataset.sh*sh.clientWidth*.8,behavior:'smooth'})));
// click-to-load map
$$('[data-loadmap]').forEach(b=>b.addEventListener('click',()=>{const f=document.createElement('iframe');f.title="Map of Lucy's Drive Thru, 1568 W Pico Blvd";f.loading='lazy';f.referrerPolicy='no-referrer-when-downgrade';f.src='https://maps.google.com/maps?q=Lucy%27s%20Drive%20Thru%2C%201568%20W%20Pico%20Blvd%2C%20Los%20Angeles%2C%20CA%2090015&z=16&output=embed';b.parentNode.replaceChildren(f)}));
const g=window.gsap;if(!g||!window.ScrollTrigger){$$('.sign .box').forEach(b=>b.style.opacity=1);const sg=$('.sign');sg&&sg.classList.add('lit');return}
g.registerPlugin(ScrollTrigger);ScrollTrigger.config({ignoreMobileResize:true});
const mm=g.matchMedia();
mm.add({isDesktop:'(min-width: 810px)',isMobile:'(max-width: 809px)',reduce:'(prefers-reduced-motion: reduce)'},ctx=>{
 const {isDesktop,reduce}=ctx.conditions, boxes=$$('.sign [data-box]');
 if(reduce){g.set(boxes,{opacity:1});$('.sign').classList.add('lit');return}
 // hero entrance: fluorescent tubes
 if(boxes.length){
  const tl=g.timeline({defaults:{ease:'power2.out'}});
  tl.from('.hero',{backgroundColor:'#000',duration:.4,ease:'none'})
   .to(boxes,{keyframes:{opacity:[0,1,.3,1,.6,1]},duration:.55,ease:'none',stagger:.2,onStart(){} },.25)
   .add(()=>$('.sign').classList.add('lit'),1.05)
   .from('[data-hero]',{y:24,opacity:0,duration:.5,stagger:.08,ease:'power3.out'},.6)
   .from('.hero .ctas .btn',{scale:.9,opacity:0,duration:.4,stagger:.08,ease:'back.out(1.6)'},1.1)
   .from('.lane',{clipPath:'inset(0 100% 0 0)',duration:.5,stagger:.12,ease:'power1.inOut'},1.3);
  // idle flicker of OPEN 24 HOURS
  let idle;const flick=()=>{idle=g.delayedCall(6+Math.random()*4,()=>{g.fromTo(boxes[0],{opacity:.25},{opacity:1,duration:.15,repeat:1,yoyo:true,ease:'steps(1)',onComplete:()=>g.set(boxes[0],{opacity:1})});flick()})};
  ScrollTrigger.create({trigger:'.hero',start:'top top',end:'bottom top',onToggle:s=>{idle&&idle.kill();if(s.isActive)flick()}});
  if(matchMedia('(pointer:fine)').matches)boxes.forEach(b=>b.addEventListener('mouseenter',()=>g.fromTo(b,{opacity:.3},{opacity:1,duration:.3,ease:'steps(3)'})));
 }
 // ch1 pull in
 if($('#pull')){
  const t=g.timeline({scrollTrigger:{trigger:'#pull',start:'top top',end:isDesktop?'+=120%':'+=60%',pin:true,scrub:.6}});
  t.fromTo('.beam',{x:'-60vw',opacity:0},{x:'60vw',opacity:1,duration:1,stagger:.25,ease:'none'},0)
   .to('.beam',{opacity:0,duration:.2},.9)
   .from('[data-board]',{x:'40vw',rotateY:-12,opacity:0,duration:.6,ease:'power2.out'},.1);
  const f=$('[data-flap]');if(f){f.innerHTML=[...f.textContent].map(c=>`<span>${c===' '?'&nbsp;':c}</span>`).join('');
   ScrollTrigger.create({trigger:'[data-board]',start:'top 75%',once:true,onEnter:()=>g.from($$('span',f),{rotateX:90,opacity:0,duration:.25,stagger:.03,ease:'power2.in'})})}
  g.from('.rows li',{opacity:0,x:20,stagger:.06,scrollTrigger:{trigger:'#pull',start:'top 40%',toggleActions:'play none none reverse'}});
 }
 // ch3 sky: dusk -> 3AM -> sunrise
 if($('#sky')){
  const clock=$('[data-clock]'),cap=$('[data-cap]'),hrs=['6 PM','7 PM','8 PM','9 PM','10 PM','11 PM','12 AM','1 AM','2 AM','3 AM','4 AM','5 AM','6 AM'];
  const caps=p=>p<.4?'6 PM. Open.':p<.75?'3 AM. Still open.':'6 AM. Yep, open.';
  const s=g.timeline({scrollTrigger:{trigger:'#sky',start:'top top',end:isDesktop?'+=200%':'+=140%',pin:true,scrub:isDesktop?1:true,
   onUpdate:st=>{const i=Math.round(st.progress*12);if(clock.textContent!==hrs[i])clock.textContent=hrs[i];const c=hrs[i]+'. '+(i===0?'Open.':i===12?'Yep, open.':'Still open.');if(cap.textContent!==c)cap.textContent=c}}});
  s.to('.l-night',{opacity:1,duration:4,ease:'none'},0).to('.stars',{opacity:1,duration:3,ease:'none'},1.5)
   .to('.stars',{opacity:0,duration:2,ease:'none'},7).to('.l-dawn',{opacity:1,duration:3.5,ease:'none'},7.5)
   .to('.sun',{y:0,duration:3.5,ease:'power1.out'},8.5).to('.stamp',{rotate:4,scale:1.06,duration:1,yoyo:true,repeat:5,ease:'sine.inOut'},0);
 }
 // pico line draw + pin drop
 $$('.route').forEach(r=>{g.fromTo($('.pico',r),{strokeDashoffset:400},{strokeDashoffset:0,ease:'none',scrollTrigger:{trigger:r,start:'top 85%',end:'top 35%',scrub:true}});
  g.from($('.pin',r),{y:-60,opacity:0,duration:.9,ease:'bounce.out',scrollTrigger:{trigger:r,start:'top 50%'}})});
 // reveals
 $$('.shelf-h,.cash h2,.find h2,.final h2,.page-hero h1').forEach(el=>g.from(el,{y:40,opacity:0,duration:.7,ease:'power3.out',scrollTrigger:{trigger:el,start:'top 88%'}}));
 g.to('.ticker',{xPercent:-30,ease:'none',scrollTrigger:{trigger:'.cash',start:'top bottom',end:'bottom top',scrub:true}});
});
})();
