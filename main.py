
a = input("Geef een getal op.\n")
b = input("Geef nog een getal op.\n")

if(a > b):
    max = a
    min = b
    print("Het maximum is: " + max)
    print("Het minimum is: " + min)
elif(a < b):
    min = a
    max = b
    print("Het maximum is: " + max)
    print("Het minimum is: " + min)
else:
    print("a en b zijn even groot")