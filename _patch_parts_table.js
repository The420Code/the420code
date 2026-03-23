const fs = require('fs');
const path = require('path');
const LANGS = ['es','fr','de','pt','nl','it','zh','ja','ko','ru','ar','hi'];

const R = [
  // Part descriptions
  ['One record exists. Everything else is consequence. The axiom, its logical proof, and the four conditions that any record requires.',{
    es:'Un registro existe. Todo lo demás es consecuencia. El axioma, su demostración lógica y las cuatro condiciones que cualquier registro requiere.',
    fr:'Un enregistrement existe. Tout le reste est conséquence. L\'axiome, sa preuve logique et les quatre conditions que tout enregistrement requiert.',
    de:'Ein Record existiert. Alles andere ist Konsequenz. Das Axiom, sein logischer Beweis und die vier Bedingungen, die jeder Record erfordert.',
    pt:'Um registro existe. Todo o resto é consequência. O axioma, sua prova lógica e as quatro condições que qualquer registro requer.',
    nl:'Eén record bestaat. Al het andere is gevolg. Het axioma, zijn logisch bewijs en de vier voorwaarden die elk record vereist.',
    it:'Un record esiste. Tutto il resto è conseguenza. L\'assioma, la sua dimostrazione logica e le quattro condizioni che ogni record richiede.',
    zh:'一条记录存在。其他一切都是后果。公理、其逻辑证明，以及任何记录所需的四个条件。',
    ja:'一つの記録が存在する。それ以外はすべて帰結だ。公理、その論理的証明、そしてあらゆる記録が要求する四つの条件。',
    ko:'하나의 기록이 존재한다. 나머지는 모두 귀결이다. 공리, 그 논리적 증명, 그리고 모든 기록이 요구하는 네 가지 조건.',
    ru:'Одна запись существует. Всё остальное — следствие. Аксиома, её логическое доказательство и четыре условия, которые требует любая запись.',
    ar:'سجلّ واحد موجود. كل ما عداه نتيجة. البديهية، برهانها المنطقي، والشروط الأربعة التي يتطلبها أي سجلّ.',
    hi:'एक अभिलेख मौजूद है। बाकी सब परिणाम है। स्वयंसिद्ध, उसका तार्किक प्रमाण, और वे चार शर्तें जो किसी भी अभिलेख के लिए आवश्यक हैं।'}],

  ['The arena the break creates. The speed of light, three spatial dimensions, and Einstein\'s field equations — all derived from the axioms.',{
    es:'La arena que la ruptura crea. La velocidad de la luz, tres dimensiones espaciales y las ecuaciones de campo de Einstein — todo derivado de los axiomas.',
    fr:'L\'arène que la brisure crée. La vitesse de la lumière, trois dimensions spatiales et les équations de champ d\'Einstein — tout dérivé des axiomes.',
    de:'Die Arena, die der Bruch erschafft. Die Lichtgeschwindigkeit, drei Raumdimensionen und Einsteins Feldgleichungen — alles aus den Axiomen abgeleitet.',
    pt:'A arena que a quebra cria. A velocidade da luz, três dimensões espaciais e as equações de campo de Einstein — tudo derivado dos axiomas.',
    nl:'De arena die de breuk creëert. De lichtsnelheid, drie ruimtelijke dimensies en Einsteins veldvergelijkingen — alles afgeleid uit de axioma\'s.',
    it:'L\'arena che la rottura crea. La velocità della luce, tre dimensioni spaziali e le equazioni di campo di Einstein — tutto derivato dagli assiomi.',
    zh:'断裂所创造的舞台。光速、三个空间维度和爱因斯坦场方程——全部由公理推导。',
    ja:'破れが創る舞台。光速、三次元空間、アインシュタインの場の方程式——すべて公理から導出。',
    ko:'깨짐이 만드는 무대. 광속, 세 공간 차원, 아인슈타인 장 방정식 — 모두 공리에서 도출.',
    ru:'Арена, которую создаёт разрыв. Скорость света, три пространственных измерения и уравнения поля Эйнштейна — всё выведено из аксиом.',
    ar:'الساحة التي يخلقها الكسر. سرعة الضوء، ثلاثة أبعاد مكانية، ومعادلات حقل آينشتاين — كلها مُشتقّة من البديهيات.',
    hi:'वह मंच जो टूट बनाती है। प्रकाश की गति, तीन स्थानिक आयाम, और आइंस्टीन की क्षेत्र समीकरण — सब स्वयंसिद्धों से व्युत्पन्न।'}],

  ['The measurement structure of the break. Superposition, uncertainty, decoherence, the Born rule, and entanglement — derived from the empty set and four axioms.',{
    es:'La estructura de medición de la ruptura. Superposición, incertidumbre, decoherencia, la regla de Born y entrelazamiento — derivados del conjunto vacío y cuatro axiomas.',
    fr:'La structure de mesure de la brisure. Superposition, incertitude, décohérence, règle de Born et intrication — dérivées de l\'ensemble vide et de quatre axiomes.',
    de:'Die Messstruktur des Bruchs. Superposition, Unschärfe, Dekohärenz, die Born-Regel und Verschränkung — abgeleitet aus der leeren Menge und vier Axiomen.',
    pt:'A estrutura de medição da quebra. Superposição, incerteza, decoerência, a regra de Born e emaranhamento — derivados do conjunto vazio e quatro axiomas.',
    nl:'De meetstructuur van de breuk. Superpositie, onzekerheid, decoherentie, de Born-regel en verstrengeling — afgeleid uit de lege verzameling en vier axioma\'s.',
    it:'La struttura di misura della rottura. Sovrapposizione, indeterminazione, decoerenza, regola di Born e entanglement — derivati dall\'insieme vuoto e quattro assiomi.',
    zh:'断裂的测量结构。叠加、不确定性、退相干、玻恩规则和纠缠——由空集和四条公理推导。',
    ja:'破れの測定構造。重ね合わせ、不確定性、デコヒーレンス、ボルン規則、エンタングルメント——空集合と四つの公理から導出。',
    ko:'깨짐의 측정 구조. 중첩, 불확정성, 결어긋남, 보른 규칙, 얽힘 — 공집합과 네 공리에서 도출.',
    ru:'Структура измерения разрыва. Суперпозиция, неопределённость, декогеренция, правило Борна и запутанность — выведены из пустого множества и четырёх аксиом.',
    ar:'بنية القياس للكسر. التراكب، عدم اليقين، فقدان التماسك، قاعدة بورن، والتشابك — مُشتقّة من المجموعة الفارغة وأربع بديهيات.',
    hi:'टूट की मापन संरचना। अध्यारोपण, अनिश्चितता, विसंबद्धता, बोर्न नियम और उलझाव — रिक्त समुच्चय और चार स्वयंसिद्धों से व्युत्पन्न।'}],

  ['The interactions the break permits. Electromagnetism, the electroweak force, the strong force, quantum gravity, and the gravitational constant — all as faces of a single break.',{
    es:'Las interacciones que la ruptura permite. Electromagnetismo, la fuerza electrodébil, la fuerza fuerte, la gravedad cuántica y la constante gravitacional — todas como facetas de una sola ruptura.',
    fr:'Les interactions que la brisure permet. L\'électromagnétisme, la force électrofaible, la force forte, la gravité quantique et la constante gravitationnelle — toutes comme facettes d\'une seule brisure.',
    de:'Die Wechselwirkungen, die der Bruch erlaubt. Elektromagnetismus, die elektroschwache Kraft, die starke Kraft, Quantengravitation und die Gravitationskonstante — alle als Facetten eines einzigen Bruchs.',
    pt:'As interações que a quebra permite. Eletromagnetismo, a força eletrofraca, a força forte, a gravidade quântica e a constante gravitacional — todas como faces de uma única quebra.',
    nl:'De interacties die de breuk toestaat. Elektromagnetisme, de elektrozwakke kracht, de sterke kracht, kwantumzwaartekracht en de gravitatieconstante — allemaal als facetten van één enkele breuk.',
    it:'Le interazioni che la rottura permette. Elettromagnetismo, la forza elettrodebole, la forza forte, la gravità quantistica e la costante gravitazionale — tutte come facce di un\'unica rottura.',
    zh:'断裂所允许的相互作用。电磁力、电弱力、强力、量子引力和引力常数——全部作为单一断裂的不同面。',
    ja:'破れが許す相互作用。電磁気力、電弱力、強い力、量子重力、重力定数——すべて一つの破れの異なる面として。',
    ko:'깨짐이 허용하는 상호작용. 전자기력, 전약력, 강력, 양자 중력, 중력 상수 — 모두 하나의 깨짐의 다른 면으로서.',
    ru:'Взаимодействия, которые допускает разрыв. Электромагнетизм, электрослабая сила, сильная сила, квантовая гравитация и гравитационная постоянная — все как грани одного разрыва.',
    ar:'التفاعلات التي يسمح بها الكسر. الكهرومغناطيسية، القوة الكهروضعيفة، القوة القوية، الجاذبية الكمّية، وثابت الجاذبية — كلها أوجه لكسر واحد.',
    hi:'वे अंतःक्रियाएँ जो टूट अनुमति देती है। विद्युत चुम्बकत्व, विद्युतदुर्बल बल, प्रबल बल, क्वांटम गुरुत्व और गुरुत्वाकर्षण स्थिरांक — सभी एक ही टूट के पहलू।'}],

  ['The building blocks the break produces. The proton mass ratio to five parts per billion, antimatter segregation, and the baryon asymmetry of the universe.',{
    es:'Los bloques de construcción que la ruptura produce. La relación de masa del protón a cinco partes por mil millones, la segregación de antimateria y la asimetría bariónica del universo.',
    fr:'Les briques que la brisure produit. Le rapport de masse du proton à cinq parties par milliard, la ségrégation d\'antimatière et l\'asymétrie baryonique de l\'univers.',
    de:'Die Bausteine, die der Bruch erzeugt. Das Proton-Massen-Verhältnis auf fünf Teile pro Milliarde, Antimaterie-Segregation und die Baryonen-Asymmetrie des Universums.',
    pt:'Os blocos de construção que a quebra produz. A razão de massa do próton a cinco partes por bilhão, a segregação de antimatéria e a assimetria bariônica do universo.',
    nl:'De bouwstenen die de breuk produceert. De proton-massaverhouding tot vijf delen per miljard, antimateriesegregatie en de baryonasymmetrie van het universum.',
    it:'I mattoni che la rottura produce. Il rapporto di massa del protone a cinque parti per miliardo, la segregazione dell\'antimateria e l\'asimmetria barionica dell\'universo.',
    zh:'断裂所产生的基本构件。质子质量比精确到十亿分之五、反物质分离和宇宙的重子不对称。',
    ja:'破れが生み出す構成要素。陽子質量比を十億分の五の精度で、反物質の分離、宇宙のバリオン非対称。',
    ko:'깨짐이 만드는 구성 요소. 양성자 질량비를 십억 분의 5까지, 반물질 분리, 우주의 바리온 비대칭.',
    ru:'Строительные блоки, которые создаёт разрыв. Отношение масс протона с точностью до пяти частей на миллиард, сегрегация антиматерии и барионная асимметрия Вселенной.',
    ar:'اللبنات التي ينتجها الكسر. نسبة كتلة البروتون إلى خمسة أجزاء من المليار، فصل المادة المضادة، وعدم تناظر الباريونات في الكون.',
    hi:'वे निर्माण खंड जो टूट उत्पन्न करती है। प्रोटॉन द्रव्यमान अनुपात प्रति अरब पाँच भाग तक, प्रतिपदार्थ पृथक्करण, और ब्रह्मांड की बैरियॉन विषमता।'}],

  ['The universe the break inhabits. Galactic rotation curves without dark matter particles, the MOND acceleration scale to 0.3%, the dark energy partition, and the cyclic cosmology.',{
    es:'El universo que la ruptura habita. Curvas de rotación galáctica sin partículas de materia oscura, la escala de aceleración MOND al 0,3%, la partición de energía oscura y la cosmología cíclica.',
    fr:'L\'univers qu\'habite la brisure. Les courbes de rotation galactique sans particules de matière noire, l\'échelle d\'accélération MOND à 0,3%, la partition d\'énergie noire et la cosmologie cyclique.',
    de:'Das Universum, das der Bruch bewohnt. Galaktische Rotationskurven ohne Dunkle-Materie-Teilchen, die MOND-Beschleunigungsskala auf 0,3%, die Dunkle-Energie-Aufteilung und die zyklische Kosmologie.',
    pt:'O universo que a quebra habita. Curvas de rotação galáctica sem partículas de matéria escura, a escala de aceleração MOND a 0,3%, a partição de energia escura e a cosmologia cíclica.',
    nl:'Het universum dat de breuk bewoont. Galactische rotatiekrommen zonder donkeremateriadeeltjes, de MOND-versnellingsschaal tot 0,3%, de donkere-energieverdeling en de cyclische kosmologie.',
    it:'L\'universo che la rottura abita. Curve di rotazione galattica senza particelle di materia oscura, la scala di accelerazione MOND allo 0,3%, la partizione di energia oscura e la cosmologia ciclica.',
    zh:'断裂所栖居的宇宙。无暗物质粒子的星系旋转曲线、MOND加速度标度精确到0.3%、暗能量分配和循环宇宙学。',
    ja:'破れが住む宇宙。ダークマター粒子なしの銀河回転曲線、MOND加速度スケール0.3%、ダークエネルギー分割、循環宇宙論。',
    ko:'깨짐이 사는 우주. 암흑물질 입자 없는 은하 회전 곡선, MOND 가속도 척도 0.3%, 암흑 에너지 분배, 순환 우주론.',
    ru:'Вселенная, в которой обитает разрыв. Кривые вращения галактик без частиц тёмной материи, шкала ускорения MOND до 0,3%, разделение тёмной энергии и циклическая космология.',
    ar:'الكون الذي يسكنه الكسر. منحنيات دوران المجرات بلا جسيمات مادة مظلمة، مقياس تسارع MOND إلى 0.3%، تقسيم الطاقة المظلمة، والكونيات الدورية.',
    hi:'वह ब्रह्मांड जिसमें टूट निवास करती है। गहरे पदार्थ कणों के बिना आकाशगंगीय घूर्णन वक्र, MOND त्वरण पैमाना 0.3% तक, गहरी ऊर्जा विभाजन और चक्रीय ब्रह्मांड विज्ञान।'}],

  ['The observer the break contains, and the ethic the break forces. Awareness derived from irreversible record-writing. The structural instability of authority-based ethics. Death as the closing of a window.',{
    es:'El observador que la ruptura contiene y la ética que la ruptura impone. La consciencia derivada de la escritura irreversible de registros. La inestabilidad estructural de las éticas basadas en autoridad. La muerte como el cierre de una ventana.',
    fr:'L\'observateur que la brisure contient, et l\'éthique que la brisure impose. La conscience dérivée de l\'écriture irréversible d\'enregistrements. L\'instabilité structurelle des éthiques fondées sur l\'autorité. La mort comme la fermeture d\'une fenêtre.',
    de:'Der Beobachter, den der Bruch enthält, und die Ethik, die der Bruch erzwingt. Bewusstsein abgeleitet aus irreversiblem Schreiben von Records. Die strukturelle Instabilität autoritätsbasierter Ethik. Tod als das Schließen eines Fensters.',
    pt:'O observador que a quebra contém e a ética que a quebra impõe. Consciência derivada da escrita irreversível de registros. A instabilidade estrutural das éticas baseadas em autoridade. A morte como o fechamento de uma janela.',
    nl:'De waarnemer die de breuk bevat, en de ethiek die de breuk afdwingt. Bewustzijn afgeleid uit onomkeerbaar schrijven van records. De structurele instabiliteit van op autoriteit gebaseerde ethiek. De dood als het sluiten van een venster.',
    it:'L\'osservatore che la rottura contiene, e l\'etica che la rottura impone. La coscienza derivata dalla scrittura irreversibile di record. L\'instabilità strutturale dell\'etica basata sull\'autorità. La morte come la chiusura di una finestra.',
    zh:'断裂所包含的观察者，以及断裂所强制的伦理。意识源于不可逆的记录书写。基于权威的伦理的结构性不稳定。死亡如同一扇窗的关闭。',
    ja:'破れが含む観察者、そして破れが強いる倫理。不可逆な記録書き込みから導かれる意識。権威に基づく倫理の構造的不安定性。死は窓の閉鎖として。',
    ko:'깨짐이 담고 있는 관찰자, 그리고 깨짐이 강제하는 윤리. 비가역적 기록 쓰기에서 도출된 의식. 권위 기반 윤리의 구조적 불안정성. 죽음은 창문의 닫힘으로서.',
    ru:'Наблюдатель, которого содержит разрыв, и этика, которую разрыв навязывает. Сознание, выведенное из необратимой записи. Структурная нестабильность этики, основанной на авторитете. Смерть как закрытие окна.',
    ar:'المراقب الذي يحتويه الكسر، والأخلاق التي يفرضها الكسر. الوعي المُشتقّ من كتابة السجلّات اللارجعية. عدم الاستقرار البنيوي للأخلاق القائمة على السلطة. الموت كإغلاق نافذة.',
    hi:'वह प्रेक्षक जो टूट में निहित है, और वह नैतिकता जो टूट बाध्य करती है। अपरिवर्तनीय अभिलेख-लेखन से व्युत्पन्न चेतना। प्राधिकार-आधारित नैतिकता की संरचनात्मक अस्थिरता। मृत्यु एक खिड़की के बंद होने के रूप में।'}],

  ['The ethic applied to civilisation. AI alignment, structural justice, bioethics, drug policy, economics, biology, and the body — all derived from the same four axioms.',{
    es:'La ética aplicada a la civilización. Alineamiento de IA, justicia estructural, bioética, política de drogas, economía, biología y el cuerpo — todo derivado de los mismos cuatro axiomas.',
    fr:'L\'éthique appliquée à la civilisation. Alignement de l\'IA, justice structurelle, bioéthique, politique des drogues, économie, biologie et le corps — tout dérivé des mêmes quatre axiomes.',
    de:'Die Ethik angewandt auf die Zivilisation. KI-Alignment, strukturelle Gerechtigkeit, Bioethik, Drogenpolitik, Wirtschaft, Biologie und der Körper — alles abgeleitet aus denselben vier Axiomen.',
    pt:'A ética aplicada à civilização. Alinhamento de IA, justiça estrutural, bioética, política de drogas, economia, biologia e o corpo — tudo derivado dos mesmos quatro axiomas.',
    nl:'De ethiek toegepast op de beschaving. AI-alignment, structurele rechtvaardigheid, bio-ethiek, drugsbeleid, economie, biologie en het lichaam — alles afgeleid uit dezelfde vier axioma\'s.',
    it:'L\'etica applicata alla civiltà. Allineamento dell\'IA, giustizia strutturale, bioetica, politica delle droghe, economia, biologia e il corpo — tutto derivato dagli stessi quattro assiomi.',
    zh:'应用于文明的伦理。AI对齐、结构正义、生物伦理、毒品政策、经济学、生物学和身体——全部源自同样的四条公理。',
    ja:'文明に適用された倫理。AIアラインメント、構造的正義、生命倫理、薬物政策、経済学、生物学、そして身体——すべて同じ四つの公理から導出。',
    ko:'문명에 적용된 윤리. AI 정렬, 구조적 정의, 생명윤리, 약물 정책, 경제학, 생물학, 그리고 몸 — 모두 같은 네 공리에서 도출.',
    ru:'Этика, применённая к цивилизации. Выравнивание ИИ, структурная справедливость, биоэтика, наркополитика, экономика, биология и тело — всё выведено из тех же четырёх аксиом.',
    ar:'الأخلاق مُطبَّقة على الحضارة. محاذاة الذكاء الاصطناعي، العدالة البنيوية، أخلاقيات الأحياء، سياسة المخدرات، الاقتصاد، الأحياء، والجسد — كلها مُشتقّة من نفس البديهيات الأربع.',
    hi:'सभ्यता पर लागू नैतिकता। AI संरेखण, संरचनात्मक न्याय, जैवनैतिकता, मादक द्रव्य नीति, अर्थशास्त्र, जीवविज्ञान और शरीर — सभी उन्हीं चार स्वयंसिद्धों से व्युत्पन्न।'}],

  // "papers" in part-count
  ['3 papers',{es:'3 artículos',fr:'3 articles',de:'3 Arbeiten',pt:'3 artigos',nl:'3 artikelen',it:'3 articoli',zh:'3 篇论文',ja:'3 本',ko:'3편',ru:'3 статьи',ar:'3 أبحاث',hi:'3 पत्र'}],
  ['4 papers',{es:'4 artículos',fr:'4 articles',de:'4 Arbeiten',pt:'4 artigos',nl:'4 artikelen',it:'4 articoli',zh:'4 篇论文',ja:'4 本',ko:'4편',ru:'4 статьи',ar:'4 أبحاث',hi:'4 पत्र'}],
  ['7 papers',{es:'7 artículos',fr:'7 articles',de:'7 Arbeiten',pt:'7 artigos',nl:'7 artikelen',it:'7 articoli',zh:'7 篇论文',ja:'7 本',ko:'7편',ru:'7 статей',ar:'7 أبحاث',hi:'7 पत्र'}],
  ['8 papers',{es:'8 artículos',fr:'8 articles',de:'8 Arbeiten',pt:'8 artigos',nl:'8 artikelen',it:'8 articoli',zh:'8 篇论文',ja:'8 本',ko:'8편',ru:'8 статей',ar:'8 أبحاث',hi:'8 पत्र'}],
  ['6 papers',{es:'6 artículos',fr:'6 articles',de:'6 Arbeiten',pt:'6 artigos',nl:'6 artikelen',it:'6 articoli',zh:'6 篇论文',ja:'6 本',ko:'6편',ru:'6 статей',ar:'6 أبحاث',hi:'6 पत्र'}],

  // Table headers
  ['<th>Claim</th><th>Predicted</th><th>Measured</th><th>Error</th><th>Paper</th>',{
    es:'<th>Afirmación</th><th>Predicho</th><th>Medido</th><th>Error</th><th>Artículo</th>',
    fr:'<th>Affirmation</th><th>Prédit</th><th>Mesuré</th><th>Erreur</th><th>Article</th>',
    de:'<th>Behauptung</th><th>Vorhergesagt</th><th>Gemessen</th><th>Fehler</th><th>Arbeit</th>',
    pt:'<th>Afirmação</th><th>Previsto</th><th>Medido</th><th>Erro</th><th>Artigo</th>',
    nl:'<th>Bewering</th><th>Voorspeld</th><th>Gemeten</th><th>Fout</th><th>Artikel</th>',
    it:'<th>Affermazione</th><th>Previsto</th><th>Misurato</th><th>Errore</th><th>Articolo</th>',
    zh:'<th>声明</th><th>预测值</th><th>测量值</th><th>误差</th><th>论文</th>',
    ja:'<th>主張</th><th>予測</th><th>測定</th><th>誤差</th><th>論文</th>',
    ko:'<th>주장</th><th>예측</th><th>측정</th><th>오차</th><th>논문</th>',
    ru:'<th>Утверждение</th><th>Предсказано</th><th>Измерено</th><th>Ошибка</th><th>Статья</th>',
    ar:'<th>الادّعاء</th><th>متوقَّع</th><th>مُقاس</th><th>الخطأ</th><th>البحث</th>',
    hi:'<th>दावा</th><th>पूर्वानुमानित</th><th>मापित</th><th>त्रुटि</th><th>पत्र</th>'}],

  // Table row labels
  ['<td>Proton mass ratio</td>',{es:'<td>Relación de masa del protón</td>',fr:'<td>Rapport de masse du proton</td>',de:'<td>Proton-Massen-Verhältnis</td>',pt:'<td>Razão de massa do próton</td>',nl:'<td>Proton-massaverhouding</td>',it:'<td>Rapporto di massa del protone</td>',zh:'<td>质子质量比</td>',ja:'<td>陽子質量比</td>',ko:'<td>양성자 질량비</td>',ru:'<td>Отношение масс протона</td>',ar:'<td>نسبة كتلة البروتون</td>',hi:'<td>प्रोटॉन द्रव्यमान अनुपात</td>'}],
  ['<td>Gravitational constant G</td>',{es:'<td>Constante gravitacional G</td>',fr:'<td>Constante gravitationnelle G</td>',de:'<td>Gravitationskonstante G</td>',pt:'<td>Constante gravitacional G</td>',nl:'<td>Gravitatieconstante G</td>',it:'<td>Costante gravitazionale G</td>',zh:'<td>引力常数 G</td>',ja:'<td>重力定数 G</td>',ko:'<td>중력 상수 G</td>',ru:'<td>Гравитационная постоянная G</td>',ar:'<td>ثابت الجاذبية G</td>',hi:'<td>गुरुत्वाकर्षण स्थिरांक G</td>'}],
  ['<td>Neutron-proton mass diff</td>',{es:'<td>Diferencia masa neutrón-protón</td>',fr:'<td>Différence masse neutron-proton</td>',de:'<td>Neutron-Proton-Massendiff.</td>',pt:'<td>Dif. massa nêutron-próton</td>',nl:'<td>Neutron-proton-massaverschil</td>',it:'<td>Diff. massa neutrone-protone</td>',zh:'<td>中子-质子质量差</td>',ja:'<td>中性子-陽子質量差</td>',ko:'<td>중성자-양성자 질량 차이</td>',ru:'<td>Разность масс нейтрон-протон</td>',ar:'<td>فرق كتلة النيوترون-البروتون</td>',hi:'<td>न्यूट्रॉन-प्रोटॉन द्रव्यमान अंतर</td>'}],
  ['<td>MOND acceleration a₀</td>',{es:'<td>Aceleración MOND a₀</td>',fr:'<td>Accélération MOND a₀</td>',de:'<td>MOND-Beschleunigung a₀</td>',pt:'<td>Aceleração MOND a₀</td>',nl:'<td>MOND-versnelling a₀</td>',it:'<td>Accelerazione MOND a₀</td>',zh:'<td>MOND 加速度 a₀</td>',ja:'<td>MOND加速度 a₀</td>',ko:'<td>MOND 가속도 a₀</td>',ru:'<td>Ускорение MOND a₀</td>',ar:'<td>تسارع MOND a₀</td>',hi:'<td>MOND त्वरण a₀</td>'}],
  ['<td>Dark energy</td>',{es:'<td>Energía oscura</td>',fr:'<td>Énergie noire</td>',de:'<td>Dunkle Energie</td>',pt:'<td>Energia escura</td>',nl:'<td>Donkere energie</td>',it:'<td>Energia oscura</td>',zh:'<td>暗能量</td>',ja:'<td>ダークエネルギー</td>',ko:'<td>암흑 에너지</td>',ru:'<td>Тёмная энергия</td>',ar:'<td>الطاقة المظلمة</td>',hi:'<td>गहरी ऊर्जा</td>'}],
  ['<td>Visible matter</td>',{es:'<td>Materia visible</td>',fr:'<td>Matière visible</td>',de:'<td>Sichtbare Materie</td>',pt:'<td>Matéria visível</td>',nl:'<td>Zichtbare materie</td>',it:'<td>Materia visibile</td>',zh:'<td>可见物质</td>',ja:'<td>可視物質</td>',ko:'<td>가시 물질</td>',ru:'<td>Видимая материя</td>',ar:'<td>المادة المرئية</td>',hi:'<td>दृश्य पदार्थ</td>'}],
];

LANGS.forEach(lang => {
  const fp = path.join('C:/Users/info/the420code', lang, 'index.html');
  let h = fs.readFileSync(fp, 'utf8');
  let c = 0;
  for (const [en, t] of R) {
    const val = t[lang];
    if (!val) continue;
    while (h.includes(en)) { h = h.replace(en, val); c++; }
  }
  fs.writeFileSync(fp, h);
  console.log('  ' + lang + ' — ' + c + ' changes');
});
console.log('Done');
