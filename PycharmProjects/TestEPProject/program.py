country_codes = {}
country_codes["US"]="USA"
country_codes["CA"]="Canada"

#or
ccodes = {"US":"USA","CA":"Canada"}

fleet = [["TR15", "US", 2400],["TR05", "CA", 3600],["TR32", "CA", 2300],["TR12", "US", 5600]]
"""
for truck in fleet:
    print ("Truck ID:", truck[0])

for truck in fleet:
    print("Destingation:",country_codes.get(truck[1],"unknown"))

print("\n")
"""
print("ID   CARGO   DEST")
for truck in fleet:
    print(truck[0],truck[2],"  ",country_codes.get(truck[1],"unknown"))

total_cargo=0
for truck in fleet:
    total_cargo += truck[2]

print("\nTotal cargo: ", total_cargo)








