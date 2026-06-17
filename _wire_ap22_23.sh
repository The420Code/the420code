#!/bin/bash
cd "C:/Users/info/the420code"

LANGS="es fr de pt nl it zh ja ko ru ar hi"
declare -A REQ_LABELS
REQ_LABELS[es]="Requiere" REQ_LABELS[fr]="Requiert" REQ_LABELS[de]="Erfordert"
REQ_LABELS[pt]="Requer" REQ_LABELS[nl]="Vereist" REQ_LABELS[it]="Richiede"
REQ_LABELS[zh]="依赖" REQ_LABELS[ja]="前提" REQ_LABELS[ko]="필요"
REQ_LABELS[ru]="Требует" REQ_LABELS[ar]="يتطلب" REQ_LABELS[hi]="आवश्यक"

for L in $LANGS; do
  F="$L/index.html"
  R="${REQ_LABELS[$L]}"

  # AP22 header PDF
  sed -i "s|ap-pdf\" href=\"../AP22_The_Ledger.pdf\"|ap-pdf\" href=\"../AP22_The_Ledger_${L^^}.pdf\"|" "$F"
  # AP22 meta PDF (Requires: AP09, AP11, AP20)
  sed -i "s|${R}: AP09, AP11, AP20</span><a href=\"#\"|${R}: AP09, AP11, AP20</span><a href=\"../AP22_The_Ledger_${L^^}.pdf\"|" "$F"

  # AP23 header PDF
  sed -i "s|ap-pdf\" href=\"../AP23_The_Single_Record.pdf\"|ap-pdf\" href=\"../AP23_The_Single_Record_${L^^}.pdf\"|" "$F"
  # AP23 meta PDF (Requires: AP07, AP09, AP25)
  sed -i "s|${R}: AP07, AP09, AP25</span><a href=\"#\"|${R}: AP07, AP09, AP25</span><a href=\"../AP23_The_Single_Record_${L^^}.pdf\"|" "$F"

  echo "  $L wired"
done
echo "All done"
