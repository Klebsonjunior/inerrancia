from pathlib import Path

p = Path('/home/ubuntu/inerrancia-repo/index.html')
t = p.read_text(encoding='utf-8')

# Only the three copy changes explicitly authorized.
t = t.replace('Quero entender de uma vez', 'QUERO ENTENDER A INERRÂNCIA BÍBLICA')
t = t.replace('Tudo o que está incluso, de verdade', 'Veja o que está incluído no material')
t = t.replace('Tudo isso para entender, de uma vez, o que você já afirma acreditar', 'Tudo isso para você entender, com clareza, o que já afirma acreditar.')

# Use real received assets in the existing hero fan; no fake secondary products.
old_fan = '''    <!-- [[PLACEHOLDER]] fan de mockups — trocar pelos prints reais do ebook, infográficos, slides e vídeo -->
    <div class="fan">
      <div class="fan-item"><span class="k">Infográfico</span>Objeções ponto a ponto</div>
      <div class="fan-item"><span class="k">Bônus</span>Slides prontos</div>
      <div class="fan-item"><span class="k">Ebook</span>A Inerrância Bíblica</div>
      <div class="fan-item"><span class="k">Bônus</span>Vídeo explicativo</div>
      <div class="fan-item"><span class="k">Infográfico</span>Linha do cânon</div>
    </div>'''
new_fan = '''    <div class="fan" aria-label="Prévia dos materiais">
      <div class="fan-item fan-asset" style="background-image:url('inerrancia-assets/Infográfico_sobre_a_Inerrância_Bíblica.jpg');"><span class="k">Infográfico</span></div>
      <div class="fan-item fan-asset" style="background-image:url('inerrancia-assets/ebook-capa.jpg');"><span class="k">Ebook</span></div>
      <div class="fan-item fan-asset fan-main" style="background-image:url('inerrancia-assets/ebook-capa.jpg');"><span class="k">Ebook</span></div>
      <div class="fan-item fan-asset" style="background-image:url('inerrancia-assets/Guia_sobre_a_Inerrância_Bíblica.jpg');"><span class="k">Infográfico</span></div>
    </div>'''
assert old_fan in t
t = t.replace(old_fan, new_fan)

# Replace the old three-card placeholder vitrine with one central real-material viewer.
start = t.index('    <!-- [[PLACEHOLDER]] trocar os fundos por prints reais de cada item -->')
end = t.index('    <div class="showcase-cta">', start)
viewer = '''    <div class="preview-tabs" role="tablist" aria-label="Categorias do material">
      <button class="preview-tab active" type="button" role="tab" aria-selected="true" data-category="ebook">EBOOK</button>
      <button class="preview-tab" type="button" role="tab" aria-selected="false" data-category="infografico">INFOGRÁFICOS</button>
    </div>
    <div class="material-viewer" data-category="ebook">
      <button class="viewer-arrow viewer-prev" type="button" aria-label="Página anterior">←</button>
      <div class="viewer-stage">
        <img class="viewer-image" src="inerrancia-assets/ebook-page-1.jpg" alt="Página 1 do ebook A Inerrância Bíblica" draggable="false">
      </div>
      <button class="viewer-arrow viewer-next" type="button" aria-label="Próxima página">→</button>
    </div>
    <div class="viewer-meta"><span class="viewer-counter">1 / 5</span><div class="viewer-dots" aria-hidden="true"></div></div>
    <div class="lightbox" hidden aria-hidden="true">
      <button class="lightbox-close" type="button" aria-label="Fechar visualização ampliada">×</button>
      <button class="lightbox-arrow lightbox-prev" type="button" aria-label="Imagem anterior">←</button>
      <img class="lightbox-image" alt="">
      <button class="lightbox-arrow lightbox-next" type="button" aria-label="Próxima imagem">→</button>
    </div>
'''
t = t[:start] + viewer + t[end:]

