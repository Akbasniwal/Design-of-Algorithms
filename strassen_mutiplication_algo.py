import numpy as np
def strassen_multi(x, y):
    n = len(x)
    if n == 1:
        return np.array([[x[0][0] * y[0][0]]])
    else:
        r=len(x)//2
        a11 = x[:r , :r]
        a12 = x[:r , r:]
        a21 = x[r: , :r]
        a22 = x[r: , r:]
        
        b11 = y[:r , :r]
        b12 = y[:r , r:]
        b21 = y[r: , :r]
        b22 = y[r: , r:]

        s1,s2,s3,s4,s5=b12-b22,a11+a12,a21+a22,b21-b11,a11+a22
        s6,s7,s8,s9,s10=b11+b22,a12-a22,b21+b22,a11-a21,b11+b12

        p1,p2,p3,p4=strassen_multi(a11,s1),strassen_multi(s2,b22),strassen_multi(s3,b11),strassen_multi(a22,s4)
        p5,p6,p7=strassen_multi(s5,s6),strassen_multi(s7,s8),strassen_multi(s9,s10)

        c11=p5+p4-p2+p6
        c12=p1+p2
        c21=p3+p4
        c22=p5+p1-p3-p7
        c=np.concatenate((np.concatenate((c11,c12),axis=1),np.concatenate((c21,c22),axis=1)),axis=0)
        return c

a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
b = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

c=a+b
c=strassen_multi(a, b)
print(c)
