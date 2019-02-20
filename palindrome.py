# def palindrome(string):
#     pal = str(input('Enter a possible palindrome '))
#     if len(string) <= 1:
#         return True
#     else:
#         if string[0] == string[-1]:
#             return palindrome(string[1:-1])
#             if palindrome(pal) == True:
#                 print('is a palindrome')
#             else:
#                 pass
#         else:
#             print('is not a palindrome')


import re

pal = input('Enter a possible palindrome: ')
pal = re.sub(r'[^A-Za-z]', '', pal.lower())
# this uses slicing for the palindrome function


# def is_palindrome():
#     print(pal)
#     return pal == pal[::-1]


# recursive palindrome function


def recursive(var):
    """this is a recursive palindrome checker """
    print(var)
    if len(var) < 2:
        return True
    return var[0] == var[-1] and recursive(var[1:len(var) - 1])


# iterative palindrome function

# def iterative(pal):
#     for char in range(len(pal)):
#         return pal(char) == pal[-(char + 1)]


if recursive(pal):
    print('is a palindrome')
else:
    print('is not a palindrome')
