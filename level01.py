#Level One
#task 01
def odd_even(a,b):
    odd_numbers=[]
    even_numbers=[]
    for i in range(a,b+1):
        if i%2 != 0:
            odd_numbers.append(i)
        else :
            even_numbers.append(i)
    print(odd_numbers)
    print(even_numbers)

#task 02
def divided_by_handred(a,b):
    result=[]
    for n in range(101):
        if n%a ==0 and n%b ==0:
            result.append(n)
    print(result)

#task 03
def multiblication_table(a,b):
    for n in range(a,b+1):
        print(f'table of {n} ')
        for i in range(1,10):
            print(f'{n}  X  {i}  =  {n*i}')
    
#task 04
def duplicate_sentence(sentence):
    words = sentence.split()
    result = set(words)
    print(' '.join(result))
#task 05
def words_count(sentence):
    words = sentence.split()
    print(len(words))

#task 06
def remove_word(sentence,word):
    words = sentence.split()
    for i in words:
        if i == word:
            words.remove(word)
    print(' '.join(words))

#task 07
def count_word(sentence,word):
    counter=0
    words = sentence.split()
    for i in words:
        if i == word:
            counter +=1
    print(f'the word {word} is repeat {counter} time(s) !')

#task 08
def divide_by(x,y):
    result=[]
    for n in range(x,100+1):
        if n%y == 0:
            result.append(n)
    print(result)


