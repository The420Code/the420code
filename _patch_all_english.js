const fs = require('fs');
const path = require('path');

const LANGS = ['es','fr','de','pt','nl','it','zh','ja','ko','ru','ar','hi'];

// ============================================================
// TRANSLATIONS FOR ALL UI/STRUCTURAL ENGLISH TEXT
// ============================================================

const T = {
  // Proofs subtitle
  proofs_subtitle: {
    en:'One measured input (α<sub>em</sub>). Zero fitted parameters. 42 papers. 285 kill switches.',
    es:'Una entrada medida (α<sub>em</sub>). Cero parámetros ajustados. 42 artículos. 285 interruptores letales.',
    fr:'Une entrée mesurée (α<sub>em</sub>). Zéro paramètre ajusté. 42 articles. 285 interrupteurs de mort.',
    de:'Eine gemessene Eingabe (α<sub>em</sub>). Null angepasste Parameter. 42 Arbeiten. 285 Kill Switches.',
    pt:'Uma entrada medida (α<sub>em</sub>). Zero parâmetros ajustados. 42 artigos. 285 interruptores letais.',
    nl:'Eén gemeten invoer (α<sub>em</sub>). Nul aangepaste parameters. 42 artikelen. 285 kill switches.',
    it:'Un input misurato (α<sub>em</sub>). Zero parametri aggiustati. 42 articoli. 285 kill switch.',
    zh:'一个测量输入（α<sub>em</sub>）。零拟合参数。42篇论文。285个灭杀开关。',
    ja:'測定入力1つ（α<sub>em</sub>）。フィッティングパラメータ0。論文42本。キルスイッチ285個。',
    ko:'측정 입력 1개(α<sub>em</sub>). 맞춤 매개변수 0개. 논문 42편. 킬 스위치 285개.',
    ru:'Один измеренный параметр (α<sub>em</sub>). Ноль подогнанных параметров. 42 статьи. 285 переключателей уничтожения.',
    ar:'مُدخل مُقاس واحد (α<sub>em</sub>). صفر معاملات مُعدَّلة. 42 بحثًا. 285 مفتاح إيقاف.',
    hi:'एक मापित इनपुट (α<sub>em</sub>)। शून्य फ़िट किए गए पैरामीटर। 42 पत्र। 285 किल स्विच।'
  },

  // "Requires:" label
  requires: {
    es:'Requiere',fr:'Requiert',de:'Erfordert',pt:'Requer',nl:'Vereist',
    it:'Richiede',zh:'依赖',ja:'前提',ko:'필요',ru:'Требует',ar:'يتطلب',hi:'आवश्यक'
  },

  // Copy / Copied buttons
  copy: {
    es:'Copiar',fr:'Copier',de:'Kopieren',pt:'Copiar',nl:'Kopiëren',
    it:'Copia',zh:'复制',ja:'コピー',ko:'복사',ru:'Копировать',ar:'نسخ',hi:'कॉपी करें'
  },
  copied: {
    es:'Copiado',fr:'Copié',de:'Kopiert',pt:'Copiado',nl:'Gekopieerd',
    it:'Copiato',zh:'已复制',ja:'コピー済み',ko:'복사됨',ru:'Скопировано',ar:'تم النسخ',hi:'कॉपी हो गया'
  },

  // Book section: The Rosin description
  rosin_desc: {
    es:'Calientas la flor y lo que gotea es la cosa misma — concentrada, sin nada añadido, sin nada perdido. Cinco libros en cinco voces. Cada uno recorre todo el argumento — desde el axioma hasta la física y la ética terminal — en una sola compresión. Empieza por la voz que suene como la tuya.',
    fr:"Tu presses la chaleur dans la fleur et ce qui s'écoule est la chose elle-même — concentrée, rien ajouté, rien perdu. Cinq livres en cinq voix. Chacun parcourt l'argument entier — de l'axiome à la physique jusqu'à l'éthique terminale — en une seule compression. Commence par la voix qui ressemble à la tienne.",
    de:'Du presst Hitze in die Blüte und was heraustropft, ist die Sache selbst — konzentriert, nichts hinzugefügt, nichts verloren. Fünf Bücher in fünf Stimmen. Jedes durchläuft das gesamte Argument — vom Axiom über die Physik bis zur terminalen Ethik — in einer einzigen Verdichtung. Beginne mit der Stimme, die wie deine klingt.',
    pt:'Você pressiona calor na flor e o que goteja é a coisa em si — concentrada, nada adicionado, nada perdido. Cinco livros em cinco vozes. Cada um percorre todo o argumento — do axioma à física até a ética terminal — em uma única compressão. Comece pela voz que soa como a sua.',
    nl:'Je perst hitte in de bloem en wat eruit druppelt is het ding zelf — geconcentreerd, niets toegevoegd, niets verloren. Vijf boeken in vijf stemmen. Elk doorloopt het hele argument — van het axioma via de fysica tot de terminale ethiek — in één enkele compressie. Begin met de stem die klinkt als de jouwe.',
    it:"Premi calore nel fiore e quello che gocciola è la cosa stessa — concentrata, nulla aggiunto, nulla perso. Cinque libri in cinque voci. Ognuno percorre l'intero argomento — dall'assioma alla fisica fino all'etica terminale — in un'unica compressione. Inizia con la voce che suona come la tua.",
    zh:'你将热量压入花朵，滴出的就是事物本身——浓缩的，什么都没加，什么都没丢。五本书，五种声音。每一本走完整个论证——从公理到物理再到终极伦理——一次压缩。从听起来像你的那个声音开始。',
    ja:'花に熱を加え、したたり落ちるのはそのものだ——凝縮された、何も加えず、何も失わず。五冊の本、五つの声。それぞれが論証全体を歩く——公理から物理学、そして終末倫理まで——一つの圧縮で。自分に似た声から始めろ。',
    ko:'꽃에 열을 가하면 떨어지는 것은 그 자체다 — 농축된, 아무것도 더하지 않은, 아무것도 잃지 않은. 다섯 권의 책, 다섯 가지 목소리. 각각이 전체 논증을 걸어간다 — 공리에서 물리학, 종말 윤리까지 — 단 하나의 압축으로. 당신과 닮은 목소리부터 시작하라.',
    ru:'Ты прессуешь жар в цветок, и то, что капает, — это сама суть — концентрированная, ничего не добавлено, ничего не потеряно. Пять книг пятью голосами. Каждая проходит весь аргумент — от аксиомы через физику до терминальной этики — в одном сжатии. Начни с голоса, похожего на твой.',
    ar:'تضغط الحرارة في الزهرة وما يقطر هو الشيء ذاته — مُركَّزًا، لا شيء مُضاف، لا شيء مفقود. خمسة كتب بخمسة أصوات. كل واحد يسير عبر الحجة بأكملها — من البديهية عبر الفيزياء إلى الأخلاق النهائية — في ضغطة واحدة. ابدأ بالصوت الذي يشبه صوتك.',
    hi:'फूल में गर्मी दबाइए और जो टपकता है वह वस्तु स्वयं है — केंद्रित, कुछ नहीं जोड़ा, कुछ नहीं खोया। पाँच पुस्तकें पाँच आवाज़ों में। हर एक पूरे तर्क को चलती है — स्वयंसिद्ध से भौतिकी होते हुए अंतिम नैतिकता तक — एक ही संपीड़न में। जो आवाज़ आपकी जैसी लगे, वहाँ से शुरू करें।'
  },

  // Book section: The Editions description
  editions_desc: {
    es:'Una voz. De principio a fin. Cada Edición toma la derivación completa y la escribe en un solo registro, de tapa a tapa — el argumento como una línea ininterrumpida. Elige la voz que suene como piensas.',
    fr:"Une voix. Du début à la fin. Chaque Édition prend la dérivation complète et l'écrit dans un seul registre, de couverture à couverture — l'argument comme une ligne ininterrompue. Choisis la voix qui ressemble à ta façon de penser.",
    de:'Eine Stimme. Von Anfang bis Ende. Jede Ausgabe nimmt die vollständige Ableitung und schreibt sie in einem einzigen Register, von Deckel zu Deckel — das Argument als eine ununterbrochene Linie. Wähle die Stimme, die so klingt, wie du denkst.',
    pt:'Uma voz. Do início ao fim. Cada Edição pega a derivação completa e a escreve em um único registro, de capa a capa — o argumento como uma linha ininterrupta. Escolha a voz que soa como você pensa.',
    nl:'Eén stem. Van begin tot eind. Elke Editie neemt de volledige afleiding en schrijft die in één register, van kaft tot kaft — het argument als één ononderbroken lijn. Kies de stem die klinkt zoals jij denkt.',
    it:"Una voce. Dall'inizio alla fine. Ogni Edizione prende la derivazione completa e la scrive in un unico registro, da copertina a copertina — l'argomento come una linea ininterrotta. Scegli la voce che suona come pensi.",
    zh:'一种声音。从头到尾。每个版本取完整推导，以单一笔调书写，从封面到封面——论证作为一条不断的线。选择听起来像你思考方式的声音。',
    ja:'一つの声。最初から最後まで。各エディションは完全な導出を取り、一つの語調で書き上げる、表紙から表紙まで——論証は一本の途切れない線として。自分の思考に似た声を選べ。',
    ko:'하나의 목소리. 처음부터 끝까지. 각 에디션은 전체 도출을 하나의 어조로 쓴다, 표지에서 표지까지 — 논증은 하나의 끊기지 않는 선으로. 당신의 사고방식과 닮은 목소리를 골라라.',
    ru:'Один голос. От начала до конца. Каждое Издание берёт полный вывод и записывает его в одном регистре, от корки до корки — аргумент как одна непрерывная линия. Выбери голос, похожий на твоё мышление.',
    ar:'صوت واحد. من البداية إلى النهاية. كل طبعة تأخذ الاشتقاق الكامل وتكتبه بنبرة واحدة، من الغلاف إلى الغلاف — الحجة كخطٍّ متصل. اختر الصوت الذي يشبه طريقة تفكيرك.',
    hi:'एक आवाज़। शुरू से अंत तक। हर संस्करण पूर्ण व्युत्पत्ति लेता है और एक ही स्वर में लिखता है, पहले पन्ने से आखिरी तक — तर्क एक अटूट रेखा के रूप में। वह आवाज़ चुनिए जो आपकी सोच जैसी लगे।'
  },

  // Book section: The Notebooks description
  notebooks_desc: {
    es:'Ocho temas. Cinco voces cada uno. Los Cuadernos son donde vive la física — cada derivación, cada resultado, cada interruptor letal, organizado por campo. Empieza por el tema que ya te quita el sueño.',
    fr:"Huit sujets. Cinq voix chacun. Les Cahiers sont là où vit la physique — chaque dérivation, chaque résultat, chaque interrupteur de mort, organisé par domaine. Commence par le sujet qui t'empêche déjà de dormir.",
    de:'Acht Themen. Je fünf Stimmen. Die Notizbücher sind der Ort, an dem die Physik lebt — jede Ableitung, jedes Ergebnis, jeder Kill Switch, nach Feld geordnet. Beginne mit dem Thema, das dich schon nachts wach hält.',
    pt:'Oito temas. Cinco vozes cada. Os Cadernos são onde a física vive — cada derivação, cada resultado, cada interruptor letal, organizado por campo. Comece pelo tema que já te tira o sono.',
    nl:'Acht onderwerpen. Elk vijf stemmen. De Notitieboeken zijn waar de fysica leeft — elke afleiding, elk resultaat, elke kill switch, georganiseerd per veld. Begin met het onderwerp dat je al wakker houdt.',
    it:"Otto argomenti. Cinque voci ciascuno. I Quaderni sono dove vive la fisica — ogni derivazione, ogni risultato, ogni kill switch, organizzato per campo. Inizia con l'argomento che già ti toglie il sonno.",
    zh:'八个主题。每个五种声音。笔记本是物理学所在之处——每个推导、每个结果、每个灭杀开关，按领域组织。从那个已经让你夜不能寐的主题开始。',
    ja:'八つの主題。それぞれ五つの声。ノートブックは物理学が生きている場所だ——すべての導出、すべての結果、すべてのキルスイッチ、分野別に整理されている。すでに夜眠れなくなっている主題から始めろ。',
    ko:'여덟 가지 주제. 각각 다섯 가지 목소리. 노트북은 물리학이 사는 곳이다 — 모든 도출, 모든 결과, 모든 킬 스위치, 분야별로 정리. 이미 밤잠을 설치게 하는 주제부터 시작하라.',
    ru:'Восемь тем. По пять голосов в каждой. Тетради — это место, где живёт физика — каждый вывод, каждый результат, каждый переключатель уничтожения, организованные по областям. Начни с темы, которая уже не даёт тебе спать.',
    ar:'ثمانية مواضيع. خمسة أصوات لكل منها. الدفاتر هي حيث تعيش الفيزياء — كل اشتقاق، كل نتيجة، كل مفتاح إيقاف، مُنظَّمة حسب المجال. ابدأ بالموضوع الذي يُقلقك بالفعل ليلًا.',
    hi:'आठ विषय। प्रत्येक में पाँच आवाज़ें। नोटबुक वह जगह है जहाँ भौतिकी रहती है — हर व्युत्पत्ति, हर परिणाम, हर किल स्विच, क्षेत्र के अनुसार व्यवस्थित। उस विषय से शुरू करें जो पहले से आपकी नींद उड़ाता है।'
  },

  // Rosin book titles
  rosin_prose:{es:'La Resina — Prosa',fr:'La Résine — Prose',de:'Das Harz — Prosa',pt:'A Resina — Prosa',nl:'De Hars — Proza',it:'La Resina — Prosa',zh:'松香 — 散文',ja:'ロジン — 散文',ko:'로진 — 산문',ru:'Канифоль — Проза',ar:'الصمغ — نثر',hi:'रोज़िन — गद्य'},
  rosin_conv:{es:'La Resina — Conversación',fr:'La Résine — Conversation',de:'Das Harz — Gespräch',pt:'A Resina — Conversa',nl:'De Hars — Gesprek',it:'La Resina — Conversazione',zh:'松香 — 对话',ja:'ロジン — 対話',ko:'로진 — 대화',ru:'Канифоль — Диалог',ar:'الصمغ — حوار',hi:'रोज़िन — संवाद'},
  rosin_meta:{es:'La Resina — Metáfora',fr:'La Résine — Métaphore',de:'Das Harz — Metapher',pt:'A Resina — Metáfora',nl:'De Hars — Metafoor',it:'La Resina — Metafora',zh:'松香 — 隐喻',ja:'ロジン — 比喩',ko:'로진 — 은유',ru:'Канифоль — Метафора',ar:'الصمغ — استعارة',hi:'रोज़िन — रूपक'},
  rosin_nursery:{es:'La Resina — Canción infantil',fr:'La Résine — Comptine',de:'Das Harz — Kinderreim',pt:'A Resina — Cantiga',nl:'De Hars — Kinderrijm',it:'La Resina — Filastrocca',zh:'松香 — 童谣',ja:'ロジン — 童謡',ko:'로진 — 동요',ru:'Канифоль — Считалка',ar:'الصمغ — أنشودة أطفال',hi:'रोज़िन — लोरी'},
  rosin_proofs:{es:'La Resina — Pruebas',fr:'La Résine — Preuves',de:'Das Harz — Beweise',pt:'A Resina — Provas',nl:'De Hars — Bewijzen',it:'La Resina — Prove',zh:'松香 — 证明',ja:'ロジン — 証明',ko:'로진 — 증명',ru:'Канифоль — Доказательства',ar:'الصمغ — براهين',hi:'रोज़िन — प्रमाण'},

  // Editions book titles
  ed_prose:{es:'Las Ediciones — Prosa',fr:'Les Éditions — Prose',de:'Die Ausgaben — Prosa',pt:'As Edições — Prosa',nl:'De Edities — Proza',it:'Le Edizioni — Prosa',zh:'版本 — 散文',ja:'エディション — 散文',ko:'에디션 — 산문',ru:'Издания — Проза',ar:'الطبعات — نثر',hi:'संस्करण — गद्य'},
  ed_conv:{es:'Las Ediciones — Conversación',fr:'Les Éditions — Conversation',de:'Die Ausgaben — Gespräch',pt:'As Edições — Conversa',nl:'De Edities — Gesprek',it:'Le Edizioni — Conversazione',zh:'版本 — 对话',ja:'エディション — 対話',ko:'에디션 — 대화',ru:'Издания — Диалог',ar:'الطبعات — حوار',hi:'संस्करण — संवाद'},
  ed_meta:{es:'Las Ediciones — Metáfora',fr:'Les Éditions — Métaphore',de:'Die Ausgaben — Metapher',pt:'As Edições — Metáfora',nl:'De Edities — Metafoor',it:'Le Edizioni — Metafora',zh:'版本 — 隐喻',ja:'エディション — 比喩',ko:'에디션 — 은유',ru:'Издания — Метафора',ar:'الطبعات — استعارة',hi:'संस्करण — रूपक'},
  ed_nursery:{es:'Las Ediciones — Canción infantil',fr:'Les Éditions — Comptine',de:'Die Ausgaben — Kinderreim',pt:'As Edições — Cantiga',nl:'De Edities — Kinderrijm',it:'Le Edizioni — Filastrocca',zh:'版本 — 童谣',ja:'エディション — 童謡',ko:'에디션 — 동요',ru:'Издания — Считалка',ar:'الطبعات — أنشودة أطفال',hi:'संस्करण — लोरी'},
  ed_proofs:{es:'Las Ediciones — Pruebas',fr:'Les Éditions — Preuves',de:'Die Ausgaben — Beweise',pt:'As Edições — Provas',nl:'De Edities — Bewijzen',it:'Le Edizioni — Prove',zh:'版本 — 证明',ja:'エディション — 証明',ko:'에디션 — 증명',ru:'Издания — Доказательства',ar:'الطبعات — براهين',hi:'संस्करण — प्रमाण'},

  // Notebooks book titles
  nb_prose:{es:'Los Cuadernos Ø Prosa',fr:'Les Cahiers Ø Prose',de:'Die Notizbücher Ø Prosa',pt:'Os Cadernos Ø Prosa',nl:'De Notitieboeken Ø Proza',it:'I Quaderni Ø Prosa',zh:'笔记本 Ø 散文',ja:'ノートブック Ø 散文',ko:'노트북 Ø 산문',ru:'Тетради Ø Проза',ar:'الدفاتر Ø نثر',hi:'नोटबुक Ø गद्य'},
  nb_conv:{es:'Los Cuadernos Ø Conversación',fr:'Les Cahiers Ø Conversation',de:'Die Notizbücher Ø Gespräch',pt:'Os Cadernos Ø Conversa',nl:'De Notitieboeken Ø Gesprek',it:'I Quaderni Ø Conversazione',zh:'笔记本 Ø 对话',ja:'ノートブック Ø 対話',ko:'노트북 Ø 대화',ru:'Тетради Ø Диалог',ar:'الدفاتر Ø حوار',hi:'नोटबुक Ø संवाद'},
  nb_meta:{es:'Los Cuadernos Ø Metáfora',fr:'Les Cahiers Ø Métaphore',de:'Die Notizbücher Ø Metapher',pt:'Os Cadernos Ø Metáfora',nl:'De Notitieboeken Ø Metafoor',it:'I Quaderni Ø Metafora',zh:'笔记本 Ø 隐喻',ja:'ノートブック Ø 比喩',ko:'노트북 Ø 은유',ru:'Тетради Ø Метафора',ar:'الدفاتر Ø استعارة',hi:'नोटबुक Ø रूपक'},
  nb_nursery:{es:'Los Cuadernos Ø Canción infantil',fr:'Les Cahiers Ø Comptine',de:'Die Notizbücher Ø Kinderreim',pt:'Os Cadernos Ø Cantiga',nl:'De Notitieboeken Ø Kinderrijm',it:'I Quaderni Ø Filastrocca',zh:'笔记本 Ø 童谣',ja:'ノートブック Ø 童謡',ko:'노트북 Ø 동요',ru:'Тетради Ø Считалка',ar:'الدفاتر Ø أنشودة أطفال',hi:'नोटबुक Ø लोरी'},
  nb_proofs:{es:'Los Cuadernos Ø Pruebas',fr:'Les Cahiers Ø Preuves',de:'Die Notizbücher Ø Beweise',pt:'Os Cadernos Ø Provas',nl:'De Notitieboeken Ø Bewijzen',it:'I Quaderni Ø Prove',zh:'笔记本 Ø 证明',ja:'ノートブック Ø 証明',ko:'노트북 Ø 증명',ru:'Тетради Ø Доказательства',ar:'الدفاتر Ø براهين',hi:'नोटबुक Ø प्रमाण'},

  // Notebooks subjects
  nb_s1:{es:'Ø.1 La Premisa',fr:'Ø.1 La Prémisse',de:'Ø.1 Die Prämisse',pt:'Ø.1 A Premissa',nl:'Ø.1 De Premisse',it:'Ø.1 La Premessa',zh:'Ø.1 前提',ja:'Ø.1 前提',ko:'Ø.1 전제',ru:'Ø.1 Предпосылка',ar:'Ø.1 المقدّمة',hi:'Ø.1 आधारवाक्य'},
  nb_s2:{es:'Ø.2 Espaciotiempo',fr:"Ø.2 Espace-temps",de:'Ø.2 Raumzeit',pt:'Ø.2 Espaço-tempo',nl:'Ø.2 Ruimtetijd',it:'Ø.2 Spaziotempo',zh:'Ø.2 时空',ja:'Ø.2 時空',ko:'Ø.2 시공간',ru:'Ø.2 Пространство-время',ar:'Ø.2 الزمكان',hi:'Ø.2 दिक्काल'},
  nb_s3:{es:'Ø.3 Mecánica cuántica',fr:'Ø.3 Mécanique quantique',de:'Ø.3 Quantenmechanik',pt:'Ø.3 Mecânica quântica',nl:'Ø.3 Kwantummechanica',it:'Ø.3 Meccanica quantistica',zh:'Ø.3 量子力学',ja:'Ø.3 量子力学',ko:'Ø.3 양자역학',ru:'Ø.3 Квантовая механика',ar:'Ø.3 ميكانيكا الكمّ',hi:'Ø.3 क्वांटम यांत्रिकी'},
  nb_s4:{es:'Ø.4 Fuerzas y constantes',fr:'Ø.4 Forces et constantes',de:'Ø.4 Kräfte und Konstanten',pt:'Ø.4 Forças e constantes',nl:'Ø.4 Krachten en constanten',it:'Ø.4 Forze e costanti',zh:'Ø.4 力与常数',ja:'Ø.4 力と定数',ko:'Ø.4 힘과 상수',ru:'Ø.4 Силы и константы',ar:'Ø.4 القوى والثوابت',hi:'Ø.4 बल और स्थिरांक'},
  nb_s5:{es:'Ø.5 Partículas y materia',fr:'Ø.5 Particules et matière',de:'Ø.5 Teilchen und Materie',pt:'Ø.5 Partículas e matéria',nl:'Ø.5 Deeltjes en materie',it:'Ø.5 Particelle e materia',zh:'Ø.5 粒子与物质',ja:'Ø.5 粒子と物質',ko:'Ø.5 입자와 물질',ru:'Ø.5 Частицы и материя',ar:'Ø.5 الجسيمات والمادة',hi:'Ø.5 कण और पदार्थ'},
  nb_s6:{es:'Ø.6 Cosmología',fr:'Ø.6 Cosmologie',de:'Ø.6 Kosmologie',pt:'Ø.6 Cosmologia',nl:'Ø.6 Kosmologie',it:'Ø.6 Cosmologia',zh:'Ø.6 宇宙学',ja:'Ø.6 宇宙論',ko:'Ø.6 우주론',ru:'Ø.6 Космология',ar:'Ø.6 علم الكونيات',hi:'Ø.6 ब्रह्मांड विज्ञान'},
  nb_s7:{es:'Ø.7 Consciencia y la ética',fr:"Ø.7 Conscience et l'éthique",de:'Ø.7 Bewusstsein und die Ethik',pt:'Ø.7 Consciência e a ética',nl:'Ø.7 Bewustzijn en de ethiek',it:"Ø.7 Coscienza e l'etica",zh:'Ø.7 意识与伦理',ja:'Ø.7 意識と倫理',ko:'Ø.7 의식과 윤리',ru:'Ø.7 Сознание и этика',ar:'Ø.7 الوعي والأخلاق',hi:'Ø.7 चेतना और नैतिकता'},
  nb_s8:{es:'Ø.8 Aplicaciones',fr:'Ø.8 Applications',de:'Ø.8 Anwendungen',pt:'Ø.8 Aplicações',nl:'Ø.8 Toepassingen',it:'Ø.8 Applicazioni',zh:'Ø.8 应用',ja:'Ø.8 応用',ko:'Ø.8 응용',ru:'Ø.8 Приложения',ar:'Ø.8 التطبيقات',hi:'Ø.8 अनुप्रयोग'},

  // Code section intro
  code_intro: {
    es:'Una entrada medida. Cero parámetros ajustados. El código siguiente reproduce cada resultado principal a partir de un solo número — la constante de estructura fina α ≈ 1/137. Cópialo. Pégalo en cualquier entorno Python. Ejecútalo. Si los números coinciden, las derivaciones se sostienen. Si no, el argumento tiene un problema y lo has encontrado.',
    fr:"Une entrée mesurée. Zéro paramètre ajusté. Le code ci-dessous reproduit chaque résultat principal à partir d'un seul nombre — la constante de structure fine α ≈ 1/137. Copie-le. Colle-le dans n'importe quel environnement Python. Exécute-le. Si les nombres correspondent, les dérivations tiennent. Sinon, l'argument a un problème et tu l'as trouvé.",
    de:'Eine gemessene Eingabe. Null angepasste Parameter. Der folgende Code reproduziert jedes Hauptergebnis aus einer einzigen Zahl — der Feinstrukturkonstante α ≈ 1/137. Kopiere ihn. Füge ihn in eine beliebige Python-Umgebung ein. Führe ihn aus. Wenn die Zahlen stimmen, halten die Ableitungen. Wenn nicht, hat das Argument ein Problem und du hast es gefunden.',
    pt:'Uma entrada medida. Zero parâmetros ajustados. O código abaixo reproduz cada resultado principal a partir de um único número — a constante de estrutura fina α ≈ 1/137. Copie. Cole em qualquer ambiente Python. Execute. Se os números coincidirem, as derivações se sustentam. Se não, o argumento tem um problema e você o encontrou.',
    nl:'Eén gemeten invoer. Nul aangepaste parameters. De onderstaande code reproduceert elk hoofdresultaat uit één enkel getal — de fijnstructuurconstante α ≈ 1/137. Kopieer het. Plak het in een willekeurige Python-omgeving. Voer het uit. Als de getallen kloppen, houden de afleidingen stand. Zo niet, dan heeft het argument een probleem en heb je het gevonden.',
    it:"Un input misurato. Zero parametri aggiustati. Il codice seguente riproduce ogni risultato principale da un singolo numero — la costante di struttura fine α ≈ 1/137. Copialo. Incollalo in qualsiasi ambiente Python. Eseguilo. Se i numeri corrispondono, le derivazioni reggono. Se no, l'argomento ha un problema e l'hai trovato.",
    zh:'一个测量输入。零拟合参数。下面的代码从一个数字——精细结构常数 α ≈ 1/137——复现每一个主要结果。复制它。粘贴到任何 Python 环境中。运行。如果数字吻合，推导成立。如果不吻合，论证有问题，而你找到了它。',
    ja:'測定入力1つ。フィッティングパラメータ0。以下のコードは一つの数——微細構造定数 α ≈ 1/137——からすべての主要結果を再現する。コピーせよ。任意のPython環境に貼り付けよ。実行せよ。数値が一致すれば導出は成立する。一致しなければ、論証に問題があり、あなたがそれを見つけたのだ。',
    ko:'측정 입력 1개. 맞춤 매개변수 0개. 아래 코드는 단 하나의 수 — 미세구조상수 α ≈ 1/137 — 로부터 모든 주요 결과를 재현한다. 복사하라. 아무 Python 환경에 붙여넣어라. 실행하라. 숫자가 맞으면 도출이 성립한다. 맞지 않으면 논증에 문제가 있고, 당신이 그것을 찾은 것이다.',
    ru:'Один измеренный параметр. Ноль подогнанных параметров. Код ниже воспроизводит каждый основной результат из одного числа — постоянной тонкой структуры α ≈ 1/137. Скопируй его. Вставь в любую среду Python. Запусти. Если числа совпадают, выводы верны. Если нет — в аргументе проблема, и ты её нашёл.',
    ar:'مُدخل مُقاس واحد. صفر معاملات مُعدَّلة. الشيفرة أدناه تُعيد إنتاج كل نتيجة رئيسية من رقم واحد — ثابت البنية الدقيقة α ≈ 1/137. انسخها. الصقها في أي بيئة بايثون. شغّلها. إذا تطابقت الأرقام، فالاشتقاقات صحيحة. وإلا، فالحجة بها مشكلة وقد وجدتها.',
    hi:'एक मापित इनपुट। शून्य फ़िट किए गए पैरामीटर। नीचे का कोड एक ही संख्या — सूक्ष्म संरचना स्थिरांक α ≈ 1/137 — से हर मुख्य परिणाम पुनः उत्पन्न करता है। इसे कॉपी करें। किसी भी Python वातावरण में पेस्ट करें। चलाएँ। यदि संख्याएँ मेल खाती हैं, तो व्युत्पत्तियाँ टिकती हैं। यदि नहीं, तो तर्क में समस्या है और आपने उसे पाया।'
  }
};

