"""
Rename this file to param.py
"""
class ParamGiphy():
    """
    input your giphy api-key
    """
    def __init__(self):
        self.API_KEY = ""

class ParamOAuth():
    """
    input twitter your OAuth information.
    https://developer.twitter.com/
    """
    def __init__(self):
        self.consumer_key =""
        self.consumer_secret = ""
        self.token = ""
        self.token_secret = ""