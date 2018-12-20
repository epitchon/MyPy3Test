country_codes = {}
country_codes["US"]="USA"
country_codes["CA"]="Canada"

#or
country_codes = {"US":"USA","CA":"Canada"}

fleet = \
    [
    {"ID":"TR15","DESC":"US","CARGO":[1000,1400]},
    {"ID":"TR05","DESC":"CA","CARGO":[2000,1000,600]},
    {"ID":"TR32","DESC":"CA","CARGO":[300,2000]},
    {"ID":"TR12","DESC":"US","CARGO":[1000,3000,600,1000]}
    ]

print("\033[4mID\033[0m   \033[4mDESC\033[0m   \033[4mCARGO\033[0m")

for truck in fleet:
    print(truck["ID"],country_codes.get(truck["DESC"],"unknown"))
    total_cargo=0
    for c in truck["CARGO"]:
        total_cargo += c
        print ("           ",c)
    print("            ____")
    print("     Total:",total_cargo)

















