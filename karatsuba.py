def karatsuba(a,b):
    """\nfunction to multiply two number's using karatsuba algorithm in a more efficient TC=n^1.585 \n"""
    if(len(str(a))==1 or len(str(b))==1):
        return a*b
    else:
        d=max(len(str(a)),len(str(b)))
        newd=d//2

        # a=x1.10^(newd)+x0
        # b=y1.10^(newd)+y0

        x1=a//(10**newd)
        x0=a%(10**newd)
        y1=b//(10**newd)
        y0=b%(10**newd)

        x0y0=karatsuba(x0,y0)
        x1y1=karatsuba(x1,y1)
        xiyj=karatsuba(x1+x0,y1+y0)-x0y0-x1y1
        # T(n)=3T(n/2)+Θ(n)

        return x1y1*(10**(2*newd))+x0y0+xiyj*(10**newd)

# print(karatsuba.__doc__) to print docstring
print(karatsuba(5484654534,2185146235))
