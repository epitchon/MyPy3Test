"""
[
    {"Banana":3.24},
    {"Apple": 2.23},
    {"Orange": 1.74}
]
"""
from xml.etree import ElementTree
import json
import pickle


fname = "fruits.json"
fin = open(fname,"r")
data = json.load(fin)
fin.close()

for i in data:
    print(i)


