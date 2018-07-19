

class Calc:
    classLog=[]

    def __init__(self, id):
        print("계산기를 시작합니다~ 아이디는" +str(id)+"입니다.~")
        self.log = []
        Calc.classLog.append(id)

    def add(self, op1, op2):
        print(op1+op2)
        self.log.append(str(op1) + " + " + str(op2))

    def mul(self, op1, op2):
        print(op1 + op2)
        self.log.append(str(op1) + " + " + str(op2))

    def printLog(self):
        print(self.log)

    def div(self, op1, op2):
        print(op1 / op2)
        self.log.append(str(op1) + " / " + str(op2))

    def div(self, op1, op2):
        try:
            print(op1 / op2)
            self.log.append(str(op1) + " / " + str(op2))


    def printLog(self):
        print(self.log)

            def div(self, op1, op2):
                print(op1 / op2)
                self.log.append(str(op1) + " / " + str(op2))

            def printLog(self):
                print(self.log)

            break
        except ZeroDivisionError:
            print("Do not put in zero")


calc1 = Calc(1)
calc2 = Calc(2)

calc1.add(1,2)
calc1.mul(3,4)
calc2.div(5,2)

calc1.printLog()
calc2.printLog()
print(Calc.classLog)
