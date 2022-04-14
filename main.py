import time
dayofyear = 0

def choise():
    if ch == "Ch":
        mainhero.work -= 10
        mainhero.teach -= 3
        mainhero.info()
        print(f"Day is {dayofyear}/365")
        time.sleep(2)
    elif ch == "Te":
        mainhero.teach += 7
        mainhero.work -= 2
        mainhero.info()
        print(f"Day is {dayofyear}/365")
        time.sleep(2)
    elif ch == "Wo":
        mainhero.work += 5
        mainhero.teach -= 2
        mainhero.info()
        print(f"Day is {dayofyear}/365")
        time.sleep(2)


def day():
    global ch
    global dayofyear
    dayofyear += 1
    ch = input(f"{mainhero.name}, do you want to:"
               f"\nChill: (Ch)"
               f"\nTeach: (Te)"
               f"\nWork: (Wo)"
               f"\nYour choose: ")

    choise()


class Student:
    def __init__(self, name, age, edu, teach, work):
        self.name = name
        self.age = age
        self.edu = edu
        self.teach = teach
        self.work = work

    def info(self):
        print(f"Youre: \nName - {self.name}"
              f"\nAge - {self.age}"
              f"\nEdu - {self.edu}"
              f"\nTeach(successfully) - {self.teach}"
              f"\nWork(money) - {self.work}")


mainhero = Student("Michael", 19, "University", 100, 100)

mainhero.info()
time.sleep(4)


while mainhero.work or mainhero.teach > 1:
    if dayofyear == 365:
        print("It's a victory!\nHurray!!")
        pass
    print("New day:\n")
    day()

print("You lose.")