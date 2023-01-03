'''
##########Sample Input##########

S;M;plasticCup()

C;V;mobile phone

C;C;coffee machine

S;C;LargeSoftwareBook

C;M;white sheet of paper

S;V;pictureFrame

#######Sample Output#################

plastic cup

mobilePhone

CoffeeMachine

large software book

whiteSheetOfPaper()

picture frame


'''
s = input().rstrip()
op,clas,word = s.split(';')
if op == 'S':
    if clas == 'M' or clas == 'V':
        if clas == 'M':    
            word = word[:-2]
        index = -100
        for i in range(len(word)):
            if word[i].isupper():
                index = i
        print(word[:index],word[index:].lower())
    elif clas == 'C': 
       index_list = []
       for i in range(len(word)):
            if word[i].isupper():
                index_list.append(i)
       new_string = ''
       for i in range(1,len(index_list)):
            new_string +=word[index_list[i-1]:index_list[i]].lower()
            new_string += ' '
       new_string += word[index_list[len(index_list)-1]:].lower()
       print(new_string)
elif op == 'C':
    if clas == 'M' or clas == 'V':
        word_list = word.split()
        new_string = ''
        for i in range(0,len(word_list)):
            if i == 0:
                new_string += word_list[i]
            else:
                new_string += word_list[i].capitalize()
        if clas == 'M':
            new_string += '()'
        print(new_string)
    elif clas == 'C':
        word_list = word.split()
        new_string = ''
        for i in range(0,len(word_list)):
            new_string += word_list[i].capitalize()
        print(new_string)
