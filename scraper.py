from bs4 import BeautifulSoup
import json
import requests

r = requests.get('http://seasite.niu.edu/Tagalog/Dictionary/diction.htm')
print(len(r.text))

soup = BeautifulSoup(r.text)
print(soup.title)

dictionary = []

def create_entry (term, altterm, pronounciation, pos, examples, audio):
    return {"term":term, "altterm":altterm, "pronounciation":pronounciation, "pos":pos, "examples":examples, "audio":audio}


