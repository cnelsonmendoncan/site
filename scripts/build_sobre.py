# Gera deploy/sobre.html (Quem sou eu completo) com o mesmo cabeçalho e rodapé do site
import re
full=open("deploy/index.html").read()
TL=[("2014–2019","Graduação em Psicologia","Universidade Tiradentes, Sergipe."),
 ("Na graduação","Navegantes Psi","Integrante de um grupo de quatro estudantes que organizava palestras e cursos com psicanalistas renomados e aproximava a psicologia da medicina, da nutrição e de temas como redes sociais, alimentação e ansiedade."),
 ("2017","Estágio em psicologia organizacional","Hospital dos Olhos de Sergipe."),
 ("2017–2019","Estágio no Centro de Combate à Homofobia (CCH)","Governo de Sergipe. Um grupo que buscava enfrentar a homofobia por meio de políticas públicas."),
 ("2018","Estágio em Recursos Humanos","Multiserv."),
 ("2020","Início da clínica","Atendimentos online, para adultos no Brasil e brasileiros no exterior."),
 ("2020–2024","Cofundador e presidente da Nave Social","O braço social do Navegantes Psi: uma clínica criada com mais quatro colegas para que pessoas em situação de vulnerabilidade tivessem acesso a uma psicanálise de qualidade."),
 ("2020–2024","Formação no Círculo Psicanalítico de Sergipe",""),
 ("2024–hoje","Tripé psicanalítico","O estudo da teoria, a análise pessoal, três vezes por semana, e a supervisão dos atendimentos."),
 ("2026","Livro Perverso é quem?",'Psicanálise, sexualidades e o medo do diferente. Em andamento. <a href="livros.html">Saiba mais</a>.'),
 ("2026","Ebook Massa de manobra",'Sobre neuromarketing, manipulação e por que a psicologia é política. <a href="livros.html">Baixar gratuitamente</a>.')]
