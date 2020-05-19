def bits1(n):
    b = []
    while n:
        b = [n & 1] + b
        n >>= 1
    return b or [0]
    

li=[]
for i in range(255):
    c=bits1(i)          
    lit=[]
    for ele in range(len(c)): 
        if c[ele]==1:
            lit.append(ele)
    li.append(lit)
#print(li)
for element in li:
    print(element)
