const fs = require('fs');
const path = require('path');
const LANGS = ['es','fr','de','pt','nl','it','zh','ja','ko','ru','ar','hi'];

// AP subtitle translations for the 9 that are still English
const SUBS = {
'The axiom 1:1 + 1×ε is structurally irrational — and true. Irrationality as the foundation of the rational. Choice as irrational coupling capacity.':{
  es:'El axioma 1:1 + 1×ε es estructuralmente irracional — y verdadero. La irracionalidad como fundamento de lo racional. La elección como capacidad de acoplamiento irracional.',
  fr:"L'axiome 1:1 + 1×ε est structurellement irrationnel — et vrai. L'irrationalité comme fondement du rationnel. Le choix comme capacité de couplage irrationnel.",
  de:'Das Axiom 1:1 + 1×ε ist strukturell irrational — und wahr. Irrationalität als Fundament des Rationalen. Wahl als irrationale Kopplungskapazität.',
  pt:'O axioma 1:1 + 1×ε é estruturalmente irracional — e verdadeiro. A irracionalidade como fundamento do racional. A escolha como capacidade de acoplamento irracional.',
  nl:'Het axioma 1:1 + 1×ε is structureel irrationeel — en waar. Irrationaliteit als fundament van het rationele. Keuze als irrationeel koppelingsvermogen.',
  it:"L'assioma 1:1 + 1×ε è strutturalmente irrazionale — e vero. L'irrazionalità come fondamento del razionale. La scelta come capacità di accoppiamento irrazionale.",
  zh:'公理 1:1 + 1×ε 在结构上是无理的——且为真。无理性作为理性的基础。选择作为无理耦合能力。',
  ja:'公理 1:1 + 1×ε は構造的に無理数的であり——そして真である。合理の基盤としての非合理。非合理結合能力としての選択。',
  ko:'공리 1:1 + 1×ε는 구조적으로 무리수적이다 — 그리고 참이다. 합리의 기초로서의 비합리. 비합리적 결합 능력으로서의 선택.',
  ru:'Аксиома 1:1 + 1×ε структурно иррациональна — и истинна. Иррациональность как основание рационального. Выбор как иррациональная ёмкость связи.',
  ar:'البديهية 1:1 + 1×ε لا عقلانية بنيويًّا — وصحيحة. اللاعقلانية كأساس للعقلاني. الاختيار كسعة اقتران لاعقلانية.',
  hi:'स्वयंसिद्ध 1:1 + 1×ε संरचनात्मक रूप से अपरिमेय है — और सत्य। परिमेय की नींव के रूप में अपरिमेयता। अपरिमेय युग्मन क्षमता के रूप में चुनाव।'},
'The spine. Papers A–D derive the actualization state, viability geometry, agency, and coupled corridors.':{
  es:'La columna vertebral. Los artículos A–D derivan el estado de actualización, la geometría de viabilidad, la agencia y los corredores acoplados.',
  fr:'La colonne vertébrale. Les articles A–D dérivent l\'état d\'actualisation, la géométrie de viabilité, l\'agentivité et les corridors couplés.',
  de:'Das Rückgrat. Die Arbeiten A–D leiten den Aktualisierungszustand, die Viabilitätsgeometrie, die Handlungsfähigkeit und gekoppelte Korridore ab.',
  pt:'A espinha dorsal. Os artigos A–D derivam o estado de atualização, a geometria de viabilidade, a agência e os corredores acoplados.',
  nl:'De ruggengraat. Artikelen A–D leiden de actualisatietoestand, viabiliteitsgeometrie, agentschap en gekoppelde corridors af.',
  it:'La spina dorsale. Gli articoli A–D derivano lo stato di attualizzazione, la geometria di viabilità, l\'agency e i corridoi accoppiati.',
  zh:'脊柱。论文A–D推导实现态、可行性几何、能动性和耦合走廊。',
  ja:'背骨。論文A–Dは実現状態、生存可能性幾何学、エージェンシー、結合回廊を導出する。',
  ko:'척추. 논문 A–D는 실현 상태, 생존 가능성 기하학, 행위능력, 결합 회랑을 도출한다.',
  ru:'Хребет. Статьи A–D выводят состояние актуализации, геометрию жизнеспособности, агентность и связанные коридоры.',
  ar:'العمود الفقري. الأبحاث A–D تشتقّ حالة التحقّق، هندسة القابلية للحياة، الفاعلية، والممرات المقترنة.',
  hi:'रीढ़। पत्र A–D साक्षात्कार अवस्था, व्यवहार्यता ज्यामिति, कर्तृत्व और युग्मित गलियारे व्युत्पन्न करते हैं।'},
'The Embedding Hypothesis as theorem. Axioms proved unconditional. All downstream results inherit.':{
  es:'La Hipótesis de Inmersión como teorema. Axiomas demostrados incondicionales. Todos los resultados derivados heredan.',
  fr:'L\'Hypothèse d\'Encastrement comme théorème. Axiomes prouvés inconditionnels. Tous les résultats en aval héritent.',
  de:'Die Einbettungshypothese als Theorem. Axiome bedingungslos bewiesen. Alle nachfolgenden Ergebnisse erben.',
  pt:'A Hipótese de Imersão como teorema. Axiomas provados incondicionais. Todos os resultados posteriores herdam.',
  nl:'De Inbeddingshypothese als theorema. Axioma\'s onvoorwaardelijk bewezen. Alle stroomafwaartse resultaten erven.',
  it:'L\'Ipotesi di Immersione come teorema. Assiomi provati incondizionali. Tutti i risultati a valle ereditano.',
  zh:'嵌入假说作为定理。公理被证明是无条件的。所有下游结果继承。',
  ja:'埋め込み仮説が定理として。公理が無条件に証明された。すべての下流結果が継承する。',
  ko:'매장 가설이 정리로서. 공리가 무조건적으로 증명됨. 모든 하류 결과가 상속한다.',
  ru:'Гипотеза вложения как теорема. Аксиомы доказаны безусловно. Все нижестоящие результаты наследуют.',
  ar:'فرضية التضمين كنظرية. البديهيات أُثبتت غير مشروطة. جميع النتائج اللاحقة ترث.',
  hi:'अंतःस्थापन परिकल्पना प्रमेय के रूप में। स्वयंसिद्ध बिना शर्त सिद्ध। सभी अनुप्रवाह परिणाम वंशानुक्रम करते हैं।'},
'c derived as the conjugacy of propagation and resistance.':{
  es:'c derivada como la conjugación de propagación y resistencia.',
  fr:'c dérivée comme la conjugaison de la propagation et de la résistance.',
  de:'c abgeleitet als Konjugation von Ausbreitung und Widerstand.',
  pt:'c derivada como a conjugação de propagação e resistência.',
  nl:'c afgeleid als de conjugatie van propagatie en weerstand.',
  it:'c derivata come la coniugazione di propagazione e resistenza.',
  zh:'c 作为传播与阻力的共轭推导。',
  ja:'c は伝播と抵抗の共役として導出。',
  ko:'c는 전파와 저항의 켤레로 도출.',
  ru:'c выведена как сопряжённость распространения и сопротивления.',
  ar:'c مُشتقّة كتزاوج الانتشار والمقاومة.',
  hi:'c प्रसार और प्रतिरोध के संयुग्मन के रूप में व्युत्पन्न।'},
'From axiom to structure. The first crack — how symmetry breaks and physics begins.':{
  es:'Del axioma a la estructura. La primera grieta — cómo se rompe la simetría y comienza la física.',
  fr:'De l\'axiome à la structure. La première fissure — comment la symétrie se brise et la physique commence.',
  de:'Vom Axiom zur Struktur. Der erste Riss — wie Symmetrie bricht und Physik beginnt.',
  pt:'Do axioma à estrutura. A primeira rachadura — como a simetria se quebra e a física começa.',
  nl:'Van axioma naar structuur. De eerste scheur — hoe symmetrie breekt en fysica begint.',
  it:'Dall\'assioma alla struttura. La prima crepa — come la simmetria si rompe e la fisica inizia.',
  zh:'从公理到结构。第一道裂缝——对称性如何破缺，物理学如何开始。',
  ja:'公理から構造へ。最初の亀裂——対称性がいかに破れ、物理学が始まるか。',
  ko:'공리에서 구조로. 첫 번째 균열 — 대칭이 어떻게 깨지고 물리학이 시작되는가.',
  ru:'От аксиомы к структуре. Первая трещина — как ломается симметрия и начинается физика.',
  ar:'من البديهية إلى البنية. الشقّ الأول — كيف ينكسر التناظر وتبدأ الفيزياء.',
  hi:'स्वयंसिद्ध से संरचना तक। पहली दरार — सममिति कैसे टूटती है और भौतिकी कैसे शुरू होती है।'},
'Why three spatial dimensions — four axioms, four degrees of freedom; one is time; three remain as space.':{
  es:'Por qué tres dimensiones espaciales — cuatro axiomas, cuatro grados de libertad; uno es el tiempo; tres quedan como espacio.',
  fr:'Pourquoi trois dimensions spatiales — quatre axiomes, quatre degrés de liberté ; un est le temps ; trois restent comme espace.',
  de:'Warum drei Raumdimensionen — vier Axiome, vier Freiheitsgrade; einer ist Zeit; drei bleiben als Raum.',
  pt:'Por que três dimensões espaciais — quatro axiomas, quatro graus de liberdade; um é o tempo; três permanecem como espaço.',
  nl:'Waarom drie ruimtelijke dimensies — vier axioma\'s, vier vrijheidsgraden; één is tijd; drie blijven als ruimte.',
  it:'Perché tre dimensioni spaziali — quattro assiomi, quattro gradi di libertà; uno è il tempo; tre restano come spazio.',
  zh:'为什么是三个空间维度——四条公理，四个自由度；一个是时间；三个是空间。',
  ja:'なぜ三次元空間か——四つの公理、四つの自由度；一つは時間；三つが空間として残る。',
  ko:'왜 세 공간 차원인가 — 네 공리, 네 자유도; 하나는 시간; 셋은 공간으로 남는다.',
  ru:'Почему три пространственных измерения — четыре аксиомы, четыре степени свободы; одна — время; три остаются как пространство.',
  ar:'لماذا ثلاثة أبعاد مكانية — أربع بديهيات، أربع درجات حرية؛ واحدة هي الزمن؛ ثلاث تبقى كفضاء.',
  hi:'तीन स्थानिक आयाम क्यों — चार स्वयंसिद्ध, चार स्वतंत्रता की कोटियाँ; एक समय है; तीन अवकाश के रूप में रहती हैं।'},
"Einstein's field equations derived from the record algebra via Lovelock's theorem.":{
  es:'Las ecuaciones de campo de Einstein derivadas del álgebra de registros mediante el teorema de Lovelock.',
  fr:"Les équations de champ d'Einstein dérivées de l'algèbre des enregistrements via le théorème de Lovelock.",
  de:'Einsteins Feldgleichungen abgeleitet aus der Record-Algebra über Lovelocks Theorem.',
  pt:'As equações de campo de Einstein derivadas da álgebra de registros pelo teorema de Lovelock.',
  nl:'Einsteins veldvergelijkingen afgeleid uit de record-algebra via de stelling van Lovelock.',
  it:"Le equazioni di campo di Einstein derivate dall'algebra dei record tramite il teorema di Lovelock.",
  zh:'通过洛夫洛克定理从记录代数推导爱因斯坦场方程。',
  ja:'ラブロックの定理を通じて記録代数からアインシュタインの場の方程式を導出。',
  ko:'러브록 정리를 통해 기록 대수에서 아인슈타인 장 방정식 도출.',
  ru:'Уравнения поля Эйнштейна, выведенные из алгебры записей через теорему Лавлока.',
  ar:'معادلات حقل آينشتاين مُشتقّة من جبر السجلّات عبر نظرية لوفلوك.',
  hi:'लवलॉक प्रमेय के माध्यम से अभिलेख बीजगणित से आइंस्टीन की क्षेत्र समीकरण व्युत्पन्न।'},
"QM from the empty set — superposition, measurement, entanglement, Schrödinger equation.":{
  es:'MC desde el conjunto vacío — superposición, medición, entrelazamiento, ecuación de Schrödinger.',
  fr:"MQ depuis l'ensemble vide — superposition, mesure, intrication, équation de Schrödinger.",
  de:'QM aus der leeren Menge — Superposition, Messung, Verschränkung, Schrödinger-Gleichung.',
  pt:'MQ do conjunto vazio — superposição, medição, emaranhamento, equação de Schrödinger.',
  nl:'QM uit de lege verzameling — superpositie, meting, verstrengeling, Schrödingervergelijking.',
  it:"MQ dall'insieme vuoto — sovrapposizione, misura, entanglement, equazione di Schrödinger.",
  zh:'从空集出发的量子力学——叠加、测量、纠缠、薛定谔方程。',
  ja:'空集合からの量子力学——重ね合わせ、測定、エンタングルメント、シュレーディンガー方程式。',
  ko:'공집합으로부터의 양자역학 — 중첩, 측정, 얽힘, 슈뢰딩거 방정식.',
  ru:'КМ из пустого множества — суперпозиция, измерение, запутанность, уравнение Шрёдингера.',
  ar:'ميكانيكا الكمّ من المجموعة الفارغة — التراكب، القياس، التشابك، معادلة شرودنغر.',
  hi:'रिक्त समुच्चय से क्वांटम यांत्रिकी — अध्यारोपण, मापन, उलझाव, श्रोडिंगर समीकरण।'},
'The complex Hilbert space derived from the axiom structure.':{
  es:'El espacio de Hilbert complejo derivado de la estructura axiomática.',
  fr:"L'espace de Hilbert complexe dérivé de la structure axiomatique.",
  de:'Der komplexe Hilbertraum abgeleitet aus der Axiomstruktur.',
  pt:'O espaço de Hilbert complexo derivado da estrutura axiomática.',
  nl:'De complexe Hilbertruimte afgeleid uit de axioma-structuur.',
  it:"Lo spazio di Hilbert complesso derivato dalla struttura assiomatica.",
  zh:'从公理结构推导的复希尔伯特空间。',
  ja:'公理構造から導出された複素ヒルベルト空間。',
  ko:'공리 구조에서 도출된 복소 힐베르트 공간.',
  ru:'Комплексное гильбертово пространство, выведенное из аксиоматической структуры.',
  ar:'فضاء هيلبرت المركّب المُشتقّ من البنية البديهية.',
  hi:'स्वयंसिद्ध संरचना से व्युत्पन्न सम्मिश्र हिल्बर्ट अवकाश।'},
};

