
#  ****
#  ****
#  ****

rows = 5
cols=5

# for i in range(1,rows):
#     for j in range(1,cols):
#         print("* ",end='')
#     print('\n')


# *
# **
# ***
# ****

# for i in range(1,rows):
#     for j in range(1,i+1):
#         print("*",end='')
#     print('\n')


# 1
# 12
# 123
# 1234
# 12345


# for i in range(1, rows):
#     for j in range(1,i+1):
#         print(j, end='')
#     print('\n')


# 1
# 22
# 333
# 4444
# 55555

# for i in range(1,rows):
#     for j in range(i):
#         print(i,end='')
#     print('\n')



# *****
# ****
# ***
# **
# *

# for i in range(rows, 1, -1):
#     for j in range(i):
#         print(j+1,end='')
    
#     print('\n')



#     *
#    *** 
#   *****
#  *******
# *********


# for i in range(1, rows+1):

#     for j in range(rows - i):
#         print(' ', end='')

#     for k in range(2 * i - 1):
#         print('*', end='')

#     print('\n')



# *********
#  *******
#   *****
#    ***
#     *


# for i in range(rows+1, 0, -1):

#     for j in range(rows - (i - 1)):
#         print(' ',end='')
    
#     for k in range(2 * i - 1):
#         print('*', end='')
    
#     print('\n')








#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *


# for i in range(1, rows+1):

#     for j in range(rows-i):
#         print(" ", end='')
#     for k in range(2*i -1):
#         print("*", end='')
    
#     print("\n")

#     if i == rows:
#         for l in range(rows-1, 0, -1):
#             for m in range(rows - l):
#                 print(' ',end='')
#             for n in range(2 * l - 1):
#                 print('*', end='')
#             print('\n')




    #  *
    #  **
    #  *** 
    #  ****
    #  *****
    #  ******  
    #  *****
    #  ****
    #  ***    
    #  **
    #  *

# for i in range(1, rows+1):
#     for j in range(1,i+1):
#         print("*", end='')
#     print('')
    
#     if i == rows:
#         for i in range(rows, 0 , -1):
#             for j in range(i):
#                 print('*',end='')
#             print()



# 1
# 01
# 101
# 0101
# 10101

# for i in range(1, rows+1):
#     for j in range(1, i):
#         print((i+j) % 2 , end='')
#     print('\n')


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# num = 1
# print(rows)
# for i in range(0, rows+1):
#     for j in range(1,i+1):
#         print(num, end='')
#         num += 1
#     print()


# a
# ab
# abc
# abcd
# abcde


ch='A'
# for i in range(1,rows+1):
#     for j in range(0, i):
#         print(chr(97+j), end='')
#     print()

# abcde
# abcd
# abc
# ab
# a


# for i in range(rows+1,0, -1):
#     for j in range(i):
#         print(chr(97+j), end='')
#     print()

# a
# bb
# ccc
# dddd
# eeeee


# for i in range(1, rows+1):
#     for j in range(1,i+1):
#         print(ch,end='')
#         ch = chr(97+j)
#     print()



# for i in range(1, rows+1):

#     ## stars
#     for j in range((rows+1)-i):
#         print('*', end='')
    
#     ## space
#     for k in range(0, rows+1, 2):
#         print(' ', end='')
    
#     ## stars
#     for l in range(2 * i - 1):
#         print('*', end='')
#     print()
