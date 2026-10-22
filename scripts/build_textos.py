# Gera a seção "A vida como ela se diz": deploy/textos.html, deploy/textos/<slug>.html
# e o bloco "Últimos textos" na página inicial. Os textos vêm de ../content/textos/*.md
import re, os, glob, json, math, html as H, unicodedata, urllib.parse as U, datetime as D
import yaml, markdown

SITE = "https://nelsonmendonca.com"
SEC = "A vida como ela se diz"
MESES = "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split()

def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:80] or "texto"

def as_date(v):
    if isinstance(v, D.datetime): return v.date()
    if isinstance(v, D.date): return v
    try: return D.date.fromisoformat(str(v)[:10])
    except Exception: return D.date.today()

def br(d): return f"{d.day} de {MESES[d.month-1]} de {d.year}"
def esc(s): return H.escape(str(s or ""), quote=True)

def load():
    posts = []
    for f in sorted(glob.glob("../content/textos/*.md")):
        raw = open(f, encoding="utf-8").read()
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", raw, re.S)
        meta, body = (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, raw)
        if meta.get("rascunho"): continue
        title = str(meta.get("title") or "").strip()
        if not title or not body.strip(): continue
        d = as_date(meta.get("date"))
        body_html = body if body.lstrip().startswith("<") else markdown.markdown(body, extensions=["extra", "sane_lists", "smarty"], extension_configs={"smarty": {"substitutions": {"left-double-quote": "“", "right-double-quote": "”", "left-single-quote": "‘", "right-single-quote": "’"}}})
        words = len(re.sub(r"<[^>]+>", " ", body_html).split())
        resumo = str(meta.get("resumo") or "").strip()
        if not resumo:
            txt = H.unescape(re.sub(r"<[^>]+>", " ", body_html)).split()
            resumo = " ".join(txt[:28]) + ("…" if len(txt) > 28 else "")
        posts.append(dict(cit=str(meta.get("citacao") or "").strip(), title=title, date=d, resumo=resumo, html=body_html,
                          min=max(1, math.ceil(words / 200)), slug=slugify(os.path.splitext(os.path.basename(f))[0])))
    posts.sort(key=lambda p: (p["date"], p["title"]), reverse=True)
    seen = set()
    for p in posts:
        while p["slug"] in seen: p["slug"] += "-2"
        seen.add(p["slug"])
    return posts

