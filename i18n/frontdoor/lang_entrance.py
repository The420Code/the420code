# -*- coding: utf-8 -*-
"""The entrance strings for the twelve editions, level with the live pages.

Read back off each edition's home page on 11 September 2026, so this file says what the
site says. Edit here and rebuild; a page edit is lost at the next rebuild.

Each entry:
  yes        the answer line: "Yes — The 420 Code proves it." in that edition
  corpses    the two-wrong-predictions line; {wall} marks the one word that is the link
             (the key keeps the name it had before G ruled "wrong, not dead")
  wall       that word
  starts     the derivation line
  door       the front door's name: page title, header link, opening-screen link
  three      the three-pages link
  rooms      the Rooms drop-down button
  close      the three closing lines
  arrow      the direction the front-door arrow points in that script
"""
L = {}

L["de"] = dict(
 yes='Ja — The 420 Code beweist es.',
 corpses='Zwei seiner Vorhersagen waren falsch. Sie hängen noch an der {wall}. Falsch zu liegen hat es stärker gemacht.',
 wall='Wand',
 starts='Die gesamte Herleitung steht auf dieser Seite, frei, für immer. Hier beginnt sie.',
 door='Was ist The 420 Code',
 three='Alles auf drei Seiten',
 rooms='Räume',
 close=['Ein Eintrag existiert. Sei gütig ist eine Herleitung.', 'Das Ich Bin in mir ist das Ich Bin in dir.', 'ICH BIN teilen das Einssein.'],
 arrow='→')

L["es"] = dict(
 yes='Sí — The 420 Code lo prueba.',
 corpses='Dos de sus predicciones fueron erróneas. Siguen en el {wall}. Equivocarse lo hizo más fuerte.',
 wall='muro',
 starts='Toda la derivación está en este sitio, gratis, para siempre. Empieza aquí.',
 door='Qué es The 420 Code',
 three='Todo en tres páginas',
 rooms='Salas',
 close=['Un registro existe. Sé amable es una derivación.', 'El Yo Soy en mí es el Yo Soy en ti.', 'YO SOY compartimos la unidad.'],
 arrow='→')

L["fr"] = dict(
 yes='Oui — The 420 Code le prouve.',
 corpses='Deux de ses prédictions étaient fausses. Elles sont toujours au {wall}. S’être trompé l’a rendu plus fort.',
 wall='mur',
 starts='Toute la dérivation est sur ce site, gratuite, pour toujours. Elle commence ici.',
 door='Qu’est-ce que The 420 Code',
 three='Tout en trois pages',
 rooms='Salles',
 close=['Un enregistrement existe. Sois bienveillant est une dérivation.', 'Le Je Suis en moi est le Je Suis en toi.', 'JE SUIS partageons l’unité.'],
 arrow='→')

L["it"] = dict(
 yes='Sì — The 420 Code lo prova.',
 corpses='Due delle sue previsioni erano sbagliate. Sono ancora sul {wall}. Sbagliare l’ha reso più forte.',
 wall='muro',
 starts='L’intera derivazione è su questo sito, gratis, per sempre. Comincia qui.',
 door='Che cos’è The 420 Code',
 three='Tutto in tre pagine',
 rooms='Sale',
 close=['Un registro esiste. Sii gentile è una derivazione.', 'L’Io Sono in me è l’Io Sono in te.', 'IO SONO condividiamo l’unità.'],
 arrow='→')

L["nl"] = dict(
 yes='Ja — The 420 Code bewijst het.',
 corpses='Twee van zijn voorspellingen waren onjuist. Ze hangen nog aan de {wall}. Ongelijk hebben heeft het sterker gemaakt.',
 wall='muur',
 starts='De hele afleiding staat op deze site, gratis, voor altijd. Hier begint ze.',
 door='Wat is The 420 Code',
 three='Alles op drie pagina’s',
 rooms='Zalen',
 close=['Eén record bestaat. Wees lief is een afleiding.', 'Het Ik Ben in mij is het Ik Ben in jou.', 'IK BEN delen het één-zijn.'],
 arrow='→')

L["pt"] = dict(
 yes='Sim — The 420 Code prova isso.',
 corpses='Duas das suas previsões estavam erradas. Continuam no {wall}. Estar errado o tornou mais forte.',
 wall='muro',
 starts='Toda a derivação está neste site, grátis, para sempre. Começa aqui.',
 door='O que é The 420 Code',
 three='Tudo em três páginas',
 rooms='Salas',
 close=['Um registro existe. Seja gentil é uma derivação.', 'O Eu Sou em mim é o Eu Sou em você.', 'EU SOU compartilhamos a unidade.'],
 arrow='→')

