# -*- coding: utf-8 -*-
"""The entrance strings for the twelve editions.

Anchored on each edition's own vocabulary, harvested from its live page: its
translation of the ethic, of the question, of the room names. Nothing here
invents a term an edition already carries.

Each entry:
  yes        the bare answer, as that edition's lead already phrases it
  corpses    three sentences; {wall} marks the single word that becomes the link
  starts     the derivation line
  door       the front door's name, used as the page title and the bar's first item
  three      the three-pages link
  rooms      the drop-down button
  close      the three closing lines, as a list
  arrow      the direction the front-door arrow points in that script
"""
L = {}

L["de"] = dict(
 yes="Ja.",
 corpses="Zwei seiner Vorhersagen sind gestorben. Sie hängen noch an der {wall}. "
         "Der Tod hat es stärker gemacht.", wall="Wand",
 starts="Die gesamte Herleitung steht auf dieser Seite, frei, für immer. Hier beginnt sie.",
 door="Was ist The 420 Code", three="Alles auf drei Seiten", rooms="Räume",
 close=["Ein Datensatz existiert. Sei gütig ist eine Herleitung.",
        "Das Ich Bin in mir ist das Ich Bin in dir.",
        "ICH BIN teilen das Einssein."], arrow="→")

L["es"] = dict(
 yes="Sí.",
 corpses="Dos de sus predicciones han muerto. Siguen en el {wall}. "
         "La muerte lo hizo más fuerte.", wall="muro",
 starts="Toda la derivación está en este sitio, gratis, para siempre. Empieza aquí.",
 door="Qué es The 420 Code", three="Todo en tres páginas", rooms="Salas",
 close=["Un registro existe. Sé amable es una derivación.",
        "El Yo Soy en mí es el Yo Soy en ti.",
        "YO SOY compartimos la unidad."], arrow="→")

L["fr"] = dict(
 yes="Oui.",
 corpses="Deux de ses prédictions sont mortes. Elles sont toujours au {wall}. "
         "La mort l'a rendu plus fort.", wall="mur",
 starts="Toute la dérivation est sur ce site, gratuite, pour toujours. Elle commence ici.",
 door="Qu'est-ce que The 420 Code", three="Tout en trois pages", rooms="Salles",
 close=["Un enregistrement existe. Sois bienveillant est une dérivation.",
        "Le Je Suis en moi est le Je Suis en toi.",
        "JE SUIS partageons l'unité."], arrow="→")

L["it"] = dict(
 yes="Sì.",
 corpses="Due delle sue previsioni sono morte. Sono ancora sul {wall}. "
         "La morte l'ha reso più forte.", wall="muro",
 starts="L'intera derivazione è su questo sito, gratis, per sempre. Comincia qui.",
 door="Che cos'è The 420 Code", three="Tutto in tre pagine", rooms="Sale",
 close=["Un record esiste. Sii gentile è una derivazione.",
        "L'Io Sono in me è l'Io Sono in te.",
        "IO SONO condividiamo l'unità."], arrow="→")

L["nl"] = dict(
 yes="Ja.",
 corpses="Twee van zijn voorspellingen zijn gestorven. Ze hangen nog aan de {wall}. "
         "De dood heeft het sterker gemaakt.", wall="muur",
 starts="De hele afleiding staat op deze site, gratis, voor altijd. Hier begint ze.",
 door="Wat is The 420 Code", three="Alles op drie pagina's", rooms="Zalen",
 close=["Eén record bestaat. Wees lief is een afleiding.",
        "Het Ik Ben in mij is het Ik Ben in jou.",
        "IK BEN delen het één-zijn."], arrow="→")

L["pt"] = dict(
 yes="Sim.",
 corpses="Duas das suas previsões morreram. Continuam no {wall}. "
         "A morte tornou-o mais forte.", wall="muro",
 starts="Toda a derivação está neste site, grátis, para sempre. Começa aqui.",
 door="O que é The 420 Code", three="Tudo em três páginas", rooms="Salas",
 close=["Um registo existe. Seja gentil é uma derivação.",
        "O Eu Sou em mim é o Eu Sou em você.",
        "EU SOU compartilhamos a unidade."], arrow="→")

