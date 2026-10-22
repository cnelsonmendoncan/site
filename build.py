# Monta o site inteiro em ./deploy  (o Netlify roda isto a cada mudança no GitHub)
import os, re, sys, glob, shutil, runpy, datetime as D

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "deploy")
SCR = os.path.join(ROOT, "scripts")

shutil.rmtree(OUT, ignore_errors=True)
shutil.copytree(os.path.join(ROOT, "static"), OUT)
os.chdir(SCR)
if os.path.lexists("deploy"): os.remove("deploy")
os.symlink(OUT, "deploy")
sys.path.insert(0, SCR)
try:
    for s in ["build_site", "build_pag", "build_livros", "build_cursos", "build_sobre", "build_lp"]:
        runpy.run_path(s + ".py", run_name="__main__")
    tx = runpy.run_path("build_textos.py")      # roda por último: acrescenta o bloco na página inicial
    posts = tx["main"]()
finally:
    os.remove("deploy")

# todos os endereços passam a ser a partir da raiz (/), para funcionarem também em /textos/...
SKIP = r"(?:https?:|//|/|#|mailto:|tel:|data:|javascript:)"
def absol(h):
    h = re.sub(r'\b(src|href|poster)="(?!' + SKIP + r')([^"]+)"', r'\1="/\2"', h)
    h = re.sub(r'\bsrcset="([^"]+)"', lambda m: 'srcset="' + ", ".join(
        (p.strip() if re.match(SKIP, p.strip()) else "/" + p.strip()) for p in m.group(1).split(",")) + '"', h)
    h = re.sub(r'url\((?![\'"]?' + SKIP + r')([\'"]?)([^)\'"]+)\1\)', r'url(\1/\2\1)', h)
    return h
for f in glob.glob(os.path.join(OUT, "**", "*.html"), recursive=True):
    s = open(f, encoding="utf-8").read()
    s = re.sub(r'<a class="skip" href="[^"]*"', '<a class="skip" href="#inicio"', absol(s))
    open(f, "w", encoding="utf-8").write(s)

# sitemap
today = D.date.today().isoformat()
urls = [("/", "1.0", today), ("/sobre", "0.7", today), ("/pagamento", "0.8", today), ("/livros", "0.7", today), ("/cursos", "0.5", today), ("/textos", "0.7", today)]
urls += [("/textos/" + p["slug"], "0.7", p["date"].isoformat()) for p in posts]
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u, pr, lm in urls:
        f.write(f"<url><loc>https://nelsonmendonca.com{u}</loc><lastmod>{lm}</lastmod><priority>{pr}</priority></url>\n")
    f.write("</urlset>\n")
print("site pronto:", len(posts), "texto(s)")