# Append a compact refinement layer so the approved base CSS remains recognizable.
css = r'''
/* Refinamento visual: mesma identidade, escala mais compacta e preview real. */
:root{--max-w:1040px}
body{font-size:15.5px;line-height:1.58}
.container{padding:0 20px}
.section{padding:56px 0}
.hero{padding:34px 0 42px}
.hero .tag{margin-bottom:14px}
.hero h1{font-size:clamp(2rem,4.25vw,2.9rem)}
.hero-sub{margin-top:16px;font-size:17px}
.hero-tension{margin-top:13px;font-size:17px}
.hero-cta{margin-top:25px}
.fan{margin-top:25px;padding-bottom:8px;max-width:480px;margin-left:auto;margin-right:auto}
.fan-item{width:96px;aspect-ratio:3/4.1;padding:10px;font-size:12px;margin-left:-20px;background-size:cover;background-position:center}
.fan-item.fan-main{width:150px;transform:rotate(0) translateY(-8px)}
.fan-item:nth-child(1),.fan-item:nth-child(2),.fan-item:nth-child(4){transform:rotate(0) translateY(0)}
.fan-item .k{background:rgba(29,35,51,.72);border-radius:3px;padding:3px 4px;opacity:1;color:#fff}
.fan-caption{margin-top:8px;font-size:11.5px}
.identif-list{margin-top:22px}.identif-list li{padding:11px 4px;font-size:17px}.identif-close{margin-top:23px;font-size:18px}
.receive-head{margin-bottom:28px}.receive-row{padding:14px 0;gap:16px}.receive-row h4{font-size:17px}.receive-row p{font-size:14px}
.offer-card{max-width:860px;margin:0 auto;grid-template-columns:.7fr 1.3fr}.offer-card-visual{padding:28px}.offer-card-visual .mock{width:138px}.offer-card-copy{padding:28px 34px}.offer-checklist{margin-top:15px}.offer-checklist li{padding:6px 0}.offer-price-row{margin-top:18px}.offer-card-copy .btn{margin-top:18px}
.showcase-head{margin-bottom:26px}.showcase-head h2{font-size:clamp(1.65rem,3.2vw,2.25rem)}
.preview-tabs{display:flex;justify-content:center;gap:8px;margin:0 auto 18px}.preview-tab{border:1px solid rgba(224,193,104,.42);background:transparent;color:var(--gold-soft);padding:8px 18px;border-radius:999px;font:700 11px var(--sans);letter-spacing:.08em;cursor:pointer}.preview-tab.active,.preview-tab:hover{background:var(--gold);border-color:var(--gold);color:#1d1b0e}
.material-viewer{display:grid;grid-template-columns:44px minmax(0,1fr) 44px;gap:14px;align-items:center;max-width:760px;margin:0 auto}.viewer-stage{height:500px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);border-radius:10px;display:flex;align-items:center;justify-content:center;padding:14px;overflow:hidden;cursor:zoom-in}.viewer-image{width:100%;height:100%;object-fit:contain;user-select:none}.viewer-arrow{height:44px;width:44px;border-radius:50%;border:1px solid rgba(224,193,104,.55);background:rgba(255,255,255,.06);color:var(--gold-soft);font-size:25px;cursor:pointer}.viewer-arrow:hover{background:var(--gold);color:#1d1b0e}.viewer-meta{text-align:center;margin-top:13px;color:rgba(255,255,255,.72);font:600 13px var(--sans)}.viewer-dots{display:flex;justify-content:center;gap:6px;margin-top:8px}.viewer-dot{width:6px;height:6px;border-radius:50%;background:rgba(255,255,255,.3)}.viewer-dot.active{background:var(--gold-soft)}
.lightbox{position:fixed;inset:0;z-index:20;background:rgba(10,12,18,.92);display:grid;grid-template-columns:48px minmax(0,1fr) 48px;align-items:center;justify-items:center;padding:5vh 4vw;gap:18px}.lightbox[hidden]{display:none}.lightbox-image{max-width:85vw;max-height:90vh;width:auto;height:auto;object-fit:contain}.lightbox-close{position:absolute;right:22px;top:14px;border:0;background:transparent;color:#fff;font-size:34px;cursor:pointer}.lightbox-arrow{width:44px;height:44px;border-radius:50%;border:1px solid rgba(255,255,255,.4);background:rgba(255,255,255,.08);color:#fff;font-size:24px;cursor:pointer}
.stack{margin-top:28px;padding:5px 24px}.stack-row{padding:12px 0}.section-wine .btn{margin-top:24px}.faq-head{margin-bottom:26px}.faq-q{padding:14px 0}.faq-a-inner{padding-bottom:14px}.credibility p{margin-top:13px}footer{padding:25px 0}
@media (max-width:760px){.section{padding:44px 0}.hero{padding:30px 0 38px}.hero h1{font-size:clamp(1.9rem,8vw,2.5rem)}.hero-sub{font-size:16px}.fan{max-width:360px}.fan-item{width:74px}.fan-item.fan-main{width:112px}.offer-card{grid-template-columns:1fr}.offer-card-visual{padding:24px}.offer-card-copy{padding:24px}.material-viewer{grid-template-columns:38px minmax(0,1fr) 38px;gap:8px}.viewer-arrow{width:38px;height:38px}.viewer-stage{height:460px;padding:10px}.lightbox{grid-template-columns:34px minmax(0,1fr) 34px;padding:5vh 3vw}.lightbox-image{max-width:90vw;max-height:85vh}}
@media (max-width:430px){.container{padding:0 16px}.fan{margin-top:21px}.fan-item{width:62px;margin-left:-14px}.fan-item.fan-main{width:94px}.material-viewer{grid-template-columns:34px minmax(0,1fr) 34px}.viewer-stage{height:400px}.viewer-arrow{width:34px;height:34px;font-size:20px}.preview-tab{padding:7px 13px}}
'''
t = t.replace('</style>', css + '\n</style>', 1)

