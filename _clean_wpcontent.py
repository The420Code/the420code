import ftplib

HOST = 'dedi1950.jnb1.host-h.net'
USER = 'thecoujhwu'
PASS = 'K67KIzaBzZxTMqX14e36'

def rm_recursive(ftp, path):
    try:
        entries = []
        ftp.retrlines('MLSD ' + path, entries.append)
        for entry in entries:
            parts = entry.split(';')
            name = parts[-1].strip()
            if name in ('.', '..'):
                continue
            entry_type = ''
            for p in parts:
                if p.strip().lower().startswith('type='):
                    entry_type = p.strip().split('=')[1].lower()
            full = path.rstrip('/') + '/' + name
            if entry_type == 'dir':
                rm_recursive(ftp, full)
            else:
                ftp.delete(full)
                print(f'  DEL {full}')
        ftp.rmd(path)
        print(f'  RMDIR {path}')
    except Exception as e:
        print(f'  FAIL {path}: {e}')

ftp = ftplib.FTP(HOST, timeout=30)
ftp.login(USER, PASS)
print('Connected')
rm_recursive(ftp, '/public_html/wp-content')
print('Done!')
ftp.quit()
