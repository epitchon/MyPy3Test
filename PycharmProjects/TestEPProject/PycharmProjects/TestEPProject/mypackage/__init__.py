def print_fleet_info(fleet):
   country_codes = {}
   country_codes["US"]="USA"
   country_codes["CA"]="Canada"

   #or
   country_codes = {"US":"USA","CA":"Canada"}


   print("\033[4mID\033[0m   \033[4mDESC\033[0m   \033[4mCARGO\033[0m")

   for truck in fleet:
       print(truck["ID"],country_codes.get(truck["DESC"],"unknown"))
       total_cargo=0
       for c in truck["CARGO"]:
           total_cargo += c
           print ("           ",c)
       print("            ____")
       print("     Total:",total_cargo)

