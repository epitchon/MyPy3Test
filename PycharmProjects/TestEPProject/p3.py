"""

import mypackage

fleet = \
    [
    {"ID":"TR15","DESC":"US","CARGO":[1000,1400]},
    {"ID":"TR05","DESC":"CA","CARGO":[2000,1000,600]},
    {"ID":"TR32","DESC":"CA","CARGO":[300,2000]},
    {"ID":"TR12","DESC":"US","CARGO":[1000,3000,600,1000]}
    ]

mypackage.print_fleet_info(fleet)

"""

def whatIsIt(x,y):
    print("Evaluating if ",x," = ",y)
    if x==y:
        return True
    else:
        return False

all([whatIsIt(1,2),whatIsIt(2,2)])
any([whatIsIt(1,2),whatIsIt(2,2)])


