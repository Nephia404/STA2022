#3127
#8201
a = 8201
b = 3127

def  Euc(a,b):
    if b == 0:
        return a
    else:
        return Euc(b,a%b)

print(Euc(a,b))
