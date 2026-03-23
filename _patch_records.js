const fs = require('fs');
const path = require('path');
const LANGS = ['es','fr','de','pt','nl','it','zh','ja','ko','ru','ar','hi'];

const R = {
  records_intro: {
    en:'Five records. The unprocessed output of a thirty-year project — mistakes, breakthroughs, dead ends, and the moments between them.',
    es:'Cinco registros. El resultado sin procesar de un proyecto de treinta años — errores, descubrimientos, callejones sin salida y los momentos intermedios.',
    fr:'Cinq enregistrements. La sortie brute d\'un projet de trente ans — erreurs, percées, impasses et les moments entre les deux.',
    de:'Fünf Aufzeichnungen. Das unbearbeitete Ergebnis eines dreißigjährigen Projekts — Fehler, Durchbrüche, Sackgassen und die Momente dazwischen.',
    pt:'Cinco registros. O resultado bruto de um projeto de trinta anos — erros, avanços, becos sem saída e os momentos entre eles.',
    nl:'Vijf verslagen. De onbewerkte uitkomst van een dertigjarig project — fouten, doorbraken, doodlopende wegen en de momenten ertussen.',
    it:'Cinque registrazioni. L\'output grezzo di un progetto trentennale — errori, scoperte, vicoli ciechi e i momenti in mezzo.',
    zh:'五份记录。一个三十年项目的未加工输出——错误、突破、死胡同，以及其间的时刻。',
    ja:'五つの記録。三十年プロジェクトの未加工の出力——失敗、突破、行き止まり、そしてその間の瞬間。',
    ko:'다섯 개의 기록. 서른 해 프로젝트의 가공되지 않은 출력 — 실수, 돌파구, 막다른 길, 그리고 그 사이의 순간들.',
    ru:'Пять записей. Необработанный результат тридцатилетнего проекта — ошибки, прорывы, тупики и моменты между ними.',
    ar:'خمسة سجلّات. المخرَج الخام لمشروع امتدّ ثلاثين عامًا — أخطاء، اختراقات، طرق مسدودة، واللحظات بينها.',
    hi:'पाँच अभिलेख। तीस साल की परियोजना का असंसाधित उत्पाद — गलतियाँ, सफलताएँ, बंद गलियाँ, और उनके बीच के क्षण।'
  },
  rec01_desc: {
    en:'<em>01 — The Scissors.</em> Written four months after a brother was murdered. Grief looking for structure. This is where the 420 Code began — not in a library, but in a wound.',
    es:'<em>01 — Las Tijeras.</em> Escrito cuatro meses después del asesinato de un hermano. El duelo buscando estructura. Aquí comenzó The 420 Code — no en una biblioteca, sino en una herida.',
    fr:'<em>01 — Les Ciseaux.</em> Écrit quatre mois après l\'assassinat d\'un frère. Le deuil cherchant une structure. C\'est là que The 420 Code a commencé — pas dans une bibliothèque, mais dans une blessure.',
    de:'<em>01 — Die Schere.</em> Geschrieben vier Monate nach dem Mord an einem Bruder. Trauer auf der Suche nach Struktur. Hier begann The 420 Code — nicht in einer Bibliothek, sondern in einer Wunde.',
    pt:'<em>01 — A Tesoura.</em> Escrito quatro meses após o assassinato de um irmão. Luto procurando estrutura. Aqui começou The 420 Code — não numa biblioteca, mas numa ferida.',
    nl:'<em>01 — De Schaar.</em> Geschreven vier maanden na de moord op een broer. Rouw op zoek naar structuur. Hier begon The 420 Code — niet in een bibliotheek, maar in een wond.',
    it:'<em>01 — Le Forbici.</em> Scritto quattro mesi dopo l\'omicidio di un fratello. Il lutto in cerca di struttura. Qui è iniziato The 420 Code — non in una biblioteca, ma in una ferita.',
    zh:'<em>01 — 剪刀。</em>在一个兄弟被谋杀四个月后写成。悲痛在寻找结构。The 420 Code从这里开始——不是在图书馆，而是在伤口中。',
    ja:'<em>01 — 鋏。</em>兄弟が殺された四ヶ月後に書かれた。構造を求める悲嘆。420 Codeはここから始まった——図書館ではなく、傷の中から。',
    ko:'<em>01 — 가위.</em> 형제가 살해된 지 네 달 후에 쓰였다. 구조를 찾는 슬픔. 420 Code는 여기서 시작되었다 — 도서관이 아니라 상처 속에서.',
    ru:'<em>01 — Ножницы.</em> Написано через четыре месяца после убийства брата. Горе, ищущее структуру. Здесь начался 420 Code — не в библиотеке, а в ране.',
    ar:'<em>01 — المقصّ.</em> كُتب بعد أربعة أشهر من مقتل أخ. حزنٌ يبحث عن بنية. هنا بدأ The 420 Code — ليس في مكتبة، بل في جرح.',
    hi:'<em>01 — कैंची।</em> एक भाई की हत्या के चार महीने बाद लिखा गया। संरचना खोजता शोक। 420 Code यहाँ शुरू हुआ — पुस्तकालय में नहीं, बल्कि एक घाव में।'
  },
  rec02_desc: {
    en:'<em>02 — The Wind.</em> A life examined through the lens of the 420 Code. Memory, mistake, and meaning — held up to the axioms to see what survives. The argument learns to carry.',
    es:'<em>02 — El Viento.</em> Una vida examinada a través del prisma de The 420 Code. Memoria, error y significado — sostenidos frente a los axiomas para ver qué sobrevive. El argumento aprende a cargar.',
    fr:'<em>02 — Le Vent.</em> Une vie examinée à travers le prisme de The 420 Code. Mémoire, erreur et sens — tenus face aux axiomes pour voir ce qui survit. L\'argument apprend à porter.',
    de:'<em>02 — Der Wind.</em> Ein Leben, untersucht durch die Linse von The 420 Code. Erinnerung, Fehler und Bedeutung — den Axiomen vorgehalten, um zu sehen, was überlebt. Das Argument lernt zu tragen.',
    pt:'<em>02 — O Vento.</em> Uma vida examinada pela lente de The 420 Code. Memória, erro e significado — sustentados frente aos axiomas para ver o que sobrevive. O argumento aprende a carregar.',
    nl:'<em>02 — De Wind.</em> Een leven onderzocht door de lens van The 420 Code. Herinnering, fout en betekenis — gehouden tegen de axioma\'s om te zien wat overleeft. Het argument leert dragen.',
    it:'<em>02 — Il Vento.</em> Una vita esaminata attraverso la lente di The 420 Code. Memoria, errore e significato — tenuti davanti agli assiomi per vedere cosa sopravvive. L\'argomento impara a portare.',
    zh:'<em>02 — 风。</em>通过 420 Code 的棱镜审视的一生。记忆、错误和意义——举在公理面前看什么能存活。论证学会了承载。',
    ja:'<em>02 — 風。</em>420 Codeのレンズを通して検証された人生。記憶、過ち、意味——公理に照らして何が生き残るかを見る。論証は運ぶことを学ぶ。',
    ko:'<em>02 — 바람.</em> 420 Code의 렌즈로 들여다본 삶. 기억, 실수, 의미 — 공리에 비추어 무엇이 살아남는지 본다. 논증은 짊어지는 법을 배운다.',
    ru:'<em>02 — Ветер.</em> Жизнь, рассмотренная через призму 420 Code. Память, ошибка и смысл — поднесённые к аксиомам, чтобы увидеть, что выживет. Аргумент учится нести.',
    ar:'<em>02 — الريح.</em> حياة مُتفحَّصة من خلال عدسة The 420 Code. ذاكرة، خطأ، ومعنى — مرفوعة أمام البديهيات لنرى ما يبقى. الحجة تتعلم أن تحمل.',
    hi:'<em>02 — हवा।</em> 420 Code के लेंस से जाँची गई एक ज़िंदगी। स्मृति, भूल और अर्थ — स्वयंसिद्धों के सामने रखकर देखना कि क्या बचता है। तर्क ढोना सीखता है।'
  },
  rec03_desc: {
    en:'<em>03 — Are You Certain.</em> The structural demolition of every system that ever claimed authority it could not prove. The evidence is the damage. The damage is the argument.',
    es:'<em>03 — ¿Estás Seguro?</em> La demolición estructural de cada sistema que alguna vez reclamó autoridad que no podía probar. La evidencia es el daño. El daño es el argumento.',
    fr:'<em>03 — Es-tu Certain ?</em> La démolition structurelle de chaque système ayant jamais revendiqué une autorité qu\'il ne pouvait prouver. La preuve est le dommage. Le dommage est l\'argument.',
    de:'<em>03 — Bist Du Sicher?</em> Die strukturelle Abrissbirne für jedes System, das je Autorität beanspruchte, die es nicht beweisen konnte. Der Beweis ist der Schaden. Der Schaden ist das Argument.',
    pt:'<em>03 — Tem Certeza?</em> A demolição estrutural de cada sistema que já reivindicou autoridade que não podia provar. A evidência é o dano. O dano é o argumento.',
    nl:'<em>03 — Weet Je Het Zeker?</em> De structurele sloop van elk systeem dat ooit autoriteit claimde die het niet kon bewijzen. Het bewijs is de schade. De schade is het argument.',
    it:'<em>03 — Sei Certo?</em> La demolizione strutturale di ogni sistema che abbia mai rivendicato un\'autorità che non poteva dimostrare. La prova è il danno. Il danno è l\'argomento.',
    zh:'<em>03 — 你确定吗？</em>对每一个曾声称拥有无法证明的权威的系统的结构性拆除。证据就是伤害。伤害就是论证。',
    ja:'<em>03 — 確かか？</em>証明できない権威を主張したすべてのシステムの構造的解体。証拠は損害だ。損害が論証だ。',
    ko:'<em>03 — 확실한가?</em> 증명할 수 없는 권위를 주장한 모든 체계의 구조적 해체. 증거는 피해다. 피해가 논증이다.',
    ru:'<em>03 — Ты Уверен?</em> Структурный снос каждой системы, когда-либо претендовавшей на власть, которую не могла доказать. Свидетельство — ущерб. Ущерб — аргумент.',
    ar:'<em>03 — هل أنت متأكد؟</em> الهدم البنيوي لكل نظام ادّعى سلطة لم يستطع إثباتها. الدليل هو الضرر. الضرر هو الحجة.',
    hi:'<em>03 — क्या आप निश्चित हैं?</em> हर उस प्रणाली का संरचनात्मक विध्वंस जिसने कभी ऐसा अधिकार जताया जो वह सिद्ध नहीं कर सकी। प्रमाण क्षति है। क्षति ही तर्क है।'
  },
  rec04_desc: {
    en:"<em>04 — Don't Be a Cunt Be Kind.</em> The ethic arrives. Not as conclusion — as eruption. The terminal line was felt first, lived for years, and only later shown to be a forced consequence of the physics.",
    es:'<em>04 — No Seas Hijo de Puta, Sé Amable.</em> La ética llega. No como conclusión — como erupción. La línea terminal se sintió primero, se vivió durante años, y solo después se demostró como consecuencia forzada de la física.',
    fr:'<em>04 — Ne Sois Pas un Connard, Sois Gentil.</em> L\'éthique arrive. Pas comme conclusion — comme éruption. La ligne terminale a été ressentie d\'abord, vécue pendant des années, et seulement ensuite montrée comme conséquence forcée de la physique.',
    de:'<em>04 — Sei Kein Arschloch, Sei Nett.</em> Die Ethik kommt. Nicht als Schlussfolgerung — als Eruption. Die terminale Linie wurde zuerst gefühlt, jahrelang gelebt und erst später als erzwungene Konsequenz der Physik gezeigt.',
    pt:'<em>04 — Não Seja Babaca, Seja Gentil.</em> A ética chega. Não como conclusão — como erupção. A linha terminal foi sentida primeiro, vivida por anos, e só depois demonstrada como consequência forçada da física.',
    nl:'<em>04 — Wees Geen Klootzak, Wees Aardig.</em> De ethiek arriveert. Niet als conclusie — als eruptie. De terminale lijn werd eerst gevoeld, jarenlang geleefd, en pas later aangetoond als een geforceerd gevolg van de fysica.',
    it:'<em>04 — Non Essere Uno Stronzo, Sii Gentile.</em> L\'etica arriva. Non come conclusione — come eruzione. La linea terminale è stata sentita prima, vissuta per anni, e solo dopo mostrata come conseguenza forzata della fisica.',
    zh:'<em>04 — 别当混蛋，善良点。</em>伦理到来了。不是作为结论——而是作为喷发。终极线先被感受到，活了多年，后来才被证明是物理学的必然后果。',
    ja:'<em>04 — クソ野郎になるな、優しくしろ。</em>倫理が到来する。結論としてではなく——噴出として。終末の線はまず感じられ、何年も生きられ、後になってようやく物理学の強制的帰結だと示された。',
    ko:'<em>04 — 개자식이 되지 마라, 친절하라.</em> 윤리가 도착한다. 결론이 아니라 — 분출로서. 종말선은 먼저 느껴졌고, 수년간 살아졌으며, 나중에야 물리학의 필연적 귀결임이 밝혀졌다.',
    ru:'<em>04 — Не Будь Мудаком, Будь Добрым.</em> Этика приходит. Не как вывод — как извержение. Терминальная линия была прочувствована первой, прожита годами, и лишь потом показана как вынужденное следствие физики.',
    ar:'<em>04 — لا تكن وغدًا، كن لطيفًا.</em> الأخلاق تصل. ليس كاستنتاج — كانفجار. الخط النهائي شُعر به أولًا، عُيش سنوات، ثم تبيّن لاحقًا أنه نتيجة حتمية للفيزياء.',
    hi:'<em>04 — गंदे मत बनो, दयालु बनो।</em> नैतिकता आती है। निष्कर्ष के रूप में नहीं — विस्फोट के रूप में। अंतिम रेखा पहले महसूस हुई, वर्षों तक जी गई, और बाद में ही भौतिकी का अनिवार्य परिणाम सिद्ध हुई।'
  },
  rec05_desc: {
    en:'<em>05 — Fuck You Leave Me-I Alone.</em> An autobiography. The person behind the anonymous exhibition.',
    es:'<em>05 — Vete a la Mierda, Déjame en Paz.</em> Una autobiografía. La persona detrás de la exposición anónima.',
    fr:'<em>05 — Va Te Faire Foutre, Laisse-Moi Tranquille.</em> Une autobiographie. La personne derrière l\'exposition anonyme.',
    de:'<em>05 — Verpiss Dich, Lass Mich in Ruhe.</em> Eine Autobiografie. Die Person hinter der anonymen Ausstellung.',
    pt:'<em>05 — Vai Se Foder, Me Deixa em Paz.</em> Uma autobiografia. A pessoa por trás da exposição anônima.',
    nl:'<em>05 — Rot Op, Laat Me Met Rust.</em> Een autobiografie. De persoon achter de anonieme tentoonstelling.',
    it:'<em>05 — Vaffanculo, Lasciami in Pace.</em> Un\'autobiografia. La persona dietro la mostra anonima.',
    zh:'<em>05 — 滚开，别烦我。</em>一部自传。匿名展览背后的人。',
    ja:'<em>05 — くたばれ、ほっとけ。</em>自叙伝。匿名の展覧会の背後にいる人物。',
    ko:'<em>05 — 꺼져, 나 혼자 놔둬.</em> 자서전. 익명 전시회 뒤의 사람.',
    ru:'<em>05 — Пошёл К Чёрту, Оставь Меня в Покое.</em> Автобиография. Человек за анонимной выставкой.',
    ar:'<em>05 — اذهب إلى الجحيم، اتركني وحدي.</em> سيرة ذاتية. الشخص خلف المعرض المجهول.',
    hi:'<em>05 — भाड़ में जाओ, मुझे अकेला छोड़ो।</em> एक आत्मकथा। गुमनाम प्रदर्शनी के पीछे का व्यक्ति।'
  },
  records_outro: {
    en:'The Records are not polished. They are not organised. They are not safe. Start here if you want the truth before it learned to dress itself.',
    es:'Los Registros no están pulidos. No están organizados. No son seguros. Empieza aquí si quieres la verdad antes de que aprendiera a vestirse.',
    fr:'Les Enregistrements ne sont pas polis. Ils ne sont pas organisés. Ils ne sont pas sûrs. Commence ici si tu veux la vérité avant qu\'elle n\'apprenne à s\'habiller.',
    de:'Die Aufzeichnungen sind nicht poliert. Sie sind nicht geordnet. Sie sind nicht sicher. Beginne hier, wenn du die Wahrheit willst, bevor sie lernte, sich anzuziehen.',
    pt:'Os Registros não são polidos. Não são organizados. Não são seguros. Comece aqui se quiser a verdade antes que ela aprendesse a se vestir.',
    nl:'De Verslagen zijn niet gepolijst. Ze zijn niet georganiseerd. Ze zijn niet veilig. Begin hier als je de waarheid wilt voordat die leerde zich aan te kleden.',
    it:'I Registri non sono rifiniti. Non sono organizzati. Non sono sicuri. Inizia qui se vuoi la verità prima che imparasse a vestirsi.',
    zh:'这些记录没有打磨。没有组织。不安全。如果你想要真相在学会打扮自己之前的样子，从这里开始。',
    ja:'記録は磨かれていない。整理されていない。安全でもない。真実が身なりを整える前の姿が欲しければ、ここから始めろ。',
    ko:'기록은 다듬어지지 않았다. 정리되지도 않았다. 안전하지도 않다. 진실이 옷 입는 법을 배우기 전의 모습을 원한다면, 여기서 시작하라.',
    ru:'Записи не отполированы. Не организованы. Не безопасны. Начни здесь, если хочешь правду до того, как она научилась одеваться.',
    ar:'السجلّات ليست مصقولة. ليست منظّمة. ليست آمنة. ابدأ هنا إن أردت الحقيقة قبل أن تتعلّم كيف ترتدي ثيابها.',
    hi:'अभिलेख चमकाए नहीं गए हैं। व्यवस्थित नहीं हैं। सुरक्षित नहीं हैं। यदि आप सत्य को उसके कपड़े पहनना सीखने से पहले चाहते हैं, तो यहाँ से शुरू करें।'
  },
  // Record titles in dl-list
  rec01_title:{es:'01 Las Tijeras',fr:'01 Les Ciseaux',de:'01 Die Schere',pt:'01 A Tesoura',nl:'01 De Schaar',it:'01 Le Forbici',zh:'01 剪刀',ja:'01 鋏',ko:'01 가위',ru:'01 Ножницы',ar:'01 المقصّ',hi:'01 कैंची'},
  rec02_title:{es:'02 El Viento',fr:'02 Le Vent',de:'02 Der Wind',pt:'02 O Vento',nl:'02 De Wind',it:'02 Il Vento',zh:'02 风',ja:'02 風',ko:'02 바람',ru:'02 Ветер',ar:'02 الريح',hi:'02 हवा'},
  rec03_title:{es:'03 ¿Estás Seguro?',fr:'03 Es-tu Certain ?',de:'03 Bist Du Sicher?',pt:'03 Tem Certeza?',nl:'03 Weet Je Het Zeker?',it:'03 Sei Certo?',zh:'03 你确定吗？',ja:'03 確かか？',ko:'03 확실한가?',ru:'03 Ты Уверен?',ar:'03 هل أنت متأكد؟',hi:'03 क्या आप निश्चित हैं?'},
  rec04_title:{es:"04 No Seas Hijo de Puta, Sé Amable",fr:'04 Ne Sois Pas un Connard, Sois Gentil',de:'04 Sei Kein Arschloch, Sei Nett',pt:'04 Não Seja Babaca, Seja Gentil',nl:'04 Wees Geen Klootzak, Wees Aardig',it:'04 Non Essere Uno Stronzo, Sii Gentile',zh:'04 别当混蛋，善良点',ja:'04 クソ野郎になるな、優しくしろ',ko:'04 개자식이 되지 마라, 친절하라',ru:'04 Не Будь Мудаком, Будь Добрым',ar:'04 لا تكن وغدًا، كن لطيفًا',hi:'04 गंदे मत बनो, दयालु बनो'},
  rec05_title:{es:'05 Vete a la Mierda, Déjame en Paz',fr:'05 Va Te Faire Foutre, Laisse-Moi Tranquille',de:'05 Verpiss Dich, Lass Mich in Ruhe',pt:'05 Vai Se Foder, Me Deixa em Paz',nl:'05 Rot Op, Laat Me Met Rust',it:'05 Vaffanculo, Lasciami in Pace',zh:'05 滚开，别烦我',ja:'05 くたばれ、ほっとけ',ko:'05 꺼져, 나 혼자 놔둬',ru:'05 Пошёл К Чёрту, Оставь Меня в Покое',ar:'05 اذهب إلى الجحيم، اتركني وحدي',hi:'05 भाड़ में जाओ, मुझे अकेला छोड़ो'}
};

LANGS.forEach(lang => {
  const fp = path.join('C:/Users/info/the420code', lang, 'index.html');
  let h = fs.readFileSync(fp, 'utf8');
  let c = 0;

  // Descriptions
  for (const key of ['records_intro','rec01_desc','rec02_desc','rec03_desc','rec04_desc','rec05_desc','records_outro']) {
    if (h.includes(R[key].en)) { h = h.replace(R[key].en, R[key][lang]); c++; }
  }

  // Titles in dl-list
  const titlePairs = [
    ['01 The Scissors','rec01_title'],
    ['02 The Wind','rec02_title'],
    ['03 Are You Certain','rec03_title'],
    ["04 Don't Be a Cunt Be Kind",'rec04_title'],
    ['05 Fuck You Leave Me-I Alone','rec05_title']
  ];
  for (const [en, key] of titlePairs) {
    if (h.includes(en + ' <span')) { h = h.replace(en + ' <span', R[key][lang] + ' <span'); c++; }
  }

  fs.writeFileSync(fp, h);
  console.log('  ' + lang + ' — ' + c + ' records changes');
});
console.log('Done');
