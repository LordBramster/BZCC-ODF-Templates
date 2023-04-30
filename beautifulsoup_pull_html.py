import requests
from bs4 import BeautifulSoup


def write_o(filename, content):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(content)
        f.close()
        print(f'SAVED :: {filename}.')


URL = "https://steamcommunity.com/sharedfiles/filedetails/?id=1423355866"
html_save_as = './src/steam_guide_odf_doc.html'

try:
    r = requests.get(URL)
    print(f'RESPONSE :: {r}')
    soup_html = BeautifulSoup(r.content, 'html5lib')
    print(f'HTML DONE.')
    write_o(html_save_as, str(soup_html))
except Exception as web_err:
    print(web_err)
