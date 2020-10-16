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

main()