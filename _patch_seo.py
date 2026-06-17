import os, re

DST = r'C:\Users\info\the420code'

SEO = {
    'en': {
        'lang': 'en',
        'url': 'https://the420code.org/',
        'title': 'the 420 code — ethics derived from physics',
        'desc': 'Can ethics be derived from physics? The 420 Code says yes. 42 Artist\'s Proofs. Over a million words. One measured input. Zero fitted parameters. Copyleft. Free forever.',
    },
    'es': {
        'lang': 'es',
        'url': 'https://the420code.org/es/',
        'title': 'the 420 code — la ética derivada de la física',
        'desc': '¿Puede la ética derivarse de la física? The 420 Code dice que sí. 42 Pruebas de Artista. Más de un millón de palabras. Una entrada medida. Cero parámetros ajustados. Copyleft. Gratis para siempre.',
    },
    'fr': {
        'lang': 'fr',
        'url': 'https://the420code.org/fr/',
        'title': "the 420 code — l'éthique dérivée de la physique",
        'desc': "L'éthique peut-elle être dérivée de la physique ? The 420 Code dit oui. 42 Épreuves d'Artiste. Plus d'un million de mots. Une entrée mesurée. Zéro paramètre ajusté. Copyleft. Gratuit pour toujours.",
    },
    'de': {
        'lang': 'de',
        'url': 'https://the420code.org/de/',
        'title': 'the 420 code — Ethik abgeleitet aus der Physik',
        'desc': 'Kann Ethik aus der Physik abgeleitet werden? The 420 Code sagt ja. 42 Künstlerbeweise. Über eine Million Wörter. Eine gemessene Eingabe. Null angepasste Parameter. Copyleft. Für immer kostenlos.',
    },
    'pt': {
        'lang': 'pt',
        'url': 'https://the420code.org/pt/',
        'title': 'the 420 code — a ética derivada da física',
        'desc': 'A ética pode ser derivada da física? The 420 Code diz que sim. 42 Provas de Artista. Mais de um milhão de palavras. Uma entrada medida. Zero parâmetros ajustados. Copyleft. Grátis para sempre.',
    },
    'nl': {
        'lang': 'nl',
        'url': 'https://the420code.org/nl/',
        'title': 'the 420 code — ethiek afgeleid uit de natuurkunde',
        'desc': 'Kan ethiek worden afgeleid uit de natuurkunde? The 420 Code zegt ja. 42 Kunstenaarsbewijzen. Meer dan een miljoen woorden. Eén gemeten invoer. Nul gefitte parameters. Copyleft. Voor altijd gratis.',
    },
    'it': {
        'lang': 'it',
        'url': 'https://the420code.org/it/',
        'title': "the 420 code — l'etica derivata dalla fisica",
        'desc': "L'etica può essere derivata dalla fisica? The 420 Code dice di sì. 42 Prove d'Artista. Oltre un milione di parole. Un input misurato. Zero parametri aggiustati. Copyleft. Gratis per sempre.",
    },
    'zh': {
        'lang': 'zh',
        'url': 'https://the420code.org/zh/',
        'title': 'the 420 code — 从物理学推导伦理',
        'desc': '伦理能从物理学推导吗？420 Code 说可以。42篇艺术家证明。超过一百万字。一个测量输入。零拟合参数。Copyleft。永远免费。',
    },
    'ja': {
        'lang': 'ja',
        'url': 'https://the420code.org/ja/',
        'title': 'the 420 code — 物理学から導かれる倫理',
        'desc': '倫理は物理学から導けるか？420 Codeはイエスと言う。42本のアーティスト・プルーフ。百万語以上。測定入力1つ。フィッティングパラメータ0。Copyleft。永遠に無料。',
    },
    'ko': {
        'lang': 'ko',
        'url': 'https://the420code.org/ko/',
        'title': 'the 420 code — 물리학에서 도출된 윤리',
        'desc': '윤리는 물리학에서 도출될 수 있는가? 420 Code는 그렇다고 말한다. 42편의 아티스트 프루프. 백만 단어 이상. 측정 입력 1개. 맞춤 매개변수 0개. Copyleft. 영원히 무료.',
    },
    'ru': {
        'lang': 'ru',
        'url': 'https://the420code.org/ru/',
        'title': 'the 420 code — этика, выведенная из физики',
        'desc': 'Можно ли вывести этику из физики? 420 Code говорит да. 42 авторских доказательства. Более миллиона слов. Один измеренный параметр. Ноль подогнанных параметров. Copyleft. Бесплатно навсегда.',
    },
    'ar': {
        'lang': 'ar',
        'url': 'https://the420code.org/ar/',
        'title': 'the 420 code — الأخلاق المُشتقّة من الفيزياء',
        'desc': 'هل يمكن اشتقاق الأخلاق من الفيزياء؟ The 420 Code يقول نعم. 42 برهانًا فنيًّا. أكثر من مليون كلمة. مُدخل مُقاس واحد. صفر معاملات مُعدَّلة. Copyleft. مجاني إلى الأبد.',
    },
    'hi': {
        'lang': 'hi',
        'url': 'https://the420code.org/hi/',
        'title': 'the 420 code — भौतिकी से व्युत्पन्न नैतिकता',
        'desc': 'क्या नैतिकता भौतिकी से व्युत्पन्न हो सकती है? 420 Code कहता है हाँ। 42 कलाकार प्रमाण। दस लाख से अधिक शब्द। एक मापित इनपुट। शून्य फ़िट किए गए पैरामीटर। Copyleft। हमेशा मुफ़्त।',
    },
}

for lang, s in SEO.items():
    if lang == 'en':
        fp = os.path.join(DST, 'index.html')
        img_path = 'Eye_of_the_Universe.jpg'
    else:
        fp = os.path.join(DST, lang, 'index.html')
        img_path = '../Eye_of_the_Universe.jpg'

    with open(fp, 'r', encoding='utf-8') as f:
        h = f.read()

    # Build SEO block
    seo_block = f'''<link rel="canonical" href="{s['url']}">
<meta property="og:type" content="website">
<meta property="og:url" content="{s['url']}">
<meta property="og:title" content="{s['title']}">
<meta property="og:description" content="{s['desc']}">
<meta property="og:image" content="https://the420code.org/Eye_of_the_Universe.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="the 420 code">
<meta property="og:locale" content="{s['lang']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{s['title']}">
<meta name="twitter:description" content="{s['desc']}">
<meta name="twitter:image" content="https://the420code.org/Eye_of_the_Universe.jpg">
<meta name="robots" content="index, follow">
<meta name="author" content="G — Studio G">
<link rel="icon" type="image/jpeg" href="{img_path}">'''

    # Also add Zenodo DOI link
    seo_block += '\n<meta name="citation_doi" content="10.5281/zenodo.19208226">'

    # Add hreflang tags for all languages
    hreflang = '<link rel="alternate" hreflang="en" href="https://the420code.org/">'
    for l2 in ['es','fr','de','pt','nl','it','zh','ja','ko','ru','ar','hi']:
        hreflang += f'\n<link rel="alternate" hreflang="{l2}" href="https://the420code.org/{l2}/">'
    hreflang += '\n<link rel="alternate" hreflang="x-default" href="https://the420code.org/">'
    seo_block += '\n' + hreflang

    # Insert after the description meta tag
    if 'og:title' not in h:
        # Insert after the closing > of the description meta tag
        desc_pattern = r'(<meta name="description" content="[^"]*">)'
        h = re.sub(desc_pattern, r'\1\n' + seo_block, h, count=1)

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(h)

    print(f'  {lang}: SEO tags added')

print('Done')
