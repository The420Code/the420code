import ftplib
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HOST = 'dedi1950.jnb1.host-h.net'
USER = 'thecoujhwu'
PASS = 'K67KIzaBzZxTMqX14e36'

ftp = ftplib.FTP(HOST, timeout=30, encoding='latin-1')
ftp.login(USER, PASS)
print('Connected')

path = '/public_html/wp-content/uploads/2026/03'
files = ftp.nlst(path)
for f in files:
    basename = f.split('/')[-1]
    if basename in ('.', '..'):
        continue
    try:
        ftp.delete(f)
        print(f'DEL: {basename}')
    except Exception as e:
        print(f'FAIL: {e}')

for d in [path, '/public_html/wp-content/uploads/2026', '/public_html/wp-content/uploads', '/public_html/wp-content']:
    try:
        ftp.rmd(d)
        print(f'RMDIR: {d}')
    except Exception as e:
        print(f'FAIL {d}: {e}')

print('Done!')
ftp.quit()
