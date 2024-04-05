from Human import Human
class Student(Human):
    def __init__(self, name:str = "", age:float = "", group:str = '', money:float = ""):
        self.Name:str = name
        self.Group:str = group
        self.Age:float= age
        self.Money:float = money
    def __str__(self):
        if self.Money  >= 15000:
            return (f"Name: {self.Name}\n"
                f"Age: {self.Age}\n"
                f"Group: {self.Group}\n"
                f"Money: {self.Money}\n")
        elif self.Money  <= 14999:
            return (f"Name: {self.Name}\n"
                f"Age: {self.Age}\n"
                f"Group: {self.Group}\n"
                f"Money: {self.Money}, he needs to find work\n")