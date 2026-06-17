import win32com.client
import os, sys, time, glob

SRC = r"C:\Users\info\OneDrive\00 - publish on line"
DST = r"C:\Users\info\the420code"

# Map AP number to clean filename
AP_NAMES = {
    'AP01': 'AP01_The_Actualization_State',
    'AP02': 'AP02_The_Operator',
    'AP03': 'AP03_The_Ratio',
    'AP04': 'AP04_The_Loop_Hypothesis',
    'AP05': 'AP05_The_Break',
    'AP06': 'AP06_The_Leakage_Constant',
    'AP07': 'AP07_The_Record_Measure',
    'AP08': 'AP08_The_Identity',
    'AP09': 'AP09_The_Break_Empty_Set',
    'AP10': 'AP10_The_Dimension',
    'AP11': 'AP11_The_Spin',
    'AP12': 'AP12_The_Limit',
    'AP13': 'AP13_The_Grain',
    'AP14': 'AP14_The_Correction',
    'AP15': 'AP15_The_Connection',
    'AP16': 'AP16_The_Break_Electroweak',
    'AP17': 'AP17_The_Room',
    'AP18': 'AP18_The_Floor',
    'AP19': 'AP19_The_Direction',
    'AP20': 'AP20_The_Proof',
    'AP21': 'AP21_The_Web',
    'AP22': 'AP22_The_Ledger',
    'AP23': 'AP23_The_Single_Record',
    'AP24': 'AP24_The_Residual',
    'AP25': 'AP25_The_Measure',
    'AP26': 'AP26_The_Surplus',
    'AP27': 'AP27_The_Harmonics',
    'AP28': 'AP28_The_Constant',
    'AP29': 'AP29_The_Actualization_Proof',
    'AP30': 'AP30_The_Resistance',
    'AP31': 'AP31_The_Alignment',
    'AP32': 'AP32_The_Correction_Ethics',
    'AP33': 'AP33_The_Boundary',
    'AP34': 'AP34_The_Inversion',
    'AP35': 'AP35_The_Ledger_Economics',
    'AP36': 'AP36_The_Feed',
    'AP37': 'AP37_The_First_Boundary',
    'AP38': 'AP38_The_Exit',
    'AP39': 'AP39_The_Scaffold',
    'AP40': 'AP40_The_Irrational',
    'AP41': 'AP41_The_Loop',
    'AP42': 'AP42_The_Clock',
}

# Find all AP docx files
docx_files = glob.glob(os.path.join(SRC, "AP*.docx"))

# Skip AP01 and AP02 (already have PDFs)
skip = ['AP01', 'AP02']

word = win32com.client.Dispatch("Word.Application")
word.Visible = False

converted = 0
skipped = 0

for docx in sorted(docx_files):
    basename = os.path.basename(docx)
    ap_num = basename[:4]

    if ap_num in skip:
        print(f"  SKIP {ap_num} (already has PDF)")
        skipped += 1
        continue

    if ap_num not in AP_NAMES:
        print(f"  SKIP {basename} (unknown AP)")
        continue

    out_name = AP_NAMES[ap_num] + '.pdf'
    out_path = os.path.join(DST, out_name)

    if os.path.exists(out_path):
        print(f"  EXISTS {out_name}")
        skipped += 1
        continue

    try:
        doc = word.Documents.Open(docx)
        doc.SaveAs(out_path, FileFormat=17)  # 17 = wdFormatPDF
        doc.Close()
        print(f"  OK {out_name}")
        converted += 1
    except Exception as e:
        print(f"  FAIL {ap_num}: {e}")

word.Quit()
print(f"\nDone: {converted} converted, {skipped} skipped")
