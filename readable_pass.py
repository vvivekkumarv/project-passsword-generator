import random

wordlist=[]
special_char=['&','*','$','#','@']


with open("wikipedia.txt",'r') as file:
    read=file.readlines()

    for line in read:
        lines=line.split()

        for item in lines:
            if(len(item)>5):
                wordlist.append(item.capitalize())

word=random.choice(wordlist)
char=random.choice(special_char)
num=str(random.randint(10,99))
password=word+char+num
print(password)
