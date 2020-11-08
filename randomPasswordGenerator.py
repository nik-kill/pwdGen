import random,string

def password(length, num=False,strength='weak'):
    """length of password, if you want number 
    and strength(weak, strong, very)"""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    dig = string.digits
    punct = string.punctuation
    pwd = ''
    if strength=='weak':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(lower)
    elif strength=='strong':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(letter)
    elif strength=='very':
        ran = random.randint(2,4)
        if num:
            length -= ran
            for i in range(ran):
                pwd += random.choice(dig)
        length -= ran
        for i in range(ran):
            pwd += random.choice(punct)
        for i in range(length):
            pwd += random.choice(letter)
    pwd = list(pwd)
    random.shuffle(pwd)
    pwd = ''.join(pwd)
    return pwd

print(password(5,num=True))
print(password(10, num=True, strength='strong'))
print(password(15, num=True, strength='very'))

#bonus
"""
student = ['john','sam','steve','bob']
grade = [6,7,7,8]

classes = list(zip(student,grade))
print(classes)
new_students, grades = zip(*classes)
print(new_students)
print(grades)

"""
"""
x = 'help'
x.center(50,'#')

"""