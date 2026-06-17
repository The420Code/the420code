import win32com.client, os

SRC = r'C:\Users\info\Downloads\files(96)'
DST = r'C:\Users\info\the420code'

files = {
    'AP20_ZH.docx': 'AP20_ZH.pdf',
    'AP20_JA.docx': 'AP20_JA.pdf',
    'AP20_KO.docx': 'AP20_KO.pdf',
    'AP20_AR.docx': 'AP20_AR.pdf',
    'AP20_HI.docx': 'AP20_HI.pdf',
}

word = win32com.client.Dispatch('Word.Application')
word.Visible = False

for docx, pdf in files.items():
    src = os.path.join(SRC, docx)
    dst = os.path.join(DST, pdf)
    doc = word.Documents.Open(src)
    doc.SaveAs(dst, FileFormat=17)
    doc.Close()
    print(f'  OK {pdf}')

word.Quit()
print('Done')
