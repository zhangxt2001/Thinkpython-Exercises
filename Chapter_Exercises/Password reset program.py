import string

def password():
    '''
()->str
Checking the validity of password
Only accepting a new password if:
1. At least eight characters long
2. Has lower case and upper case letters
The program would also ask the password twice
'''
    first = input('Please input the password :')
    second = input('Please confirm your password:')
    while first != second:
        print ('Two passwords are inconsistent, please check again')
        second = input('Please confirm your password:')
    if len(first) < 8:
        raise ValueError('Password should not be less than 8 characters long')
    if not((first.lower()).islower()):
        raise ValueError('Password needs to contain at least one letter')
    if not(first.isupper() != first and first.islower() != first):
        raise ValueError ('Password must contain both lower/upper case letters')
    print('Password reset successful !')
    return first

def strength(my_string):
    '''
(str)->...
Returns the strength of the password
The definition of strength is as follows:
There are three big categories:
(letter, number, special character)
1. containing only one category - weak
2. containing two categories - medium
3. containing three categories - strong
'''
    special = string.punctuation
    number = string.digits
    letter = string.ascii_letters
    type_counter = 0
    type_rec = []
    for value in my_string:
        if value in letter:
            if 'letter' not in type_rec:
                type_counter += 1
                type_rec += ['letter']
            else:
                continue
        elif value in number:
            if 'number' not in type_rec:
                type_counter += 1
                type_rec += ['number']
            else:
                continue
        elif value in special:
            if 'special' not in type_rec:
                type_counter += 1
                type_rec += ['special']
            else:
                continue
    if type_counter == 3:
        print('This password is strong')
    elif type_counter == 2:
        print('This password is medium')
    else:
        print('This password is weak')
        
def read_file(filename='password.txt'):
    '''
Read the password file and returns a dictionary
containing the account name and password

Assuming the password file takes the following form:
John_Smith Johnsmith2000
i.e. the username cannot have space and a space separates the
password and the username
'''
    obj = open(filename,'r')
    password_dict = dict()
    for line in obj:
        comb = line.strip()
        user = comb.split()
        password_dict[user[0]] = user[1]
    obj.close()
    return password_dict

def validate_username(my_dict):
    '''
Check if the username exists, and if it does exist
let user input old password. And if it matches then return True
'''
    username = input("Please input your username: ")
    if username in my_dict.keys():
        print("Username exists please now input your old password: ")
        password = input("Please input your old password: ")
        if password == my_dict[username]:
            print("Password inputted matches the old password on file")
            return True,username
        else:
            print("Password doesn't match with the old password on file")
            return False,username
    else:
        print("username doesn't exist")
        return False,username

def save_dict(filename,my_dict):
    obj = open(filename,'w')
    for key in my_dict:
        my_string = key+' '+my_dict[key]+'\n'
        obj.write(my_string)
    obj.close()


def password_changer():
    password_dict = read_file()
    user_result, username = validate_username(password_dict)
    counter = 0
    while not user_result:
        print("Input your username again")
        user_result, username = validate_username(password_dict)
    new_password = password()
    strength(new_password)
    password_dict[username] = new_password
    save_dict('password.txt',password_dict)
    print("All done ! The password has been changed")
    