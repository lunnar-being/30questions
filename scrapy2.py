# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:15:18 2020

@author: 19000
"""

import requests
from bs4 import BeautifulSoup
num_li=[4,71,1,231,158,118,50,282,112,263,339,281,266,96,236,69,546,791,58,116,977,122,617,160,
        266,110,59,41,133,734]
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"
    }
f=open("pa.txt","w",encoding="utf-8")
for num,i in enumerate(num_li,start=1):
    response=requests.get("https://codeforces.com/problemset/problem/"+str(i)+"/A",headers=headers)
    html=response.text
    soup=BeautifulSoup(html,"lxml")
    f.write("第"+str(num)+"个题目")
    f.write("\n")
    f.write(soup.find("div",attrs={"class":"title"}).get_text())
    f.write("\n")
    for p in soup.find_all("p"):
        f.write(p.get_text())
        f.write("\n")
f.close()

