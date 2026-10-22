(()=>{
const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
const root=document.documentElement;
const prm=matchMedia('(prefers-reduced-motion: reduce)');
let userOff=localStorage.getItem('lucys-motion')==='off';
const motionOK=()=>!prm.matches&&!userOff;
// micro feedback (never blocks navigation)
$$('[data-dir]').forEach(a=>a.addEventListener('click',()=>{const l=$('.lbl',a);if(!l)return;const t=l.textContent;l.textContent='Opening Maps…';setTimeout(()=>l.textContent=t,1600)}));
$$('[data-call]').forEach(a=>a.addEventListener('click',()=>{const l=$('.lbl',a);if(!l)return;const t=l.textContent;l.textContent='Calling…';setTimeout(()=>l.textContent=t,1600)}));
const sh=$('[data-shelf]');$$('[data-sh]').forEach(b=>b.addEventListener('click',()=>sh&&sh.scrollBy({left:+b.dataset.sh*sh.clientWidth*.8,behavior:motionOK()?'smooth':'auto'})));
$$('[data-loadmap]').forEach(b=>b.addEventListener('click',()=>{const f=document.createElement('iframe');f.title="Map of Lucy's Drive Thru, 1568 W Pico Blvd";f.loading='lazy';f.referrerPolicy='no-referrer-when-downgrade';f.src='https://maps.google.com/maps?q=Lucy%27s%20Drive%20Thru%2C%201568%20W%20Pico%20Blvd%2C%20Los%20Angeles%2C%20CA%2090015&z=16&output=embed';b.parentNode.replaceChildren(f)}));
// motion toggle
const mbtn=$('[data-motion]');
const paintBtn=()=>{if(!mbtn)return;mbtn.setAttribute('aria-pressed',String(!motionOK()));mbtn.textContent='Motion: '+(motionOK()?'on':'off');mbtn.title=motionOK()?'Turn animations off':'Turn animations on'};
let mm,glStop;
const g=window.gsap;
function stopAll(){root.classList.add('no-motion');if(mm){mm.revert();mm=null}if(glStop)glStop();if(window.ScrollTrigger)ScrollTrigger.getAll().forEach(t=>t.kill())}
function startAll(){root.classList.remove('no-motion');if(!g||!window.ScrollTrigger)return;g.registerPlugin(ScrollTrigger);ScrollTrigger.config({ignoreMobileResize:true});
 mm=g.matchMedia();
 mm.add({isDesktop:'(min-width: 810px)',reduce:'(prefers-reduced-motion: reduce)'},ctx=>{
  const {isDesktop,reduce}=ctx.conditions; if(reduce)return;
  // Hero: scroll-linked parallax only (no pin). Content is never hidden.
  if($('.hero')){
   g.to('.hero-media',{yPercent:12,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});
   g.to('.hero-copy',{yPercent:-10,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});
  }
  // Headlights: light sweep across the board while it passes (no pin)
  if($('#pull')){
   g.fromTo('.beam',{x:'-50vw',opacity:0},{x:'50vw',opacity:1,ease:'none',scrollTrigger:{trigger:'#pull',start:'top 80%',end:'bottom 20%',scrub:true}});
   g.fromTo('[data-board]',{rotateY:-8,transformPerspective:1200},{rotateY:0,ease:'none',scrollTrigger:{trigger:'#pull',start:'top 90%',end:'center center',scrub:true}});
  }
  // Sky: night lifts to sunrise as the section passes; camera push-in. No pin.
  if($('#hours')){
   const clock=$('[data-clock]'),hrs=['6 PM','8 PM','10 PM','12 AM','2 AM','3 AM','4 AM','5 AM','6 AM'];
   g.timeline({scrollTrigger:{trigger:'#hours',start:'top bottom',end:'bottom top',scrub:true,
    onUpdate:st=>{const i=Math.min(hrs.length-1,Math.max(0,Math.round((st.progress-.15)/.7*(hrs.length-1))));if(clock.textContent!==hrs[i])clock.textContent=hrs[i]}}})
    .fromTo('.night',{opacity:.92},{opacity:.15,ease:'none'},0).fromTo('.stars',{opacity:.9},{opacity:0,ease:'none'},0)
    .fromTo('.sky-pic',{scale:1.15,yPercent:-6},{scale:1,yPercent:6,ease:'none'},0);
  }
  $$('.route').forEach(r=>g.fromTo($('.pico',r),{strokeDashoffset:400},{strokeDashoffset:0,ease:'none',scrollTrigger:{trigger:r,start:'top 90%',end:'top 40%',scrub:true}}));
  // Subtle reveals: transform only, content stays readable/clickable
  $$('.shelf-h,.cash h2,.find h2,.final h2,.mcat,.fcard').forEach(el=>g.from(el,{y:24,duration:.5,ease:'power2.out',scrollTrigger:{trigger:el,start:'top 95%',once:true}}));
 });
 if(matchMedia('(min-width: 1024px) and (pointer:fine)').matches)loadGL();
}
// three.js PBR accent: desktop only, lazy, decorative, pauses off-screen
function loadGL(){const cv=$('.gl');if(!cv||glStop)return;
 const io=new IntersectionObserver(async es=>{if(!es[0].isIntersecting||glStop)return;io.disconnect();
  try{const T=await import('https://cdn.jsdelivr.net/npm/three@0.169.0/build/three.module.min.js');
   const {RoomEnvironment}=await import('https://cdn.jsdelivr.net/npm/three@0.169.0/examples/jsm/environments/RoomEnvironment.js/+esm');
   const r=new T.WebGLRenderer({canvas:cv,antialias:true,alpha:true});r.setPixelRatio(Math.min(devicePixelRatio,1.5));
   const sc=new T.Scene(),cam=new T.PerspectiveCamera(35,1,.1,100);cam.position.set(0,0,9);
   const pm=new T.PMREMGenerator(r);sc.environment=pm.fromScene(new RoomEnvironment(),.04).texture;
   const glass=new T.MeshPhysicalMaterial({color:0xffd27a,emissive:0xffb238,emissiveIntensity:1.6,roughness:.15,transmission:.4,thickness:.5,clearcoat:1});
   const steel=new T.MeshStandardMaterial({color:0x9aa3b5,metalness:1,roughness:.28});
   const grp=new T.Group();const tube=new T.Mesh(new T.TorusGeometry(1.6,.09,24,120),glass);const ring=new T.Mesh(new T.TorusGeometry(1.85,.05,16,120),steel);
   const tube2=new T.Mesh(new T.TorusGeometry(1.2,.07,24,100),glass);tube2.rotation.x=1.2;grp.add(tube,ring,tube2);sc.add(grp);
   const pl=new T.PointLight(0xffb238,30,20);pl.position.set(2,1,3);sc.add(pl);
   let run=true,raf;const size=()=>{const w=cv.clientWidth,h=cv.clientHeight;r.setSize(w,h,false);cam.aspect=w/h;cam.updateProjectionMatrix();grp.position.x=w>h?3.2:0};size();addEventListener('resize',size);
   const vis=new IntersectionObserver(e=>{run=e[0].isIntersecting;if(run)loop()});vis.observe(cv);
   const loop=()=>{if(!run||glStop===null)return;grp.rotation.y+=.004;grp.rotation.z+=.0015;r.render(sc,cam);raf=requestAnimationFrame(loop)};
   cv.classList.add('on');loop();glStop=()=>{run=false;cancelAnimationFrame(raf);cv.classList.remove('on');vis.disconnect();glStop=undefined};
  }catch(e){/* decorative only */}
 },{rootMargin:'200px'});io.observe(cv);glStop=undefined}
paintBtn();
if(motionOK())startAll();else root.classList.add('no-motion');
mbtn&&mbtn.addEventListener('click',()=>{userOff=motionOK();localStorage.setItem('lucys-motion',userOff?'off':'on');if(userOff)stopAll();else startAll();paintBtn()});
prm.addEventListener&&prm.addEventListener('change',()=>{paintBtn();if(!motionOK())stopAll();else startAll()});
// Esc skips all motion instantly
addEventListener('keydown',e=>{if(e.key==='Escape'&&motionOK()){userOff=true;localStorage.setItem('lucys-motion','off');stopAll();paintBtn()}});
})();
