# Gera deploy/cursos.html (cursos e palestras), a partir da página de livros (mesmo estilo)
import re, urllib.parse as U
def wa(t): return "https://wa.me/5579996041731?text="+U.quote(t)
W_CURSO=wa("Olá, Nelson. Vim pelo site e quero ser avisado(a) quando abrirem os cursos.")
W_PAL=wa("Olá, Nelson. Vim pelo site e gostaria de conversar sobre uma palestra ou um encontro.")
full=open("deploy/livros.html").read()
main=f'''<main id="inicio" class="lv" tabindex="-1">
<section class="lv-hero">
  <div class="wrap">
    <nav class="crumb" aria-label="Você está em"><a href="index.html">← Início</a><span aria-hidden="true">/</span><span>Cursos e palestras</span></nav>
    <p class="eb">Para colegas, instituições e grupos</p>
    <h1>Cursos e <em>palestras.</em></h1>
    <p class="lv-lead">Formação para colegas de profissão e encontros abertos para levar a escuta psicanalítica a outros espaços.</p>
  </div>
</section>
<section class="lv-sec" aria-labelledby="t-cursos">
  <div class="wrap lv-two">
    <div class="lv-box">
      <p class="eb">Cursos</p>
      <h2 id="t-cursos">Em <em>preparação.</em></h2>
      <p>Os primeiros cursos estão sendo preparados. Se você quer saber quando abrirem, me avise pelo WhatsApp.</p>
      <a class="pill pill-line" href="{W_CURSO}" target="_blank" rel="noopener">Quero ser avisado <span aria-hidden="true">→</span></a>
    </div>
    <div class="lv-box">
      <p class="eb">Palestras e encontros</p>
      <h2>Para instituições <em>e grupos.</em></h2>
      <p>Escolas, empresas, coletivos e grupos de estudo que queiram levar a escuta psicanalítica para uma conversa aberta.</p>
      <a class="pill pill-line" href="{W_PAL}" target="_blank" rel="noopener">Fazer um convite <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>
</main>'''
a=full.index('<main id="inicio"'); b=full.index('</main>')+7
out=full[:a]+main+full[b:]
out=re.sub(r'<dialog class="bk-dlg".*?</dialog>\n*','',out,flags=re.S)
out=out.replace('aria-current="page" style="color:var(--acol)">Livros e textos</a>','>Livros e textos</a>')
out=out.replace('<a class="hide-m" href="cursos.html">Cursos</a>','<a class="hide-m" href="cursos.html" aria-current="page" style="color:var(--acol)">Cursos</a>')
out=out.replace("<title>Livros e textos · Nelson Mendonça Neto</title>","<title>Cursos e palestras · Nelson Mendonça Neto</title>")
out=out.replace('https://nelsonmendonca.com/livros"','https://nelsonmendonca.com/cursos"')
out=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Cursos de psicanálise para colegas e palestras para instituições e grupos, com Nelson Mendonça Neto, psicólogo e psicanalista.">',out)
out=out.replace('<meta property="og:image" content="https://nelsonmendonca.com/capa_massa.jpg">','<meta property="og:image" content="https://nelsonmendonca.com/nelson_hero.jpg">')
open("deploy/cursos.html","w").write(out)
print("ok cursos")
