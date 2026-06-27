// ====== 导航滚动效果 ======
const navbar = document.getElementById('navbar');
window.addEventListener('scroll',()=>{
  navbar.classList.toggle('scrolled',window.scrollY>60);
});

// ====== 移动端菜单 ======
const toggle=document.getElementById('navToggle');
const links=document.getElementById('navLinks');
toggle.addEventListener('click',()=>links.classList.toggle('open'));
document.querySelectorAll('.nav-links a').forEach(a=>{
  a.addEventListener('click',()=>links.classList.remove('open'));
});

// ====== 滚动渐入观察器 ======
const observer=new IntersectionObserver(entries=>{
  entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');observer.unobserve(e.target)}});
},{threshold:.1});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));

// ====== 项目展示 Canvas 动效 ======
function initProjectCanvas(containerEl,colors){
  if(!containerEl)return;
  const c=document.createElement('canvas');
  c.width=containerEl.clientWidth||400;
  c.height=containerEl.clientHeight||360;
  containerEl.appendChild(c);
  const ctx=c.getContext('2d');

  // 响应式尺寸
  const resize=()=>{
    const rect=containerEl.getBoundingClientRect();
    c.width=rect.width||400;
    c.height=rect.height||360;
  };
  window.addEventListener('resize',resize);

  // 粒子
  const count=70;
  const particles=[];
  for(let i=0;i<count;i++){
    particles.push({
      x:Math.random()*c.width,
      y:Math.random()*c.height,
      vx:(Math.random()-0.5)*0.6,
      vy:(Math.random()-0.5)*0.6,
      r:Math.random()*2+1,
    });
  }

  let frame;
  function draw(){
    ctx.clearRect(0,0,c.width,c.height);

    // 背景渐变
    const grad=ctx.createRadialGradient(c.width/2,c.height/2,0,c.width/2,c.height/2,Math.max(c.width,c.height)*0.7);
    grad.addColorStop(0,colors.bg0);
    grad.addColorStop(1,colors.bg1);
    ctx.fillStyle=grad;
    ctx.fillRect(0,0,c.width,c.height);

    // 连线
    for(let i=0;i<particles.length;i++){
      for(let j=i+1;j<particles.length;j++){
        const dx=particles[i].x-particles[j].x;
        const dy=particles[i].y-particles[j].y;
        const dist=Math.sqrt(dx*dx+dy*dy);
        if(dist<120){
          ctx.beginPath();
          ctx.moveTo(particles[i].x,particles[i].y);
          ctx.lineTo(particles[j].x,particles[j].y);
          ctx.strokeStyle=`rgba(255,255,255,${0.04*(1-dist/120)})`;
          ctx.lineWidth=0.8;
          ctx.stroke();
        }
      }
    }

    // 粒子
    particles.forEach(p=>{
      ctx.beginPath();
      ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fillStyle=colors.dot;
      ctx.fill();

      p.x+=p.vx;
      p.y+=p.vy;
      if(p.x<0||p.x>c.width)p.vx*=-1;
      if(p.y<0||p.y>c.height)p.vy*=-1;
    });

    frame=requestAnimationFrame(draw);
  }
  draw();

  // 清理
  const observer2=new MutationObserver(()=>{
    if(!document.body.contains(c)){
      cancelAnimationFrame(frame);
      observer2.disconnect();
    }
  });
  observer2.observe(document.body,{childList:true,subtree:true});
}

// ====== 从 data 属性初始化 Canvas ======
document.querySelectorAll('[data-canvas-bg0]').forEach(el=>{
  initProjectCanvas(el,{
    bg0: el.dataset.canvasBg0,
    bg1: el.dataset.canvasBg1,
    dot: el.dataset.canvasDot,
  });
});
