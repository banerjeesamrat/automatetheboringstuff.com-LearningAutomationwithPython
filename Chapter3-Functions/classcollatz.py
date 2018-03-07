

class Col:
    inp = 0

    def __init__(self, inp):
        self.inp = inp

    def collatz(self):
        while(self.inp != 1):
            if (self.inp%2 == 0):
                self.inp = self.inp//2
                print (self.inp)
            elif(self.inp%2!=0):
                self.inp = ((3*self.inp)+1)
                print (self.inp)

    def main():
        try:
            obj = Col(inp = int(input("Enter An Integer\n")))
            if(obj.inp<=0):
                print("Positive integers only",end="\n")
            else:
                obj.collatz()
        except:
            print("Integers Only")


if __name__ == "__main__":
    Col.main()
