# coding=utf-8
from urllib import request
import re
from pymystem3 import Mystem

url = "http://web-corpora.net/Test2_2016/short_story.html"
output = request.urlopen(url).read().decode("utf-8") 


result = re.findall('\s[сС][а-я]*', output)

set_res = set(result)
for item in set_res:
    print(item)

print('------Конец первого задания ---------')

mystem = Mystem()
verbs = mystem.analyze(''.join(set_res))
for item in verbs:
    if('analysis' in item):
        if (item['analysis'][0]['gr'][0] == 'V'):
          print(item['text'])

print('------Конец второго задания ---------')
