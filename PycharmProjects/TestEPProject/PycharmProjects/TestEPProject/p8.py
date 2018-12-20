
from xml.etree import ElementTree
import json
import pickle
import sqlite3

print("Starting..")
def readjson():
    fname = "fleetData.json"
    fin = open(fname,"r")
    data = json.load(fin)
    fin.close()
    #print(data)
    #for item in data:
    #    print("The item is:",item)
    return data

def lookupTruck(f, truck_id):
    for i in f:
        if i["id"]==truck_id:
            return i


#print("The value of TR15 cargo is:",data)


fleetD=readjson()
x=lookupTruck(fleetD,"TR15")
#print (x)
#print (fleetD)

print("Open DB conn")
conn = sqlite3.connect("acme.sqlite")
print("Open cur")
cur = conn.cursor()


cur.execute("drop table if exists TRUCKS")
cur.execute("create table TRUCKS (ID varchar(10) primary key, DEST varchar(10))")
cur.execute("drop table if exists CARGO")
cur.execute("create table CARGO (TRUCK_ID varchar(10) , CARGO_BOX number)")

try:
    for truckD in fleetD:
        stm = "INSERT INTO TRUCKS VALUES('" + truckD["id"] + "','" + truckD["dest"] + "')"
        cur.execute(stm)
        for c in truckD["cargo"]:
            stm = "INSERT INTO CARGO VALUES('" + truckD["id"] + "','" + str(c) + "')"
            cur.execute(stm)

    results=cur.execute("select id,dest,cargo_box from trucks a, cargo b where a.id=b.truck_id order by a.id")
except Exception as e:
    print (e)
finally:
    print("Close cur")
    cur.close()
    print("Close DB conn")
    conn.close()

for r in results:
    print (r)


print("Done.")
