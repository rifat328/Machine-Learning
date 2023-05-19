from csv import DictWriter, DictReader
from csv import writer
mycars = ['Bugaty Chiron', 'Bugaty vayron', 'ferary fiyasta', 'meclaren p1']
mycars = mycars
abc = 'bangla vasa'
# function for car separation


def cars_sep(cars):
    for car in cars:
        return car.title()


def titlecase(cars):
    for car in cars:
        return car.title()


abc.title()  # title case
print(abc.title())
Samins_Cars = ['volvo', 'tesla', 'bmw m1']

print("=========================================== 01 =================================================")
total_cars = mycars[:]
total_cars.append(Samins_Cars[0:])
print(total_cars)

# tuple constent type, imutable
dimensions = (20, 40, 30, 90)
print(dimensions[2:])
# items(),get(),keys(),values() functions for dictionary
# set( ) returns unique items.
#dictionary in dictionary , dictionary in list, linst in dictionary
google_salary = (12000, 12100, 500000, 130000)
print(f'Total google_salary :{len(google_salary)}')
i = 0
for salary in google_salary:
    print(f'monthly income of an google employee:{i+1} {salary / 12}')
    i += 1
    # google_salary.append((salary/12)) tuple object cant have append
print(total_cars)
print(total_cars[-1])
print(total_cars[-2])
print("############################################################### checkpoint ###############################")
for i in total_cars:
    print(i.title())
   # print(total_cars.sort()) #dosent work that way result different
    # for sorted() used to store that return result to a variable
    # like  a=sorted(b) where b= [3,4,5,1,4]
    print(total_cars.sort)
# string sorta and reverse practice
a = [1, 2, 3, 6, 4, 5, 6, 7]
print(a)
print(a.sort())
print('print a again', a)
b = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print('print b', b)
c = sorted(b)
print(b)
print('sorted b stored in b', c)
c.sort(reverse=True)
print('sorted b stored in b in reverse', c)
c.insert(0, 100)
print(sorted(c))
print(len(c))
del c[9]
print(c)
c.pop()  # will pop last element
c.pop(0)
print(c)
print(Samins_Cars)
Samins_Cars.remove('volvo')
Samins_Cars.reverse()
print(Samins_Cars)
print('volvo' in Samins_Cars)
if 'bugati' not in Samins_Cars:
    print('ypu can not drive bugati')
requested_toppings = ['a', 'b', 'c']
available_toppings = ['c', 'd', 'e']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        added = [].append(requested_topping)
    else:
        print('its not abailable')

numbers = list(range(1, 6))
print(numbers)
print(list(range(2, 11, 2)))
print(
    f'statisticsa min: {min(numbers)} , max: {max(numbers)}, summation {sum(numbers)}')

# list_comprihension
squares = [value**2 for value in range(2, 50, 2)]
print(squares)
# dictionary practice
# dictionary is a key value payer
rifat = {'position': 'software Engineer', "business": 'pharmecy'}
dic1 = rifat['position']
dic1_2 = rifat['business']
print(f'rifat is a {dic1} and \n he also own businesses related to {dic1_2}')
# list under dictionary
rifat_hossain = {'positions': ['software Engineer', 'Machine Learning Engineer', 'Data Scientist', 'CEO', 'Researcher'],
                 'business': ['Software Company', 'pharmecy']}
dic2 = rifat_hossain['positions']
dic2_2 = rifat_hossain['business']
print(
    f'Mister rifat has these {dic2} titels \n and he owns these businesses : {dic2_2}')
# adding key and value to an existing dictionary
rifat['hobby'] = 'programming'
print(rifat)
rifat_hossain['hobby'] = 'programming'

#    rifat_hossain['hobby'].append('Book reading')
print(rifat_hossain['hobby'])

# get() function to know if that value exist or not
print(rifat.get('age', 'age dosent exist'))

# The method items(), which returns a list of key-value pairs .....loop through
for position, business in rifat.items():
    print(position, business)

# kays() ...2 ways to do things , same shit
for keys in rifat:
    print(keys)
for n in rifat.keys():
    print(n)
# values()   print values
print("---------------------------------------------------------------------------------------")
print(rifat.values())
for value in rifat.values():
    print(value)
print("---------------------------------------------------------------------------------------")
# A set is a collection in which each item must be unique:
fevorite_language = {'a': 'python', 'b': 'python', 'c': 'c++', 'd': 'java'}
for language in set(fevorite_language.values()):
    print(language.title())
# also define set by coma
nana = {'nani', "nani", "nana", 'nani'}
print(nana)
print("----------------------------------Last Side test-------------------------------------------")

vaivai = [1, 2, 3, 4]
courses = []
for vaiva in vaivai:
    courses.append(input(f'name vai {vaiva}'))
print(courses[:])
print("---------------------------------------------------------------\n\n\t")


def check2(name, code, pre_req):
    input_arg = []

    input_arg.append(name)
    input_arg.append(code)
    input_arg.append(pre_req)

    with open('course_data_updated.csv', 'r') as file:

        csv_reader = DictReader(file, lineterminator='\n')
        for row in csv_reader:
            if row['Pre-Requisite'].split() == input_arg:
                # return True
                print('this Course Exist\n')
                '''print('this Course Exist\n')'''
    print('this Course Exist\n')


name = 'DISCRETE MATHEMATICS'
code = 'CSC1204'
pre_req = 'MAT1102  CSC1102'
check2(name, code, pre_req)
# ---------------------------------------------------------------------------------------------------------------
'''
with open('course_data_updated.csv', 'r') as file:

        csv_reader = DictReader(file, lineterminator='\n')
        data = list(csv_reader)
        for row in data:
               if row['Name'] == input_arg[0] or row['Code'] == input_arg[1]:

                    prompt.append(row["Name"])
                    prompt.append(row["Code"])
                    prompt.append(row["Credit"])
                    prompt.append(row["Pre-Requisite"])
                    print(
                        f'Name: {prompt[0]} code: {prompt[1]} \n Credit: {prompt[2]}  Pre-Requisite: {prompt[3]}')
                else:

                    print(' this course dosent exist ')
                    break
'''