CSS = '''
/* ===== A vida como ela se diz ===== */
/* --- coluna de jornal --- */
.art-aq{position:relative;overflow:hidden;background:#E3D0B8 url(tex_textos.jpg) center 35%/cover;padding:22px 0 0;height:clamp(150px,18vw,230px)}
.art-aq .crumb{display:flex;flex-wrap:wrap;gap:10px;font-size:13px;color:#4F4A45}.art-aq .crumb a{color:var(--terra);text-decoration:none;font-weight:700}
.art-xic{position:absolute;right:max(-40px,calc(50% - 640px));top:-60px;width:clamp(200px,24vw,330px);height:auto;filter:drop-shadow(10px 16px 18px rgba(30,39,52,.28));animation:xic 8s ease-in-out infinite;pointer-events:none}
@keyframes xic{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-8px) rotate(-2deg)}}
@media (prefers-reduced-motion:reduce){.art-xic{animation:none}}
@media (max-width:760px){.art-aq{height:150px}.art-xic{width:150px;right:-36px;top:-26px}.art-aq .crumb{max-width:62%}.art-aq .crumb a[href="livros.html"],.art-aq .crumb a[href="livros.html"]+span{display:none}}
.tx .art{padding-top:0}
.jn{max-width:720px;margin:-56px auto 0;position:relative;background:#FBF8F3;padding:34px clamp(20px,4vw,40px) 26px;text-align:center}
.jn-col{display:flex;justify-content:space-between;align-items:center;gap:12px;border-top:3px double var(--ink);border-bottom:1px solid var(--ink);padding:8px 0;margin:0 0 30px;font:700 11px var(--body);letter-spacing:.22em;text-transform:uppercase;color:var(--muted)}
.jn-col b{font-family:var(--display);font-style:italic;font-weight:400;font-size:clamp(17px,2vw,22px);letter-spacing:0;text-transform:none;color:var(--terra)}
@media (max-width:560px){.jn-col span{display:none}.jn-col{justify-content:center}}
.jn h1{font-family:var(--display);font-weight:400;font-size:clamp(34px,5vw,58px);line-height:1.06;letter-spacing:-.015em;color:var(--ink);margin:0 auto;max-width:18ch}
.jn-dek{font-family:var(--display);font-style:italic;font-size:clamp(19px,2vw,23px);line-height:1.45;color:#4A4038;margin:18px auto 0;max-width:40ch}
.jn-by{margin:24px 0 0;padding-top:16px;border-top:1px solid var(--line);font-size:13.5px;color:var(--muted)}.jn-by b{color:var(--ink)}
.jn-body{margin-top:30px}
.jn-body>p:first-of-type::first-letter{float:left;font-size:4.1em;line-height:.82;padding:6px 10px 0 0;color:var(--terra);font-weight:500}
.art-body .art-pull{margin:2em 0;padding:30px 28px 24px;border:0;border-top:3px double var(--ink);border-bottom:1px solid var(--ink);background:#F3EBDF;text-align:center;position:relative}
.art-body .art-pull .pq-mark{display:block;font-family:var(--display);font-size:64px;line-height:.5;color:var(--terra);margin-bottom:6px}
.art-body .art-pull blockquote{margin:0;padding:0;border:0}
.art-body .art-pull blockquote p{margin:0;font-style:italic;font-size:clamp(23px,2.5vw,30px);line-height:1.35;color:var(--ink)}
.art-body .art-pull figcaption{margin-top:18px;font:600 12px var(--body);letter-spacing:.06em;color:var(--terra)}
.art-body .art-pull figcaption b{font-weight:700}

.tx-hero{background:var(--prof) url(tex_navy.jpg) center/cover;color:var(--paper);padding:clamp(56px,8vw,110px) 0 clamp(48px,6vw,80px)}
.tx-hero .crumb{display:flex;flex-wrap:wrap;gap:10px;font-size:13px;color:#9AA3AF;margin-bottom:26px}
.tx-hero .crumb a{color:var(--acol);text-decoration:none;font-weight:700}
.tx-hero .eb{color:#9CC0D3}
.tx h1{font-family:var(--display);font-weight:400;font-size:clamp(42px,6vw,76px);line-height:1.04;letter-spacing:-.02em}
.tx h1 em{font-style:italic;font-weight:300;color:var(--acol)}
.tx-lead{font-size:18px;line-height:1.65;color:#D3D7DD;max-width:56ch;margin-top:20px}
.tx-list{background:var(--paper) url(tex_paper.jpg) center/cover}
.tx-items{list-style:none;margin:0;padding:0;display:grid;gap:0;max-width:820px}
.tx-item{border-top:1px solid var(--line)}.tx-item:last-child{border-bottom:1px solid var(--line)}
.tx-list .tx-items{gap:18px}.tx-list .tx-item,.tx-list .tx-item:last-child{border:0;background:rgba(251,248,243,.94);box-shadow:0 18px 40px rgba(30,39,52,.14);border-left:3px solid var(--terra)}.tx-list .tx-item a{padding:26px 28px}
.tx-item a{display:block;padding:30px 0;text-decoration:none;color:var(--ink)}
.tx-meta{font:700 12px var(--body);letter-spacing:.2em;text-transform:uppercase;color:var(--terra)}
.tx-item h2,.tx-card h3{font-family:var(--display);font-weight:400;font-size:clamp(24px,2.8vw,32px);line-height:1.2;margin:10px 0 10px;letter-spacing:-.01em}
.tx-item p,.tx-card p{font-size:16px;line-height:1.65;color:var(--muted);max-width:62ch}
.tx-go{display:inline-block;margin-top:12px;font-weight:700;font-size:14.5px;color:var(--terra)}
.tx-item a:hover h2,.tx-card a:hover h3{color:var(--terra)}
.tx-empty{font-family:var(--display);font-style:italic;font-size:22px;color:var(--muted)}
.art-hero h1{font-size:clamp(34px,5vw,60px);max-width:22ch}
.art-hero .tx-meta{color:#E3D0C8;margin-top:22px;display:block;font-size:12.5px}
.art{background:#FBF8F3}
.tx .art{padding-top:clamp(40px,5vw,64px)}
.art-body{max-width:640px;margin:0 auto;font-family:var(--display);font-size:clamp(18px,1.6vw,20px);line-height:1.75;color:#262E3A}
.art-body p{margin:0 0 1.15em}
.art-body h2,.art-body h3{font-family:var(--display);font-weight:500;font-size:1.35em;line-height:1.25;margin:1.6em 0 .6em;color:var(--ink)}
.art-body blockquote{margin:1.6em 0;padding:4px 0 4px 24px;border-left:2px solid var(--terra);font-style:italic;font-size:1.12em;color:var(--terra)}
.art-body blockquote p{margin:0}
.art-body a{color:var(--terra)}
.art-body ul,.art-body ol{padding-left:1.3em;margin:0 0 1.15em}
.art-body img{max-width:100%;height:auto;margin:1em 0}
.art-sign{max-width:640px;margin:36px auto 0;padding-top:20px;border-top:1px solid var(--line);font-size:14px;color:var(--muted)}
.art-sign b{display:block;font-family:var(--display);font-weight:500;font-size:18px;color:var(--ink)}
.art-share{max-width:640px;margin:22px auto 0;display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.art-share span{font:700 11px var(--body);letter-spacing:.2em;text-transform:uppercase;color:var(--terra);margin-right:6px}
.art-share a,.art-share button{font:600 13.5px var(--body);color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:999px;padding:8px 16px;cursor:pointer;text-decoration:none}
.art-share a:hover,.art-share button:hover{border-color:var(--prof)}
.art-cta{max-width:640px;margin:48px auto 0;background:var(--prof) url(tex_navy.jpg) center/cover;color:var(--paper);padding:clamp(28px,4vw,40px)}
.art-cta p{font-family:var(--display);font-style:italic;font-size:clamp(21px,2.2vw,26px);line-height:1.35;margin:0 0 20px}
.art-cta .pill{background:var(--paper);color:var(--prof)}.art-cta .pill:hover{background:var(--acol)}
.tx-more{background:var(--paper) url(tex_paper.jpg) center/cover}
.tx-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:36px}
.tx-cards.n1{grid-template-columns:minmax(0,520px)}.tx-cards.n2{grid-template-columns:repeat(2,1fr)}
.tx-card{border-top:2px solid var(--prof);padding-top:6px;min-width:0}
.tx-card a{display:block;text-decoration:none;color:var(--ink);padding-top:12px}
.tx-home{background:#E3D0B8 url(tex_textos.jpg) center/cover}
@media (max-width:760px){.tx-home{background-image:linear-gradient(rgba(242,235,224,.55),rgba(242,235,224,.2) 40%,rgba(242,235,224,0)),url(tex_textos_m.jpg);background-position:center,0 70%;background-size:cover,cover}}
.txq{margin:8px 0 0;max-width:900px}
.txq blockquote{margin:0;font-family:var(--display);font-style:italic;font-weight:400;font-size:clamp(30px,4.4vw,54px);line-height:1.15;letter-spacing:-.01em;color:var(--ink)}
.txq figcaption{margin-top:22px;font-size:15px;color:var(--muted)}
.txq figcaption a{color:var(--terra);font-weight:700;text-decoration:none}
.txq-btns{display:flex;flex-wrap:wrap;gap:12px;margin-top:34px}
@media (max-width:820px){.tx-cards,.tx-cards.n2{grid-template-columns:1fr}}
'''

