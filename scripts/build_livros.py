# Gera deploy/livros.html (livros, cursos e palestras) com o mesmo cabeçalho e rodapé do site
import re, urllib.parse as U
full=open("deploy/index.html").read()
def wa(t): return "https://wa.me/5579996041731?text="+U.quote(t)
W_SHARE="https://wa.me/?text="+U.quote("Achei que você ia gostar deste ebook gratuito do psicólogo Nelson Mendonça Neto: Massa de manobra, sobre neuromarketing, manipulação e por que a psicologia é política. https://nelsonmendonca.com/livros#massa")
W_PQ=wa("Olá, Nelson. Vim pelo site e quero ser avisado(a) do lançamento do livro Perverso é quem?")
W_CURSO=wa("Olá, Nelson. Vim pelo site e quero ser avisado(a) quando abrirem os cursos.")
W_PAL=wa("Olá, Nelson. Vim pelo site e gostaria de conversar sobre uma palestra ou um encontro.")
main=f'''<main id="inicio" class="lv" tabindex="-1">
<section class="lv-hero">
  <div class="wrap">
    <nav class="crumb" aria-label="Você está em"><a href="index.html">← Início</a><span aria-hidden="true">/</span><span>Livros e textos</span></nav>
    <p class="eb">Livros e textos</p>
    <h1>Para além <em>do consultório.</em></h1>
    <p class="lv-lead">Livros e textos em que levo a psicanálise para fora da sessão: para colegas de profissão e para quem quer entender melhor o que nos atravessa.</p>
  </div>
</section>

<section class="lv-sec" aria-labelledby="t-livros">
  <div class="wrap">
    <p class="eb">Livros</p>
    <h2 id="t-livros">O que <em>escrevi.</em></h2>
    <p class="lv-hint">Toque em um livro para saber mais.</p>
    <div class="shelf">
      <button type="button" class="book" data-open="bk-massa" aria-haspopup="dialog">
        <span class="b-cover"><picture><source type="image/webp" srcset="capa_massa.webp"><img src="capa_massa.jpg" alt="" width="640" height="920" loading="lazy"></picture></span>
        <span class="b-tag t-free">Gratuito · PDF</span>
        <span class="b-title">Massa de manobra</span>
        <span class="b-sub">Neuromarketing, manipulação e por que a psicologia é política</span>
        <span class="b-more">Saber mais <span aria-hidden="true">→</span></span>
      </button>
      <button type="button" class="book" data-open="bk-perverso" aria-haspopup="dialog">
        <span class="b-cover"><picture><source type="image/webp" srcset="capa_perverso.webp"><img src="capa_perverso.jpg" alt="" width="640" height="920" loading="lazy"></picture></span>
        <span class="b-tag t-wip">Em andamento</span>
        <span class="b-title">Perverso é quem?</span>
        <span class="b-sub">Psicanálise, sexualidades e o medo do diferente</span>
        <span class="b-more">Saber mais <span aria-hidden="true">→</span></span>
      </button>
    </div>
  </div>
</section>

<dialog class="bk-dlg" id="bk-massa" aria-labelledby="bk-massa-t">
  <button type="button" class="bk-x" data-close aria-label="Fechar">×</button>
  <div class="bk-in">
    <picture><source type="image/webp" srcset="capa_massa.webp"><img class="bk-cap" src="capa_massa.jpg" alt="Capa do ebook Massa de manobra: uma multidão de pessoas iguais ouvindo um homem com um megafone" width="640" height="920" loading="lazy"></picture>
    <div class="bk-txt">
      <p class="tags"><span class="tag t-breve">Gratuito</span><span class="tag">Ebook para psicólogos</span><span class="tag">PDF e EPUB</span></p>
      <h3 id="bk-massa-t">Massa de manobra</h3>
      <p class="sub">Neuromarketing, manipulação e por que a psicologia é política.</p>
      <p>Tudo o que a psicologia sabe sobre desejo, vínculo e defesa já está sendo usado por agências, plataformas e campanhas para decidir o que as pessoas compram, do que têm medo e em quem votam. Este ebook mostra como esse mecanismo funciona, o que a neurociência diz sobre por que nos agarramos às nossas crenças, como isso chega ao consultório e o que nós, psicólogos, podemos fazer.</p>
      <p>Capítulos curtos, frases diretas e fontes declaradas, para ler sem cansar e terminar com algo que dá para usar já na próxima semana.</p>
      <div class="obra-btns"><a class="pill pill-dark" href="Massa-de-Manobra-Nelson-Mendonca-Neto.pdf" download>Baixar em PDF <span aria-hidden="true">↓</span></a><a class="pill pill-dark" href="Massa-de-Manobra-Nelson-Mendonca-Neto.epub" download type="application/epub+zip">Baixar em EPUB <span aria-hidden="true">↓</span></a><a class="pill pill-line" href="{W_SHARE}" target="_blank" rel="noopener">Enviar para um colega</a></div>
      <p class="fmt-nota">O EPUB ajusta o texto à tela: ideal para ler no celular, no Kindle ou no Apple Livros.</p>
      <details class="sumario"><summary>Ver o sumário</summary><ol>
        <li>Quando a psicologia aprendeu a vender</li><li>Todos nós desejamos como capitalistas</li><li>O cérebro político não pensa a frio</li>
        <li>Quando o teste de personalidade vira arma</li><li>A polarização como produto</li><li>O que chega na minha clínica</li>
        <li>Um país que corta o próprio braço</li><li>A psicologia é política. Sempre foi.</li><li>Como a gente intervém</li></ol></details>
    </div>
  </div>
</dialog>

<dialog class="bk-dlg" id="bk-perverso" aria-labelledby="bk-perverso-t">
  <button type="button" class="bk-x" data-close aria-label="Fechar">×</button>
  <div class="bk-in">
    <picture><source type="image/webp" srcset="capa_perverso.webp"><img class="bk-cap" src="capa_perverso.jpg" alt="Capa do livro Perverso é quem?: silhueta de uma pessoa sobre fundo azul, recortada como papel antigo, com um triângulo rosa" width="640" height="920" loading="lazy"></picture>
    <div class="bk-txt">
      <p class="tags"><span class="tag t-breve">Em andamento</span><span class="tag">Livro</span></p>
      <h3 id="bk-perverso-t">Perverso é quem?</h3>
      <p class="sub">Psicanálise, sexualidades e o medo do diferente.</p>
      <p>Tudo começa numa mesa de formação em psicanálise, quando um colega fala em “homossexualismo” e ninguém responde. A partir dessa cena, o livro revisita Freud, Lacan, Winnicott e Bion para enfrentar, com fonte e com afeto, uma pergunta que ainda machuca muita gente: a homossexualidade é uma perversão?</p>
      <p>A resposta é não. E o caminho até ela passa pelas lésbicas, pelas pessoas bi, ace, trans e não binárias, pela história do Brasil, pelos mitos que ainda circulam, pela clínica e pelas famílias. Escrito para pessoas LGBTQIAPN+, para colegas que querem escutar sem patologizar e para mães e pais que querem entender.</p>
      <div class="obra-btns"><a class="pill pill-dark" href="{W_PQ}" target="_blank" rel="noopener">Quero ser avisado do lançamento <span aria-hidden="true">→</span></a></div>
      <details class="sumario"><summary>Ver as partes do livro</summary><ol>
        <li>Fundamentos</li><li>As orientações</li><li>Gênero</li><li>Sociedade</li><li>Perverso é quem?</li><li>Viver e escutar</li></ol></details>
    </div>
  </div>
</dialog>

<!--TEXTOS-->
</main>'''
css='''

/* ===== estante de livros + janela de detalhes ===== */
.lv-hint{font-size:15px;color:var(--muted);margin:-18px 0 30px}
.shelf{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,260px));gap:clamp(28px,4vw,56px)}
.book{all:unset;cursor:pointer;display:flex;flex-direction:column;gap:8px;text-align:left;border-radius:4px}
.book:focus-visible{outline:2px solid var(--terra);outline-offset:8px}
.b-cover{display:block;aspect-ratio:640/920;border-radius:2px 6px 6px 2px;overflow:hidden;box-shadow:0 18px 40px rgba(30,39,52,.25);transition:transform .35s cubic-bezier(.2,.7,.2,1),box-shadow .35s ease;margin-bottom:10px}
.b-cover img{width:100%;height:100%;object-fit:cover;display:block}
.book:hover .b-cover,.book:focus-visible .b-cover{transform:translateY(-6px);box-shadow:0 28px 56px rgba(30,39,52,.32)}
.b-tag{align-self:flex-start;font:700 10.5px var(--body);letter-spacing:.18em;text-transform:uppercase;padding:5px 10px;border-radius:999px}
.t-free{background:var(--terra);color:var(--paper)}.t-wip{border:1px solid var(--terra);color:var(--terra)}
.b-title{font-family:var(--display);font-size:24px;line-height:1.15;color:var(--ink)}
.b-sub{font-size:14.5px;line-height:1.5;color:#3B4452}
.b-more{font:700 13.5px var(--body);color:var(--terra);margin-top:2px}
.bk-dlg{border:0;padding:0;width:min(920px,calc(100% - 32px));max-height:calc(100svh - 48px);background:#F2EBE0 url(tex_paper.jpg) center/cover;color:var(--ink);box-shadow:0 40px 100px rgba(16,22,30,.45);border-radius:4px;overflow:auto}
.bk-dlg::backdrop{background:rgba(30,39,52,.6);backdrop-filter:blur(3px)}
.bk-dlg[open]{animation:bkin .35s cubic-bezier(.2,.7,.2,1)}
@keyframes bkin{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
.bk-in{display:grid;grid-template-columns:minmax(180px,260px) 1fr;gap:clamp(24px,4vw,48px);padding:clamp(28px,4vw,52px)}
.bk-cap{width:100%;height:auto;display:block;box-shadow:0 18px 40px rgba(30,39,52,.28);border-radius:2px 6px 6px 2px}
.bk-txt .tags{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px}
.bk-txt .tag{font:700 10.5px var(--body);letter-spacing:.18em;text-transform:uppercase;padding:6px 10px;border:1px solid var(--line);border-radius:999px;color:#4F4A45}
.bk-txt .t-breve{background:var(--terra);border-color:var(--terra);color:var(--paper)}
.bk-txt h3{font-family:var(--display);font-weight:400;font-size:clamp(28px,3.4vw,36px);line-height:1.1}
.bk-txt .sub{font-family:var(--display);font-style:italic;font-size:19px;color:var(--terra);margin:6px 0 18px}
.bk-txt p{font-size:16px;line-height:1.7;color:#2E3744}
.bk-txt p+p{margin-top:12px}
.bk-x{position:sticky;top:12px;float:right;margin:12px 12px -56px 0;z-index:2;width:44px;height:44px;border-radius:50%;border:0;background:var(--prof);color:var(--paper);font-size:26px;line-height:1;cursor:pointer}
.bk-x:hover{background:var(--terra)}
@media (max-width:640px){.bk-in{grid-template-columns:1fr}.bk-cap{width:min(200px,60%)}.bk-dlg{width:100vw;max-width:100vw;max-height:100svh;height:100svh;margin:0;inset:0;border-radius:0}.shelf{grid-template-columns:1fr 1fr;gap:20px}.b-title{font-size:19px}.b-sub{display:none}}
@media (prefers-reduced-motion:reduce){.bk-dlg[open]{animation:none}.b-cover{transition:none}}
/* ===== página Livros e cursos ===== */
.lv-hero{background:var(--prof) url(tex_navy.jpg) center/cover;color:var(--paper);padding:clamp(56px,8vw,110px) 0 clamp(48px,6vw,80px)}
.lv-hero .crumb{display:flex;gap:10px;font-size:13px;color:#9AA3AF;margin-bottom:26px}.lv-hero .crumb a{color:var(--acol);text-decoration:none;font-weight:700}
.lv-hero .eb{color:#9CC0D3}
.lv h1{font-family:var(--display);font-weight:400;font-size:clamp(42px,6vw,76px);line-height:1.02;letter-spacing:-.02em}
.lv h1 em,.lv h2 em{font-style:italic;font-weight:300}
.lv-hero h1 em{color:var(--acol)}
.lv-lead{font-size:18px;line-height:1.65;color:#D3D7DD;max-width:56ch;margin-top:20px}
.lv-sec{background:#F2EBE0 url(tex_paper.jpg) center/cover;padding:clamp(56px,7vw,96px) 0}
.lv-sec h2{font-family:var(--display);font-weight:400;font-size:clamp(30px,3.6vw,44px);line-height:1.08;margin:6px 0 34px}
.lv-sec h2 em{color:var(--terra)}
.obra{display:grid;grid-template-columns:minmax(200px,280px) 1fr;gap:clamp(28px,5vw,64px);align-items:start}
.capa{aspect-ratio:2/3;background:var(--prof) url(tex_navy.jpg) center/cover;color:var(--paper);padding:26px 22px;display:flex;flex-direction:column;box-shadow:0 22px 50px rgba(30,39,52,.28),inset 6px 0 0 rgba(0,0,0,.18);border-radius:2px 6px 6px 2px}
.capa .c-eb{font:700 9px var(--body);letter-spacing:.24em;text-transform:uppercase;color:#9CC0D3}
.capa b{font-family:var(--display);font-weight:400;font-size:clamp(30px,3vw,38px);line-height:1;margin-top:auto}
.capa b em{font-style:italic;font-weight:300;color:var(--acol)}
.capa .c-sub{font-size:12px;line-height:1.45;color:#C3C8D0;margin-top:14px}
.capa img{width:54px;margin-top:22px}
.obra+.obra{margin-top:clamp(56px,7vw,88px);padding-top:clamp(40px,5vw,64px);border-top:1px solid var(--line)}
.obra-txt .tags{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px}
.obra-txt .tag{font:700 10.5px var(--body);letter-spacing:.18em;text-transform:uppercase;padding:6px 10px;border:1px solid var(--line);border-radius:999px;color:#4F4A45}
.obra-txt .t-breve{background:var(--terra);border-color:var(--terra);color:var(--paper)}
.obra-txt h3{font-family:var(--display);font-weight:400;font-size:32px;line-height:1.1}
.obra-txt .sub{font-family:var(--display);font-style:italic;font-size:19px;color:var(--terra);margin:6px 0 18px}
.obra-txt p{font-size:16.5px;line-height:1.7;color:#2E3744;max-width:58ch}
.obra-btns{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px}
.fmt-nota{font-size:.86rem;opacity:.75;margin-top:12px}
.obra-txt p+p{margin-top:14px}
.capa-img{display:block;box-shadow:0 22px 50px rgba(30,39,52,.28);border-radius:2px 6px 6px 2px;overflow:hidden;transition:box-shadow .25s}
.capa-img:hover{box-shadow:0 26px 60px rgba(30,39,52,.38)}.capa-img img{display:block;width:100%;height:auto}
.sumario{margin-top:26px;border-top:1px solid var(--line);padding-top:14px;max-width:58ch}
.sumario summary{cursor:pointer;font:700 13px var(--body);letter-spacing:.06em;color:var(--terra)}
.sumario ol{margin:14px 0 0 20px;display:grid;gap:6px;font-size:15px;color:#2E3744;line-height:1.5}
.lv-alt{background:#E9DFCF}
.lv-two{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,56px)}
.lv-box{border-top:2px solid var(--prof);padding-top:20px}
.lv-box h2{margin-bottom:16px}
.lv-box p:not(.eb){font-size:16px;line-height:1.7;color:#2E3744;max-width:46ch}
.lv-box .pill{margin-top:22px}
@media (max-width:760px){.obra{grid-template-columns:1fr}.capa-img{width:min(240px,70%)}.obra-btns{flex-direction:column}.lv-two{grid-template-columns:1fr}
 .obra-btns .pill,.lv-box .pill{width:100%;justify-content:center}}
'''
a=full.index('<main id="inicio"'); b=full.index('</main>')+7
out=full[:a]+main+full[b:]
out=out.replace("</style>",css+"</style>",1)
out=re.sub(r'href="#(?!")', 'href="index.html#', out)
out=out.replace('<title>Nelson Mendonça Neto · Psicanálise</title>','<title>Livros e textos · Nelson Mendonça Neto</title>')
out=out.replace('<a class="hide-m" href="livros.html">Livros e textos</a>','<a class="hide-m" href="livros.html" aria-current="page" style="color:var(--acol)">Livros e textos</a>')
out=re.sub(r'<script type="application/ld\+json">.*?</script>\n?','',out,flags=re.S)
out=out.replace('<link rel="canonical" href="https://nelsonmendonca.com/">','<link rel="canonical" href="https://nelsonmendonca.com/livros">')
out=out.replace('<meta property="og:url" content="https://nelsonmendonca.com/">','<meta property="og:url" content="https://nelsonmendonca.com/livros">')
out=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Baixe gratuitamente o ebook Massa de manobra: neuromarketing, manipulação e por que a psicologia é política. Livros, cursos e palestras de Nelson Mendonça Neto, psicólogo e psicanalista.">',out)
out=out.replace('<meta property="og:image" content="https://nelsonmendonca.com/nelson_hero.jpg">','<meta property="og:image" content="https://nelsonmendonca.com/capa_massa.jpg">')
out=out.replace("</main>","</main>"+'<script>(function(){\ndocument.querySelectorAll(".book[data-open]").forEach(function(b){b.addEventListener("click",function(){var d=document.getElementById(b.dataset.open);if(d&&d.showModal){d.showModal();d.dataset.from=b.dataset.open}})});\ndocument.querySelectorAll(".bk-dlg").forEach(function(d){\n d.querySelectorAll("[data-close]").forEach(function(x){x.addEventListener("click",function(){d.close()})});\n d.addEventListener("click",function(e){if(e.target===d)d.close()});\n d.addEventListener("close",function(){var b=document.querySelector(\'.book[data-open="\'+d.id+\'"]\');if(b)b.focus()});});\nvar h=location.hash.slice(1);if(h==="massa"||h==="perverso"){var d=document.getElementById("bk-"+h);if(d&&d.showModal)d.showModal()}\n})();</script>\n',1)
open("deploy/livros.html","w").write(out)
print("ok livros")
