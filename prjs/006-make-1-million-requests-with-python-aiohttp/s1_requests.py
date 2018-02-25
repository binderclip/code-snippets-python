import requests


def hello():
    return requests.get("http://httpbin.org/get")


print(hello().text)
