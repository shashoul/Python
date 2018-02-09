#-------------------------------------------------
# Ex1: bellow function will receive a list
#      and calculate the sum and the
#      average of that list.
#-------------------------------------------------
def sum_avg(list):

    # if the list is empty show a message and exit.
    if not list:
        print("List is empty!!!")
        return

    sum = 0
    # iterate thru the list and calculate the sum.
    for num in list:
        sum += num

    # print the sum and the average of the list.
    print("The sum of the list :" , sum)
    print("The Average of the list :", sum/len(list))

#-------------------------------------------------
# Ex2: bellow function will receive a string
#      and counts the vowel letters in it.
#-------------------------------------------------
def vowel(string):
    # define vowel letters dic that will hold the counter for each letter.
    vowel_letters = { 'a':0 , 'e':0, 'i':0, 'o':0 ,'u':0 }

    for l in string:
        if l in vowel_letters:           #  vowel letter?
            vowel_letters[l] += 1        #  increment letter counter

    print("Vowel letters counters:" , vowel_letters)

#---------------------------------------------------
# Ex3: bellow function will ask for your name
#      and age and will print on which year you will
#      celebrate your 120 birthday.
#---------------------------------------------------
from datetime import datetime
def your120():
    # get input from the user
    name = input("Please enter your name:")
    age = int(input("Please enter your age:"))

    if age <=0:
        print("Please Enter a valid age!!!")
        return
    elif age >= 120:
        print("Hello " + name + " You already reach your 120 birthday")
    else:
        cur_year = datetime.now().year          # extract current year
        year = cur_year + (120 - age)           # calculate your 120 birthday year
        print("Hello " + name + " you will celebrate your 120 birthday on " + str(year))

