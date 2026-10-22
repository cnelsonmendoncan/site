# Site · Nelson Mendonça Neto

Site de nelsonmendonca.com. O Netlify monta e publica sozinho a cada mudança aqui.

## Publicar um texto novo
1. Entre em **app.pagescms.org** com a conta do GitHub.
2. Abra **Textos · A vida como ela se diz** e clique em **Add an entry** (novo).
3. Preencha título, data, frase de abertura e o texto. Clique em **Save**.
4. Em cerca de 1 minuto ele aparece em nelsonmendonca.com/textos e na página inicial.

Para salvar sem publicar, marque **Rascunho**. Para tirar um texto do ar, marque Rascunho ou apague.

## Estrutura (para quem for mexer no código)
- `content/textos/` · os textos (um arquivo por texto)
- `scripts/` · modelo do site (`index.src.html`) e os montadores de cada página
- `static/` · imagens, ícones, PDFs e músicas
- `build.py` · monta tudo em `deploy/`
