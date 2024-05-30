class static_fu():
    def __init__(self):
        self.name = "shubham"
        self.subject = ["english","hindi","math"]
    @staticmethod
    def add(num,num2):
        return num + num2
    
if __name__ == "__main__":
    re = static_fu.add(num=0,num2=3)
    print("add of result: ",re)