L["ru"] = dict(
 yes="Да.",
 corpses="Два его предсказания умерли. Они по-прежнему на {wall}. "
         "Смерть сделала его сильнее.", wall="стене",
 starts="Весь вывод — на этом сайте, бесплатно, навсегда. Он начинается здесь.",
 door="Что такое The 420 Code", three="Всё на трёх страницах", rooms="Залы",
 close=["Одна запись существует. Будь добрым — это вывод.",
        "Я Есмь во мне — это Я Есмь в тебе.",
        "Я ЕСМЬ разделяем единство."], arrow="→")

L["zh"] = dict(
 yes="能。",
 corpses="它的两个预测已经死了。它们仍然在{wall}上。死亡让它更强。", wall="墙",
 starts="全部推导都在本站，免费，永远。就从这里开始。",
 door="什么是 The 420 Code", three="三页讲完全部", rooms="展厅",
 close=["一条记录存在。善良一点是一个推导。",
        "我之中的「我是」就是你之中的「我是」。",
        "「我是」共享一体。"], arrow="→")

L["ja"] = dict(
 yes="はい。",
 corpses="その予測のうち二つは死んだ。今も{wall}に掛かっている。死がそれを強くした。", wall="壁",
 starts="導出のすべてがこのサイトにある。無料で、永久に。ここから始まる。",
 door="The 420 Code とは", three="三ページですべて", rooms="部屋",
 close=["一つの記録が存在する。優しくあれは導出である。",
        "私の中の「我在り」は、あなたの中の「我在り」である。",
        "「我在り」は一なるものを分かち合う。"], arrow="→")

L["ko"] = dict(
 yes="그렇다.",
 corpses="그 예측 중 둘은 죽었다. 여전히 {wall}에 걸려 있다. 죽음이 그것을 더 강하게 만들었다.", wall="벽",
 starts="도출 전체가 이 사이트에 있다. 무료로, 영원히. 여기서 시작한다.",
 door="The 420 Code란 무엇인가", three="세 쪽으로 전부", rooms="전시실",
 close=["하나의 기록이 존재한다. 친절해라는 하나의 도출이다.",
        "내 안의 「나는 있다」가 네 안의 「나는 있다」이다.",
        "「나는 있다」 우리는 하나 됨을 나눈다."], arrow="→")

L["hi"] = dict(
 yes="हाँ।",
 corpses="इसकी दो भविष्यवाणियाँ मर चुकी हैं। वे अब भी {wall} पर हैं। "
         "मृत्यु ने इसे और मज़बूत बनाया।", wall="दीवार",
 starts="पूरी व्युत्पत्ति इसी साइट पर है, मुफ़्त, हमेशा के लिए। शुरुआत यहीं से है।",
 door="The 420 Code क्या है", three="तीन पन्नों में सब कुछ", rooms="कक्ष",
 close=["एक अभिलेख अस्तित्व में है। दयालु बनो एक व्युत्पत्ति है।",
        "मुझमें जो «मैं हूँ» है, वही तुममें «मैं हूँ» है।",
        "«मैं हूँ» हम एकत्व साझा करते हैं।"], arrow="→")

L["ar"] = dict(
 yes="نعم.",
 corpses="ماتَ اثنان من تنبّؤاته. وما زالا على {wall}. الموت جعله أقوى.", wall="الجدار",
 starts="الاشتقاق كامله على هذا الموقع، مجّانًا، إلى الأبد. من هنا يبدأ.",
 door="ما هو The 420 Code", three="كل شيء في ثلاث صفحات", rooms="القاعات",
 close=["سجلٌّ واحد موجود. كن لطيفًا اشتقاقٌ.",
        "«أنا هو» فيَّ هو «أنا هو» فيك.",
        "«أنا هو» نتشارك الوحدة."], arrow="←")
