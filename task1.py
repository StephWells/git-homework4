def is_prime( number ):
    evenDivisionsCounter = 0
    if number <= 1:
        return False
    for thisNumber in range( 1, number + 1 ): # plus one because the range will not include the last number
        if number % thisNumber == 0:
            evenDivisionsCounter = evenDivisionsCounter + 1
            if evenDivisionsCounter > 2:
                return False
    return True  

def main():
    usersNumber = int(input("Please enter a number: "))
    print()
    if is_prime(usersNumber):
        print(usersNumber, 'IS a prime number')
    else:
        print(usersNumber, 'IS NOT a prime number')
    print()
    print('Now I will randomly generate 6 numbers and I will determine if they are prime numbers...')
    print()
main()

def random():
    import random
    random1 = random.randint(1,100)
    random2 = random.randint(1,100)
    random3 = random.randint(1,100)
    random4 = random.randint(1,100)
    random5 = random.randint(1,100)
    random6 = random.randint(1,100)

    if is_prime(random1):
        print('The random number', random1, 'is a prime number.')
    else:
        print('The random number', random1, 'is not a prime number.')
    if is_prime(random2):
        print('The random number', random2, 'is a prime number.')
    else:
        print('The random number', random2, 'is not a prime number.')
    if is_prime(random3):
        print('The random number', random3, 'is a prime number.')
    else:
        print('The random number', random3, 'is not a prime number.')
    if is_prime(random4):
        print('The random number', random4, 'is a prime number.')
    else:
        print('The random number', random4, 'is not a prime number.')
    if is_prime(random5):
        print('The random number', random5, 'is a prime number.')
    else:
        print('The random number', random5, 'is not a prime number.')
    if is_prime(random6):
        print('The random number', random6, 'is a prime number.')
    else:
        print('The random number', random6, 'is not a prime number.')
random()
