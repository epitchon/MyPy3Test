
from xml.etree import ElementTree
import json
import pickle

data = "Some line of text\nThis is another line"

def writetxt():
    fname = "test.txt"
    fout = open(fname, "w", encoding="utf-8")
    fout.write(data)
    fout.close()

def readtxt():
    fname = "test.txt"
    fin = open(fname, "r", encoding="utf-8")
    lines = fin.readlines()
    fin.close()
    for line in lines:
        print(line, end="")

def writecsv():
    data = "\"apple\",3.25\n\"lemon\",3.67\n\"kiwi\",4.55"
    fname = "test.csv"
    fout = open(fname,"w",encoding="utf-8")
    fout.write(data)
    fout.close()

def readcsv():
    fname = "test.csv"
    fin = open(fname,"r", encoding="utf-8")
    lines = fin.readlines()
    fin.close()
    # reading is done and now it's time for cleaning the data
    fruits = []
    for line in lines:
        fruit = line[:-1].split(",")
        fruit[0] = fruit[0].replace("\"","")
        fruit[1] = float(fruit[1])
        fruits.append(fruit)
    for fruit in fruits:
        print(fruit[0], fruit[1])

def writexml():
    # same as saving a text file
    # ensure your data is in the proper XML format
    # e.g (incomplete) data = "<fruits><fruit><name>apple</name><price>3.25</price></fruit><fruit></fruit><fruit></fruit></fruits>"
    pass

def readxml():
    fname = "fruits.xml"
    dom = ElementTree.parse(fname)
    fruits = dom.findall("./fruit")
    for fruit in fruits:
        name = fruit.find("name").text
        price = float(fruit.find("price").text)
        print(name,price)

def writejason():
    # same as saving a text file
    # ensure your data is in the proper JSON format
    pass

def readjson():
    fname = "fruits-LIST.json"
    fin = open(fname,"r")
    data = json.load(fin)
    fin.close()
    print(data)
    for item in data:
        print(item)

# need a class to demo object serialization

class Employee:

    def __init__(self, id, name="", age=0):
        self.id = id
        self.name = name
        self.age = age

    def display(self):
        print(self.id, self.name, self.age)

"""
# create an object populating it with data, then save it

emp1 = Employee("362","Dave", 32)
fname = emp1.id + ".bin"
fout = open(fname, "wb+")
pickle.dump(emp1, fout)
fout.close()

# create an object but populate it with data from disk

emp2 = Employee("362")
fname = emp2.id + ".bin"
fin = open(fname,"rb")
emp2 = pickle.load(fin)
fin.close()
emp2.display()
"""