// Replacement pairs: [english, key_in_T]
const bookTitleReplacements = [
  ['The Rosin — Prose','rosin_prose'],
  ['The Rosin — Conversation','rosin_conv'],
  ['The Rosin — Metaphor','rosin_meta'],
  ['The Rosin — Nursery Rhyme','rosin_nursery'],
  ['The Rosin — Proofs','rosin_proofs'],
  ['The Editions — Prose','ed_prose'],
  ['The Editions — Conversation','ed_conv'],
  ['The Editions — Metaphor','ed_meta'],
  ['The Editions — Nursery Rhyme','ed_nursery'],
  ['The Editions — Proofs','ed_proofs'],
  ['The Notebooks Ø Prose','nb_prose'],
  ['The Notebooks Ø Conversation','nb_conv'],
  ['The Notebooks Ø Metaphor','nb_meta'],
  ['The Notebooks Ø Nursery Rhyme','nb_nursery'],
  ['The Notebooks Ø Proofs','nb_proofs'],
  ['Ø.1 The Premise','nb_s1'],
  ['Ø.2 Spacetime','nb_s2'],
  ['Ø.3 Quantum Mechanics','nb_s3'],
  ['Ø.4 Forces and Constants','nb_s4'],
  ['Ø.5 Particles and Matter','nb_s5'],
  ['Ø.6 Cosmology','nb_s6'],
  ['Ø.7 Consciousness and the Ethic','nb_s7'],
  ['Ø.8 Applications','nb_s8'],
];

