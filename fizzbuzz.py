"""
Print numbers from 1 to n, when it's divisible by 3 print "Fizz", 
when divisible by 5 print "Buzz", when divisible by 3 and 5 print "FizzBuzz",
Do this using 4 threads:
(1) checking for divisibility 3, printing "Fizz"
(2) checking for divisibility by 5 printing "Buzz"
(3) Checking for divisibility by 3 and 5 printing "FizzBuzz"
(4) Printing all the numbers
"""
import threading


def fizzbuzz(n: int):

    t1 = threading.Thread(target=check_div_by_three, args=range(n))
    t3 = threading.Thread(target=check_div_by_five, args=range(n))
    t2 = threading.Thread(target=check_div_by_three_and_five, args=range(n))

    t1.start()


def print_fizz(n):
    for i in range(n):
        if check_div_by_three_and_five(i):
            print("FizzBuzz")
        elif check_div_by_three(i):
            print("Fizz")
        elif check_div_by_five:
            print()


def check_div_by_three(n):
    return n % 3 == 0


def check_div_by_five(n):
    return n % 5 == 0


def check_div_by_three_and_five(n):
    return check_div_by_three(n) and check_div_by_five(n)


def print_numbers(n):
    for i in range(n):
        print(i)
