# Gera deploy/comecar.html: landing page escondida para quem chega pelos anúncios
import re
full=open("deploy/index.html").read()
WA="https://wa.me/5579996041731?text=Ol%C3%A1%2C%20Nelson.%20Vi%20seu%20an%C3%BAncio%20e%20gostaria%20de%20agendar%20a%20entrevista%20inicial."
A=f'href="{WA}" target="_blank" rel="noopener"'
header=f'''<header>
  <div class="wrap">
    <span class="brand"><img src="mono_acol.png" alt="" width="58" height="21"><span>Nelson Mendonça Neto<br>Psicólogo e Psicanalista</span></span>
    <nav aria-label="Ação principal"><a class="btn btn-dark" {A}>Agendar entrevista</a></nav>
  </div>
</header>'''
main=f'''<main id="inicio" tabindex="-1">
<section class="hero2">
  <picture><source media="(min-width:761px)" type="image/webp" srcset="nelson_hero_wide.webp"><source media="(min-width:761px)" srcset="nelson_hero_wide.jpg"><source type="image/webp" srcset="nelson_hero.webp"><img class="hero-photo" src="nelson_hero.jpg" alt="Nelson Mendonça Neto, psicólogo e psicanalista" fetchpriority="high"></picture>
  <div class="hero-side hero-left"><b class="hs-name">Nelson<br>Mendonça<br>Neto</b><span class="hs-bar" aria-hidden="true"></span><span class="hs-info"><span>Psicólogo e Psicanalista</span><span>CRP 19/3888</span><span class="hero-aud">Psicanálise online</span><span class="hero-aud2">Brasileiros no exterior<br>Adultos no Brasil</span></span></div>
  <a class="pill hero-right" {A}>Agendar entrevista inicial <span aria-hidden="true">→</span></a>
  <h1 class="hero-h1">Há coisas que só mudam quando <em>são ditas.</em></h1>
</section>

<section class="intro lp-intro"><div class="wrap">
  <p class="intro-lead">Um espaço de escuta, no seu tempo, para olhar com cuidado <em style="color:var(--terra)">para o que está pesando.</em></p>
  <p class="intro-sub">Atendimento online, em português, para adultos no Brasil e brasileiros em qualquer país, num horário fixo que, com o tempo, vira um lugar seu.</p>
</div></section>

<section class="recog lp-recog"><div class="wrap">
  <p class="eb">Talvez seja o seu momento se…</p>
  <h2>Às vezes a vida segue funcionando, <em>mas algo não sai do lugar.</em></h2>
  <ul>
    <li>Algo se repete na sua vida e você não sabe bem por quê.</li>
    <li>A angústia, o cansaço ou a tristeza estão ocupando espaço demais.</li>
    <li>Construiu uma vida em outro país, e a saudade virou peso.</li>
    <li>Você quer se conhecer melhor, não apenas aliviar um sintoma.</li>
  </ul>
</div></section>

<section class="process lp-steps"><div class="wrap">
  <p class="eb">Como começar</p>
  <h2>Três passos, <em>sem pressa.</em></h2>
  <div class="steps">
    <div class="step"><h3>1. Você me chama</h3><p>Pelo WhatsApp. Combinamos um horário e eu te passo as informações da entrevista.</p></div>
    <div class="step"><h3>2. Entrevista inicial</h3><p>Um encontro online para escutar o seu momento e avaliarmos juntos se faz sentido seguir.</p></div>
    <div class="step"><h3>3. Combinamos o acompanhamento</h3><p>Frequência, horários e honorários são conversados ali, de forma individual.</p></div>
  </div>
  <p class="lp-cta"><a class="pill pill-dark" {A}>Agendar entrevista inicial <span aria-hidden="true">→</span></a></p>
</div></section>

<section class="about"><div class="wrap">
  <img class="cutout" src="foto_sobre.webp" alt="Nelson Mendonça Neto" decoding="async">
  <div class="about-txt">
    <p class="eb">Quem vai te escutar</p>
    <h2>Uma clínica voltada <em>à vida adulta.</em></h2>
    <p class="lead" style="margin-top:18px">Sou psicólogo e psicanalista e atendo desde 2020. Escuto relações, escolhas, desejo, trabalho e repetição: o modo como alguém tenta sustentar a própria vida sem desaparecer dela.</p>
    <p>Atendo online pessoas em todo o Brasil e brasileiros no exterior, no fuso de cada um.</p>
    <p class="about-more"><a class="pill pill-acol" href="sobre.html">Conheça minha trajetória <span aria-hidden="true">→</span></a></p>
    <p class="crp">Psicólogo e Psicanalista · CRP 19/3888</p>
  </div>
</div></section>

<section id="duvidas"><div class="wrap">
  <p class="eb">Dúvidas rápidas</p>
  <h2>Antes de <em>começar.</em></h2>
  <details><summary>A análise online funciona?</summary><p>Sim. O que sustenta o trabalho é a escuta e a regularidade dos encontros. Basta um lugar reservado e boa conexão.</p></details>
  <details><summary>É sigiloso?</summary><p>Sim, sempre. Tudo o que você disser fica entre nós.</p></details>
  <details><summary>Moro em outro país. Como funciona?</summary><p>Os horários são ajustados ao seu fuso e a cobrança é feita na moeda do seu país, sem conversões.</p></details>
  <details><summary>Quanto custa?</summary><p>O valor da entrevista inicial é informado quando você agenda. O do acompanhamento é combinado com você na própria entrevista.</p></details>
  <details><summary>Preciso saber exatamente o que falar?</summary><p>Não. A análise também começa pelo que ainda não está organizado.</p></details>
</div></section>

<section class="slogan" id="contato"><div class="wrap lp-end">
  <img class="closing-mono" src="mono_acol.png" alt="" width="120" height="44">
  <h2 class="lp-end-h">O primeiro passo pode ser <span>só uma conversa.</span></h2>
  <p style="margin-top:28px"><a class="btn btn-dark" {A}>Agendar entrevista inicial</a></p>
</div></section>
</main>'''
css='''
/* ===== landing page dos anúncios ===== */
.lp-intro .wrap{max-width:860px;text-align:center}.lp-intro .intro-sub{margin-inline:auto;max-width:56ch}.lp-intro .intro-lead{margin-inline:auto}
.lp-recog{padding-top:clamp(64px,9vw,112px)}
.lp-steps .steps{grid-template-columns:repeat(3,1fr)}
@media (max-width:820px){.lp-steps .steps{grid-template-columns:1fr}}
.lp-cta{margin-top:40px}
.lp-end{text-align:center}
.lp-end .closing-mono{margin:0 auto 24px;display:block}
.lp-end-h{font-family:var(--display);font-weight:400;font-size:clamp(32px,4.4vw,54px);line-height:1.1;color:var(--paper)}
.lp-end-h span{display:block;font-style:italic;color:var(--acol)}
'''
a=full.index('<header>'); b=full.index('</main>')+7
out=full[:a]+header+"\n\n"+main+full[b:]
out=out.replace("</style>",css+"</style>",1)
# sem trilha nem menu
out=re.sub(r'<button class="trilha".*?</button>\n?','',out,flags=re.S)
out=re.sub(r'<script data-persist>.*?</script>\n?','',out,flags=re.S)
out=re.sub(r'<script type="application/ld\+json">.*?</script>\n?','',out,flags=re.S)
out=out.replace('<title>Nelson Mendonça Neto · Psicanálise</title>','<title>Psicanálise online · Nelson Mendonça Neto</title>\n<meta name="robots" content="noindex, follow">')
out=out.replace('<link rel="canonical" href="https://nelsonmendonca.com/">','<link rel="canonical" href="https://nelsonmendonca.com/comecar">')
out=out.replace('<meta property="og:url" content="https://nelsonmendonca.com/">','<meta property="og:url" content="https://nelsonmendonca.com/comecar">')
out=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Psicanálise online com Nelson Mendonça Neto, psicólogo e psicanalista. O primeiro passo é uma entrevista inicial.">',out)
assert 'trilha' not in out.split('</style>',1)[1], "trilha restante"
open("deploy/comecar.html","w").write(out)
print("ok")
