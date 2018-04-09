# -*- coding: utf-8 -*-
'''图灵'''
import sys
import os
import requests
import json
import urllib2
import demjson
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import bsidu_stt
from tts import baidu_tts
import snowboy
import speaker
import recorder

def start(text):
  
    main(text)
    
def main(text):
    
    ak = 'c380ed8f2880443c84892ace36ba6bad'
    ui = '167031'
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    dataf = {
	      "reqType":0,
              "perception": {
                  "inputText": {
                      "text": text
                  },
              },
              "userInfo": {
                  "apiKey": ak,
                  "userId": ui
              }
           }
    data = json.dumps(dataf)
    talkback = requests.post(url, data=data)
    talkback_data = talkback.json()
    print talkback_data
    talkback_list = talkback_data["results"]
    talkback_dict = talkback_list[-1]
    talkback_val = talkback_dict["values"]
    text = talkback_val["text"]
    print text
    saytext = text.encode('utf-8','strict')
    bt = baidu_tts()
    tok = bt.get_token()
    bt.tts(saytext, tok)
    speaker.speak()
    
