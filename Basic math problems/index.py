### counting number of digits

# user_num = input("Enter a number: ")

# count = 0
# for ch in user_num:
#     if count == len(user_num):
#         print(count)
#     else:
#         count += 1
#         print(ch)

# print("The total count of the number entered is:", count)


#### reverse a number


# user_num  = int(input("Enter a number"))

# rev_num = 0
# flag = False
# while user_num > 0: #1230000
#     rem_num = user_num % 10
#     if flag or rem_num != 0:
#         flag = True
#         rev_num = rev_num * 10 + rem_num
    
#     user_num = user_num // 10
   


# print("The reverse of the entered number is: ", rev_num)


## pallindrom or not



# user_num  = int(input("Enter a number: "))
# rev = 0
# org_num = user_num

# while user_num > 0:
#     rem = user_num % 10
#     rev = rev * 10 + rem
#     user_num = user_num // 10

#     if user_num == 0:
#         break


# if org_num == rev:
#     print(True)
# else:
#     print(False)


class Solution:
    def GCD(self, n1, n2):
        divisors = []

        if n1 < n2:
            for i in range(1,n1+1):
                if n1 % i == 0 and n2 % i == 0:
                    divisors.append(i)
        else:
            for i in range(1, n2+1):
                if n1%i == 0 and n2%i == 0:
                    divisors.append(i)

        max_div = divisors[0]

        for num in divisors:
            print(num)
            if num > max_div:
                max_div = num

       

        print("The greatest divisor is: ", max_div)




obj = Solution()
n1 = int(input("Enter first number"))  ##4
n2 = int(input("Enter second number")) ##6
obj.GCD(n1,n2)