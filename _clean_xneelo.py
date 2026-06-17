import ftplib
import sys

HOST = 'dedi1950.jnb1.host-h.net'
USER = 'thecoujhwu'
PASS = 'K67KIzaBzZxTMqX14e36'

def rm_recursive(ftp, path):
    """Recursively delete a directory tree"""
    try:
        # Try to list contents (it's a directory)
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
            full = path + '/' + name
            if entry_type == 'dir':
                rm_recursive(ftp, full)
            else:
                print(f'  DEL {full}')
                ftp.delete(full)
        print(f'  RMDIR {path}')
        ftp.rmd(path)
    except Exception as e:
        # Maybe not a dir, try delete as file
        try:
            ftp.delete(path)
            print(f'  DEL {path}')
        except Exception as e2:
            print(f'  FAIL {path}: {e2}')

ftp = ftplib.FTP(HOST, timeout=30)
ftp.login(USER, PASS)
print('Connected to', HOST)

# List public_html
print('\n=== public_html contents ===')
entries = []
ftp.retrlines('MLSD /public_html', entries.append)

for entry in entries:
    parts = entry.split(';')
    name = parts[-1].strip()
    if name in ('.', '..'):
        continue
    full = '/public_html/' + name
    print(f'\nRemoving: {full}')
    entry_type = ''
    for p in parts:
        if p.strip().lower().startswith('type='):
            entry_type = p.strip().split('=')[1].lower()
    if entry_type == 'dir':
        rm_recursive(ftp, full)
    else:
        ftp.delete(full)
        print(f'  DEL {full}')

# Also remove backup tarballs from root
print('\n=== Cleaning root backups ===')
root_entries = []
ftp.retrlines('MLSD /', root_entries.append)
for entry in root_entries:
    parts = entry.split(';')
    name = parts[-1].strip()
    if name.startswith('app_installer_backup'):
        print(f'Removing: /{name}')
        ftp.delete('/' + name)

print('\nDone!')
ftp.quit()
