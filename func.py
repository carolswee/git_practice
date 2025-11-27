#function to print a list of names
def func(list):
    for name in list:
        print(name)
    return func


list1=['carol','ann','jay','rose']
print(func(list1))