// Part numbers
const PARTS = {
  'Part I':{es:'Parte I',fr:'Partie I',de:'Teil I',pt:'Parte I',nl:'Deel I',it:'Parte I',zh:'第一部分',ja:'第I部',ko:'제1부',ru:'Часть I',ar:'الجزء الأول',hi:'भाग I'},
  'Part II':{es:'Parte II',fr:'Partie II',de:'Teil II',pt:'Parte II',nl:'Deel II',it:'Parte II',zh:'第二部分',ja:'第II部',ko:'제2부',ru:'Часть II',ar:'الجزء الثاني',hi:'भाग II'},
  'Part III':{es:'Parte III',fr:'Partie III',de:'Teil III',pt:'Parte III',nl:'Deel III',it:'Parte III',zh:'第三部分',ja:'第III部',ko:'제3부',ru:'Часть III',ar:'الجزء الثالث',hi:'भाग III'},
  'Part IV':{es:'Parte IV',fr:'Partie IV',de:'Teil IV',pt:'Parte IV',nl:'Deel IV',it:'Parte IV',zh:'第四部分',ja:'第IV部',ko:'제4부',ru:'Часть IV',ar:'الجزء الرابع',hi:'भाग IV'},
  'Part V':{es:'Parte V',fr:'Partie V',de:'Teil V',pt:'Parte V',nl:'Deel V',it:'Parte V',zh:'第五部分',ja:'第V部',ko:'제5부',ru:'Часть V',ar:'الجزء الخامس',hi:'भाग V'},
  'Part VI':{es:'Parte VI',fr:'Partie VI',de:'Teil VI',pt:'Parte VI',nl:'Deel VI',it:'Parte VI',zh:'第六部分',ja:'第VI部',ko:'제6부',ru:'Часть VI',ar:'الجزء السادس',hi:'भाग VI'},
  'Part VII':{es:'Parte VII',fr:'Partie VII',de:'Teil VII',pt:'Parte VII',nl:'Deel VII',it:'Parte VII',zh:'第七部分',ja:'第VII部',ko:'제7부',ru:'Часть VII',ar:'الجزء السابع',hi:'भाग VII'},
  'Part VIII':{es:'Parte VIII',fr:'Partie VIII',de:'Teil VIII',pt:'Parte VIII',nl:'Deel VIII',it:'Parte VIII',zh:'第八部分',ja:'第VIII部',ko:'제8부',ru:'Часть VIII',ar:'الجزء الثامن',hi:'भाग VIII'},
};

