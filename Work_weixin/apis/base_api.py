import requests
from requests import request


class BaseApi:
    #���
    def send(self,req):
        r = request(**req)
        return r