from collections import deque
import re
from bs4 import BeautifulSoup
import requests
import urllib.parse
import pyfiglet

def crawl_emails(start_url, max_pages):
    urls = deque([start_url])
    scraped_urls = set()
    emails = set()
    count = 0

    while urls and count < max_pages:
        url = urls.popleft()
        if url in scraped_urls:
            continue
        scraped_urls.add(url)
        count += 1
        print(f'{count} Sedang Membaca {url}')

        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        # Cari email menggunakan regex
        new_emails = set(re.findall(r'[a-z0-9\.\-+_]+@\w+\.[a-z\.]+', response.text, re.I))
        emails.update(new_emails)

        # Cari link-link baru menggunakan BeautifulSoup dan bentuk URL absolut
        soup = BeautifulSoup(response.text, 'html.parser')
        for anchor in soup.find_all('a', href=True):
            link = anchor['href']
            full_link = urllib.parse.urljoin(url, link)
            if full_link not in scraped_urls and full_link not in urls:
                urls.append(full_link)
                
    return emails

def main():
    print(pyfiglet.figlet_format("RED--CHIKA", font="slant"))
    start_url = input('[+] Silahkan Masukan URL : ')
    max_pages = int(input('[+] Masukan Jumlah Halaman Yang Akan Dibaca : '))
    
    try:
        emails = crawl_emails(start_url, max_pages)
    except KeyboardInterrupt:
        print('[-] Closing!!')
        return

    print('\nHacking Successful!')
    print(f'\n{len(emails)} email ditemukan\n====================================')
    for email in emails:
        print('  ' + email)
    print()

if __name__ == '__main__':
    main()
