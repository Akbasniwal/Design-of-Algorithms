import numpy as np
def multiMatrix(x, y):
    n = len(x)
    if n == 1:
        return np.array([[x[0][0] * y[0][0]]])
    else:
        r=len(x)//2
        a = x[:r , :r]
        b = x[:r , r:]
        c = x[r: , :r]
        d = x[r: , r:]

        e = y[:r , :r]
        f = y[:r , r:]
        g = y[r: , :r]
        h = y[r: , r:]
        ae = multiMatrix(a,e)
        bg = multiMatrix(b,g)
        af = multiMatrix(a,f)
        bh = multiMatrix(b,h)
        ce = multiMatrix(c,e)
        dg = multiMatrix(d,g)
        cf = multiMatrix(c,f)
        dh = multiMatrix(d,h)

        c=np.concatenate((np.concatenate((ae+bg,af+bh),axis=1),np.concatenate((ce+dg,cf+dh),axis=1)),axis=0)
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
c=multiMatrix(a, b)
print(c)