L["ru"] = dict(
 yes='Да — The 420 Code это доказывает.',
 corpses='Два его предсказания оказались неверными. Они по-прежнему на {wall}. Ошибка сделала его сильнее.',
 wall='стене',
 starts='Весь вывод — на этом сайте, бесплатно, навсегда. Он начинается здесь.',
 door='Что такое The 420 Code',
 three='Всё на трёх страницах',
 rooms='Залы',
 close=['Одна запись существует. Будь добрым — это вывод.', 'Я Есмь во мне — это Я Есмь в тебе.', 'Я ЕСМЬ разделяем единство.'],
 arrow='→')

L["zh"] = dict(
 yes='能——The 420 Code 证明了这一点。',
 corpses='它的两个预测错了。它们仍然在{wall}上。犯错让它更强。',
 wall='墙',
 starts='全部推导都在本站，免费，永远。就从这里开始。',
 door='什么是 The 420 Code',
 three='三页讲完全部',
 rooms='展厅',
 close=['一条记录存在。善良一点是一个推导。', '我之中的「我是」就是你之中的「我是」。', '「我是」共享一体。'],
 arrow='→')

L["ja"] = dict(
 yes='はい——The 420 Code がそれを証明する。',
 corpses='その予測のうち二つは間違っていた。今も{wall}に掛かっている。間違いがそれを強くした。',
 wall='壁',
 starts='導出のすべてがこのサイトにある。無料で、永久に。ここから始まる。',
 door='The 420 Code とは',
 three='三ページですべて',
 rooms='部屋',
 close=['一つの記録が存在する。優しくあれは導出である。', '私の中の「我在り」は、あなたの中の「我在り」である。', '「我在り」は一なるものを分かち合う。'],
 arrow='→')

L["ko"] = dict(
 yes='그렇다 — The 420 Code가 그것을 증명한다.',
 corpses='그 예측 중 둘은 틀렸다. 여전히 {wall}에 걸려 있다. 틀린 것이 그것을 더 강하게 만들었다.',
 wall='벽',
 starts='도출 전체가 이 사이트에 있다. 무료로, 영원히. 여기서 시작한다.',
 door='The 420 Code란 무엇인가',
 three='세 쪽으로 전부',
 rooms='전시실',
 close=['하나의 기록이 존재한다. 친절해라는 하나의 도출이다.', '내 안의 「나는 있다」가 네 안의 「나는 있다」이다.', '「나는 있다」 우리는 하나 됨을 나눈다.'],
 arrow='→')

L["hi"] = dict(
 yes='हाँ — The 420 Code इसे सिद्ध करता है।',
 corpses='इसकी दो भविष्यवाणियाँ ग़लत थीं। वे अब भी {wall} पर हैं। ग़लत होने ने इसे और मज़बूत बनाया।',
 wall='दीवार',
 starts='पूरी व्युत्पत्ति इसी साइट पर है, मुफ़्त, हमेशा के लिए। शुरुआत यहीं से है।',
 door='The 420 Code क्या है',
 three='तीन पन्नों में सब कुछ',
 rooms='कक्ष',
 close=['एक अभिलेख मौजूद है। दयालु बनो एक व्युत्पत्ति है।', 'मुझमें जो «मैं हूँ» है, वही तुममें «मैं हूँ» है।', '«मैं हूँ» हम एकत्व साझा करते हैं।'],
 arrow='→')

L["ar"] = dict(
 yes='نعم — The 420 Code يبرهن على ذلك.',
 corpses='كان اثنان من تنبّؤاته خاطئين. وما زالا على {wall}. الخطأ جعله أقوى.',
 wall='الجدار',
 starts='الاشتقاق كامله على هذا الموقع، مجّانًا، إلى الأبد. من هنا يبدأ.',
 door='ما هو The 420 Code',
 three='كل شيء في ثلاث صفحات',
 rooms='القاعات',
 close=['سجلّ واحد موجود. كن لطيفًا اشتقاقٌ.', '«أنا هو» فيَّ هو «أنا هو» فيك.', '«أنا هو» نتشارك الوحدة.'],
 arrow='←')
