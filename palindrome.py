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


# palindrome()

# get a string from the user that may be a palindrome    
def is_palindrome():
    pal = input('Enter a possible palindrome: ')
    string = pal.replace(" ", "").replace(".", "").replace(",", "").replace("-", "")
    string = string.lower()
    # need to strip string of punctuation
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        if string[-1::-1] == string[::1]:
            return True
        else:
            return False


if is_palindrome() is True:
    print('is a palindrome')
else:
    print('is not a palindrome')