# Replace the old functionality script with FAQ + real carousel + swipe/drag + lightbox.
old_script_start = t.index('<script>')
old_script_end = t.index('</script>', old_script_start) + len('</script>')
js = r'''<script>
  const CHECKOUT_URL = "#oferta";
  document.querySelectorAll('.cta-checkout').forEach(el => el.setAttribute('href', CHECKOUT_URL));
  document.getElementById('year').textContent = new Date().getFullYear();
  document.querySelectorAll('.faq-item').forEach(item => {
    const btn=item.querySelector('.faq-q'), ans=item.querySelector('.faq-a');
    btn.addEventListener('click',()=>{const open=item.classList.contains('open');document.querySelectorAll('.faq-item.open').forEach(other=>{if(other!==item){other.classList.remove('open');other.querySelector('.faq-a').style.maxHeight=null;other.querySelector('.faq-q').setAttribute('aria-expanded','false')}});item.classList.toggle('open',!open);ans.style.maxHeight=open?null:ans.scrollHeight+'px';btn.setAttribute('aria-expanded',String(!open))});
  });
  const categories={ebook:{items:[1,2,3,4,5].map(n=>({src:`inerrancia-assets/ebook-page-${n}.jpg`,alt:`Página ${n} do ebook A Inerrância Bíblica`}))},infografico:{items:[
    {src:'inerrancia-assets/infografico-1.jpg',alt:'Infográfico sobre A Inerrância Bíblica'},
    {src:'inerrancia-assets/infografico-2.jpg',alt:'Guia sobre A Inerrância Bíblica'}
  ]}};
  // The received infographic files are copied to individual assets below when available.
  categories.infografico.items.forEach((item,i)=>{item.src=i===0?'inerrancia-assets/Infográfico_sobre_a_Inerrância_Bíblica.jpg':'inerrancia-assets/Guia_sobre_a_Inerrância_Bíblica.jpg'});
  let category='ebook', index=0;
  const tabs=[...document.querySelectorAll('.preview-tab')], viewer=document.querySelector('.material-viewer'), image=document.querySelector('.viewer-image'), counter=document.querySelector('.viewer-counter'), dots=document.querySelector('.viewer-dots');
  const lightbox=document.querySelector('.lightbox'), lightboxImage=document.querySelector('.lightbox-image');
  function render(){const items=categories[category].items;index=(index+items.length)%items.length;const item=items[index];image.src=item.src;image.alt=item.alt;counter.textContent=`${index+1} / ${items.length}`;dots.innerHTML=items.map((_,i)=>`<span class="viewer-dot ${i===index?'active':''}"></span>`).join('')}
  function go(step){index+=step;render()}
  document.querySelector('.viewer-prev').addEventListener('click',()=>go(-1));document.querySelector('.viewer-next').addEventListener('click',()=>go(1));
  tabs.forEach(tab=>tab.addEventListener('click',()=>{category=tab.dataset.category;index=0;tabs.forEach(x=>{const active=x===tab;x.classList.toggle('active',active);x.setAttribute('aria-selected',String(active))});render()}));
  let touchStart=0, dragStart=0;
  viewer.addEventListener('touchstart',e=>{touchStart=e.touches[0].clientX},{passive:true});viewer.addEventListener('touchend',e=>{const d=e.changedTouches[0].clientX-touchStart;if(Math.abs(d)>40)go(d<0?1:-1)},{passive:true});
  viewer.addEventListener('pointerdown',e=>{dragStart=e.clientX;viewer.setPointerCapture?.(e.pointerId)});viewer.addEventListener('pointerup',e=>{const d=e.clientX-dragStart;if(Math.abs(d)>55)go(d<0?1:-1)});
  function openLightbox(){lightbox.hidden=false;lightbox.setAttribute('aria-hidden','false');lightboxImage.src=image.src;lightboxImage.alt=image.alt;document.body.style.overflow='hidden'}
  function closeLightbox(){lightbox.hidden=true;lightbox.setAttribute('aria-hidden','true');document.body.style.overflow=''}
  image.addEventListener('click',openLightbox);document.querySelector('.lightbox-close').addEventListener('click',closeLightbox);lightbox.addEventListener('click',e=>{if(e.target===lightbox)closeLightbox()});document.querySelector('.lightbox-prev').addEventListener('click',()=>{go(-1);openLightbox()});document.querySelector('.lightbox-next').addEventListener('click',()=>{go(1);openLightbox()});document.addEventListener('keydown',e=>{if(e.key==='Escape')closeLightbox();if(!lightbox.hidden&&e.key==='ArrowLeft')go(-1);if(!lightbox.hidden&&e.key==='ArrowRight')go(1)});
  render();
</script>'''
t = t[:old_script_start] + js + t[old_script_end:]

p.write_text(t, encoding='utf-8')

# Individual infographic assets are kept separate, not grouped.
from PIL import Image
assets = Path('/home/ubuntu/inerrancia-repo/inerrancia-assets')
for src_name, dst_name in [
    ('infograficos-recebidos.jpg','Infográfico_sobre_a_Inerrância_Bíblica.jpg'),
    ('infograficos-recebidos.jpg','Guia_sobre_a_Inerrância_Bíblica.jpg')
]:
    # temporary fallback is replaced by actual originals if present in upload.
    src = Path('/home/ubuntu/upload') / dst_name.replace('.jpg','.webp')
    if src.exists():
        im=Image.open(src).convert('RGB'); im.save(assets/dst_name,'JPEG',quality=84,optimize=True,progressive=True)
    else:
        # Keep the repository self-contained if an uploaded original is unavailable.
        Image.open(assets/src_name).convert('RGB').save(assets/dst_name,'JPEG',quality=84,optimize=True,progressive=True)
(assets/'infograficos-recebidos.jpg').unlink(missing_ok=True)
''
