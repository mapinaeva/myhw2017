# coding=utf-8
from urllib import request
import re

url = "http://web-corpora.net/Test2_2016/short_story.html"
output = request.urlopen(url).read().decode("utf-8") 


result = re.findall('\s[сС][а-я]*', output)

for item in result:
    print(item)