tl="".join(f'<li><span class="tl-y">{y}</span><div><b>{t}</b>'+(f'<p>{d}</p>' if d else '')+'</div></li>' for y,t,d in TL)
main=f'''<main id="inicio" class="sb" tabindex="-1">
<section class="about sb-about" id="sobre">
  <div class="wrap">
    <img class="cutout" src="foto_sobre.webp" alt="Nelson Mendonça Neto">
    <div class="about-txt">
      <nav class="crumb" aria-label="Você está em"><a href="index.html">← Início</a><span aria-hidden="true">/</span><span>Sobre</span></nav>
      <p class="eb">Quem sou eu</p>
      <h1>Uma clínica voltada <em>à vida adulta.</em></h1>
      <p class="lead" style="margin-top:18px">Psicólogo e psicanalista, escuto relações, escolhas, desejo, trabalho e repetição: o modo como alguém tenta sustentar a própria vida sem desaparecer dela.</p>
      <p>Cheguei à psicanálise por dois caminhos. Na faculdade, ela me parecia a abordagem mais difícil, e isso me instigou: eu pensava que era preciso conhecê-la de verdade antes de criticá-la. Ao mesmo tempo, era a única que parecia capaz de responder a perguntas muito pessoais sobre quem eu sou. Fui atrás dessas respostas, e foi assim que a psicanálise virou o meu caminho.</p>
      <p class="crp">Psicólogo e Psicanalista · CRP 19/3888</p>
    </div>
  </div>
</section>

<section class="sb-tl" aria-labelledby="t-traj">
  <div class="wrap sb-tl-grid">
    <div><p class="eb">Trajetória</p><h2 id="t-traj">Formação <em>e percurso.</em></h2></div>
    <ol class="tl">{tl}</ol>
  </div>
</section>

<section class="sb-story" aria-labelledby="t-hist">
  <div class="wrap sb-story-in">
    <p class="eb">Minha história</p>
    <h2 id="t-hist">O caminho <em>até aqui.</em></h2>
    <p>Me formei em Psicologia pela Universidade Tiradentes, entre 2014 e 2019. Ainda na graduação, fiz parte do Navegantes Psi, um grupo de quatro estudantes que organizava palestras e cursos, convidava psicanalistas renomados e aproximava a psicologia de outras áreas, como a medicina e a nutrição, e de temas do dia a dia, como redes sociais, alimentação e ansiedade.</p>
    <p>Também passei pela psicologia organizacional, no Hospital dos Olhos de Sergipe e no RH da Multiserv, e por dois anos estagiei no Centro de Combate à Homofobia (CCH) do Governo de Sergipe, num grupo que buscava enfrentar a homofobia por meio de políticas públicas.</p>
    <p>Em 2020, com mais quatro colegas, fundei a Nave Social, o braço social do Navegantes Psi: uma clínica para que pessoas em situação de vulnerabilidade tivessem acesso a uma psicanálise de qualidade. Estive à frente dela, como presidente, até 2024.</p>
    <p>No mesmo ano, comecei minha formação em psicanálise no Círculo Psicanalítico de Sergipe. Com o tempo, percebi que não me identificava com aquele modelo e, em 2024, escolhi seguir um caminho mais freudiano: o tripé que sustenta a formação de todo psicanalista. O estudo da teoria, a minha própria análise, três vezes por semana, e a supervisão dos meus atendimentos. É esse percurso que sigo até hoje.</p>
    <p>Atendo desde 2020, online, adultos no Brasil e brasileiros no exterior, em português.</p>
  </div>
</section>

<section class="sb-next" aria-labelledby="t-proximo">
  <div class="wrap sb-two">
    <div class="lv-box"><p class="eb">Também escrevo</p><h2 id="t-proximo">Massa <em>de manobra.</em></h2>
      <p>Um ebook gratuito para psicólogos sobre neuromarketing, manipulação e por que a psicologia é política.</p>
      <a class="pill pill-line" href="livros.html">Ver livros e cursos <span aria-hidden="true">→</span></a></div>
    <div class="lv-box"><p class="eb">Para começar</p><h2>O primeiro passo é <em>uma conversa.</em></h2>
      <p>Tudo começa por uma entrevista inicial, para entender o seu momento e combinar como seguimos.</p>
      <a class="pill pill-dark" href="pagamento.html">Quero começar <span aria-hidden="true">→</span></a></div>
  </div>
</section>
</main>'''
css='''
/* ===== página Sobre ===== */
.sb-about{padding-top:clamp(56px,7vw,96px)!important}
.sb-about .about-txt{padding-bottom:clamp(56px,7vw,96px)}
.sb-about .crumb{display:flex;gap:10px;font-size:13px;color:#9AA3AF;margin-bottom:26px}.sb-about .crumb a{color:var(--acol);text-decoration:none;font-weight:700}
.sb h1{font-family:var(--display);font-weight:400;font-size:clamp(40px,5vw,64px);line-height:1.04;letter-spacing:-.02em}
.sb h1 em{font-style:italic;font-weight:300;color:var(--acol)}
.sb-about .about-txt p+p{margin-top:16px}
.sb-tl{background:#F2EBE0 url(tex_paper.jpg) center/cover;padding:clamp(56px,7vw,96px) 0}
.sb-tl-grid{display:grid;grid-template-columns:minmax(220px,.8fr) 2fr;gap:clamp(24px,5vw,72px);align-items:start}
.sb-tl h2,.sb-story h2{font-family:var(--display);font-weight:400;font-size:clamp(30px,3.6vw,44px);line-height:1.08;margin-top:6px}
.sb-tl h2 em,.sb-story h2 em{font-style:italic;font-weight:300;color:var(--terra)}
.tl{list-style:none;margin:0;padding:0;border-left:2px solid var(--terra)}
.tl li{display:grid;grid-template-columns:120px 1fr;gap:20px;padding:0 0 26px 24px;position:relative}
.tl li::before{content:"";position:absolute;left:-7px;top:6px;width:12px;height:12px;border-radius:50%;background:#F2EBE0;border:2px solid var(--terra)}
.tl-y{font-family:var(--display);font-style:italic;font-size:18px;color:var(--terra);line-height:1.35}
.tl b{font-family:var(--display);font-weight:400;font-size:20px;line-height:1.3;color:var(--ink);display:block}
.tl p{font-size:15px;line-height:1.6;color:#3B4452;margin-top:4px;max-width:56ch}
.tl a{color:var(--terra);font-weight:700}
.sb-story{background:#E9DFCF;padding:clamp(56px,7vw,96px) 0}
.sb-story-in{max-width:760px}
.sb-story h2{margin-bottom:26px}
.sb-story p:not(.eb){font-size:17px;line-height:1.75;color:#2E3744}
.sb-story p+p{margin-top:16px}
.sb-next{background:#F2EBE0 url(tex_paper.jpg) center/cover;padding:clamp(56px,7vw,96px) 0}
.sb-two{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,56px)}
.sb-next .lv-box{border-top:2px solid var(--prof);padding-top:20px}
.sb-next h2{font-family:var(--display);font-weight:400;font-size:clamp(28px,3.2vw,40px);line-height:1.1;margin:6px 0 14px}
.sb-next h2 em{font-style:italic;font-weight:300;color:var(--terra)}
.sb-next p:not(.eb){font-size:16px;line-height:1.7;color:#2E3744;max-width:46ch}
.sb-next .pill{margin-top:22px}
@media (max-width:760px){.sb-tl-grid{grid-template-columns:1fr}.tl li{grid-template-columns:1fr;gap:2px}.sb-two{grid-template-columns:1fr}.sb-next .pill{width:100%;justify-content:center}}
'''
a=full.index('<main id="inicio"'); b=full.index('</main>')+7
out=full[:a]+main+full[b:]
out=out.replace("</style>",css+"</style>",1)
out=re.sub(r'href="#(?!")', 'href="index.html#', out)
out=out.replace('<title>Nelson Mendonça Neto · Psicanálise</title>','<title>Sobre · Nelson Mendonça Neto</title>')
out=out.replace('<a class="hide-m" href="sobre.html">Sobre</a>','<a class="hide-m" href="sobre.html" aria-current="page" style="color:var(--acol)">Sobre</a>')
out=re.sub(r'<script type="application/ld\+json">.*?</script>\n?','',out,flags=re.S)
out=out.replace('<link rel="canonical" href="https://nelsonmendonca.com/">','<link rel="canonical" href="https://nelsonmendonca.com/sobre">')
out=out.replace('<meta property="og:url" content="https://nelsonmendonca.com/">','<meta property="og:url" content="https://nelsonmendonca.com/sobre">')
out=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Formação e trajetória de Nelson Mendonça Neto, psicólogo (CRP 19/3888) formado pela Universidade Tiradentes, em clínica desde 2020, com orientação psicanalítica.">',out)
open("deploy/sobre.html","w").write(out)
print("ok sobre")
