#!/bin/bash
cd "C:/Users/info/the420code"

do_lang() {
  local L=$1; shift
  local F="$L/index.html"
  while [ $# -ge 2 ]; do
    local EN="$1"; local TR="$2"; shift 2
    sed -i "s|ap-title\">$EN</span>|ap-title\">$TR</span>|g" "$F"
  done
  echo "  $L done"
}

do_lang es \
"The Irrational" "Lo Irracional" \
"The Actualization State" "El Estado de Actualización" \
"The Proof" "La Prueba" \
"The Ratio" "La Razón" \
"The Break — Electroweak" "La Ruptura — Electrodébil" \
"The Break — Empty Set" "La Ruptura — Conjunto Vacío" \
"The Break" "La Ruptura" \
"The Dimension" "La Dimensión" \
"The Identity" "La Identidad" \
"The Record Measure" "La Medida del Registro" \
"The Spin" "El Espín" \
"The Limit" "El Límite" \
"The Grain" "El Grano" \
"The Measure" "La Medida" \
"The Single Record" "El Registro Único" \
"The Leakage Constant" "La Constante de Fuga" \
"The Connection" "La Conexión" \
"The Harmonics" "Los Armónicos" \
"The Direction" "La Dirección" \
"The Residual" "El Residuo" \
"The Correction — Ethics" "La Corrección — Ética" \
"The Correction" "La Corrección" \
"The Constant" "La Constante" \
"The Resistance" "La Resistencia" \
"The Ledger" "El Libro Mayor" \
"The First Boundary" "El Primer Límite" \
"The Surplus" "El Excedente" \
"The Inversion" "La Inversión" \
"The Floor" "El Suelo" \
"The Clock" "El Reloj" \
"The Loop Hypothesis" "La Hipótesis del Bucle" \
"The Loop" "El Bucle" \
"The Room" "La Habitación" \
"The Scaffold" "El Andamio" \
"The Operator" "El Operador" \
"The Exit" "La Salida" \
"The Alignment" "La Alineación" \
"The Boundary" "El Límite" \
"The Actualization Proof" "La Prueba de Actualización" \
"The Feed" "La Alimentación" \
"The Web" "La Red" \
"The Curve" "La Curva" \
"The Scale" "La Escala"

do_lang fr \
"The Irrational" "L'Irrationnel" \
"The Actualization State" "L'État d'Actualisation" \
"The Proof" "La Preuve" \
"The Ratio" "Le Rapport" \
"The Break — Electroweak" "La Brisure — Électrofaible" \
"The Break — Empty Set" "La Brisure — Ensemble Vide" \
"The Break" "La Brisure" \
"The Dimension" "La Dimension" \
"The Identity" "L'Identité" \
"The Record Measure" "La Mesure du Record" \
"The Spin" "Le Spin" \
"The Limit" "La Limite" \
"The Grain" "Le Grain" \
"The Measure" "La Mesure" \
"The Single Record" "L'Enregistrement Unique" \
"The Leakage Constant" "La Constante de Fuite" \
"The Connection" "La Connexion" \
"The Harmonics" "Les Harmoniques" \
"The Direction" "La Direction" \
"The Residual" "Le Résidu" \
"The Correction — Ethics" "La Correction — Éthique" \
"The Correction" "La Correction" \
"The Constant" "La Constante" \
"The Resistance" "La Résistance" \
"The Ledger" "Le Registre" \
"The First Boundary" "La Première Frontière" \
"The Surplus" "Le Surplus" \
"The Inversion" "L'Inversion" \
"The Floor" "Le Plancher" \
"The Clock" "L'Horloge" \
"The Loop Hypothesis" "L'Hypothèse de la Boucle" \
"The Loop" "La Boucle" \
"The Room" "La Salle" \
"The Scaffold" "L'Échafaudage" \
"The Operator" "L'Opérateur" \
"The Exit" "La Sortie" \
"The Alignment" "L'Alignement" \
"The Boundary" "La Frontière" \
"The Actualization Proof" "La Preuve d'Actualisation" \
"The Feed" "L'Alimentation" \
"The Web" "Le Réseau" \
"The Curve" "La Courbe" \
"The Scale" "L'Échelle"

do_lang de \
"The Irrational" "Das Irrationale" \
"The Actualization State" "Der Aktualisierungszustand" \
"The Proof" "Der Beweis" \
"The Ratio" "Das Verhältnis" \
"The Break — Electroweak" "Der Bruch — Elektroschwach" \
"The Break — Empty Set" "Der Bruch — Leere Menge" \
"The Break" "Der Bruch" \
"The Dimension" "Die Dimension" \
"The Identity" "Die Identität" \
"The Record Measure" "Das Record-Maß" \
"The Spin" "Der Spin" \
"The Limit" "Die Grenze" \
"The Grain" "Das Korn" \
"The Measure" "Das Maß" \
"The Single Record" "Der Einzelne Record" \
"The Leakage Constant" "Die Leckagekonstante" \
"The Connection" "Die Verbindung" \
"The Harmonics" "Die Harmonischen" \
"The Direction" "Die Richtung" \
"The Residual" "Das Residuum" \
"The Correction — Ethics" "Die Korrektur — Ethik" \
"The Correction" "Die Korrektur" \
"The Constant" "Die Konstante" \
"The Resistance" "Der Widerstand" \
"The Ledger" "Das Hauptbuch" \
"The First Boundary" "Die Erste Grenze" \
"The Surplus" "Der Überschuss" \
"The Inversion" "Die Umkehrung" \
"The Floor" "Der Boden" \
"The Clock" "Die Uhr" \
"The Loop Hypothesis" "Die Schleifen-Hypothese" \
"The Loop" "Die Schleife" \
"The Room" "Der Raum" \
"The Scaffold" "Das Gerüst" \
"The Operator" "Der Operator" \
"The Exit" "Der Ausgang" \
"The Alignment" "Die Ausrichtung" \
"The Boundary" "Die Grenze" \
"The Actualization Proof" "Der Aktualisierungsbeweis" \
"The Feed" "Die Zuführung" \
"The Web" "Das Netz" \
"The Curve" "Die Kurve" \
"The Scale" "Die Skala"

do_lang pt \
"The Irrational" "O Irracional" \
"The Actualization State" "O Estado de Atualização" \
"The Proof" "A Prova" \
"The Ratio" "A Razão" \
"The Break — Electroweak" "A Quebra — Eletrofraco" \
"The Break — Empty Set" "A Quebra — Conjunto Vazio" \
"The Break" "A Quebra" \
"The Dimension" "A Dimensão" \
"The Identity" "A Identidade" \
"The Record Measure" "A Medida do Registro" \
"The Spin" "O Spin" \
"The Limit" "O Limite" \
"The Grain" "O Grão" \
"The Measure" "A Medida" \
"The Single Record" "O Registro Único" \
"The Leakage Constant" "A Constante de Vazamento" \
"The Connection" "A Conexão" \
"The Harmonics" "Os Harmônicos" \
"The Direction" "A Direção" \
"The Residual" "O Resíduo" \
"The Correction — Ethics" "A Correção — Ética" \
"The Correction" "A Correção" \
"The Constant" "A Constante" \
"The Resistance" "A Resistência" \
"The Ledger" "O Livro-Razão" \
"The First Boundary" "O Primeiro Limite" \
"The Surplus" "O Excedente" \
"The Inversion" "A Inversão" \
"The Floor" "O Piso" \
"The Clock" "O Relógio" \
"The Loop Hypothesis" "A Hipótese do Laço" \
"The Loop" "O Laço" \
"The Room" "A Sala" \
"The Scaffold" "O Andaime" \
"The Operator" "O Operador" \
"The Exit" "A Saída" \
"The Alignment" "O Alinhamento" \
"The Boundary" "A Fronteira" \
"The Actualization Proof" "A Prova de Atualização" \
"The Feed" "A Alimentação" \
"The Web" "A Rede" \
"The Curve" "A Curva" \
"The Scale" "A Escala"

do_lang nl \
"The Irrational" "Het Irrationele" \
"The Actualization State" "De Actualisatietoestand" \
"The Proof" "Het Bewijs" \
"The Ratio" "De Verhouding" \
"The Break — Electroweak" "De Breuk — Elektrozwak" \
"The Break — Empty Set" "De Breuk — Lege Verzameling" \
"The Break" "De Breuk" \
"The Dimension" "De Dimensie" \
"The Identity" "De Identiteit" \
"The Record Measure" "De Recordmaat" \
"The Spin" "De Spin" \
"The Limit" "De Grens" \
"The Grain" "De Korrel" \
"The Measure" "De Maat" \
"The Single Record" "Het Enkele Record" \
"The Leakage Constant" "De Lekkageconstante" \
"The Connection" "De Verbinding" \
"The Harmonics" "De Harmonischen" \
"The Direction" "De Richting" \
"The Residual" "Het Residu" \
"The Correction — Ethics" "De Correctie — Ethiek" \
"The Correction" "De Correctie" \
"The Constant" "De Constante" \
"The Resistance" "De Weerstand" \
"The Ledger" "Het Grootboek" \
"The First Boundary" "De Eerste Grens" \
"The Surplus" "Het Overschot" \
"The Inversion" "De Inversie" \
"The Floor" "De Bodem" \
"The Clock" "De Klok" \
"The Loop Hypothesis" "De Lushypothese" \
"The Loop" "De Lus" \
"The Room" "De Kamer" \
"The Scaffold" "De Steiger" \
"The Operator" "De Operator" \
"The Exit" "De Uitgang" \
"The Alignment" "De Uitlijning" \
"The Boundary" "De Grens" \
"The Actualization Proof" "Het Actualisatiebewijs" \
"The Feed" "De Voeding" \
"The Web" "Het Web" \
"The Curve" "De Kromme" \
"The Scale" "De Schaal"

do_lang it \
"The Irrational" "L'Irrazionale" \
"The Actualization State" "Lo Stato di Attualizzazione" \
"The Proof" "La Prova" \
"The Ratio" "Il Rapporto" \
"The Break — Electroweak" "La Rottura — Elettrodebole" \
"The Break — Empty Set" "La Rottura — Insieme Vuoto" \
"The Break" "La Rottura" \
"The Dimension" "La Dimensione" \
"The Identity" "L'Identità" \
"The Record Measure" "La Misura del Record" \
"The Spin" "Lo Spin" \
"The Limit" "Il Limite" \
"The Grain" "Il Grano" \
"The Measure" "La Misura" \
"The Single Record" "Il Record Singolo" \
"The Leakage Constant" "La Costante di Perdita" \
"The Connection" "La Connessione" \
"The Harmonics" "Le Armoniche" \
"The Direction" "La Direzione" \
"The Residual" "Il Residuo" \
"The Correction — Ethics" "La Correzione — Etica" \
"The Correction" "La Correzione" \
"The Constant" "La Costante" \
"The Resistance" "La Resistenza" \
"The Ledger" "Il Registro" \
"The First Boundary" "Il Primo Confine" \
"The Surplus" "Il Surplus" \
"The Inversion" "L'Inversione" \
"The Floor" "Il Pavimento" \
"The Clock" "L'Orologio" \
"The Loop Hypothesis" "L'Ipotesi del Ciclo" \
"The Loop" "Il Ciclo" \
"The Room" "La Stanza" \
"The Scaffold" "L'Impalcatura" \
"The Operator" "L'Operatore" \
"The Exit" "L'Uscita" \
"The Alignment" "L'Allineamento" \
"The Boundary" "Il Confine" \
"The Actualization Proof" "La Prova di Attualizzazione" \
"The Feed" "L'Alimentazione" \
"The Web" "La Rete" \
"The Curve" "La Curva" \
"The Scale" "La Scala"

do_lang zh \
"The Irrational" "无理数" \
"The Actualization State" "实现态" \
"The Proof" "证明" \
"The Ratio" "比率" \
"The Break — Electroweak" "断裂 — 电弱" \
"The Break — Empty Set" "断裂 — 空集" \
"The Break" "断裂" \
"The Dimension" "维度" \
"The Identity" "恒等式" \
"The Record Measure" "记录测度" \
"The Spin" "自旋" \
"The Limit" "极限" \
"The Grain" "颗粒" \
"The Measure" "测度" \
"The Single Record" "单一记录" \
"The Leakage Constant" "泄漏常数" \
"The Connection" "连接" \
"The Harmonics" "谐波" \
"The Direction" "方向" \
"The Residual" "残余" \
"The Correction — Ethics" "修正 — 伦理" \
"The Correction" "修正" \
"The Constant" "常数" \
"The Resistance" "阻力" \
"The Ledger" "账簿" \
"The First Boundary" "第一边界" \
"The Surplus" "盈余" \
"The Inversion" "反转" \
"The Floor" "底限" \
"The Clock" "时钟" \
"The Loop Hypothesis" "循环假说" \
"The Loop" "循环" \
"The Room" "房间" \
"The Scaffold" "脚手架" \
"The Operator" "算子" \
"The Exit" "出口" \
"The Alignment" "对齐" \
"The Boundary" "边界" \
"The Actualization Proof" "实现证明" \
"The Feed" "供给" \
"The Web" "网络" \
"The Curve" "曲线" \
"The Scale" "标度"

do_lang ja \
"The Irrational" "無理数" \
"The Actualization State" "実現状態" \
"The Proof" "証明" \
"The Ratio" "比率" \
"The Break — Electroweak" "破れ — 電弱" \
"The Break — Empty Set" "破れ — 空集合" \
"The Break" "破れ" \
"The Dimension" "次元" \
"The Identity" "恒等式" \
"The Record Measure" "記録測度" \
"The Spin" "スピン" \
"The Limit" "極限" \
"The Grain" "粒" \
"The Measure" "測度" \
"The Single Record" "単一記録" \
"The Leakage Constant" "漏洩定数" \
"The Connection" "接続" \
"The Harmonics" "調和" \
"The Direction" "方向" \
"The Residual" "残余" \
"The Correction — Ethics" "補正 — 倫理" \
"The Correction" "補正" \
"The Constant" "定数" \
"The Resistance" "抵抗" \
"The Ledger" "台帳" \
"The First Boundary" "第一境界" \
"The Surplus" "余剰" \
"The Inversion" "反転" \
"The Floor" "床" \
"The Clock" "時計" \
"The Loop Hypothesis" "ループ仮説" \
"The Loop" "ループ" \
"The Room" "部屋" \
"The Scaffold" "足場" \
"The Operator" "作用素" \
"The Exit" "出口" \
"The Alignment" "整列" \
"The Boundary" "境界" \
"The Actualization Proof" "実現証明" \
"The Feed" "供給" \
"The Web" "網" \
"The Curve" "曲線" \
"The Scale" "スケール"

do_lang ko \
"The Irrational" "무리수" \
"The Actualization State" "실현 상태" \
"The Proof" "증명" \
"The Ratio" "비율" \
"The Break — Electroweak" "깨짐 — 전약" \
"The Break — Empty Set" "깨짐 — 공집합" \
"The Break" "깨짐" \
"The Dimension" "차원" \
"The Identity" "항등식" \
"The Record Measure" "기록 측도" \
"The Spin" "스핀" \
"The Limit" "극한" \
"The Grain" "입자" \
"The Measure" "측도" \
"The Single Record" "단일 기록" \
"The Leakage Constant" "누출 상수" \
"The Connection" "연결" \
"The Harmonics" "조화" \
"The Direction" "방향" \
"The Residual" "잔여" \
"The Correction — Ethics" "보정 — 윤리" \
"The Correction" "보정" \
"The Constant" "상수" \
"The Resistance" "저항" \
"The Ledger" "원장" \
"The First Boundary" "첫 번째 경계" \
"The Surplus" "잉여" \
"The Inversion" "역전" \
"The Floor" "바닥" \
"The Clock" "시계" \
"The Loop Hypothesis" "순환 가설" \
"The Loop" "순환" \
"The Room" "방" \
"The Scaffold" "비계" \
"The Operator" "작용소" \
"The Exit" "출구" \
"The Alignment" "정렬" \
"The Boundary" "경계" \
"The Actualization Proof" "실현 증명" \
"The Feed" "공급" \
"The Web" "그물" \
"The Curve" "곡선" \
"The Scale" "척도"

do_lang ru \
"The Irrational" "Иррациональное" \
"The Actualization State" "Состояние актуализации" \
"The Proof" "Доказательство" \
"The Ratio" "Соотношение" \
"The Break — Electroweak" "Разрыв — Электрослабый" \
"The Break — Empty Set" "Разрыв — Пустое множество" \
"The Break" "Разрыв" \
"The Dimension" "Размерность" \
"The Identity" "Тождество" \
"The Record Measure" "Мера записи" \
"The Spin" "Спин" \
"The Limit" "Предел" \
"The Grain" "Зерно" \
"The Measure" "Мера" \
"The Single Record" "Единственная запись" \
"The Leakage Constant" "Константа утечки" \
"The Connection" "Связь" \
"The Harmonics" "Гармоники" \
"The Direction" "Направление" \
"The Residual" "Остаток" \
"The Correction — Ethics" "Поправка — Этика" \
"The Correction" "Поправка" \
"The Constant" "Константа" \
"The Resistance" "Сопротивление" \
"The Ledger" "Реестр" \
"The First Boundary" "Первая граница" \
"The Surplus" "Избыток" \
"The Inversion" "Инверсия" \
"The Floor" "Основание" \
"The Clock" "Часы" \
"The Loop Hypothesis" "Гипотеза петли" \
"The Loop" "Петля" \
"The Room" "Комната" \
"The Scaffold" "Леса" \
"The Operator" "Оператор" \
"The Exit" "Выход" \
"The Alignment" "Выравнивание" \
"The Boundary" "Граница" \
"The Actualization Proof" "Доказательство актуализации" \
"The Feed" "Подача" \
"The Web" "Сеть" \
"The Curve" "Кривая" \
"The Scale" "Масштаб"

do_lang ar \
"The Irrational" "اللاعقلاني" \
"The Actualization State" "حالة التحقّق" \
"The Proof" "البرهان" \
"The Ratio" "النسبة" \
"The Break — Electroweak" "الكسر — الكهروضعيف" \
"The Break — Empty Set" "الكسر — المجموعة الفارغة" \
"The Break" "الكسر" \
"The Dimension" "البُعد" \
"The Identity" "الهوية" \
"The Record Measure" "قياس السجلّ" \
"The Spin" "اللَّف" \
"The Limit" "الحدّ" \
"The Grain" "الحبّة" \
"The Measure" "القياس" \
"The Single Record" "السجلّ الواحد" \
"The Leakage Constant" "ثابت التسرّب" \
"The Connection" "الوصلة" \
"The Harmonics" "التوافقيات" \
"The Direction" "الاتجاه" \
"The Residual" "المتبقّي" \
"The Correction — Ethics" "التصحيح — الأخلاق" \
"The Correction" "التصحيح" \
"The Constant" "الثابت" \
"The Resistance" "المقاومة" \
"The Ledger" "السجلّ" \
"The First Boundary" "الحدّ الأول" \
"The Surplus" "الفائض" \
"The Inversion" "الانعكاس" \
"The Floor" "الأرضية" \
"The Clock" "الساعة" \
"The Loop Hypothesis" "فرضية الحلقة" \
"The Loop" "الحلقة" \
"The Room" "الغرفة" \
"The Scaffold" "السقالة" \
"The Operator" "المُشغِّل" \
"The Exit" "المخرج" \
"The Alignment" "المحاذاة" \
"The Boundary" "الحدود" \
"The Actualization Proof" "برهان التحقّق" \
"The Feed" "التغذية" \
"The Web" "الشبكة" \
"The Curve" "المنحنى" \
"The Scale" "المقياس"

do_lang hi \
"The Irrational" "अपरिमेय" \
"The Actualization State" "साक्षात्कार अवस्था" \
"The Proof" "प्रमाण" \
"The Ratio" "अनुपात" \
"The Break — Electroweak" "टूट — विद्युतदुर्बल" \
"The Break — Empty Set" "टूट — रिक्त समुच्चय" \
"The Break" "टूट" \
"The Dimension" "आयाम" \
"The Identity" "सर्वसमिका" \
"The Record Measure" "अभिलेख माप" \
"The Spin" "स्पिन" \
"The Limit" "सीमा" \
"The Grain" "कण" \
"The Measure" "माप" \
"The Single Record" "एकल अभिलेख" \
"The Leakage Constant" "रिसाव स्थिरांक" \
"The Connection" "संयोजन" \
"The Harmonics" "स्वरक" \
"The Direction" "दिशा" \
"The Residual" "अवशेष" \
"The Correction — Ethics" "सुधार — नैतिकता" \
"The Correction" "सुधार" \
"The Constant" "स्थिरांक" \
"The Resistance" "प्रतिरोध" \
"The Ledger" "बही-खाता" \
"The First Boundary" "पहली सीमा" \
"The Surplus" "अधिशेष" \
"The Inversion" "उलटाव" \
"The Floor" "तल" \
"The Clock" "घड़ी" \
"The Loop Hypothesis" "लूप परिकल्पना" \
"The Loop" "लूप" \
"The Room" "कमरा" \
"The Scaffold" "मचान" \
"The Operator" "प्रचालक" \
"The Exit" "निकास" \
"The Alignment" "संरेखण" \
"The Boundary" "सीमा" \
"The Actualization Proof" "साक्षात्कार प्रमाण" \
"The Feed" "आपूर्ति" \
"The Web" "जाल" \
"The Curve" "वक्र" \
"The Scale" "पैमाना"

echo "All done"
