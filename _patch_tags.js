const fs = require('fs');
const path = require('path');
const LANGS = ['es','fr','de','pt','nl','it','zh','ja','ko','ru','ar','hi'];

const TAGS = {
'Mathematics':{es:'Matemáticas',fr:'Mathématiques',de:'Mathematik',pt:'Matemática',nl:'Wiskunde',it:'Matematica',zh:'数学',ja:'数学',ko:'수학',ru:'Математика',ar:'الرياضيات',hi:'गणित'},
'Foundations':{es:'Fundamentos',fr:'Fondements',de:'Grundlagen',pt:'Fundamentos',nl:'Grondslagen',it:'Fondamenti',zh:'基础',ja:'基礎',ko:'기초',ru:'Основы',ar:'الأسس',hi:'आधार'},
'Logic':{es:'Lógica',fr:'Logique',de:'Logik',pt:'Lógica',nl:'Logica',it:'Logica',zh:'逻辑',ja:'論理',ko:'논리',ru:'Логика',ar:'المنطق',hi:'तर्क'},
'Relativity':{es:'Relatividad',fr:'Relativité',de:'Relativität',pt:'Relatividade',nl:'Relativiteit',it:'Relatività',zh:'相对论',ja:'相対性',ko:'상대성',ru:'Относительность',ar:'النسبية',hi:'सापेक्षता'},
'Symmetry Breaking':{es:'Ruptura de simetría',fr:'Brisure de symétrie',de:'Symmetriebrechung',pt:'Quebra de simetria',nl:'Symmetriebreking',it:'Rottura di simmetria',zh:'对称性破缺',ja:'対称性の破れ',ko:'대칭 깨짐',ru:'Нарушение симметрии',ar:'كسر التناظر',hi:'सममिति भंग'},
'Dimensionality':{es:'Dimensionalidad',fr:'Dimensionnalité',de:'Dimensionalität',pt:'Dimensionalidade',nl:'Dimensionaliteit',it:'Dimensionalità',zh:'维度性',ja:'次元性',ko:'차원성',ru:'Размерность',ar:'البُعدية',hi:'आयामिता'},
'General Relativity':{es:'Relatividad general',fr:'Relativité générale',de:'Allgemeine Relativität',pt:'Relatividade geral',nl:'Algemene relativiteit',it:'Relatività generale',zh:'广义相对论',ja:'一般相対性',ko:'일반 상대성',ru:'Общая относительность',ar:'النسبية العامة',hi:'सामान्य सापेक्षता'},
'Quantum Foundations':{es:'Fundamentos cuánticos',fr:'Fondements quantiques',de:'Quantengrundlagen',pt:'Fundamentos quânticos',nl:'Kwantumgrondslagen',it:'Fondamenti quantistici',zh:'量子基础',ja:'量子基礎',ko:'양자 기초',ru:'Квантовые основы',ar:'أسس الكمّ',hi:'क्वांटम आधार'},
'Hilbert Space':{es:'Espacio de Hilbert',fr:'Espace de Hilbert',de:'Hilbertraum',pt:'Espaço de Hilbert',nl:'Hilbertruimte',it:'Spazio di Hilbert',zh:'希尔伯特空间',ja:'ヒルベルト空間',ko:'힐베르트 공간',ru:'Гильбертово пространство',ar:'فضاء هيلبرت',hi:'हिल्बर्ट अवकाश'},
'Spin':{es:'Espín',fr:'Spin',de:'Spin',pt:'Spin',nl:'Spin',it:'Spin',zh:'自旋',ja:'スピン',ko:'스핀',ru:'Спин',ar:'اللَّف',hi:'स्पिन'},
'Uncertainty':{es:'Incertidumbre',fr:'Incertitude',de:'Unschärfe',pt:'Incerteza',nl:'Onzekerheid',it:'Indeterminazione',zh:'不确定性',ja:'不確定性',ko:'불확정성',ru:'Неопределённость',ar:'عدم اليقين',hi:'अनिश्चितता'},
'Decoherence':{es:'Decoherencia',fr:'Décohérence',de:'Dekohärenz',pt:'Decoerência',nl:'Decoherentie',it:'Decoerenza',zh:'退相干',ja:'デコヒーレンス',ko:'결어긋남',ru:'Декогеренция',ar:'فقدان التماسك',hi:'विसंबद्धता'},
'Born Rule':{es:'Regla de Born',fr:'Règle de Born',de:'Born-Regel',pt:'Regra de Born',nl:'Born-regel',it:'Regola di Born',zh:'玻恩规则',ja:'ボルン規則',ko:'보른 규칙',ru:'Правило Борна',ar:'قاعدة بورن',hi:'बोर्न नियम'},
'Entanglement':{es:'Entrelazamiento',fr:'Intrication',de:'Verschränkung',pt:'Emaranhamento',nl:'Verstrengeling',it:'Entanglement',zh:'纠缠',ja:'エンタングルメント',ko:'얽힘',ru:'Запутанность',ar:'التشابك',hi:'उलझाव'},
'Fine Structure':{es:'Estructura fina',fr:'Structure fine',de:'Feinstruktur',pt:'Estrutura fina',nl:'Fijnstructuur',it:'Struttura fine',zh:'精细结构',ja:'微細構造',ko:'미세구조',ru:'Тонкая структура',ar:'البنية الدقيقة',hi:'सूक्ष्म संरचना'},
'Electromagnetism':{es:'Electromagnetismo',fr:'Électromagnétisme',de:'Elektromagnetismus',pt:'Eletromagnetismo',nl:'Elektromagnetisme',it:'Elettromagnetismo',zh:'电磁学',ja:'電磁気学',ko:'전자기학',ru:'Электромагнетизм',ar:'الكهرومغناطيسية',hi:'विद्युत चुम्बकत्व'},
'Gauge Structure':{es:'Estructura gauge',fr:'Structure de jauge',de:'Eichstruktur',pt:'Estrutura gauge',nl:'IJkstructuur',it:'Struttura di gauge',zh:'规范结构',ja:'ゲージ構造',ko:'게이지 구조',ru:'Калибровочная структура',ar:'بنية المعيار',hi:'गेज संरचना'},
'Electroweak':{es:'Electrodébil',fr:'Électrofaible',de:'Elektroschwach',pt:'Eletrofraco',nl:'Elektrozwak',it:'Elettrodebole',zh:'电弱',ja:'電弱',ko:'전약',ru:'Электрослабое',ar:'كهروضعيف',hi:'विद्युतदुर्बल'},
'Strong Force':{es:'Fuerza fuerte',fr:'Force forte',de:'Starke Kraft',pt:'Força forte',nl:'Sterke kracht',it:'Forza forte',zh:'强力',ja:'強い力',ko:'강력',ru:'Сильная сила',ar:'القوة القوية',hi:'प्रबल बल'},
'Unification':{es:'Unificación',fr:'Unification',de:'Vereinigung',pt:'Unificação',nl:'Unificatie',it:'Unificazione',zh:'统一',ja:'統一',ko:'통일',ru:'Объединение',ar:'التوحيد',hi:'एकीकरण'},
'Quantum Gravity':{es:'Gravedad cuántica',fr:'Gravité quantique',de:'Quantengravitation',pt:'Gravidade quântica',nl:'Kwantumzwaartekracht',it:'Gravità quantistica',zh:'量子引力',ja:'量子重力',ko:'양자 중력',ru:'Квантовая гравитация',ar:'الجاذبية الكمّية',hi:'क्वांटम गुरुत्व'},
'Gravity':{es:'Gravedad',fr:'Gravité',de:'Gravitation',pt:'Gravidade',nl:'Zwaartekracht',it:'Gravità',zh:'引力',ja:'重力',ko:'중력',ru:'Гравитация',ar:'الجاذبية',hi:'गुरुत्व'},
'Mass':{es:'Masa',fr:'Masse',de:'Masse',pt:'Massa',nl:'Massa',it:'Massa',zh:'质量',ja:'質量',ko:'질량',ru:'Масса',ar:'الكتلة',hi:'द्रव्यमान'},
'Antimatter':{es:'Antimateria',fr:'Antimatière',de:'Antimaterie',pt:'Antimatéria',nl:'Antimaterie',it:'Antimateria',zh:'反物质',ja:'反物質',ko:'반물질',ru:'Антиматерия',ar:'المادة المضادة',hi:'प्रतिपदार्थ'},
'Baryon Asymmetry':{es:'Asimetría bariónica',fr:'Asymétrie baryonique',de:'Baryonenasymmetrie',pt:'Assimetria bariônica',nl:'Baryonasymmetrie',it:'Asimmetria barionica',zh:'重子不对称',ja:'バリオン非対称',ko:'바리온 비대칭',ru:'Барионная асимметрия',ar:'عدم تناظر الباريونات',hi:'बैरियॉन विषमता'},
'Rotation Curves':{es:'Curvas de rotación',fr:'Courbes de rotation',de:'Rotationskurven',pt:'Curvas de rotação',nl:'Rotatiekrommen',it:'Curve di rotazione',zh:'旋转曲线',ja:'回転曲線',ko:'회전 곡선',ru:'Кривые вращения',ar:'منحنيات الدوران',hi:'घूर्णन वक्र'},
'Acceleration Scale':{es:'Escala de aceleración',fr:"Échelle d'accélération",de:'Beschleunigungsskala',pt:'Escala de aceleração',nl:'Versnellingsschaal',it:'Scala di accelerazione',zh:'加速度标度',ja:'加速度スケール',ko:'가속도 척도',ru:'Шкала ускорения',ar:'مقياس التسارع',hi:'त्वरण पैमाना'},
'Dark Energy':{es:'Energía oscura',fr:'Énergie noire',de:'Dunkle Energie',pt:'Energia escura',nl:'Donkere energie',it:'Energia oscura',zh:'暗能量',ja:'ダークエネルギー',ko:'암흑 에너지',ru:'Тёмная энергия',ar:'الطاقة المظلمة',hi:'गहरी ऊर्जा'},
'Structure Formation':{es:'Formación de estructuras',fr:'Formation de structures',de:'Strukturbildung',pt:'Formação de estruturas',nl:'Structuurvorming',it:'Formazione di strutture',zh:'结构形成',ja:'構造形成',ko:'구조 형성',ru:'Формирование структур',ar:'تكوين البنى',hi:'संरचना निर्माण'},
'Cosmology':{es:'Cosmología',fr:'Cosmologie',de:'Kosmologie',pt:'Cosmologia',nl:'Kosmologie',it:'Cosmologia',zh:'宇宙学',ja:'宇宙論',ko:'우주론',ru:'Космология',ar:'علم الكونيات',hi:'ब्रह्मांड विज्ञान'},
'Cyclic Cosmology':{es:'Cosmología cíclica',fr:'Cosmologie cyclique',de:'Zyklische Kosmologie',pt:'Cosmologia cíclica',nl:'Cyclische kosmologie',it:'Cosmologia ciclica',zh:'循环宇宙学',ja:'循環宇宙論',ko:'순환 우주론',ru:'Циклическая космология',ar:'الكونيات الدورية',hi:'चक्रीय ब्रह्मांड विज्ञान'},
'Consciousness':{es:'Consciencia',fr:'Conscience',de:'Bewusstsein',pt:'Consciência',nl:'Bewustzijn',it:'Coscienza',zh:'意识',ja:'意識',ko:'의식',ru:'Сознание',ar:'الوعي',hi:'चेतना'},
'Religion':{es:'Religión',fr:'Religion',de:'Religion',pt:'Religião',nl:'Religie',it:'Religione',zh:'宗教',ja:'宗教',ko:'종교',ru:'Религия',ar:'الدين',hi:'धर्म'},
'Agency':{es:'Agencia',fr:'Agentivité',de:'Handlungsfähigkeit',pt:'Agência',nl:'Agentschap',it:'Agency',zh:'能动性',ja:'エージェンシー',ko:'행위능력',ru:'Агентность',ar:'الفاعلية',hi:'कर्तृत्व'},
'Death':{es:'Muerte',fr:'Mort',de:'Tod',pt:'Morte',nl:'Dood',it:'Morte',zh:'死亡',ja:'死',ko:'죽음',ru:'Смерть',ar:'الموت',hi:'मृत्यु'},
'AI Alignment':{es:'Alineamiento de IA',fr:"Alignement de l'IA",de:'KI-Alignment',pt:'Alinhamento de IA',nl:'AI-alignment',it:"Allineamento dell'IA",zh:'AI 对齐',ja:'AIアラインメント',ko:'AI 정렬',ru:'Выравнивание ИИ',ar:'محاذاة الذكاء الاصطناعي',hi:'AI संरेखण'},
'Justice':{es:'Justicia',fr:'Justice',de:'Gerechtigkeit',pt:'Justiça',nl:'Rechtvaardigheid',it:'Giustizia',zh:'正义',ja:'正義',ko:'정의',ru:'Справедливость',ar:'العدالة',hi:'न्याय'},
'Bioethics':{es:'Bioética',fr:'Bioéthique',de:'Bioethik',pt:'Bioética',nl:'Bio-ethiek',it:'Bioetica',zh:'生物伦理',ja:'生命倫理',ko:'생명윤리',ru:'Биоэтика',ar:'أخلاقيات الأحياء',hi:'जैवनैतिकता'},
'Drug Policy':{es:'Política de drogas',fr:'Politique des drogues',de:'Drogenpolitik',pt:'Política de drogas',nl:'Drugsbeleid',it:'Politica delle droghe',zh:'毒品政策',ja:'薬物政策',ko:'약물 정책',ru:'Наркополитика',ar:'سياسة المخدرات',hi:'मादक द्रव्य नीति'},
'Economics':{es:'Economía',fr:'Économie',de:'Wirtschaft',pt:'Economia',nl:'Economie',it:'Economia',zh:'经济学',ja:'経済学',ko:'경제학',ru:'Экономика',ar:'الاقتصاد',hi:'अर्थशास्त्र'},
'Biology':{es:'Biología',fr:'Biologie',de:'Biologie',pt:'Biologia',nl:'Biologie',it:'Biologia',zh:'生物学',ja:'生物学',ko:'생물학',ru:'Биология',ar:'الأحياء',hi:'जीवविज्ञान'},
'The Body':{es:'El Cuerpo',fr:'Le Corps',de:'Der Körper',pt:'O Corpo',nl:'Het Lichaam',it:'Il Corpo',zh:'身体',ja:'身体',ko:'몸',ru:'Тело',ar:'الجسد',hi:'शरीर'},
};

LANGS.forEach(lang => {
  const fp = path.join('C:/Users/info/the420code', lang, 'index.html');
  let h = fs.readFileSync(fp, 'utf8');
  let c = 0;
  for (const [en, t] of Object.entries(TAGS)) {
    const val = t[lang];
    if (!val) continue;
    const find = 'ap-tag">' + en + '</span>';
    const repl = 'ap-tag">' + val + '</span>';
    while (h.includes(find)) { h = h.replace(find, repl); c++; }
  }
  fs.writeFileSync(fp, h);
  console.log('  ' + lang + ' — ' + c + ' tags translated');
});
console.log('Done');
