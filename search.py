import os
class Inventory:
    def __init__(self):
        self.items = {}
        self.shops = {}
    def add(self, inp):
        temp = inp.split(", ")
        if int(temp[0]) not in self.shops.keys():
            self.shops[int(temp[0])] = []
        self.shops[int(temp[0])].extend(temp[2:])
        if tuple(temp[2:]) not in self.items:
            self.items[tuple(temp[2:])] = []
        self.items[tuple(temp[2:]) ].append( ( int(temp[0]) , float(temp[1])))

    def getShopId(self, item):
        result = []
        for shopid in self.shops:
            if item in self.shops[shopid]:
                result.append(shopid)
        return set(result)     
    def search(self, items):
        result = None
        minPrice = None
        if len(items) < 1:
            return result,MinPrice
        elif len(items) < 2:
            try:
                shops = []
                for i in self.items.keys():
                    if items[0] in i:
                        shops.extend(self.items[i])
            except Exception,e:
                result = None
                print e
            else:
                if len(shops) > 1:
                    minPrice = shops[0][1]
                    result = shops[0][0]
                    for shop,price in shops:
                        if price < minPrice:
                            minPrice = price
                            result = shop
                else:
                    result = shops[0][0]
                    minPrice = shops[0][1]
        else:
            shops = []
            for i in self.shops.keys():
                if set(items) <= set(self.shops[i]):
                    shops.append(i)
            if len(shops) < 1:
                return None,None
            elif len(shops) < 2:
                result = shops[0]
                minPrice = 0
                for item in items:
                    temp = []
                    for i in self.items.keys():
                        if item in i:
                            temp.extend(self.items[i])
                    for shop,price in temp:
                        if shop == result:
                            minPirce += price
            else:
                temps = {}
                for shop in shops:
                    tempPrice = 0
                    for item in items:
                        temp = []
                        for i in self.items.keys():
                            if item in i:
                                temp.extend(self.items[i])
                        for sid,price in temp:
                            if sid == shop:
                                tempPrice += price
                    temps[shop] = tempPrice
                minPrice = temps[temps.keys()[0]]
                result  = temps.keys()[0]
                for shop in temps.keys():
                    if temps[shop] < minPrice:
                        minPrice = temps[shop]
                        result = shop
        return result,minPrice


import sys

fileName = sys.argv[1]
items = tuple(sys.argv[2:])


inventory = Inventory()
#os.chdir("Dekstop")
inFile = open(fileName)
lines  = inFile.readlines()
for line in lines:
    inventory.add(line[:-1])
shop,price = inventory.search(items)
if shop is None:
    print None
else:
    print "{}, {}".format(shop,price)