const enRosinDesc = 'You press heat into flower and what drips out is the thing itself — concentrated, nothing added, nothing lost. Five books in five voices. Each one walks the entire argument — from the axiom through the physics to the terminal ethic — in a single compression. Start with whichever voice sounds like yours.';
const enEditionsDesc = 'One voice. Beginning to end. Each Edition takes the full derivation and writes it in a single register, cover to cover — the argument as one unbroken line. Choose the voice that sounds like the way you think.';
const enNotebooksDesc = 'Eight subjects. Five voices each. The Notebooks are where the physics lives — every derivation, every result, every kill switch, organised by field. Start with the subject that already keeps you up at night.';
const enCodeIntro = 'One measured input. Zero fitted parameters. The code below reproduces every headline result from a single number — the fine-structure constant α ≈ 1/137. Copy it. Paste it into any Python environment. Run it. If the numbers match, the derivations hold. If they don\'t, the argument has a problem and you\'ve found it.';

LANGS.forEach(lang => {
  const fp = path.join('C:/Users/info/the420code', lang, 'index.html');
  let h = fs.readFileSync(fp, 'utf8');
  let changes = 0;

  // 1. Proofs subtitle
  if (h.includes(T.proofs_subtitle.en)) {
    h = h.replace(T.proofs_subtitle.en, T.proofs_subtitle[lang]);
    changes++;
  }

  // 2. "Requires:" label
  h = h.replace(/Requires: /g, T.requires[lang] + ': ');
  h = h.replace(/Requires: —/g, T.requires[lang] + ': —');
  changes++;

  // 3. Copy/Copied buttons
  h = h.replace("btn.textContent='Copied'", "btn.textContent='" + T.copied[lang] + "'");
  h = h.replace("btn.textContent='Copy'", "btn.textContent='" + T.copy[lang] + "'");
  h = h.replace(">Copy</button>", ">" + T.copy[lang] + "</button>");
  changes++;

  // 4. Book descriptions
  if (h.includes(enRosinDesc)) { h = h.replace(enRosinDesc, T.rosin_desc[lang]); changes++; }
  if (h.includes(enEditionsDesc)) { h = h.replace(enEditionsDesc, T.editions_desc[lang]); changes++; }
  if (h.includes(enNotebooksDesc)) { h = h.replace(enNotebooksDesc, T.notebooks_desc[lang]); changes++; }

  // 5. Book titles in dl-lists
  for (const [en, key] of bookTitleReplacements) {
    if (h.includes(en + ' <span')) {
      h = h.replace(en + ' <span', T[key][lang] + ' <span');
      changes++;
    }
  }

  // 6. Code section intro
  if (h.includes(enCodeIntro)) { h = h.replace(enCodeIntro, T.code_intro[lang]); changes++; }

  fs.writeFileSync(fp, h);
  console.log('  ' + lang + ' — ' + changes + ' changes');
});

console.log('Done');
