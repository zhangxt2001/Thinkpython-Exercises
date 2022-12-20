# Exercises from section 9.2 in the book
from itertools import combinations
import string
# 9.1
def print_twenty(filename):
    '''
>>> print_twenty("words.txt")
counterdemonstrations
hyperaggressivenesses
microminiaturizations
'''
    obj = open(filename,'r')
    for line in obj:
        word = line.strip() # removing the \n character in the word
        if len(word)>20:
            print(word)
    obj.close()

# 9.2

def has_no_e(my_str):
    for value in my_str:
        if value == 'e':
            return False
    return True

def no_e_word(filename):
    '''
>>> no_e_word('words.txt')
the percentage of words that do not have e is 33.06%
'''
    obj = open(filename,'r')
    counter = 0
    total = 0 
    for line in obj:
        total += 1
        word = line.strip()
        if has_no_e(word):
            counter += 1
    print('the percentage of words that do not have e is' , str(round((counter/total)*100,2))+'%')
    obj.close()

# 9.3
def avoid(my_word, my_list):
    for value in my_word:
        if value in my_list:
            return False
    return True

def count_no_words(filename,forbid):
    '''
returns the number of words that don't contain letters in
forbid string (any 5 letters in the alphabet)
'''
    obj = open(filename,'r')
    counter = 0
    for_list = []
    for char in forbid:
        for_list.append(char)
    for line in obj:
        word = line.strip()
        if avoid(word, for_list):
            counter += 1
    obj.close()
    return counter

def min_words(filename):
    '''
>>> min_words('words.txt')
[110409, 'jq']
This means the combination jq is the rarest in the entire file
'''
    alphabet = list(string.ascii_lowercase)
    comb = combinations(alphabet,2)
    init_list = [0,'origin']
    for i in list(comb):
        l1,l2 = i
        comb_str = l1+l2
        num = count_no_words(filename,comb_str)
        if num > init_list[0]:
            init_list[0] = num
            init_list[1] = comb_str
    return init_list

# 9.4
def uses_all(my_word,my_letters):
    ''' 
my_letters need to be a string
'''
    for value in list(my_word):
        if value not in list(my_letters):
            return False
    return True
    
# 9.5
def is_abecedarian(my_word):
    '''
Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok).

'''
    alphabet = list(string.ascii_lowercase)
    alpha_dict = {}
    for i,letter in enumerate(alphabet):
        alpha_dict[letter]=i
    init_i = alpha_dict[my_word[0]]
    for value in my_word:
        if alpha_dict[value] < init_i:
            return False
        else:
            init_i = alpha_dict[value]
    return True