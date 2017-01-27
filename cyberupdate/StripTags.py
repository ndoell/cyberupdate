'''
Created on Dec 5, 2016

@author: nicholasdoell

Source: http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
'''

from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)       