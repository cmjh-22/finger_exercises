complete = []
class Animals:
    id = 0
    zoo = []
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        Animals.id +=1
        Animals.zoo.append(self)
        complete.append(self)
    def __str__(self):
        return "name is " + (str(self.name)) + " and the gender is " + (str(self.gender))
    @classmethod
    def show(cls):
        for animal in Animals.zoo:
            print(animal.name, sep= ',', end=' ')

class dogs(Animals):
    def __init__(self,name,gender,age,color):
        super().__init__(name,gender)
        self.age = age
        self.color = color
    def lives(self):
        lives = self.age * 7
        return lives

def main():
    lizard = Animals("lily","female")
    fucidin = dogs("fuci","male",7,"gray")
    #without str method
   #print(lizard.name)
   #print(fucidin.name)
   #with stringmethod
    print(lizard)
    print(fucidin)
    print(fucidin.lives())
    Animals.show()


if __name__ == "__main__":
    main()



