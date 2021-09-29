# day-2



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