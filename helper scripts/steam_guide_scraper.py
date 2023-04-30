import requests
from bs4 import BeautifulSoup

URL = "https://steamcommunity.com/sharedfiles/filedetails/?id=1423355866"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

"""
WIP
"""
