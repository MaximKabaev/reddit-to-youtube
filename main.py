import requests
import json
import pyttsx3
import os
from PIL import Image
from selenium import webdriver
from io import BytesIO
engine = pyttsx3.init()

import time

post_num = 4

r = requests.get("https://www.reddit.com/r/askreddit/top/.json?limit=5?t=day", headers = {'User-agent': 'your bot 0.1'})
rjson = r.json()
title = rjson['data']['children'][post_num]['data']['title']
print(title)

engine.save_to_file(text=title, filename='title.wav')

creq = requests.get(rjson['data']['children'][post_num]['data']['url']+'.json?limit=2', headers = {'User-agent': 'your bot 0.1'})

jscreq = creq.json()
comment1 = jscreq[1]['data']['children'][0]['data']['body']
comment2 = jscreq[1]['data']['children'][1]['data']['body']

print(comment1)
print(comment2)

engine.save_to_file(text=comment1, filename='comment.wav')
engine.runAndWait()

##################IMAGE CUT####################################################################################

# driver = webdriver.Firefox()

# driver.get(rjson['data']['children'][post_num]['data']['url'])

# # now that we have the preliminary stuff out of the way time to get that image :D
# element = driver.find_element('id', rjson['data']['children'][post_num]['data']['name']) # find part of the page you want image of
# # image = driver.find_element('id', rjson['data']['children'][post_num]['data']['name']).screenshot_as_png
# driver.find_element('xpath', "//*[contains(text(), " + rjson['data']['children'][post_num]['data']['title']+")]")
# screenshot = driver.save_screenshot('test.png')

# driver.quit()

###############
###############
#####IMAGE#####
###############
###############

# im = Image.open(r'title.png')



# width, height = im.size

# t_left = width/5 + 50
# t_top = height/2 - 100
# t_right = 3*width/4 -100
# t_bottom = 3*height/4 - 100
 
# im1 = im.crop((t_left, t_top, t_right, t_bottom))
# rgb_im = im1.convert('RGB')
# rgb_im.save('im3.jpg')

# im1.show()

# with open('data.json', 'w') as f:
#     f.write(json.dumps(jscreq, indent=4))

