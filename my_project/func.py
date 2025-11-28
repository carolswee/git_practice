#function to print a list of names
def func(names):
    for name in names:
        print(name)
   


list1=['carol','ann','jay','rose']
func(list1)

#function to remove duplicates from a list
def remove_duplicates(random_list):
    new_list=list(set(random_list))
    return new_list

cars=['vitz','demio','vitz','subaru']
print(remove_duplicates(cars))
