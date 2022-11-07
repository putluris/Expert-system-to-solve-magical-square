Doubly even magic square:
def DoublyEven(n): 
        arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)] 
        l=int(n/4); 
        for i in range(0,l): 
                for j in range(0,l): 
                        arr[i][j] = (n*n + 1) - arr[i][j];  
        for i in range(0,l): 
                for j in range(3 * l,n): 
                        arr[i][j] = (n*n + 1) - arr[i][j];  
        for i in range(3 * l,n): 
                for j in range(0,l): 
                        arr[i][j] = (n*n + 1) - arr[i][j];  
        for i in range(3 * l,n): 
                for j in range(3 * l,n): 
                        arr[i][j] = (n*n + 1) - arr[i][j];
        for i in range(l,3 *l): 
                for j in range(l,3 * l): 
                        arr[i][j] = (n*n + 1) - arr[i][j]; 
        print(isMagicSquare(arr))
        return arr,N
Odd magic square:
def  odd(s):
    if s % 2 == 0:
        s += 1
    q = [[0 for j in range(s)] for i in range(s)]
    p = 1
    i = s // 2
    j = 0
    while p <= (s * s):
        q[i][j] = p
        ti = i + 1
        if ti >= s: ti = 0
        tj = j - 1
        if tj < 0: tj = s - 1
        if q[ti][tj] != 0:
            ti = i
            tj = j + 1
        i = ti
        j = tj
        p = p + 1
    print(isMagicSquare(q))
    return q, s
Single even magic square:
def  singleeven(s):
    if s % 2 == 1:
        s += 1
    while s % 4 == 0:
        s += 2
    q = [[0 for j in range(s)] for i in range(s)]
    z = s // 2
    b = z * z
    c = 2 * b
    d = 3 * b
    o = odd(z)
    for j in range(0, z):
        for i in range(0, z):
            a = o[0][i][j]
            q[i][j] = a
            q[i + z][j + z] = a + b
            q[i + z][j] = a + c
            q[i][j + z] = a + d
 
    lc = z // 2
    rc = lc
    for j in range(0, z):
        for i in range(0, s):
            if i < lc or i > s - rc or (i == lc and j == lc):
                if not (i == 0 and j == lc):
                    t = q[i][j]
                    q[i][j] = q[i][j + z]
                    q[i][j + z] = t
    print(isMagicSquare(q))
    return q, s
Ramanujan magic square:
date=input("date of birth dd:mm:yyyy->")
d=''
m=''
y1=''
y2=''
for i in range(0,2):
    d=d+date[i]
for i in range(3,5):
    m=m+date[i]
for i in range(6,8):
    y1=y1+date[i]
for i in range(8,10):
    y2=y2+date[i]
d=int(d)
m=int(m)
y1=int(y1)
y2=int(y2)
print(d,m,y1,y2)
print(d-1,y1-1,m-3,d+3)
print(m-2,d+2,y2+2,y1-2)
print(y1+1,y2-1,d+1,m-1)
print('ramanujan square sum for you name',d+m+y1+y2)
