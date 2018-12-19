fleet = \
    [
    {"ID":"TR15","DESC":"US","CARGO":[1000,1400]},
    {"ID":"TR05","DESC":"CA","CARGO":[2000,1000,600]},
    {"ID":"TR32","DESC":"CA","CARGO":[300,2000]},
    {"ID":"TR12","DESC":"US","CARGO":[1000,3000,600,1000]}
    ]

rates = {"US":25.64,"CA":31.87}

class Truck:
    def __init__(self,id,dest,cargo):
        self.id=id
        self.dest=dest
        self.cargo=cargo

    def display(self):
        print ("Truck ID:", self.id,end=" ")
        print("Desc:", self.dest,end=" ")
        print("Cargo:", self.cargo,end=" ")

    def get_total_weight(self):
       tweight =0
       for w in self.cargo:
           tweight += w
       return tweight

    def get_average_weight(self):
        aweight = 0
        aweight=self.get_total_weight()/len(self.cargo)
        return aweight

    def get_cost(self):
        return rates[self.dest]*self.get_total_weight()

    def save(self):
        pass

    def read(self):
        pass

t1 = Truck("TR15","US",[1000,1200])
t2 = Truck("TR15","CA",[1200,2200])
t3 = Truck("TR15","US",[1100,3200, 32000])

fleet = [t1,t2,t3]

for t in fleet:
    t.display()
    print("\nTotal weight:", t.get_total_weight())
    print("\nAverage weight:", t.get_average_weight())
    print("\nTotal cost is:", "{0:,}".format(t.get_cost()))





