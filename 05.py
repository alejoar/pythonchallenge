# coding: utf-8
import requests
res = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
import pickle
data = pickle.loads(res.content)
for item in data:
    print(''.join([tup[0]*tup[1] for tup in item]))
