export default function(p){const cv=p.querySelector('.pd-gl'),g=cv.getContext('webgl',{premultipliedAlpha:false});if(!g)return;
const img=new Image();img.src=p.querySelector('img').currentSrc;img.decode().then(()=>{
const dpr=Math.min(devicePixelRatio,1.5),W=()=>p.clientWidth*dpr,H=()=>p.clientHeight*dpr;
const tx=document.createElement('canvas');
const draw=()=>{cv.width=W();cv.height=H();tx.width=cv.width;tx.height=cv.height;const c=tx.getContext('2d');
const s=Math.max(cv.width/img.width,cv.height/img.height);c.drawImage(img,(cv.width-img.width*s)/2,(cv.height-img.height*s)/2,img.width*s,img.height*s);
const fs=Math.min(320*dpr,cv.width*.19);c.save();c.globalCompositeOperation='screen';c.globalAlpha=.5;c.fillStyle='#FF6A13';c.font=`900 ${fs}px "Big Shoulders Display"`;c.textBaseline='alphabetic';c.scale(1,-1);c.fillText('STILL ON.',-.04*fs,-.04*fs);c.restore();up()};
const vs='attribute vec2 a;varying vec2 u;void main(){u=a*.5+.5;u.y=1.-u.y;gl_Position=vec4(a,0,1);}';
const fs='precision mediump float;varying vec2 u;uniform sampler2D t;uniform float T;uniform vec2 m;uniform float k;void main(){vec2 q=u;float d=distance(q*vec2(3.,1.),m*vec2(3.,1.));float w=sin(d*38.-T*5.)*exp(-d*3.)*.012*k+sin(q.x*14.+T*1.3)*.002+sin(q.y*60.+T*2.)*.0015;q+=vec2(w*.6,w);vec4 c=texture2D(t,q);c.rgb*=.85+.15*sin(d*38.-T*5.)*k;gl_FragColor=c;}';
const sh=(t,s)=>{const o=g.createShader(t);g.shaderSource(o,s);g.compileShader(o);return o},pr=g.createProgram();g.attachShader(pr,sh(g.VERTEX_SHADER,vs));g.attachShader(pr,sh(g.FRAGMENT_SHADER,fs));g.linkProgram(pr);g.useProgram(pr);
const b=g.createBuffer();g.bindBuffer(g.ARRAY_BUFFER,b);g.bufferData(g.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),g.STATIC_DRAW);const al=g.getAttribLocation(pr,'a');g.enableVertexAttribArray(al);g.vertexAttribPointer(al,2,g.FLOAT,false,0,0);
const te=g.createTexture();g.bindTexture(g.TEXTURE_2D,te);[g.TEXTURE_WRAP_S,g.TEXTURE_WRAP_T].forEach(x=>g.texParameteri(g.TEXTURE_2D,x,g.CLAMP_TO_EDGE));g.texParameteri(g.TEXTURE_2D,g.TEXTURE_MIN_FILTER,g.LINEAR);
function up(){g.bindTexture(g.TEXTURE_2D,te);g.texImage2D(g.TEXTURE_2D,0,g.RGBA,g.RGBA,g.UNSIGNED_BYTE,tx);g.viewport(0,0,cv.width,cv.height)}
const uT=g.getUniformLocation(pr,'T'),uM=g.getUniformLocation(pr,'m'),uK=g.getUniformLocation(pr,'k');let mx=.3,my=.5,k=.4,vis=false,raf=0,t0=performance.now();
p.addEventListener('pointermove',e=>{const r=p.getBoundingClientRect();mx=(e.clientX-r.left)/r.width;my=(e.clientY-r.top)/r.height;k=1});
const loop=n=>{k=Math.max(.25,k*.985);g.uniform1f(uT,(n-t0)/1000);g.uniform2f(uM,mx,my);g.uniform1f(uK,k);g.drawArrays(g.TRIANGLE_STRIP,0,4);raf=vis?requestAnimationFrame(loop):0};
new IntersectionObserver(([e])=>{vis=e.isIntersecting;if(vis&&!raf)raf=requestAnimationFrame(loop)}).observe(p);
document.fonts.ready.then(()=>{draw();p.classList.add('gl')});addEventListener('resize',draw)})}
