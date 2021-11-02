# -*- coding: utf-8 -*-
"""pydp-27_PETROV_I_A_dz2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FQJzFlpjfArFplaMv4k9Kd-ilBJKjXl2

#Петров Игорь (pydp-27)

##ДЗ 02 "Управляющие конструкции и коллекции(ч1)"

### Задание 1
"""

#Задание 1
word = input('Enter word:')
len_word = len(word)

for i in word:
  if(len_word %2 == 0):
    res_str = 'четное'
    min = int((len_word / 2) - 1)
    max = int((len_word / 2) + 1)
    res = word[min : max]
  
  else:
   res_str = 'нечетное'
   midle = round(int(len_word / 2))
   res = word[midle]

print(f"В слове {word} {res_str} кол-во букв, а в середине буквы: {res}")

"""###Задание 2"""

#Задание 2
brk = 0
res = 0
while (brk == 0):
  number = int(input('Введи число:'))
  if(number > 0):
    res += number
  else:
    brk = 0
    break

print("Сумма введенных чисел =:",res)

"""###Задание 3"""

#Задание 3
cnt_boys  = int(input('Парней четное кол-во? (1/0):'))
cnt_girls = int(input('Девушек четное кол-во? (1/0):'))

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if (cnt_boys %2 != 0)  : boys.append('Michael')
if (cnt_girls %2 != 0) : girls.append('Nastya')

len_boys = int(len(boys))
len_girls = int(len(girls))

sort_boys = []
sort_girls = []
i = 0

if(len_boys != len_girls): 
  print('Не всем достанется пара!')
else:
  sort_boys = sorted(boys)
  sort_girls = sorted(girls)
  print('Идеальные пары:')
  while i <= len_boys - 1:
    print(f"Пара {i + 1}: {sort_boys[i]} и {sort_girls[i]}")
    i += 1

"""###Задание 4"""

#Задание 4
countries_temperature = [
['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

print('Средняя температура в странах:')
for countries in countries_temperature:
  country = countries[0]
  avg_temp_cels = round( (((sum(countries[1]) / len(countries[1])) - 32) * 5/9),2)
  print(f'{country} - {avg_temp_cels} С')

"""###Задание 5"""

#Задание 5
var = int(input('Вариант задачи? (1/2):'))
if(var == 1):
  stream = [
  '2018-01-01,user1,3',
  '2018-01-07,user1,4',
  '2018-03-29,user1,1',
  '2018-04-04,user1,13',
  '2018-01-05,user2,7',
  '2018-06-14,user3,4',
  '2018-07-02,user3,10',
  '2018-03-21,user4,19',
  '2018-03-22,user4,4',
  '2018-04-22,user4,8',
  '2018-05-03,user4,9',
  '2018-05-11,user4,11',
  ]
else:
  stream = [
  '2018-01-01,user100,150',
  '2018-01-07,user99,205',
  '2018-03-29,user1001,81'
  ]

users = []
usrs_values = []

for user in stream:
    usr = user.split(',')
    usrs_values.append(int(usr[2]))
    usr_now = usr[1]
        
    if(usr_now not in users): users.append(usr_now)
    usrs_avg = sum(usrs_values) / len(users)

print('Уникальное кол-во пользователей:', len(users))
print('Среднее количество просмотров на уникального пользователя:', round(usrs_avg,2))

"""### Задание 6"""

#Задание 6
input_nums = input("Введите числа через пробел:")

list_nums = input_nums.split()
res_list = []

for i in list_nums:
    if(list_nums.count(i) > 1) and (int(i) not in res_list):
      res_list.append(int(i))

print(sorted(res_list))