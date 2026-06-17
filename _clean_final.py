import ftplib
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HOST = 'dedi1950.jnb1.host-h.net'
USER = 'thecoujhwu'
PASS = 'K67KIzaBzZxTMqX14e36'

# Try UTF-8 encoding
ftp = ftplib.FTP(HOST, timeout=30, encoding='utf-8')
ftp.login(USER, PASS)
print('Connected with UTF-8')

path = '/public_html/wp-content/uploads/2026/03'

# Get raw listing
lines = []
ftp.retrlines('NLST ' + path, lines.append)
for f in lines:
    basename = f.split('/')[-1]
    if basename in ('.', '..'):
        continue
    print(f'Trying: {repr(f)}')
    try:
        ftp.delete(f)
        print(f'  DEL OK')
    except Exception as e:
        # Try sending raw command
        try:
            ftp.sendcmd('DELE ' + f)
            print(f'  RAW DEL OK')
        except Exception as e2:
            print(f'  FAIL: {e2}')

for d in [path, '/public_html/wp-content/uploads/2026', '/public_html/wp-content/uploads', '/public_html/wp-content']:
    try:
        ftp.rmd(d)
        print(f'RMDIR: {d}')
    except Exception as e:
        print(f'FAIL {d}: {e}')

ftp.quit()
