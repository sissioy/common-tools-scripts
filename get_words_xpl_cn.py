# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re

def read_list():
    words = []
    with open('2022-05-29-六级.txt',encoding='utf-8') as f:
        words = f.read().splitlines()
    return words

def look_up(words):
    # try:
    for word in words:
        try:
            url = r'https://dict.youdao.com/w/eng/{}'.format(word)
            ### <div class="trans-container"> # <ul> # <li>
            html=requests.get(url,timeout=30).text
            # print(html)
            soup = BeautifulSoup(html,"html.parser")
            rough_meaning = soup.find('div',class_="trans-container")
            # print(rough_meaning)
            a = rough_meaning.find('ul').find('li').get_text()
            
            pattern=r'^.*?；.*?；'
            try:
                meaning = re.match(pattern,a)
                write_txt('{}\t{}\n'.format(word,meaning.group()))
            except:
                write_txt('{}\t{}\n'.format(word,a))
                
        except:
            print("Oops, {} is wrong".format(word))

def write_txt(line):
    with open('2022-05-29-wAm.txt','a+') as f:
        f.write(line)

if __name__=="__main__":
    # look_up(['hello'])
    look_up(read_list())
    # print(read_list())
