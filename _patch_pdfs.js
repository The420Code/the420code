const fs = require('fs');
const path = require('path');
const LANGS = ['es','fr','de','pt','nl','it','zh','ja','ko','ru','ar','hi'];

const BOOK_PDF = {
  de: { file: 'Die_Illusion_des_Anderen.pdf', title: 'Die Illusion des Anderen' },
  fr: { file: 'L_Illusion_de_l_Autre.pdf', title: "L'Illusion de l'Autre" },
};

LANGS.forEach(lang => {
  const fp = path.join('.', lang, 'index.html');
  let h = fs.readFileSync(fp, 'utf8');

  if (BOOK_PDF[lang]) {
    const b = BOOK_PDF[lang];
    // Replace href="#" with localised PDF
    h = h.split('href="#">The Illusion of the Other').join('href="../' + b.file + '">' + b.title);
  } else {
    // Link to English PDF
    h = h.split('href="#">The Illusion of the Other').join('href="../Illusion_of_the_Other.pdf">The Illusion of the Other');
  }

  fs.writeFileSync(fp, h);
  console.log('  ' + lang + ' — PDF link set');
});
console.log('Done');
