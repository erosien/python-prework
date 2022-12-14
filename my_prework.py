## Question 1

def hello_name(user_name):
    """Print a greeting"""
    print("hello_" + user_name + "!")

hello_name("USERNAME")

## Question 2
def first_odds():
    """Print odd numbers 1-100"""
    for value in range(1,101,2):
        print(value)

first_odds()

## Question 3
def max_num_in_list(a_list):
    """Return max number in list"""
    return max(a_list)

num = max_num_in_list([1, 4, 55, 120, 358, 1000])
print(num)

## Question 4
def is_leap_year(a_year):
    """Return if the given year is a leap year"""
    x = a_year
    if x % 4 == 0 and x % 100 != 0:
        return True
    elif x % 400 == 0:
        return True
    else:
        return False

this_year = is_leap_year(2022)
print(this_year)

## Question 5
def is_consecutive(a_list):
    maximum = max(a_list)
    if sum(a_list) == maximum * (maximum + 1) / 2:
        return True
    else:
        return False

answer = is_consecutive([1, 2, 3, 4, 5])
print(answer)