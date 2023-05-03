Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

#task01
#1.1
Names_upper=[]
for n in Names:
    Names_upper.append(n.upper())
#print(Names_upper)
#1.2
Names_list = [n.upper() for n in Names ]
#print(Names_list)
#1.3
def names_uper(Names):
    Names_list = [n.upper() for n in Names ]
    print(Names_list)
#2.1
Names_a=[]
for n in Names:
    if "a" in n:
        Names_a.append(n)
#print(Names_a)
#2.2
Names_a = [n for n in Names if "a" in n]
#print(Names_a)

#2.3
def is_a(Names):
    Names_a=[]
    for n in Names:
        if "a" in n:
            Names_a.append(n)
    print(Names_a)

#3.1
Names_t=[]
for n in Names:
    if "t" == n[0]:
        Names_t.append(n)
#print(Names_t)

#3.2
Names_t = [n for n in Names if 't'== n[0]]
#print(Names_t)
#3.3
def start_with(Names):
    Names_t=[]
    for n in Names:
        if "t" == n[0]:
            Names_t.append(n)
    return Names_t

#4.1
Names_2a=[]
count=0
for n in Names:
    for i in n :
        if "a" == i:
            count +=1
    if count >= 2:
        Names_2a.append(n)
    count =0
#print(Names_2a)

#4.2
Names_2a = [n for n in Names if n.count('a') >= 2  ]
#print(Names_2a)

#4.3
def double_a(Names):
    Names_2a=[]
    count=0
    for n in Names:
        for i in n :
            if "a" == i:
                count +=1
        if count >= 2:
            Names_2a.append(n)
        count =0
    return(Names_2a)

#5
Names_len=[]
for n in Names:
    Names_len.append(len(n))
#print(Names_len)

#5.1
Names_len=[len(n) for n in Names ]
#print(Names_len)

#5.3
def Names_len(Names):
    Names_len=[]
    for n in Names:
        Names_len.append(len(n))
    return Names_len
#7
a,*b=Names
# print("a: ",a)
# print("b: ",b)
#8
a,*b,c = Names
# print("a: ",a)
# print("b: ",b)
# print("c: ",c)

#9
a,b,*c = Names
print("a: ",a)
print("b: ",b)

    



