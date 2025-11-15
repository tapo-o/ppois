from math import sqrt

class Vector():
    def __init__(self, x, y, z):
        self.coords = [x, y, z]

    def get(self):
        return self.coords
    
    def set(self, other):
        self.coords = other.coords

    def print_coords(self):
        for i in self.coords:
            if(self.coords.index(i)!=2):
                print(str(i)+", ", end="")
            else:
                print(str(i), end="\n")

    def length(self):
        answ = 0
        for i in range(3):
            answ += self.coords[i]*self.coords[i]
        
        return sqrt(answ)

    def __add__(self, other):
        res = self.coords
        try:
            for i in range(3):
                res[i] += other.coords[i]
            return Vector(res[0], res[1], res[2])
        except:
            print("only 'vector + vector'")

    def __iadd__(self, other):
        res = self.coords
        try:
            for i in range(3):
                res[i] += other.coords[i]
            return Vector(res[0], res[1], res[2])
        except:
            print("only 'vector + vector'")

    def __sub__(self, other):
        res = self.coords
        try:
            for i in range(3):
                res[i] -= other.coords[i]
            return Vector(res[0], res[1], res[2])
        except:
            print("only 'vector - vector'")

    def __isub__(self, other):
        res = self.coords
        try:
            for i in range(3):
                res[i] -= other.coords[i]
            return Vector(res[0], res[1], res[2])
        except:
            print("only 'vector - vector'")

    def __mul__(self, other):
        res = 0
        try:
            if isinstance(other, Vector):
                for i in range(3):
                    res += self.coords[i] * other.coords[i]
                return res

            else:
                for i in range(3):
                    res += self.coords[i] * other
                return res
        except:
            print("only 'vector * vector' or 'vector * scalar'")

    def __truediv__(self, other):
        res = self.coords
        try:
            for i in range(3):
                res[i] /= other.coords[i]
            return Vector(res[0], res[1], res[2])
        except:
            print("only 'vector / vector'")

    def __xor__(self, other):
        return self*other/(self.length()*other.length())
    
    def __ixor__(self, other):
        return self*other/(self.length()*other.length())
    
    def __eq__(self, other):
        try:
            if(self.length()==other.length()):
                return True
            return False
        except:
            print("only vector==vector")

    def __ne__(self, other):
        try:
            if(self.length()!=other.length()):
                return True
            return False
        except:
            print("only vector==vector")
    
    def __lt__(self, other):
        try:
            if(self.length()<other.length()):
                return True
            return False
        except:
            print("only vector<vector")

    def __le__(self, other):
        try:
            if(self.length()<=other.length()):
                return True
            return False
        except:
            print("only vector<vector")        

    def __gt__(self, other):
        try:
            if(self.length()>other.length()):
                return True
            return False
        except:
            print("only vector<vector")

    def __ge__(self, other):
        try:
            if(self.length()>=other.length()):
                return True
            return False
        except:
            print("only vector<vector")
