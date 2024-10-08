def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    if word == word[::-1]:
        return True
    return False

print(lab2Question1("racecar"))

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    a = 0
    b = 1
    c = b
    
    while b <= number_val:
        print(a)
        a += b
        a, b = b, c
        c = a + b
    return a

print(lab2Question2(13))

def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    num_of_times = (str1.count(str2))
    return num_of_times
    
print(lab2Question3("sally sale: salt", "sa"))
    
def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    if len(list1) == len(list2):
        sum_list = [list1[i] + list2[i] for i in range(len(list1))]
    else:
        return[]
    return sum_list

print(lab2Question4([1, 2, 3], [1, 2, 3]))

def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    if len(input()) < 8:
        return "Enter a password"
    for char in input():
    elif char.password:
        
    else:
        isValidPassword(input)

    return password

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    if input == password:
        return True
    else:
        return False


