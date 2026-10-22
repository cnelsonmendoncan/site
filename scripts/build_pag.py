# Gera deploy/pagamento.html com o mesmo cabeçalho, menu, rodapé e favicon do site
import re
full=open("deploy/index.html").read()
pix,pp,wise=open("logos.txt").read().split("\n")[:3]
WA="https://wa.me/5579996041731?text=Ol%C3%A1%2C%20Nelson.%20Vim%20pelo%20site%20e%20gostaria%20de%20agendar%20a%20entrevista%20inicial."
WAS="https://wa.me/5579996041731?text=Ol%C3%A1%2C%20Nelson.%20Vim%20pelo%20site%20e%20gostaria%20de%20agendar%20uma%20entrevista%20pela%20agenda%20social."
main=f'''<main id="inicio" class="pg" tabindex="-1">
<section class="pg-hero">
  <div class="pg-card">
    <nav class="crumb" aria-label="Você está em"><a href="index.html">← Início</a><span aria-hidden="true">/</span><span>Como começar</span></nav>
    <p class="eb">O processo de início &amp; acolhimento</p>
    <h1>O primeiro passo é <em>uma entrevista inicial.</em></h1>
    <p class="pg-lead">É um encontro online dedicado a escutar o seu momento, compreender a sua demanda e avaliar juntos a viabilidade de darmos início ao processo analítico.</p>

    <div class="pg-block">
      <p class="eb">O tempo do tratamento</p>
      <p>Na psicanálise, os combinados fazem parte do próprio trabalho. Frequência, horários e honorários, inclusive os da própria entrevista, são conversados em conjunto, na sessão, de forma individual e confidencial.</p>
      <p style="margin-top:12px">As sessões duram de 45 a 50 minutos. Quando a demanda pede, podem ser duas vezes por semana ou ter encontros extras, sempre combinados em sessão.</p>
    </div>

    <div class="pg-block">
      <p class="eb">Formas de pagamento</p>
      <div class="ghost" aria-label="Pix, PayPal e Wise">
        <span class="g">{pix}<b>Pix</b></span><span class="g">{pp}<b>PayPal</b></span><span class="g">{wise}<b>Wise</b></span>
      </div>
      <p>Pix, cartão pelo PayPal e, para brasileiros no exterior, PayPal ou Wise, com a cobrança na moeda do seu país, sem conversões. Os planos mensais podem ser parcelados no cartão; sessões avulsas, não.</p>
      <p class="pg-small">Os dados para pagamento são enviados em particular.</p>
    </div>

    <div class="pg-block pg-inv">
      <p><b>A entrevista inicial é um atendimento profissional e é remunerada.</b> Os honorários são combinados com você, em conjunto, na própria sessão.</p>
      <div class="pg-btns pg-btns-in"><a class="pill pill-dark" href="{WA}" target="_blank" rel="noopener">Agendar entrevista inicial <span aria-hidden="true">→</span></a></div>
    </div>

    <div class="pg-btns">
      <a class="pill pill-line" href="index.html">← Voltar ao site</a>
    </div>
    <p class="pg-small" style="margin-top:18px">Remarcações com pelo menos 24 horas de antecedência. As condições acordadas entre nós ficam registradas em contrato.</p>
  </div>
</section>
</main>'''
css='''
/* ===== página Início e honorários ===== */
.pg-hero{background:#EDE3D3 url(pag_bg.jpg) left top/cover fixed;padding:clamp(48px,7vw,96px) 0}
.pg-card{margin-left:max(36vw,calc(50% - 540px + 330px));margin-right:max(20px,calc(50% - 540px));max-width:640px;background:rgba(247,241,232,.93);padding:clamp(28px,4vw,48px);box-shadow:0 24px 60px rgba(30,39,52,.12)}
.crumb{display:flex;gap:10px;font-size:13px;color:var(--muted);margin-bottom:26px}.crumb a{color:var(--terra);text-decoration:none;font-weight:700}
.pg h1{font-family:var(--display);font-weight:400;font-size:clamp(40px,5vw,64px);line-height:1.02;letter-spacing:-.02em}
.pg h1 em{font-style:italic;font-weight:300;color:var(--terra)}
.pg-lead{font-size:18px;line-height:1.65;color:#2E3744;margin-top:18px}
.pg-btns.pg-btns-in{margin-top:22px}
.pg-block{margin-top:30px;padding-top:24px;border-top:1px solid var(--line)}
.pg-block p{font-size:16px;line-height:1.65;color:#2E3744}
.pg-block p.eb{font-size:11px;line-height:1.4;color:var(--terra);margin-bottom:12px}
.pg-social{margin-top:16px;padding:14px 16px;border-left:3px solid var(--hor);background:#fff;display:grid;gap:3px}
.pg-social b{font-size:15px;color:var(--ink)}.pg-social span{font-size:14.5px;line-height:1.6;color:#3B4452}.pg-social span+span{margin-top:6px}
.pg-social a{font-weight:700;font-size:14.5px;color:var(--terra);text-decoration:none;margin-top:4px}
.ghost{display:flex;flex-wrap:wrap;gap:12px 26px;color:rgba(30,39,52,.4);margin-top:4px}
.g{display:inline-flex;align-items:center;gap:9px}.g .lg{width:24px;height:24px}.g b{font-family:var(--display);font-size:20px;font-weight:600;color:#66625C}
.pg-small{font-size:14px!important;color:#4F4A45!important;margin-top:12px}
.pg-inv{border-top:2px solid var(--terra)}
.pg-price{font-family:var(--display)!important;font-size:52px!important;line-height:1!important;color:var(--ink)!important;margin:10px 0 14px}
.cx{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:-4px 0 8px}
.cx-l{font-weight:700;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--terra);margin-right:4px}
.cx button{font:600 13.5px var(--body);color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:999px;padding:7px 14px;cursor:pointer}
.cx button:hover{border-color:var(--prof)}
.cx button.on{background:var(--prof);color:var(--paper);border-color:var(--prof)}
.cx-note{font-size:13px!important;color:#4F4A45!important;margin-bottom:14px}
.pg-imp{padding:14px 16px;background:#E7EEF2;border-radius:2px}
.pg-imp b{color:var(--terra)}
.pg-btns{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
@media (max-width:520px){.pg-btns{flex-direction:column;align-items:stretch}.pg-btns .pill{justify-content:center}}
@media (max-width:1200px){.pg-hero{background:#EDE3D3 url(pag_bg_m.jpg) left top/100% auto no-repeat;padding-top:calc(41.6vw - 30px)}
.pg-card{margin:0 auto;max-width:720px;width:calc(100% - 32px);background:#F7F1E8}}
@media (max-width:520px){.pg-card{width:100%;box-shadow:none}.pg-price{font-size:44px!important}}
'''
a=full.index('<main id="inicio"'); b=full.index('</main>')+7
out=full[:a]+main+full[b:]
out=out.replace("</style>",css+"</style>",1)
out=re.sub(r'href="#(?!")', 'href="index.html#', out)
out=out.replace('<title>Nelson Mendonça Neto · Psicanálise</title>','<title>Como começar · Nelson Mendonça Neto</title>')
out=out.replace('<a class="hide-m" href="pagamento.html">Como começar</a>','<a class="hide-m" href="pagamento.html" aria-current="page" style="color:var(--acol)">Como começar</a>')
# na própria página, o botão flutuante e o "Agendar agora" vão direto ao WhatsApp
out=out.replace('class="btn btn-dark" href="pagamento.html"',f'class="btn btn-dark" href="{WA}" target="_blank" rel="noopener"')
out=re.sub(r'<a class="float-cta"[^>]*>.*?</a>','',out,flags=re.S)
out=re.sub(r'<script type="application/ld\+json">.*?</script>\n?','',out,flags=re.S)
out=out.replace('<link rel="canonical" href="https://nelsonmendonca.com/">','<link rel="canonical" href="https://nelsonmendonca.com/pagamento">')
out=out.replace('<meta property="og:url" content="https://nelsonmendonca.com/">','<meta property="og:url" content="https://nelsonmendonca.com/pagamento">')
out=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Como começar: a entrevista inicial e as formas de pagamento do consultório de Nelson Mendonça Neto, psicólogo e psicanalista.">',out)
out=out.replace('<a class="skip" href="#inicio">','<a class="skip" href="#inicio">')
open("deploy/pagamento.html","w").write(out)
print("ok")
