
import re, json, html as H
src=open("index.src.html").read()
faq=[]
for q,a in re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>',src,re.S):
    t=lambda x:H.unescape(re.sub(r'<[^>]+>','',x)).strip()
    faq.append({"@type":"Question","name":t(q),"acceptedAnswer":{"@type":"Answer","text":t(a)}})
data=[{"@context":"https://schema.org","@type":"ProfessionalService","@id":"https://nelsonmendonca.com/#consultorio",
 "name":"Nelson Mendonça Neto · Psicanálise","url":"https://nelsonmendonca.com/","image":"https://nelsonmendonca.com/nelson_hero.jpg",
 "description":"Psicanálise online em português para brasileiros no exterior e adultos no Brasil.",
 "telephone":"+55 79 99604-1731","email":"consultorio@nelsonmendonca.com","priceRange":"$$",
 "address":{"@type":"PostalAddress","addressLocality":"Aracaju","addressRegion":"SE","addressCountry":"BR"},
 "areaServed":"Mundo","availableLanguage":"pt-BR","sameAs":["https://instagram.com/nelsonmendonca.psi"],
 "founder":{"@type":"Person","name":"Nelson Mendonça Neto","jobTitle":"Psicólogo e Psicanalista",
   "identifier":{"@type":"PropertyValue","propertyID":"CRP","value":"19/3888"},"url":"https://nelsonmendonca.com/sobre"}},
 {"@context":"https://schema.org","@type":"FAQPage","mainEntity":faq}]
LD='<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False)+'</script>\n'
# Gera deploy/index.html a partir de index.src.html (com favicons no topo do <head>)
s=open("index.src.html").read(); head,rest=s.split("<style>",1)
icons=('<link rel="icon" type="image/png" sizes="32x32" href="/fav32.png">\n<link rel="icon" type="image/png" sizes="16x16" href="/fav16.png">\n'
       '<link rel="icon" type="image/png" sizes="48x48" href="/fav48.png">\n<link rel="icon" type="image/svg+xml" href="/fav.svg">\n'
       '<link rel="shortcut icon" href="/favicon.ico">\n<link rel="apple-touch-icon" sizes="180x180" href="/nmn-180.png">\n')
full=('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'+icons+
      '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'+head+
      '<meta name="theme-color" content="#1E2734">\n<meta property="og:title" content="Nelson Mendonça Neto · Psicanálise">\n'
      '<meta property="og:description" content="Psicanálise online em português para brasileiros no exterior e adultos no Brasil.">\n'
      '<meta property="og:image" content="https://nelsonmendonca.com/nelson_hero.jpg">\n<meta property="og:url" content="https://nelsonmendonca.com/">\n<meta property="og:type" content="website">\n<meta property="og:locale" content="pt_BR">\n<link rel="canonical" href="https://nelsonmendonca.com/">\n'+LD+'<style>'+rest.replace("</style>","</style>\n</head>\n<body>",1)+"\n</body>\n</html>\n")
full=full.replace("</style>",open("trilha.css").read()+"</style>",1)
full=full.replace("\n</body>","\n"+open("trilha.html").read()+"</body>",1)
open("deploy/index.html","w").write(full)
