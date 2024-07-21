from Database import Database

class Name:
    def __init__(self, name, year, gender, count):
        self.__name = name
        self.__year = year
        self.__gender = gender
        self.__count = count
    

    def setName(self, name):
        self.__name = name
    

    def getName(self):
        return self.__name
    

    def setYear(self, year):
        self.__year = year
    

    def getYear(self):
        return self.__year
    

    def setGender(self, gender):
        self.__gender = gender
    

    def getGender(self):
        return self.__gender
    

    def setCount(self, count):
        self.__count = count
    

    def getCount(self):
        return self.__count
    
    def showNames():
        names = Database().showNames()
        data = []
        for i in range(0, len(names)):
            name = names[i]
            data.append(Name(name["name"], name["year"], name["gender"], name["count"]))
        return data

