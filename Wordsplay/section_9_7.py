# 9.7
def is_triple_double(my_string):
    ''' determining if a word contains
three consecutive letter pairs. Returning
True if they do contain them.
'''
    counter = 0
    i = 0
    while i < len(my_string)-1:
        if my_string[i] == my_string[i+1]:
            counter += 1
            i += 2
        else:
            i += 1
    return counter == 3

def find_triple_word(filename):
    '''
Reads a file and then print the word that
contains triple letter pairs. Used the function written
just above.
'''
    obj = open(filename,'r')
    for line in obj:
        word = line.strip()
        if is_triple_double(word):
            print(word)

# 9.8
def is_palindromic (num,start_i,end_i):
    '''
(int,int,int)->Boolean
'''
    num_str = str(num)[start_i : end_i+1]
    return num_str[::-1] == num_str

def check_number(num):
    return (is_palindromic(num,2,5) and
            is_palindromic(num+1,1,5) and
            is_palindromic(num+2,1,4) and is_palindromic(num+3,0,5))
    
def check_six_digit():
    '''
The solution for that is:
>>> check_all()
198888
199999
'''
    init_num = 100000
    while init_num < 1000000:
        if check_number(init_num):
            print(init_num)
        init_num += 1

# 9.9
def reversible(num1,num2):
    '''checks if two numbers are
reversible. Returns true if they are.
'''
    return str(num1).zfill(2)[::-1] == str(num2).zfill(2)

def num_reversible():
    '''
>>> num_reversible()
(10, 0)
(9, 9)
(8, 18) # therefore, 18 might be the answer seeing the ages are reversible for eight times
(7, 27)
(6, 36)
(5, 45)
(4, 54)
(3, 63)
(2, 72)
(1, 81)
'''
    for i in range(0,100): #age difference between mom and son
        son = 0
        mom = i
        counter = 0
        while mom < 100:
            if reversible(son,mom):
                counter += 1
            mom += 1
            son += 1
        if counter != 0:
            print((counter,i))

def print_age():
    '''
>>> print_age()
[(2, 20), (13, 31), (24, 42), (35, 53), (46, 64), (57, 75), (68, 86), (79, 97)]
These are all the times that their ages are reversible
'''
    son = 0
    mom = 18
    result_list = []
    while mom < 100:
        if reversible(son,mom):
            result_list.append((son,mom))
        mom += 1
        son += 1
    return result_list