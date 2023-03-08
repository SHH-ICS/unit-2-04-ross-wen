# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

result = ""
for myNumber in range(1,33):
    if myNumber%3 == 0:
        if myNumber%5 == 0:
            result = str(result) + str("Fizzbuzz") + "\n"
        else:
            result = str(result) + str("Fizz") + "\n"
    elif myNumber%5 == 0:
        result = str(result) + str("Buzz") + "\n"
    else:
        result = str(result) + str(myNumber) + "\n"
print(result)
