import random
import time

# 10.8 birthday paradox
def generate_birthday(num=23):
    '''
(int)->list<str>
num is the number of random birthdays to
generate
'''
    return_list = []
    for i in range(num):
        month = random.randint(1,12)
        if month in [1,3,5,7,8,10,12]:
            date = random.randint(1,31)
        elif month == 2:
            date = random.randint(1,28) # assume feb always have 28 days
        else:
            date = random.randint(1,30)
        birthday = str(month).zfill(2) + str(date).zfill(2)
        return_list.append(birthday)
    return return_list

def count_match(my_list):
    counter = 0
    counted_list = []
    for value in my_list:
        if value in counted_list:
            continue
        if my_list.count(value)>1:
            counter += 1
            counted_list.append(value)
    return counter

def check_match(num):
    '''
compute the number of at least one match of birthday
for a specified number of iterations
>>> check_match(10000)
50.78 % out of total 10000 iterations have at least one match
>>> check_match(100000)
50.564 % out of total 100000 iterations have at least one match
so the answer is around 50 percent, which is expected
'''
    counter = 0
    for i in range(num):
        if count_match(generate_birthday())>=1:
            counter += 1
    print(str((counter/num)*100),'%','out of total',num,'iterations have at least one match')

# 10.9 Comparing the time of append method and list concact
def words_append(filename):
    '''
>>> words_append("words.txt")
the time it takes to append is0.023967981338500977s

'''
    time_start = time.time()
    obj = open(filename,'r')
    words_list = []
    for line in obj:
        word = line.strip()
        words_list.append(word)
    time_end = time.time()
    print("the time it takes to append is" + str(time_end-time_start)+"s")

def words_append_2(filename):
    '''
>>> words_append_2("words.txt")
the time it takes to append is0.022937774658203125s
# so as it turns out, concentanate is faster
# because append() can cause python to allocate more memory, which takes time. 
'''
    time_start = time.time()
    obj = open(filename,'r')
    words_list = []
    for line in obj:
        word = line.strip()
        words_list += [word]
    time_end = time.time()
    print("the time it takes to append is" + str(time_end-time_start)+"s")

# 10.10 Binary search for a specific word in a list

def in_bisect(my_list, word):
    '''(list,str)->Boolean
This list doesn't have be sorted. The function returns True if a
specified word if the word is in the list False otherwise
'''
    my_list.sort() # sorting the list based on words' first letter
    start = 0
    end  = len(my_list)-1
    while start <= end: # two strings are compared alphabetically
        middle = (start+end)//2
        if word < my_list[middle]:
            end = middle-1
        elif word > my_list[middle]:
            start = middle+1
        else:
            return True
    return False

# 10.11 reverse pair

def make_word_list():
    '''auxiliary function
that makes a word list from words.txt if called
returning a list
'''
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

def finding_reverse(my_list):
    '''s = ['hello', 'hi', 'how','ih','woh']
>>> finding_reverse(s)
[('hi', 'ih'), ('how', 'woh')]
'''
    result_list = []
    for value in my_list:
        reversed_word = value[::-1]
        if in_bisect(my_list, reversed_word):
            if ((value,reversed_word) not in result_list) and ((reversed_word,value) not in result_list):
                result_list.append((value,reversed_word))
    return result_list