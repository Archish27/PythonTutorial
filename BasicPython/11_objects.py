class Animal:
    __name = None
    __height = 0
    __weight = 0
    __sound = None
    #NOTE : __ Double Underscore defines that variables are private

    #Creating Constructor
    def __init__(self,name,height,weight,sound):
        self.__name = name
        self.__height= height
        self.__weight = weight
        self.__sound = sound
        
    #Getter Setter Methods
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def setWeight(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    def setSound(self, sound):
        self.__sound = sound

    def getSound(self):
        return self.__sound

    def getType(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} Kgs and says {}".format(self.__name,
                                                               self.__height,
                                                               self.__weight,
                                                               self.__sound)

cat = Animal('Whiskers',33,10,'Meow')

print(cat.toString())


#Inheritance
class Dog(Animal):
    __owner = None

    def __init__(self,name,height,weight,sound,owner):
        super(Dog,self).__init__(name,height,weight,sound)
        self.__owner = owner
        

    def setOwner(self,owner):
        self.__owner = owner
    def getOwner(self):
        return self.__owner

    def getType(self):
        print("Dog")
    def toString(self):
        return "{} is {} cm tall and {} Kgs and says {} His Owner is {}".format(self.__name,
                                                               self.__height,
                                                               self.__weight,
                                                               self.__sound,
                                                               self.__owner)


tom = Dog('Tom',43,85,'Bark','John')
print(tom.getType())
print(tom.toString())


