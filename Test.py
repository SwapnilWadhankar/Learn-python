# # function to check string is
# # palindrome or not
# def isPalindrome(str):

# 	# Run loop from 0 to len/2
# 	for i in range(0, int(len(str)/2)):
# 		if str[i] != str[len(str)-i-1]:
# 			return False
# 	return True

# # main function
# s = "mississim"
# ans = isPalindrome(s)

# if (ans):
# 	print("Yes")
# else:
# 	print("No")

# def isEven(x):
#     if x%2==0:
#         print("even")
#     else:
#         print("odd")

# isEven(121232)

# CODE TO RETURN ALL THE EVEN NUMBERS IN THE LIST

# def code_to_even(userlist):
#     for num in userlist:
#         if num%2==0:
#             print(num)
#         else: 
#             pass
#     return False

# code_to_even([1,2,34,5,4,6,7,7,8])

# GOAT = [("Ronaldo", 800), ("Messi", 1000), ("Suarez", 700), ("Maradona", 950), ("Pele", 950)]

# def goat_of_football(GOAT):
#     points = 0
#     goat = ""
#     for player,player_points in GOAT:
#         if player_points > points:
#             points = player_points
#             goat = player
#         else:
#             pass
#     return [(goat,points)]

# x= goat_of_football(GOAT)
# print(x)
# def evenfunc(somestring):
#     helo = ''
#     for i in range(len(somestring)):
#         if i%2==0:
#             helo = helo + somestring[i].upper()
#         else:
#             helo =  helo + somestring[i].lower()
#     return helo

# x = evenfunc("ThdfiisdfFhdnf")
# print(x)

# def even_less(x,y):
#     if x%2 !=0 or y%2 !=0:
#         if x>y:
#             return x
#         else:
#             return y
#     elif x % 2 == 0 and y % 2 == 0:
#         if x>y:
#             return x
#         else: 
#             return y

# x = even_less(6,3)
# print(x)



































