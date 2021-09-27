
# project 1

# usernum = int(input("Enter the number : "))

# if (usernum%3==0 and usernum%5==0):
#     print("Your no. is divisible by 3 as well as 5")
# elif(usernum%5 == 0):
#     print("No. id=s only divisible by 5")
# elif(usernum%3 == 0):
#     print("No. is only divisible by 3")    
# else:
#     print("you no. is nither divisible by 3 nor by 5")

#  project 2
# addition 


# num_1 = int(input("Enter the First no. : "))
# num_2 = int(input("Enter the second no. : "))
# sum = num_1 + num_2
# print("addition of the two no. is :",sum )



# project
# Calcy

print("For Suntraction enter  : s")
print("For Multiplication enter  : m")
print("For addition enter  : a")
print("For Division enter : d")

entry = input("Ente what you want to do : ")

n1 = int(input("Enter the First no. : "))
n2 = int(input("Enter the second no. : "))

if(entry == "s"):
    print("solution  : " , n1-n2)
elif(entry == "m"):
    print("solution  : " , n1*n2)
elif(entry == "a"):
    print("solution  : " , n1+n2)
elif(entry == "d"):
    print("solution  : " , n1/n2)
