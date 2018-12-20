x = 5
y = 0

try:
    print(x/y)
except AssertionError as e:
    print("A")
except EOFError as e:
    print("e")
except  Exception as e:
    pass
finally:
    print("Finally")

print("Done")

data = "some line of text\nanother line of text\n"
fname = "text.txt"
fout = open(fname,"a", encoding="utf-8")
fout.write(data)
fout.close()

fin = open(fname,"r",encoding="utf-8")
lines = fin.readlines()
fin.close()
for l in lines:
    print(l)

