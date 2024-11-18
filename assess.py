def grade_average(grades):
    """ Write a program that returns the average number of a given list of grades.
    It should not add any negative grades to the average.

    Args:
        grades (list): List of grades to calculate
    """
    
    if not all(isinstance(grade, int) for grade in grades):
        return "Items in list must be integers"
    
    if len(grades) == 0:
        return -1
    
    total = 0
    neg_count = 0
    
    for grade in grades:
        grade = int(grade)
        
        if grade < 0: neg_count += 1
        
        if grade > 0: total += grade
        
    divisor = len(grades) - neg_count
        
    if divisor == 0:
        return total
    else:
        return total / divisor

def find_prime_factors(number):
    """
    Write code to return the prime factors of the number. 

    Args: number (int): Number to find the prime factors of
    """
    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
            
        return True

    prime_factors = []
    
    for i in range(2, number + 1):
        if number % i == 0:
            if is_prime(i):
                prime_factors.append(i)
            
    return prime_factors

def calculate_interest(principal, rate, years):
    """Write a program that returns the compound interest

    Args:
        principal (int): The principal amount
        rate (int): The interest rate
        years (int): The amount of years to calculate the interest for
    """
    
    return principal * (1 + rate) ** years

def code_word(code):
    """Write a program that returns the word given a code.

    e.g. Given code: [3,1,20]
    Expected Word: "cat"

    Args:
        code (list): The code to decipher
    """
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded = []
    
    for i in code:
        if (i == 0):
            decoded.append(" ")
        else:
            decoded.append(alphabet[i - 1])
        
    return "".join(decoded)

def triangles(length):
    """Write a program that returns a triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    ** 
    ***
    ****
    *****

    Args:
        length (int): The ;ength your triangle should be
    """
    
    result = []
    
    for i in range(length):
        result.append("*" * (i + 1))
        
        if i != length - 1:
            result.append("\n")
        
    return "".join(result)
        
def hollow_triangle(length):
    """Write a program that returns a hollow triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    * *
    *  *
    *****

    Args:
        length (int): The ;ength your triangle should be
    """
    
    result = []
    
    for i in range(length):
        if i == 0 or i == length - 1:
            result.append("*" * (i + 1))
        else:
            result.append("*" + " " * (i - 1) + "*")
            
        if i != length - 1:
            result.append("\n")
        
    return "".join(result)

# There are no tests for this function so test by running the program. 
def number_guessing(number):
    """Write a guessing game. The player has 10 opprtunites to guess.

    e.g. Number: 4
         User Input: 5
         Output: Incorrect

         Number: 4
         User Input: 4
         Output: Correct

    Args:
        number (int): The number to be guessed
    """
    
    is_correct = False
    
    for _ in range(2):
        guess = int(input("Enter your guess: "))
        
        if guess == number:
            print("Correct")
            is_correct = True
            break
        else:
            print("Incorrect")
     
    if not is_correct:    
        print("Game Over: You have run out of guesses")
        

