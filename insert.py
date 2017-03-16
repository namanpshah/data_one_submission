fileName = raw_input("Enter File Name : ")
outFile = open(fileName, "a")
print " ****** NOTE :  Enter exit or quit to stop.. ********"
pname = ""
while True:
    pname = raw_input("Enter Product Name : ")
    if pname.lower() == "quit" or pname.lower() == "exit":
        break
    price = float(raw_input("Enter Product Price : "))
    shopid = int(raw_input("Enter Shop Id : "))
    print
    outFile.write("{}, {}, {}\n".format(shopid,price,pname))
outFile.close()
