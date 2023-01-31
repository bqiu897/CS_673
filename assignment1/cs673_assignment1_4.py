def is_palindrome(string):
    reverse = string[::-1]
    if string == reverse:
        print(string + ' is a palindrome')
        return True
    else:
        print(string + ' is not a palindrome')
        return False


is_palindrome('racecar')          # returns True

is_palindrome('cat')              # returns False
