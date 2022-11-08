import numpy as np

# Assaienment 1

""" input_list_helper function()
 input_list_helper for collecting the user input
    :return: list of numbers that were given
 calculate their sum and return it as a list
 the last object is the sum of all the others
 :return: result
"""


def input_list_helper(lst):

    x = len(lst)
    result = 0.0
    while x != 0:
        result = float(result) + float(lst[x-1])
        x = x - 1

    return result


"""
user_list() function
return input text
collects numbers from user input

"""


def user_list(input_text):
    lst = []
    x = len(input_text)

    while x != 0:
        lst.append(input_text[x-1])
        x = x - 1

    return lst


# input numbers
lst = []

while True:
    try:

        input_text = input()
        # input string
        lst = user_list(input_text)
        print(input_list_helper(lst))
        break
    except ValueError:
        print("Please enter numbers example 2188 88123 123")

#Assienment 2 ########################################


def check_monotonic_sequence(sequence):

    sequence.append(0)

    x = len(sequence)

    result = [True]*4


    for i in range(x-1):
        if sequence[i] < sequence[i+1]:
            result.append(False)

    for i in range(x-1):
        if sequence[i] > sequence[i+1]:
            result.append(False)

    return result


#data = [1, 2, 3 , 3]
#data = [1, 2, 3, 4, 5, 6, 7, 8]
data = [1, 2, 2, 3]
#data = [1, 1, 1, 1]

# call check_monotonic_sequence(sequence) function

result = check_monotonic_sequence(data)

print(result)

#3 ##############################


def myfunction(num):
    # define a flag variable
    flag = False
    num = int(num)
# prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

# check if flag is True
    if flag != True:
        return num

    if flag:
        #print(num, "is not a prime number")
        return None

    else:
        #print(num, "is a prime number")
        return num


# Program to check if a number is prime or not
def primes_generator(n):
    q = []
    if n == 0:
        return q
    x = 0
    Flag = True
    for i in range(9999):
     q.append(myfunction(i+2))
     if (q[i] != None):
        x = x + 1

     if (x == n):
      q = [i for i in q if i != None]
      return q




#4 vector


#check if a vector list is empty

def is_empty_vecotr(vec_lst):
    #vec_lst = np.vec_lst([])

    #True when empty and False when not
    flag = not np.any(vec_lst)

    if flag:
        return ("Array is empty")
    else:
        return vec_lst

# vectors_list_sum(vec_lst) returns a vector of their sum


def vectors_list_sum(arr):

    arr = np.array(arr)
    
    if arr.shape[0] == 2:
        vec_sum = np.sum(arr, axis=0)
        return vec_sum
   
    elif arr.shape[0] == 3:
        vec_sum = np.sum(arr, axis = 0)
        return vec_sum
          
# 5 Orthogonal vectors


def calc_the_inner_product(vec_1, vec_2):

   vec_1 = np.array(vec_1)
   vec_2 = np.array(vec_2)

   

   count = np.multiply(vec_1, vec_2)

   return count





""" gets two list, calculates their inner
        product and returns it

    :param vec_1: list of numbers
    :param vec_2: list of numbers
    :return: the inner product of the two lists.
    """


def orthogonal_number(vectors):

    arr = np.array(vectors)
    
    n = arr.shape[0]
    arr = np.array_split(arr, n)  

    for i in range(n):
        arr[i] = np.array(arr[i])

    vec1 = []
    vec2 = []
    vec3 = []
    vec4 = []
    vec5 = []
    temp_array = []
    if n == 3:
       vec1 = np.array(arr[0])
       vec2 = np.array(arr[1])
       vec3 = np.array(arr[2])
       temp_array.append(calc_the_inner_product(vec1, vec2))
       temp_array.append(calc_the_inner_product(vec2, vec3))
       temp_array.append(calc_the_inner_product(vec1, vec3))
    elif n == 4:
       vec1 = np.array(arr[0])
       vec2 = np.array(arr[1])
       vec3 = np.array(arr[2])
       vec4 = np.array(arr[3])
       temp_array.append(calc_the_inner_product(vec1, vec2))
       temp_array.append(calc_the_inner_product(vec2, vec3))
       temp_array.append(calc_the_inner_product(vec3, vec4))
       temp_array.append(calc_the_inner_product(vec1, vec4))
       temp_array.append(calc_the_inner_product(vec1, vec3))
       temp_array.append(calc_the_inner_product(vec2, vec4))
       temp_array.append(calc_the_inner_product(vec2, vec4))
    elif n == 5:
        vec1 = np.array(arr[0])
        vec2 = np.array(arr[1])
        vec3 = np.array(arr[2])
        vec4 = np.array(arr[3])   
        vec5 = np.array(arr[4])

        temp_array.append(calc_the_inner_product(vec1, vec2))
        temp_array.append(calc_the_inner_product(vec1, vec3))
        temp_array.append(calc_the_inner_product(vec2, vec3))
        temp_array.append(calc_the_inner_product(vec2, vec4))
        temp_array.append(calc_the_inner_product(vec2, vec5))
        temp_array.append(calc_the_inner_product(vec3, vec4))
        temp_array.append(calc_the_inner_product(vec3, vec5))
        temp_array.append(calc_the_inner_product(vec4, vec1))
        temp_array.append(calc_the_inner_product(vec4, vec5))
        


   # print(temp_array)
    q = 0
    if (np.array_equal(temp_array[0],temp_array[1])):
        q = q + 1
    elif (np.array_equal(temp_array[1], temp_array[2])):
        q = q + 1
    elif (np.array_equal(temp_array[0], temp_array[2])):
        q = q + 1

    return str(q)



