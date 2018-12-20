def foo(x,y,z):
    print (x,y,z)

dic = { "x":1,"y":2,"z":3}

foo(**dic)

dic = {"id":"TR15","cargo":[1200,1000]}

truck = Truck(**dic) # createa a truck instance of class Truck