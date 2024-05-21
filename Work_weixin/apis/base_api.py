import requests
from requests import request


class BaseApi:
    #½â°ü
    def send(self,req):
        r = request(**req)
        return r