class NameSort():
    def __init__(self,infile,):
        file=open(infile)
        master=file.readline()
        self.M=master
        self.count=0
        self.D={}
    def __repr__(self):
        return self.D
    def maker(self):
        x=" "
        z=0
        done=False
        while not done:
            self.M.lower()
            if x in self.M:
                self.D.update({self.M[0:self.M.index(x)]:self.M[self.M.index(x)+1:-1]})
                z+=1
                if z==self.count:
                    self.D.update({self.M[0:self.M.index(x)]:self.M[self.M.index(x)+1:-1]})
                    done=True
                else:
                    done=False
    def lines(self):
        self.count=self.M.count("\n")
        #self.Q=self.Q.replace("\n","@@")
        return self.count+2
    def book(self):
        for keys,values in self.D.items():
            print(keys)
            print(values)
        
