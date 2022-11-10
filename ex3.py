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

def array_refarence():

    arr_ref = [0, 1, 0, -1]

    return arr_ref

def check_monotonic_sequence(sequence):
    
    arr_ref = [0, 1, 0, -1]

    lst = sequence

    q = [False]*4

    for i in range(len(arr_ref)-1):
        if arr_ref[i] >= lst[i]:
            q[i] = True
        elif arr_ref[i] > lst[i]:
            q[i] = True
        elif arr_ref[i] <= lst[i]:
            q[i] = True
        elif arr_ref[i] < lst[i]:
            q[i] = True

    return q

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


def calc_the_inner_product(arr1,arr2):

   len_arr1 = len(arr1)
   len_arr2 = len(arr2)

   arr1 = np.array(arr1)
   arr2 = np.array(arr2)

   
   if np.shape(arr1) != np.shape(arr2):
      if len(arr1) == 0 or len(arr2) == 0:
          return None
      elif np.shape(arr1) < np.shape(arr2):
        arr1 = np.full(np.shape(arr2),fill_value = "",dtype=int)
      elif np.shape(arr1) > np.shape(arr2):
            arr2 = np.full(np.shape(arr1),fill_value = "",dtype=int)
        
   
   count = np.multiply(arr1, arr2)

   total = np.sum(count)

   return total


def function_skip_same_array(Flag_array, a, b):

  if a == b == 0 or Flag_array == [] or a == b:
    return False
  elif len(Flag_array) <= 2:
    return False
  else:     
  
    lst = Flag_array

    lst.reverse()

    #lst_revarce = lst(reversed(lst))
    
    lst_revarce = np.array(lst)
    lst_revarce_len = int(len(lst))
    lst_revarce = np.array_split(lst_revarce, (lst_revarce_len/2))

    #Swap a, and b
    temp1 = a 
    temp2 = b
    a = temp2
    b = temp1    


    arr = np.array([a, b])

    for i in range(int((lst_revarce_len)/2)):
        if np.array_equal(arr[i], lst_revarce[i]):
        #if arr[i] == lst_revarce[i]:
            return True
        else:
            return False    

def orthogonal_number(vectors):
    arr = np.array(vectors, dtype=int)
    

    n = arr.shape[0]
    arr = np.array_split(arr, n)

    for i in range(n):
        arr[i] = np.array(arr[i])
   
    count = 0
    Flag_no_repit = []
    #Flag_no_repit = np.array(Flag_no_repit,dtype=int)
    
            
    for x in range(len(vectors)):
            for y in range(len(vectors)):
                if function_skip_same_array(Flag_no_repit, x, y) == False:
                    if x != y:
                        if calc_the_inner_product(arr[x], arr[y]) == 0:
                            count = count + 1
                            Flag_no_repit.append(x)
                            Flag_no_repit.append(y)
                            #np.append(Flag_no_repit, x) #
                            #np.append(Flag_no_repit, y) #
                            continue 

    return (count/2)
            
                
