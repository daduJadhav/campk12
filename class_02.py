# day-2



from math import e


row  = 5

b = 0

for i in range(row,0,-1):
    b = b  + 1

    for j in range(1, i +1):
        print(b, end=" ")

    print("\r")

# will print like this 
# 11111
# 2222
# 333
# 44
# 5


# project 2

def trangle(n):
    k = n - 1

    for i in range(0,n):
        # print(end=" ")

        for j in range(0,k):
            # print(" \n")

            k = k-1

        for j in range(0,i+1):
            print("* " ,end="")
        print()
    print("\r")

n = 6

trangle(n)



# project 3
# Hart project 

n = 8

m = n+1

for i in range(n//2-1):

    for j in range (m):
        if i==n//2-2 and (j == 0 or j == m-1):
            print("*", end=" ")
        elif j <= m//2 and ((i+j == n//2-3 and j <= m//4)\
                                                or(j-i == m//2-n//2+3 and j > m//4)):
            print("*", end=" ")
        elif j > m//2 and ((i+j == m//2-n//2+3+m//2 and j < 3*m//4)\
                                                or(j-i == m//2-n//2+3+m//2 and  j >= 3*m//4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

for i in range (n//2-1,n):
    for j in range (m):

            if (i-j == n//2-1) or (i+j == n-1+m//2):
                print("*", end=" ")
            else:
                print(" " , end=" ")
                                               
    print()