def page(full, main, title, desc, path, ld=None, og_type="website"):
    out = full[:full.index('<main id="inicio"')] + main + full[full.index('</main>') + 7:]
    out = out.replace("</style>", CSS + "</style>", 1)
    out = re.sub(r'href="#(?!")', 'href="index.html#', out)
    out = out.replace('<a class="hide-m" href="livros.html">Livros e textos</a>', '<a class="hide-m" href="livros.html" aria-current="page" style="color:var(--acol)">Livros e textos</a>')
    out = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', '', out, flags=re.S)
    if ld: out = out.replace("</head>", '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>\n</head>", 1)
    out = re.sub(r"<title>.*?</title>", "<title>" + esc(title) + "</title>", out, count=1, flags=re.S)
    out = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="' + esc(desc) + '">', out)
    out = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="' + esc(title) + '">', out)
    out = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="' + esc(desc) + '">', out)
    out = re.sub(r'<meta property="og:type" content="[^"]*">', '<meta property="og:type" content="' + og_type + '">', out)
    out = out.replace('<link rel="canonical" href="https://nelsonmendonca.com/">', '<link rel="canonical" href="' + SITE + path + '">')
    out = out.replace('<meta property="og:url" content="https://nelsonmendonca.com/">', '<meta property="og:url" content="' + SITE + path + '">')
    return out

def with_quote(p):
    h = p["html"]
    if not p["cit"]: return h
    paras = [x for x in re.split(r'(?<=</p>)', h) if x.strip()]
    k = max(1, len(paras) // 2)
    q = ('<figure class="art-pull"><span class="pq-mark" aria-hidden="true">“</span><blockquote><p>' + esc(p["cit"].strip(chr(8220)+chr(8221)+chr(34)+" ")) + '</p></blockquote>'
         '<figcaption><b>Nelson Mendonça Neto</b> · A vida como ela se diz · nelsonmendonca.com</figcaption></figure>')
    return "".join(paras[:k]) + q + "".join(paras[k:])

def card(p, tag="h3"):
    return (f'<article class="tx-card"><a href="textos/{p["slug"]}.html"><span class="tx-meta">{br(p["date"])} · {p["min"]} min de leitura</span>'
            f'<{tag}>{esc(p["title"])}</{tag}><p>{esc(p["resumo"])}</p><span class="tx-go">Ler o texto <span aria-hidden="true">→</span></span></a></article>')

def main():
    full = open("deploy/index.html", encoding="utf-8").read()
    posts = load()
    os.makedirs("deploy/textos", exist_ok=True)

    # lista
    if posts:
        items = "\n".join(
            f'<li class="tx-item"><a href="textos/{p["slug"]}.html"><span class="tx-meta">{br(p["date"])} · {p["min"]} min de leitura</span>'
            f'<h2>{esc(p["title"])}</h2><p>{esc(p["resumo"])}</p><span class="tx-go">Ler o texto <span aria-hidden="true">→</span></span></a></li>' for p in posts)
        lst = f'<ul class="tx-items">{items}</ul>'
    else:
        lst = '<p class="tx-empty">Os primeiros textos chegam em breve.</p>'
    m = f'''<main id="inicio" class="tx" tabindex="-1">
<section class="tx-hero"><div class="wrap">
  <nav class="crumb" aria-label="Você está em"><a href="index.html">← Início</a><span aria-hidden="true">/</span><a href="livros.html">Livros e textos</a><span aria-hidden="true">/</span><span>A vida como ela se diz</span></nav>
  <p class="eb">Textos de Nelson Mendonça Neto</p>
  <h1>A vida como ela <em>se diz.</em></h1>
  <p class="tx-lead">O que a psicanálise escuta no amor, na saudade, no trabalho e em tudo aquilo que se repete. Textos para pensar tomando um cafezinho.</p>
</div></section>
<section class="tx-list tx-home" aria-label="Todos os textos"><div class="wrap">{lst}</div></section>
</main>'''
    open("deploy/textos.html", "w", encoding="utf-8").write(page(full, m, SEC + " · Textos de Nelson Mendonça Neto",
        "Textos do psicanalista Nelson Mendonça Neto sobre amor, repetição, saudade e o que a psicanálise escuta na vida de todo dia.", "/textos"))

    # cada texto
    for i, p in enumerate(posts):
        others = [q for q in posts if q is not p][:2]
        url = f"{SITE}/textos/{p['slug']}"
        share = "https://wa.me/?text=" + U.quote(f"{p['title']} — um texto de Nelson Mendonça Neto: {url}")
        more = ""
        if others:
            more = (f'<section class="tx-more" aria-labelledby="t-mais"><div class="wrap"><p class="eb">Continue lendo</p>'
                    f'<h2 id="t-mais">Outros textos <em>do Nelson.</em></h2>'
                    f'<div class="tx-cards n{len(others)}">' + "".join(card(q) for q in others) + '</div></div></section>')
        m = f'''<main id="inicio" class="tx" tabindex="-1">
<article>
<div class="art-hero art-aq"><div class="wrap">
  <nav class="crumb" aria-label="Você está em"><a href="index.html">← Início</a><span aria-hidden="true">/</span><a href="livros.html">Livros e textos</a><span aria-hidden="true">/</span><a href="textos.html">{SEC}</a></nav>
  <img class="art-xic" src="xicara.webp" alt="" width="520" height="499">
</div></div>
<section class="art"><div class="wrap">
  <div class="jn">
    <p class="jn-col"><span>Coluna</span><b>A vida como ela se diz</b><span>nelsonmendonca.com</span></p>
    <h1>{esc(p["title"])}</h1>
    <p class="jn-dek">{esc(p["resumo"])}</p>
    <p class="jn-by">Por <b>Nelson Mendonça Neto</b>, psicólogo e psicanalista <span aria-hidden="true">·</span> <time datetime="{p["date"].isoformat()}">{br(p["date"])}</time> <span aria-hidden="true">·</span> {p["min"]} min de leitura</p>
  </div>
  <div class="art-body jn-body">{with_quote(p)}</div>
  <p class="art-sign"><b>Nelson Mendonça Neto</b>Psicólogo e psicanalista · CRP 19/3888</p>
  <div class="art-share"><span>Compartilhar</span><a href="{share}" target="_blank" rel="noopener">WhatsApp</a><button type="button" class="copy" data-url="{url}">Copiar link</button></div>
  <div class="art-cta"><p>Se este texto falou de você, a análise pode ser um lugar para isso.</p><a class="pill" href="pagamento.html">Quero começar <span aria-hidden="true">→</span></a></div>
</div></section>
</article>
{more}
</main>
<script>(function(){{var b=document.querySelector(".art-share .copy");if(!b)return;b.addEventListener("click",function(){{var u=b.getAttribute("data-url"),t=b.textContent;
function ok(){{b.textContent="Link copiado";setTimeout(function(){{b.textContent=t}},1800)}}
if(navigator.clipboard)navigator.clipboard.writeText(u).then(ok,function(){{prompt("Copie o link:",u)}});else prompt("Copie o link:",u)}})}})();</script>'''
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "description": p["resumo"],
              "datePublished": p["date"].isoformat(), "inLanguage": "pt-BR", "url": url, "mainEntityOfPage": url,
              "image": SITE + "/nelson_hero.jpg",
              "author": {"@type": "Person", "name": "Nelson Mendonça Neto", "jobTitle": "Psicólogo e Psicanalista", "url": SITE + "/sobre"},
              "isPartOf": {"@type": "Blog", "name": SEC, "url": SITE + "/textos"}}
        open(f"deploy/textos/{p['slug']}.html", "w", encoding="utf-8").write(
            page(full, m, p["title"] + " · " + SEC, p["resumo"], f"/textos/{p['slug']}", ld, "article"))

    # bloco na página inicial: a citação do texto mais recente que tiver uma
    if posts:
        p = next((q for q in posts if q["cit"]), posts[0])
        frase = (p["cit"] or p["resumo"]).strip('“”"\' ')
        blk = (f'<section class="tx-home" id="textos" aria-labelledby="t-textos"><div class="wrap">'
               f'<p class="eb" id="t-textos">A vida como ela se diz</p>'
               f'<figure class="txq reveal"><blockquote>“{esc(frase)}”</blockquote>'
               f'<figcaption>Nelson Mendonça Neto, em <a href="textos/{p["slug"]}.html">{esc(p["title"])}</a></figcaption></figure>'
               f'<div class="txq-btns"><a class="pill pill-dark" href="textos/{p["slug"]}.html">Ler o texto <span aria-hidden="true">→</span></a>'
               f'<a class="pill pill-line" href="textos.html">Outros textos do Nelson</a></div></div></section>\n')
        anchor = '<div class="sec-div" aria-hidden="true"><span><img src="mono_terra.png" alt="" width="40" height="15"></span></div>\n<section id="para-quem-e">' if '<section id="para-quem-e">' in full else '<section id="duvidas">'
        home = full.replace(anchor, '<div class="sec-div" aria-hidden="true"><span><img src="mono_terra.png" alt="" width="40" height="15"></span></div>\n' + blk + anchor, 1).replace("</style>", CSS + "</style>", 1)
        open("deploy/index.html", "w", encoding="utf-8").write(home)
    # seção de textos na página Livros e textos (abaixo dos livros)
    lv = open("deploy/livros.html", encoding="utf-8").read()
    if "<!--TEXTOS-->" in lv:
        def short(d): return f"{d.day} {MESES[d.month-1][:3]}. {d.year}"
        if posts:
            top = posts[:3]
            def fcard(p, i):
                q = f'<blockquote class="txc-q">“{esc(p["cit"].strip(chr(8220)+chr(8221)+chr(34)+" "))}”</blockquote>' if (i == 0 and p["cit"]) else ""
                return (f'<li><a class="txc{" txc-main" if i == 0 else ""}" href="textos/{p["slug"]}.html">{q}'
                        f'<span class="tx-meta">{short(p["date"])} · {p["min"]} min de leitura</span>'
                        f'<h3>{esc(p["title"])}</h3><p>{esc(p["resumo"])}</p><span class="tx-go">Ler o texto <span aria-hidden="true">→</span></span></a></li>')
            body = '<ul class="txc-list">' + "".join(fcard(p, i) for i, p in enumerate(top)) + '</ul>'
        else:
            body = '<p class="tx-empty">Os primeiros textos chegam em breve.</p>'
        n = len(posts)
        sec = (f'<section class="lv-sec tx-home tx-feat" id="textos" aria-labelledby="t-txt"><div class="wrap txf">'
               f'<div class="txf-intro"><p class="eb">Textos</p><h2 id="t-txt">A vida como ela <em>se diz.</em></h2>'
               f'<p class="txf-lead">Além dos livros, eu escrevo textos curtos sobre o que a psicanálise escuta no amor, na saudade, no trabalho e em tudo aquilo que se repete. <em class="txf-cafe-t">Textos para pensar tomando um cafezinho.</em></p>'
               f'<a class="pill pill-line" href="textos.html">Todos os textos <span aria-hidden="true">→</span></a></div>'
               f'<div class="txf-cards">{body}<a class="pill pill-line txf-m" href="textos.html">Todos os textos <span aria-hidden="true">→</span></a></div></div><img class="xicara" src="xicara.webp" alt="" width="520" height="499" loading="lazy"></section>')
        FEAT = """.tx-feat{padding:clamp(64px,8vw,112px) 0;background-image:linear-gradient(90deg,rgba(242,235,224,.6),rgba(242,235,224,.35) 40%,rgba(242,235,224,0) 60%),url(tex_textos.jpg);background-size:cover,cover;background-position:center,center}
.txf{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:clamp(32px,5vw,72px);align-items:center}
.tx-home .eb{color:var(--prof);font-size:12px}.tx-home .eb::after{background:var(--prof)}
.txc-main{padding:34px 34px 30px}
.txc-q{margin:0 0 22px;padding-bottom:20px;border-bottom:1px solid var(--line);font-family:var(--display);font-style:italic;font-size:clamp(21px,2.2vw,26px);line-height:1.35;color:var(--terra)}
.txf-intro h2{font-family:var(--display);font-weight:400;font-size:clamp(36px,4.6vw,56px);line-height:1.05;margin:6px 0 18px}
.txf-intro h2 em{font-style:italic;font-weight:300;color:var(--terra)}
.txf-lead{font-family:var(--display);font-size:clamp(19px,1.8vw,22px);line-height:1.5;color:#262E3A;margin:0 0 28px;max-width:34ch}
.txc-list{list-style:none;margin:0;padding:0;display:grid;gap:18px}
.txc{display:block;text-decoration:none;color:var(--ink);background:rgba(251,248,243,.94);padding:26px 28px;box-shadow:0 18px 40px rgba(30,39,52,.14);border-left:3px solid var(--terra);transition:transform .25s ease,box-shadow .25s ease}
.txc:hover{transform:translateY(-3px);box-shadow:0 24px 50px rgba(30,39,52,.2)}
.txc h3{font-family:var(--display);font-weight:400;font-size:clamp(22px,2.2vw,27px);line-height:1.2;margin:10px 0 8px}
.txc p{font-size:16px;line-height:1.6;color:#3F3A35;margin:0}
.txf-m{display:none}
.txf-cafe-t{display:block;margin-top:10px;font-style:italic;color:var(--terra)}
.tx-feat{position:relative;overflow:hidden}.tx-feat .wrap{position:relative;z-index:1}
.xicara{position:absolute;right:-50px;bottom:-110px;width:290px;height:auto;z-index:0;pointer-events:none;filter:drop-shadow(10px 16px 18px rgba(30,39,52,.28));animation:xic 8s ease-in-out infinite}
@keyframes xic{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-8px) rotate(-2deg)}}
@media (prefers-reduced-motion:reduce){.xicara{animation:none}}
@media (max-width:1240px){.xicara{width:220px;right:-50px;bottom:-80px}}
@media (max-width:860px){.tx-feat{padding-bottom:130px}.xicara{width:170px;right:-30px;bottom:-50px}}

@media (max-width:860px){.txf{grid-template-columns:1fr}.txf-intro .pill{display:none}.txf-m{display:flex;width:100%;justify-content:center;margin-top:22px}.txc,.txc-main{padding:24px 22px}}
@media (prefers-reduced-motion:reduce){.txc{transition:none}.txc:hover{transform:none}}
"""
        lv = lv.replace("<!--TEXTOS-->", sec).replace("</style>", CSS + FEAT + "</style>", 1)
        open("deploy/livros.html", "w", encoding="utf-8").write(lv)
    return posts

if __name__ == "__main__":
    print(len(main()), "texto(s)")