// Copyleft
const COPYLEFT = {
  en:'Copyleft 2026',
  es:'Copyleft 2026',fr:'Copyleft 2026',de:'Copyleft 2026',pt:'Copyleft 2026',
  nl:'Copyleft 2026',it:'Copyleft 2026',zh:'Copyleft 2026',ja:'Copyleft 2026',
  ko:'Copyleft 2026',ru:'Copyleft 2026',ar:'Copyleft 2026',hi:'Copyleft 2026'
};
// Actually Copyleft is a universal term - keep as is. Skip.

LANGS.forEach(lang => {
  const fp = path.join('C:/Users/info/the420code', lang, 'index.html');
  let h = fs.readFileSync(fp, 'utf8');
  let c = 0;

  // Fix AP subtitles
  for (const [en, t] of Object.entries(SUBS)) {
    const val = t[lang];
    if (!val) continue;
    if (h.includes(en)) { h = h.replace(en, val); c++; }
  }

  // Fix Part numbers (only in part-num spans)
  for (const [en, t] of Object.entries(PARTS)) {
    const val = t[lang];
    if (!val) continue;
    const find = 'part-num">' + en + '</span>';
    const repl = 'part-num">' + val + '</span>';
    while (h.includes(find)) { h = h.replace(find, repl); c++; }
  }

  fs.writeFileSync(fp, h);
  console.log('  ' + lang + ' — ' + c + ' fixes');
});
console.log('Done');
