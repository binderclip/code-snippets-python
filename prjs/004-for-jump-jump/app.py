# coding: utf-8
from Crypto.Cipher import AES
import requests
import json
import base64


action_data = {
    "score": 111,
    "times": 111,
    "game_data": "{}"
}

session_id = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=="
aes_key = session_id[0:16]
aes_iv = aes_key

cryptor = AES.new(aes_key, AES.MODE_CBC, aes_iv)

str_action_data = json.dumps(action_data).encode("utf-8")
print("json_str_action_data ", str_action_data)

# PKCS7
length = 16 - (len(str_action_data) % 16)
str_action_data += chr(length) * length
print(str_action_data)
cipher_action_data = base64.b64encode(cryptor.encrypt(str_action_data)).decode("utf-8")
print("action_data ", cipher_action_data)

post_data = {
  "base_req": {
    "session_id": session_id,
    "fast": 1,
  },
  "action_data": cipher_action_data
}

headers = {
    "charset": "utf-8",
    "Accept-Encoding": "gzip",
    "referer": "https://servicewechat.com/wx7c8d593b2c3a7703/3/page-frame.html",
    "content-type": "application/json",
    "User-Agent": "MicroMessenger/6.6.1.1200(0x26060130) NetType/WIFI Language/zh_CN",
    "Content-Length": "0",
    "Host": "mp.weixin.qq.com",
    "Connection": "Keep-Alive"
}

url = "https://mp.weixin.qq.com/wxagame/wxagame_settlement"


response = requests.post(url, json=post_data, headers=headers)
print(json.loads(response.text))
