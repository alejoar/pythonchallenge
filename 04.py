# coding: utf-8
import requests
import re

def follow_chain(url):
    nothing = "12345"
    i = 1
    while True:
        try:
            res = requests.get(url)
            nothing = re.findall('and the next nothing is ((?s).*)', res.text)[0]
            url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}'
            print(res.text, '->', url, f'({i})')
            i += 1
        except:
            print(url)
            print(res.text)
            break

follow_chain('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
follow_chain(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={16044 // 2}')