def is_divisible(number, divisor):
    return number % divisor == 0


def is_leap_year(year):
    if is_divisible(year, 4) & (not is_divisible(year, 100)) | is_divisible(year, 400):
        print(str(year) + ' is a leap year')
        return True
    else:
        print(str(year) + ' is not a leap year')
        return False


is_leap_year(1900)  # returns False
is_leap_year(2000)  # returns True
is_leap_year(2023)  # returns False
is_leap_year(2024)  # returns True
