

def get_box_valume(side):
    return side*side*side

def get_box_basearea(side):
    return side*side

box1_side = 5
box1_volume = get_box_valume(box1_side)
box1_basearea   = get_box_basearea(box1_side)

box2_side = 8
box2_volume = get_box_valume(box1_side)
box2_basearea = get_box_basearea(box1_side)


print("box 1:",box1_volume,box1_basearea)
print("box 2:", box2_volume, box2_basearea)



