# for i in range(1, 10):
#    print(i)


#import turtle
#myTurtle = turtle.Turtle()
#myTurtle.forward(100)
#myTurtle.right(90)
#myTurtle.forward(100)
#myTurtle.right(90)
#myTurtle.forward(100)
#myTurtle.right(90)
#myTurtle.forward(100)


# print("I love Alyse!!!")


#k = 0
#while k < 100:
#    print("poopoo")
#    k = k + 1


##Gets the library we need to see the date
#from datetime import date
##Prints the integer 5
#print(5)
##Prints the number 5.1
#print(5.1)
##Prints today's date
#print(date.today())


##Countdown function
##Prints the numbers from 1 to i
##on a single line
#def countdown(i):
#    for j in range(1,i + 1):
#        print(j, end = " ")
#    print()
#countdown(10)
#countdown(5)
#countdown(2)


#from datetime import date
#import random
#a = "Hello, world!"
#b = date.today()
#c = random.randint(0,100)
#d = random

#print(type(a))
#print(type(b))
#print(type(c))
#print(type(d))


#a = "Hello"
#b = "world"
#c = a + b
#d = print(c)
#print(d)


#from datetime import date
#new_integer = 8
#new_float = 8.2
#new_date = date.today()
#new_boolean = False

#integer_as_string = str(new_integer)
#float_as_string = str(new_float)
#date_as_string = str(new_date)
#boolean_as_string = str(new_boolean)

##The lines of code below will test your code.
##If it works, they will print the four string
##values, each followed by "<class 'str'>".
#print(integer_as_string, type(integer_as_string))
#print(float_as_string, type(float_as_string))
#print(date_as_string, type(date_as_string))
#print(boolean_as_string, type(boolean_as_string))


#a = "5.1"
#b = "Hello!"
#c = "5"

##Add your code here!

#as_integer = int(c)
#as_float = float(c)
#as_boolean = bool(c)

##The lines of code below will test your submission! If it's
##working, it will print the value three times, followed by three
##different types: <class 'int'>, <class 'float'>, and
##<class 'bool'>.
#print(as_integer, type(as_integer))
#print(as_float, type(as_float))
#print(as_boolean, type(as_boolean))


#import keyword
#print(keyword.kwlist)


#from datetime import date
#import datetime
#todays_date = date.today()
#current_time = datetime.datetime.now()

##Don't modify the code above!

##Complete the line below to print today's date with the
##form year/month/day. For example, January 15th, 2016
##would be 2016/1/15.
#print(todays_date.year,"/",todays_date.month,"/",todays_date.day)

##Complete the line below to print the current time with
##the form hour:minute:second, such as 12:57:15. Don't worry
##about the leading 0s for single-digit times. If it's
##1:05PM and 7 seconds, the correct answer would be:
##13:5:7 (13 because Python uses 24-hour timeby default).
#print(current_time.hour,":",current_time.minute,":",current_time.second)


#mystery_value_1 = 4
#mystery_value_2 = 6

##When you submit your code, we'll test it with different
##values for mystery_value_1 and mystery_value_2 by
##overwriting the lines above. So, don't add any code before
##those two lines! However, you can change the two lines
##above to test your code with different values.

##Complete this program so that it prints True if
##mystery_value_2 is greater than or equal to mystery_value_1,
##and False otherwise.
##
##Hint: You can print the result of that comparison directly!

##Write your code here!

#print(mystery_value_2 > mystery_value_1)


#from datetime import time
#from datetime import date
#mystery_string_1 = "Hello, world"
#mystery_string_2 = "Hello, world"
#mystery_date_1 = date(2017, 1, 15)
#mystery_date_2 = date(2017, 1, 15)
#mystery_time_1 = time(12, 45)
#mystery_time_2 = time(12, 45)

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.
##
##Add code below to print whether or not mystery_string_1 and
##mystery_string_2 are equal, whether or not mystery_date_1
##and mystery_date_2 are equal, and whether or not
##mystery_time_1 and mystery_time_2 are equal.

##Write your code here! When you Run your code, it should print
##True, True, True. When you submit your code, we'll test it
##with other input as well!

#print(mystery_string_1 == mystery_string_2,",",mystery_date_1 == mystery_date_2,",",mystery_time_1 == mystery_time_2)


#list_of_fruits = ["grape", "orange", "banana", "kiwi", "pear"]
#search_fruit = "kiwi"

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.
##
##We'll learn more about lists in chapter 4.3, but you can
##change the items in the list just by following the same format:
##put strings in quotes, separate different items with commas.
##
##Write some code that will print True if the value of
##search_fruit is in the list, and False if it is not. For
##example, with the original values above, it would print True
##because "kiwi" is an item in the list. if we changed the value
##of search_fruit to "strawberry", it would print False.

##Add your code here!

#print(search_fruit in list_of_fruits)


#hungry = True
#coworkers_going = False
#brought_lunch = False

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##Imagine you're deciding whether or not to go out to lunch.
##You only want to go if you're hungry. If you're hungry, even
##then you only want to go if you didn't bring lunch or if
##your coworkers are going. If your coworkers are going, you
##still want to go to be social even if you brought your lunch.
##
##Write some code that will use the three boolean variables
##defined above to print whether or not to go out to lunch.
##It should print True if hungry is True, and either
##coworkers_going is True or brought_lunch is False.
##Otherwise, it should print False.

#print(hungry and (coworkers_going or not brought_lunch))


#mystery_value_1 = 6
#mystery_value_2 = 2

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##Write some lines of code below that will perform the
##following operations in the given order:
##
## - Print the sum of mystery_value_1 and mystery_value_2
## - Print the difference between mystery_value_1 and mystery_value_2
##   (mystery_value_1 minus mystery_value_2)
## - Print the product of mystery_value_1 and mystery_value_2
## - Print the quotient of mystery_value_1 and mystery_value_2
##   (mystery_value_1 divided by mystery_value_2)
## - Print the modulus of mystery_value_1 and mystery_value_2
##   (the remainder of the division operation above)
##
##These operations should not carry forward: each one should
##act on the original values of mystery_value_1 and
##mystery_value_2.


##Add your code here!

#print(mystery_value_1 + mystery_value_2)
#print(mystery_value_1 - mystery_value_2)
#print(mystery_value_1 * mystery_value_2)
#print(mystery_value_1 / mystery_value_2)
#print(mystery_value_1 % mystery_value_2)


#basecapturerate = 0.33
#cpmultiplier = 0.75
#ball, curve, berry, throw, medal = 1, 1, 1, 1, 1
#baserate = (1 - (basecapturerate / (2 * cpmultiplier)))
#multipliers = ball * curve * berry * throw * medal
#probability = 1 - baserate ** multipliers
#print(round(probability, 2))


#mystery_string = "ABCDE"

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##In the example above, we saw using operators to add
##characters to the end of a string, and using operators to
##multiply a string.
##
##Add some code below that uses those operators to modify
##mystery_string such that its value at the end of the
##program is: ABCDE.ABCDE.ABCDE.??? Then, print the final
##value of mystery_string.
##
##You should not create any new strings longer than one
##character. We'll test your code with a couple other
##variants on mystery_string, but in all cases the results
##should be the same: the string repeated three times with
##a period after each repetition and three question marks
##at the end.

#print(mystery_string + "." + mystery_string + "." +mystery_string + ".???")


#old_balance = "500.45"
#deposit = "10"

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##Imagine you're writing code for an ATM that accepts cash
##deposits. You need to update the customer's balance based
##on a deposit amount. However, both the old balance and the
##deposit are given as strings.
##
##Write code below that will print the new balance after the
##deposit is processed. This should be printed along with
##the following text labeling the amount:
##
##The new balance is: 510.45
##
##Note that the old balance will always include change, but
##the deposit will never include change because the ATM has
##no coin slot, only a slot for paper money.
##
##With the initial values of the variables shown above, your
##code should print the text shown on line 17.


##Add your code here!

#print("The new balance is:", float(old_balance) + float(deposit))



#my_var_1 = 10
#my_var_2 = 3
#print(my_var_1, my_var_2)

#my_var_1 **= my_var_2
#print(my_var_1, my_var_2)

#my_var_2 *= my_var_1
#print(my_var_1, my_var_2)

#my_var_1 %= my_var_2
#print(my_var_1, my_var_2)

#my_var_2 += my_var_1
#print(my_var_1, my_var_2)



#number = 211

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.
##
##The number above is given in base 10. Let's convert it to
##base 2 and print it in binary. For example, 215 can be written
##in binary as 11010111.
##
##Each digit of that string corresponds to a power of 2. The far
##left digit represents 128, then 64, then 32, then 16, then 8,
##then 4, then 2, and then finally 1 at the far right.
##
##To convert the number to binary, first check to see if it is
##greater than or equal to 128. If it is, your first digit is 1.
##If not, your first digit is 0. If the number was greater than
##128, subtract 128 (because the 128 is captured by the first
##digit of the string).
##
##Then, repeat that process for 64, 32, 16, 8, 4, 2, and 1.
##
##For example:
##
##215 is >= 128: 1
##87 is >= 64: 11
##23 is not >= 32: 110
##23 is >= 16: 1101
##7 is not >= 8: 11010
##7 is >= 4: 110101
##3 is >= 2: 1101011
##1 is >= 1: 11010111
##
##Note that although we use 'if' a lot to describe this problem,
##this can be done entirely with floor division and modulus.
##Remember, if you convert a boolean to an integer, True becomes
##1 and False becomes 0.
##
##Note that we always work with binary in 8-bit chunks: the
##number 7 would be 00000111, not just 111. That's because inside
##the computer, 8 1s and 0s make a byte, which is the smallest
##practical unit of storage (rarely are bits used outside 8-bit
##bytes).
##
##Print the string that results from this conversion.


##Add your code here!

#digit_1 = str(int(number >= 128))
#rem_1 = number % 128
##print(digit_1, rem_1)

#digit_2 = str(int(rem_1 >= 64))
#rem_2 = rem_1 % 64
##print(digit_2, rem_2)

#digit_3 = str(int(rem_2 >= 32))
#rem_3 = rem_2 % 32
##print(digit_3, rem_3)

#digit_4 = str(int(rem_3 >= 16))
#rem_4 = rem_3 % 16
##print(digit_4, rem_4)

#digit_5 = str(int(rem_4 >= 8))
#rem_5 = rem_4 % 8
##print(digit_5, rem_5)

#digit_6 = str(int(rem_5 >= 4))
#rem_6 = rem_5 % 4
##print(digit_6, rem_6)

#digit_7 = str(int(rem_6 >= 2))
#rem_7 = rem_6 % 2
##print(digit_7, rem_7)

#digit_8 = str(int(rem_7 >= 1))
#rem_8 = rem_7 % 1
##print(digit_8, rem_8)

#print(digit_1 + digit_2 + digit_3 + digit_4 + digit_5 + digit_6 + digit_7 + digit_8) 



#myNum1 = 1
#myNum2 = 2
##Checks if myNum1 is less than myNum2
#if myNum1 < myNum2: 
#    #Prints this if so
#    print("myNum2 is greater than myNum1!") 
##Prints this regardless
#print("Execution complete!")



#mystery_int_1 = 9
#mystery_int_2 = 27

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##The variables below hold two integers, mystery_int_1 and
##mystery_int_2. Complete this program below such that it
##prints "Factors!" if either of the numbers is a factor of
##the other. If neither number is a factor of the other,
##do not print anything.
##
##Hint: You can do this with just one conditional statement
##by using the logical expressions we learned earlier (and,
##or, and not). You'll also use the modulus operator we
##learned in Chapter 2.4.


##Add your code here!

#if (mystery_int_1 % mystery_int_2 == 0 or mystery_int_2 % mystery_int_1 == 0):
#    print("Factors!")



#mystery_int_1 = 15
#mystery_int_2 = 4

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##Remember the code we wrote in the last exercise? Let's
##modify it!
##
##Previously, you printed "Factors!" if one factor was a
##factor of the other. Now, add to that code: you should still
##print "Factors!" if one number is a factor of the other, but
##also print "Not factors :(" if neither number is a factor of
##the other.


##Add your code here! You can feel free to copy/paste your
##code or the exemplary answer from last exercise.

#if (mystery_int_1 % mystery_int_2 == 0 or mystery_int_2 % mystery_int_1 == 0):
#    print("Factors!")
#else:
#    print("Not factors :(")



#mystery_state = "North Carolina"

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##It's snowing!
##
##The variable above holds the name of the state that you're
##in (hypothetically). Complete the code below so that it
##prints the following messages depending on what state you're
##in:
##
## - "School isn't cancelled." if we're in New Jersey
## - "School is postponed." if we're in North Carolina
## - "School is cancelled!" if we're in Georgia
## - "idk wear a sweater" if we're in any other state (or if
##   the value doesn't represent a valid state).


##Add your code here!

#if mystery_state == "New Jersey":
#    print("School isn't cancelled.")
#elif mystery_state == "North Carolina":
#    print("School is postponed.")
#elif mystery_state == "Georgia":
#    print("School is cancelled!")
#else:
#    print("idk wear a sweater")



#mystery_string = "zizzazle"

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##The variable above creates a string. Add some code below
##that will print based on the maximum number of consecutive
##z's in the string:
##
## - If z appears three or more times in a row, print "I'm sleepy..."
## - If z appears two times in a row, print "I love ZZ Top!"
## - If z appears once, print "One is the loneliest number."
## - If z does not appear, print "Who needs z anyway?"
##
##The message you print should correspond to the most
##consecutive z's: in the original value of mystery_string,
##for example, you'd print "I love ZZ Top!" because there are
##two consecutive z's, even though there are also some
##individual z's.
##
##Ignore upper-case z's -- only look for lower-case z's.
##
##Hint: Remember the 'in' operator! It returns true if the
##first string is found within the second string. For example,
##"bog" in "boggle" would return True, but "bog" in "artemis"
##would return False.


##Add your code here!

#if 3 * "z" in mystery_string:
#    print("I'm sleepy...")
#elif 2 * "z" in mystery_string:
#    print("I love ZZ Top!")
#elif "z" in mystery_string:
#    print("One is the loneliest number.")
#else:
#    print("Who needs z anyway?")




#team_1 = "Georgia Tech"
#team_1_score = 23
#team_2 = "Georgia"
#team_2_score = 28

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##Above we've created four variables: two team names and two
##scores. A team wins if their score is greater than the other
##team's score.
##
##Add to the code below. To print a messages like these
##depending on the values:
##
## - If one team beat the other, print:
##     "[winner] beat [loser] by [margin]"
## - If neither team won, print:
##     "[team_1] played [team_2] and it was a tie"
##
##For example, with the original values in this code, you
##should print "Georgia Tech beat Georgia by 1"
##
##Hint: to make this easier, create three variables: winner,
##loser, and margin. Then, find their values before worrying
##about printing the final message.


##Add your code here!

#if team_1_score > team_2_score:
#    winner = team_1
#    loser = team_2
#    margin = str(team_1_score - team_2_score)
#    print(winner + " beat " + loser + " by " + margin)
#elif team_2_score > team_1_score:
#    winner = team_2
#    loser = team_1
#    margin = str(team_2_score - team_1_score)
#    print(winner + " beat " + loser + " by " + margin)
#else:
#    print(team_1 + " played " + team_2 + " and it was a tie")



##In the designated areas below, write the three for loops
##that are described. Do not change the print statements that
##are currently there.

#print("First loop:")

##Write a loop here that prints the numbers from 1 to 10,
##inclusive (meaning that it prints both 1 and 10, and all
##the numbers in between). Print each number on a separate
##line.

#for i in range(1, 11):
#    print(i)


#print("Second loop:")

##Write a loop here that prints the numbers from -5 to 5,
##inclusive. Print each number on a separate line.

#for i in range (-5, 6):
#    print(i)


#print("Third loop:")

##Write a loop here that prints the even numbers only from 1
##to 20, inclusive. Print each number on a separate line.
##
##Hint: There are two ways to do this. You can use the syntax
##for the range() function shown in the multiple-choice
##problem above, or you can use a conditional with a modulus
##operator to determine whether or not to print.

#for i in range(2, 22, 2):
#    print(i)



#mystery_int = 20

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##In math, factorial is a mathematical operation where an
##integer is multipled by every number between itself and 1.
##For example, 5 factorial is 5 * 4 * 3 * 2 * 1, or 120.
##Factorial is represented by an exclamation point: 5!
##
##Use a for loop to calculate the factorial of the number
##given by mystery_int above. Then, print the result.
##
##Hint: Running a loop from 1 to mystery_int will give you
##all the integers you need to multiply together. You'll need
##to track the total product using a variable declared before
##starting the loop, though!


##Add your code here!

#factorial = 1
#for i in range(1, mystery_int + 1):
#    factorial *= i

#print(factorial)



#a_string = "Indices! Yay!"
#a_character = a_string[3]
#print("The character is", a_character)



#some_range = range(5, 10)
#print(some_range[0])
#print(some_range[4])



#some_string = "Georgia Tech"
#print(some_string[0])
#print(some_string[8])



#some_list = ["I", "like", "shorts", "they're", "comfy", "and", "easy", "to", "wear"]
#print(some_list[0])
#print(some_list[4])



#for i in range(5, 9):
#    print("Index", i)



#    some_string = "Georgia Tech"
#for i in range(0, len(some_string)):
#    print(i, some_string[i])



#some_list = ["I", "like", "shorts", "they're", "comfy", "and", "easy", "to", "wear"]
#for i in range(0, len(some_list)):
#    print(i, some_list[i])



#mystery_string = "Poopoo"

##Write a for-each loop that lists each character in
##mystery_string with its index. For example, if the string
##was "David", the output would be:
##0 D
##1 a
##2 v
##3 i
##4 d
##
##Note that the first item is #0, the second is #1, and so
##on! We'll talk about why that is in Unit 4.
##
##Hint: You'll need a separate variable to keep track of how
##many letters you've printed! You may not use the range
##function on this problem.


##Add your code here!

#index = 0
#for character in mystery_string:
#    print(index, character)
#    index += 1



#mystery_value = 87

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##Write a while loop that continues to add 9 to mystery_value
##until mystery_value is greater than 100. Each time 9 is
##added, print the *new* value of mystery_value. For example,
##with mystery_value = 87, your code should print 96 and 105.


##Add your code here!

#while mystery_value <= 100:
#    mystery_value += 9
#    print(mystery_value)



#mystery_int_1 = 3
#mystery_int_2 = 4
#mystery_int_3 = 5

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##Above are three values. Run a while loop until all three
##values are less than or equal to 0. Every time you change
##the value of the three variables, print out their new values
##all on the same line, separated by single spaces. For
##example, if their values were 3, 4, and 5 respectively, your
##code would print:
##
##2 3 4
##1 2 3
##0 1 2
##-1 0 1
##-2 -1 0


##Add your code here!

#while mystery_int_1 > 0 or mystery_int_3 > 0 or mystery_int_3 > 0: 
#    mystery_int_1 -= 1
#    mystery_int_2 -= 1
#    mystery_int_3 -= 1
#    print(mystery_int_1, mystery_int_2, mystery_int_3) 



#num = 5
#result = 1
#for i in range(1, num + 1):
#    print(i, result)
#    result *= i
#print(result)



#beats_per_measure = 4
#measures = 5

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##In music, a song's time signature is given in terms of beats
##per measure. A common time signature is 4 beats per measure:
##for every measure of music, a conductor might count from 1
##to 4 with the tempo of the music.
##
##A song then has a number of measures. For example, a short
##song might have only 5 measures. In which case, a conductor
##would count from 1 to 4 five times. If the time signature had
##instead been 3 beats per measure, she would could from 1 to 3
##five times instead.
##
##Write a nested for loop that will print out the beats of the
##piece of music. For example, if the song had 4 beats per
##measure and only 2 measures, this would print out:
##
##1
##2
##3
##4
##1
##2
##3
##4
##
##We print from 1 to 4 before starting over because there are
##4 beats per measure, and we print them all twice because there
##are two measures.


##Add your code here! Using the original values of the variables
##above, this will initially print 1 through 4 five times for a
##total of 20 lines.

#for measure in range(measures):
#    for beat in range(beats_per_measure):
#        print(beat + 1)



#lyrics = ["I wanna be your endgame", "I wanna be your first string",
#          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
#lines_of_sanity = 6

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##Imagine you have a song stuck in your head. Worse, you have
##only a few lines from a song stuck in your head. They just
##keep repeating over and over. The specific lines you have
##stuck in your head are stored in the variable lyrics.
##
##You can only stay sane so long while doing this.
##Specifically, you can only listen to lines_of_sanity lines
##before going crazy. Once you've reached lines_of_sanity,
##your brain will finish out the current list, then crumble.
##
##Write some code that will print the lyrics that run through
##your head. It should keep repeating each line one-by-one
##until you've reached lines_of_sanity lines. Then, it should
##keep going to finish out the current verse. After that, print
##"MAKE IT STOP" in all caps (without the quotes).
##
##HINT: Remember, we can iterate through items in a list using
##this syntax:
##
##  for item in list_of_items:
##
##HINT 2: You'll probably need a counter to count how many lines
##have been printed so far.


##Add your code here! Using the initial inputs from above, this
##should print 9 lines: all 4 lines of the list twice, followed
##by MAKE IT STOP

#total_lines = 0
#while total_lines <= lines_of_sanity:
#    for line in lyrics:
#        print(line)
#        total_lines += 1
#print("MAKE IT STOP")




#def multiply(num1, num2):
#    product = num1 * num2
#    return product

#num1 = 2
#num2 = 3
#print(multiply(num1, num2))



##Take a look at the three functions completely written
##below. It's your job to correctly call each function with
##the following parameters:
##
##  Function 1: the string "Black Horse and a Cherry Tree" 
##  Function 2: no parameters
##  Function 3: these five numbers: 80, 80, 95, 86, 79

##Function 1
#def cherry_pie(song):
#    if ("Cherry" in song):
#        print("Sheee's my cherry pie")
#    else:
#        print("Huh... must be an American Pie.")

##Function 2
#def should_I_go_to_Waffle_House():
#    print(True)

##Function 3
#def average_grades(num1, num2, num3, num4, num5):
#    sum = num1 + num2 + num3 + num4 + num5
#    average = sum / 5
#    print(average)


##Add your function calls here! Don't change any of the
##code above.

#cherry_pie("Black Horse and a Cherry Tree")
#should_I_go_to_Waffle_House()
#average_grades(80, 80, 95, 86, 79)




##Write a function called get_todays_date that returns
##today's date as a string, in the form year/month/day.
##For example, if today is January 15th, 2017, then it
##would return 2017/1/15.
##
##Remember, you took care of the string formatting part of
##this exercise in 2.2.9 Coding Exercise 1! Now, you're
##converting it to a function that returns the string.
##
##Note that the line below will let you access today's date
##using date.today() anywhere in your code.
#from datetime import date


##Write your function here!

#def get_todays_date():
    
#    today = date.today()
    
#    year = str(today.year)
#    month = str(today.month)
#    day = str(today.day)
    
#    return year + "/" + month + "/" + day
    
##If you want to test your code, you can do so by calling
##your function below. However, this is no longer required
##for grading.
#print(get_todays_date())




##Helping us develop this class are a team of teaching
##assistants, often called TAs for short.
##
##Write a function called my_TAs. The function should take as
##input three strings: first_TA, second_TA, and third_TA. It
##should return as output the string, "[first_TA], [second_TA],
##and [third_TA] are awesome!", with the values replacing the
##variable names.
##
##For example, my_TAs("Sridevi", "Lucy", "Xu") would return
##the string "Sridevi, Lucy, and Xu are awesome!"
##
##Hint: Notice that because you're returning a string instead
##of printing a string, you can't use the print() statement
## -- you'll have to create the string yourself, then return
##it!


##Write your function here!

#def my_TAs(first_TA, second_TA, third_TA):
#    return first_TA + ", " + second_TA + ", and " + third_TA + " are awesome!"

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: "Joshua, Jackie, and Marguerite are awesome!".
#test_first_TA = "Joshua"
#test_second_TA = "Jackie"
#test_third_TA = "Marguerite"
#print(my_TAs(test_first_TA, test_second_TA, test_third_TA))



##We've written the function, reverse, below. This function
##takes a string and returns the reverse of it. There are two
##scope errors somewhere in the code. Read through all the
##code below to find and fix the errors, so that the function
##produces the correct output and the result of the function
##is correctly printed. Note that you should not change the
##three lines that are already present in the function, but
##you may add lines before them, or you may change or add to
##the lines outside the function.
##
##Note that your goal here is to fix both the function itself
##and the program as a whole. So, your function should be
##able to be called on a new string, and the program when
##run should print the reverse of the string originally on
##line 29.

#def reverse(a_string):
#    #You may add code before the following three lines.
    
#    rev = ""
    
#    #Don't change these three lines.
#    for i in range(len(a_string)-1, -1, -1):
#        rev = rev + a_string[i]
#    return rev


##You may change or add to the following lines.
#answer = reverse("This string should be reversed!")
#print(answer)



##Write a function called snowed_in that will determine
##whether school is closed based on the weather and
##temperature. We'll pretend the school is in Georgia, where
##a little snow or sub-freezing temperatures are enough to
##close down schools!
##
##The function should take three parameters:
##
## - temperature, a float
## - weather, a string
## - is_celsius, a boolean
##
##The function should return True if temperature is below
##freezing (32 if is_celsius is False, 0 if is_celsius is
##True) or if weather is "snowy". Otherwise, it should
##return False.
##
##Note, however, that is_celsius should be an optional
##argument. If the function call does not supply a value for
##is_celsius, assume it is True.
##
##For example:
##
## snowed_in(15, "sunny") -> False
## is_celsius is assumed to be True, so 15 is not below
## freezing.
##
## snowed_in(15, "sunny", is_celsius = False) -> True
## is_celsius is False, so 15 is below freezing.
##
## snowed_in(15, "snowy", is_celsius = True) -> True
## The weather is "snowy", so the temperature doesn't matter.


##Write your function here!

#def snowed_in(temperature, weather, is_celsius = True):
#    if is_celsius == True:
#        return temperature <= 0 or weather == "snowy"
#    elif is_celsius == False:
#        return temperature <= 32 or weather == "snowy"

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print False, True, and True, each on their own line.

#print(snowed_in(15, "sunny")) #Should print False
#print(snowed_in(15, "sunny", is_celsius = False)) #Should print True
#print(snowed_in(15, "snowy", is_celsius = True)) #Should print True



#mystery_value = "9"

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##Create a program that divides 10 by mystery_value and prints
##the result. In the case that an error occurs, print "Not
##possible".
##
##Use error handling to determine if an error will occur; do
##not use the type() function. You might be surprised how many
##types Python can divide by 10!


##Add your code here!

#try:
#    print(10 / mystery_value)
#except:
#    print("Not possible")



#mystery_value = "9"

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##Create a program that divides 10 by mystery_value and prints
##the result. In the case that mystery_value is equal to 0,
##print "Not possible". Do not catch any other errors. This
##means there will be an uncaught error in the correct answer!
##
##You may not use any conditionals or the type() function.


##Add your code here!

#try:
#    print(10 / mystery_value)
#except ZeroDivisionError:
#    print("Not possible")



#mystery_value = "hello"

##You may modify the lines of code above, but don't move them!
##When you Submit your code, we'll change these lines to
##assign different values to the variables.

##Create a program that divides 10 by mystery_value and 
##prints the result. In the case that mystery_value is 
##equal to 0, print "Can't divide by zero". If for any other
##reason the operation fails, print "Not possible".
##
##You may not use any conditionals or the type() function.


##Add your code here!

#try:
#    print(10 / mystery_value)
#except ZeroDivisionError:
#    print("Can't divide by zero")
#except Exception:
#    print("Not possible")




##Write a function called has_a_vowel. has_a_vowel should have
##one parameter, a string. It should return True if the string
##has any vowels in it, False if it does not.

#def has_a_vowel(a_str):
#    print("Starting...")
#    for letter in a_str:
#        print("Checking", letter)
#        if letter in "aeiou":
#            print(letter, "is a vowel")
#            return True
#        else:
#            print(letter, "is not a vowel")
#    return False
#    print("Done!")
    
    
##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: True, then True, then False, then False, each on
##its own line.
#print(has_a_vowel("abba"))
#print(has_a_vowel("beeswax"))
#print(has_a_vowel("szyg"))
#print(has_a_vowel(""))



##Right now, the code below will encounter an error when num
##is 0, but it will not print anything when it does, and then
##it will keep running for num = 1, num = 2, and num = 3
##afterwards. Modify this code so that once it hits an error,
##the loop stops altogether.
##
##You still should not print anything when the error is
##encountered, and the loop definition on line 10 should not
##be changed.

##for num in range(-3, 3):
##    try:
##	    print(5 / num)
##    except:
##       pass

#try:
#    for num in range(-3, 3):
#        print(5 / num)
#except:
#    pass




##Write a function called get_integer that takes as input one
##variable, my_var. If my_var can be converted to an integer,
##do so and return that integer. If my_var cannot be converted
##to an integer, return a message that says, "Cannot convert!"
##
##For example, for "5" as the value of my_var, get_integer would
##return the integer 5. If the value of my_var is the string
##"Boggle.", then get_integer would return a string with the
##value "Cannot convert!"
##
##Do not use any conditionals or the type() function.


##Write your function here!

#def get_integer(my_var):
#    try:
#        return int(my_var)
#    except:
#        return "Cannot convert!"

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: 5, Cannot convert!, and 5.

#print(get_integer("5"))
#print(get_integer("Boggle."))
#print(get_integer(5.1))




##This exercise is identical to the previous exercise,
##except that instead of printing "Cannot convert!" when my_var
##cannot be converted to an integer, you should instead return
##the error message that results. For a reminder of how to
##access the error message in the except block, check out
##3.5.3, specifically CatchingASpecificError-4.py from 3.5.3.3
##and CatchingMultipleSpecificErrors-5.py from 3.5.3.4.
##
##Write a function called get_integer that takes as input one
##variable, my_var. If my_var can be converted to an integer,
##do so and return that integer. If my_var cannot be converted
##to an integer, return the error message that results from
##attempting to do so.
##
##Do not use any conditionals or the type() function.


##Write your function here!

#def get_integer(my_var):
#    try:
#        return int(my_var)
#    except ValueError as error:
#        return error


##You can use the lines below to test out your function. When
##the function is written correctly, the output of these three
##lines should be:
##5
##invalid literal for int() with base 10: 'Boggle.'
##5
#print(get_integer("5"))
#print(get_integer("Boggle."))
#print(get_integer(5.1))



##A common formula in probability and statistics is the
##formula for the number of possible combinations of r
##objects from a set of n objects. For example, the question,
##"How many possible 2-card hands can you deal from a deck of
##52 unique cards?" is saying, "How many combinations of 2
##can you make from a set of 52?"
##
##The formula for the number of combinations of length r from
##a set of n objects is:
##
##  numCombinations = n! / r!(n-r)!
##
##The ! mark is the symbol for factorial. Factorial means the
##product of the number times every number between itself and
##1. For example, 5! is 120: 5 * 4 * 3 * 2 * 1 = 120.
##
##Write a function called numCombinations with two parameters:
##n, the number of objects from which to choose, and r, the
##number of objects to choose. numCombinations should return
##the number of combinations according to the formula above.
##Don't worry if you don't fully understand what combinations
##are -- just focus on implementing a function that solves
##that formula given n and r.
##
##You may *not* use Python's built-in factorial method to
##complete this; you should implement that yourself.
##
##Hint: We'd suggest writing two functions: factorial() and
##numCombinations(). Then, call factorial() in your code for 
##numCombinations(). You don't have to do this, but it will
##make your answer a little easier!
##
##Hint 2: Remember to put parentheses around the denominator.


##Write your numCombinations function (and any other functions) 
##here!

#def numCombinations(n, r):
#    return factorial(n) / (factorial(r) * factorial(n - r))

#def factorial(number):
#    result = 1
#    for i in range(1, number + 1):
#        result *= i
#    return result


##The lines below will test your code. They are not used for
##grading, so feel free to modify them. As written, they should
##print: 1326.0, 252.0, and 4.0, each on their own line.
#print(numCombinations(52, 2))
#print(numCombinations(10, 5))
#print(numCombinations(4, 1))



##An object's weight is defined as its mass times the gravity
##on the planet where it sits. We tend to assume that the
##planet is earth and its gravity is 9.807 m/s^2. However,
##sometimes we might want to calculate an object's weight on
##a different planet.
##
##Write a function called calculateWeight. calculateWeight
##should have three parameters: mass, planet, and gravity.
##planet and gravity should be keyword parameters: by
##default, they should take the values "Earth" (a string) and
##9.807 (a float). However, they should be able to be
##overriden to let us calculate weights on other planets.
##
##The function should return a string that looks like this:
##"A [mass] kg object weighs [weight] Newtons on [planet]."
##You should round the weight to two decimal points. You
##can do this by calling round() on the weight, e.g.
##roundedWeight = round(weight, 2). The 2 dictates how
##many decimal points should be included.
##
##For example:
##
## calculateWeight(10.0) ->
##       "A 10.0 kg object weighs 98.07 Newtons on Earth."
##
## calculateWeight(5.0, planet="Jupiter", gravity=24.79) ->
##       "A 5.0 kg object weighs 24.79 Newtons on Jupiter."
##
##Hint: If you're having trouble with creating the string to
##return, here's the first part:
##result = "A " + str(mass) + " kg object weighs " ...


##Write your function here!

#def calculateWeight(mass, planet = "Earth", gravity = 9.807):
#    weight = round(mass * gravity, 2)
#    return "A " + str(mass) + " kg object weighs " + str(weight) + " Newtons on " + planet + "."


##The lines of code below will test your function. They are
##not used for grading, so feel free to change them. As
##written, these lines should output the two lines of output
##shown above.
#print(calculateWeight(10.0))
#print(calculateWeight(5.0, planet="Jupiter", gravity=24.79))



##Imagine you're writing a cash register application. To make
##interaction easier on the user, it doesn't have separate
##areas for passwords, PIN numbers, or cash totals --
##instead, it looks at what the cashier enters and infers
##whether it's their PIN number, their password, or the cash
##total for a transaction.
##
##The register makes this decision with the following rules:
##
## - If the cashier entered only digits, then it's a PIN
##   number.
## - If the cashier entered a decimal number, then it's the
##   transaction amount.
## - If the cashier entered anything else, then it's their
##   password.
##
##Write a function named interpretCashier. interpretCashier
##should take one parameter as input, which will always be
##a string initially.
##
## - If the string entered represents a PIN number, return
##   "PIN". 
## - If the string entered represents a transaction amount,
##   return "Transaction".
## - If the string entered represents a password, return
##   "Password".
##
##Hint: There is a very easy way to do this, and a very hard
##way to do this. Remember, this test is on control
##structures, not strings.

##Write your function here!

#def interpretCashier(input_string):
#    try:
#        input_string_as_int = int(input_string)
#        return "PIN"
#    except ValueError:
#        pass
#    try:
#        input_string_as_float = float(input_string)
#        return "Transaction"
#    except ValueError:
#        pass
#    return "Password"


##The lines of code below will test your function. It is not
##used for grading, so feel free to change it. As written,
##these lines should print Transaction, PIN, and Password,
##each on a separate line.
#print(interpretCashier("24.59"))
#print(interpretCashier("123456"))
#print(interpretCashier("my$up3rs3cur3p4$$w0rd"))




##Write a function called sortString. sortString should take
##one parameter as input, a string. If the input is not a
##string, sortString should return the string "Not a string!"
##If the input is a string, sortString should return a four-
##line string according to the following directions:
##
## - On the first line should be each capital letter in the
##   string, in the order in which they appear.
## - On the second line should be each lower-case letter in
##   the string, in the order in which they appear.
## - On the third line should be each punctuation mark or
##   numeral in the string, in the order in which they
##   appear.
## - On the fourth line should be an integer representing
##   how many spaces were found in the string.
##
##There should be no other text in the string that you output
##besides these four lines and the line breaks between them.
##To insert a line break into a string, insert the character
##sequence "\n". For example, line1 + "\n" + line2 would give
##a string with the first two lines and a line break in
##between. You may assume that the string will only be
##letters, spaces, and punctuation -- no numbers, line breaks,
##tabs, etc.
##
##For example, calling sortString("Hello, world!!1" should
##return: "H\nelloworld\n,!!1\n1", which would look like this
##when printed:
##H
##elloworld
##,!!1
##1
##
##Hint: Use the ord() function! Remember, when you pass a
##one-character string into ord(), it returns a number.
##
## - Lower-case letters will return a number from 97 to 122.
## - Upper-case letters will return a number from 65 to 90.
## - Puncutation marks and numbers will return a number from
##   33 to 64.
## - Spaces will return the number 32.
##
##So, you can check if a letter is lowercase by seeing if
##ord(letter) is between 97 and 122 (inclusive; 97 is 'a',
##122 is 'z'), and so on for uppercase and punctuation.
##
##Hint 2: Build up three separate strings (one for
##uppercase, one for lowercase, and one for punctuation),
##then combine them and the count of the number of spaces
##into a string to return at the end.


##Write your sortString function here!

#def sortString(my_string):
#    if not type(my_string) == str:
#        return "Not a string!"
#    else:
#        line_1 = ""
#        line_2 = ""
#        line_3 = ""
#        number_of_spaces = 0
#        for character in my_string:
#            if ord(character) >= 65 and ord(character) <= 90:
#                line_1 += character
#            elif ord(character) >= 97 and ord(character) <= 122:
#                line_2 += character
#            elif ord(character) >= 33 and ord(character) <= 64:
#                line_3 += character
#            elif ord(character) == 32:
#                number_of_spaces += 1
#        return line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + str(number_of_spaces)

##The line of code below will test your function. It is not
##used for grading, so feel free to modify it. As written,
##it should print:
##ZOMGHCS
##ello
##,1301!!
##2
#print(sortString("ZOMG Hello, CS1301!!") + "\n")
#print(sortString(9))




##Write a function called random_marks. random_marks should
##take three parameters, all integers. It should return a
##string.
##
##The first parameter represents how many apostrophes should
##be in the string. The second parameter represents how many
##quotation marks should be in the string. The third
##parameter represents how many apostrophe-quotation mark
##pairs should be in the string.
##
##For example, random_marks(3, 2, 3) would return this
##string: #'''""'"'"'"
##
##Note that there are three apostrophes, then two quotation
##marks, then three '" pairs.


##Add your function here!

#def random_marks(apostrophes, quotation_marks, pairs):
#    string = apostrophes * "'" + quotation_marks * '"' + pairs * ''''"'''
#    return string

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: '''""'"'"'"

#print(random_marks(3, 2, 3))



##Write a function called "steps" that should return a string 
##that, if printed, looks like this:
##
##111
##	222
##		333
##
##Note that the characters at the beginning of the second and
##third lines must be tabs, not spaces. There should be one
##tab on the second line and two on the third line.
##
##You may only declare ONE string in your function.
##
##Hint: Don't overthink this! We're literally just asking you
##to return one single string that just holds the above text.
##You don't have to build the string dynamically or anything.


##Write your function here!

#def steps():
#    return "111\n\t222\n\t\t333"    

##The line below will test your function.
#print(steps())




##-----------------------------------------------------------
##Write a function called align_right. align_right should
##take two parameters: a string (a_string) and an integer
##(string_length), in that order.
##
##The function should return the same string with spaces
##added to the left so that the text is "right aligned" in a
##string. The number of spaces added should make the total
##string length equal string_length.
##
##For example: align_right("CS1301", 10) would return the
##string "    CS1301". Four spaces are added to the left so
##"CS1301" is right-aligned and the total string length is
##10.
##
##HINT: Remember, len(a_string) will give you the number of
##characters currently in a_string.


##Add your function here!

#def align_right(a_string, string_length):
#    number_of_spaces = string_length - len(a_string)
#    new_string = number_of_spaces * " " + a_string
#    return new_string
    
##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: "    CS1301"
#print(align_right("CS1301", 10))



##Write a function called "last_n" that accepts two arguments:
##a string search_string and an integer n. The function should
##return the last n characters from search_string. If
##search_string is shorter than n characters, then it should
##return the entire value of search_string.


##Write your function here!

#def last_n(search_string, n):
#    if len(search_string) < n:
#        return search_string
#    else:
#        new_string = search_string[len(search_string) - n:]
#        return new_string

##The code below will test your function. If your function
##works correctly, this should print 789, saur, and 1.
#print(last_n("123456789", 3))
#print(last_n("Bulbasaur", 4))
#print(last_n("1", 5))




#myString = "You-are-a-strange-loop"
#myString[-5:-15]



##Write a function called "scramble" that accepts a string
##as an argument and returns a new string. The new string 
##should start with the last half of the original string
##and end with the first half. 
##
##If the length of the string is odd, split the string 
##at the floor of the length / 2 (in other words, the second
##half is the longer half).
##
##For example:
##  scramble("abcd") -> "cdab"
##  screamble("abcde") -> "cdeab"
##  scramble("railroad")) -> "roadrail"
##  scramble("fireworks")) -> "worksfire"


##Write your function here!

#def scramble(my_string):
#    string_length = len(my_string)
#    new_string = my_string[string_length // 2:] + my_string[:string_length // 2]
#    return new_string

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print the results you see in the examples above.

#string1 = "abcd"
#string2 = "abcde"
#string3 = "railroad"
#string4 = "fireworks"
#print(string1 + " -> " + scramble(string1))
#print(string2 + " -> " + scramble(string2))
#print(string3 + " -> " + scramble(string3))
#print(string4 + " -> " + scramble(string4))



##Write a function called fancy_find. fancy_find should have
##two parameters: search_within and search_for.
##
##fancy_find should check if search_for is found within the
##string search_within. If it is, it should print the message
##"[search_for] found at index [index]!", with [search_for]
##and [index] replaced by the value of search_for and the
##index at which it is found. If search_for is not found
##within search_within, it should print, "[search_for] was
##not found within [search_within]!", again with the values
##of search_for and search_within.
##
##For example:
##
##  fancy_find("ABCDEF", "DEF") -> "DEF found at index 3!"
##  fancy_find("ABCDEF", "GHI") -> "GHI was not found within ABCDEF!"


##Add your function here!

#def fancy_find(search_within, search_for):
#    index = search_within.find(search_for)
#    if index >= 0:
#        return search_for + " found at index " + str(index) + "!"
#    else:
#        return search_for + " was not found within " + search_within + "!"

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print:
##DEF found at index 3!
##GHI was not found within ABCDEF!

#print(fancy_find("ABCDEF", "DEF"))
#print(fancy_find("ABCDEF", "GHI"))



##Recall in Unit 3 you wrote a function that would count the
##number of words in a string using loops. Now that you know
##something about string methods, though, let's do that again
##using a different approach.
##
##Write a function called "num_words" that accepts a string 
##as an argument and returns the number of words in the 
##string. You can assume all words are separated by a space,
##and that the string has at least one word. You do not need
##to worry about punctuation.
##
##For example:
##
##  num_words("Veni, Vidi, Vici.") -> 3
##
##This time, you may not use any loops. Hint: split() might
##come in handy.


##Write your function here!

#def num_words(my_string):
#    list_of_words = my_string.split(" ")
#    #print(list_of_words)
#    return len(list_of_words)

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: 3, 2, 1, each on their own line.
#print(num_words("Vini, Vidi, Vici."))
#print(num_words("Hello, world!"))
#print(num_words("HeyDavidwhyaren'ttherespacesinthissentence"))



##Write a function called string_length. string_length should
##have one parameter, a string. It should return a 2-tuple:
##the first item in the 2-tuple should be the string itself,
##and the second item should be the length of the string as
##given by the len() function.


##Write your function here!

#def string_length(string):
#    return (string, len(string))

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print:
##('Hello, world!', 13)
##('CS1301', 6)
##("Some people pronounce it 'toople'. Others pronounce it 'tuhple'. Either is correct.", 83)
#print(string_length("Hello, world!"))
#print(string_length("CS1301"))
#print(string_length("Some people pronounce it 'toople'. Others pronounce it 'tuhple'. Either is correct."))



##Write a function called unpack_and_reverse that will
##accept one parameter, a tuple with at least three items.
##The function should return a new tuple with only the first
##three items, but listed in reverse order.
##
##For example:
##
## a_tuple = ("a", "b", "c", "d", "e")
## unpack_and_reverse(a_tuple) -> ("c", "b", "a")
##
##However, to do this, you should not access any value in
##the tuple directly (e.g. with a_tuple[1]). Instead, you
##should use tuple unpacking to unpack them into variables.
##You also should not touch any items past the third item
##in the tuple: use tuple slicing instead to only access
##the first three.


##Write your function here!

#def unpack_and_reverse(my_tuple):
#    short_tuple = my_tuple[:3]
#    (item_0, item_1, item_2) = short_tuple
#    short_tuple_reversed = (item_2, item_1, item_0)
#    return short_tuple_reversed

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print:
##('c', 'b', 'a')
##('h', 'g', 'f')
##('k', 'j', 'i')
#print(unpack_and_reverse(("a", "b", "c", "d", "e")))
#print(unpack_and_reverse(("f", "g", "h")))
#print(unpack_and_reverse(("i", "j", "k", "l", "m", "n", "o", "p", "q", "r")))




##Remember asciitable.com from an earlier exercise? We're
##going to use it again. Remember, ordinal values for
##characters are given in the 'Dec' column of asciitable.com.
##
##Write a function called character_info. character_info will
##take as input a string with only one character. It should
##return a 3-tuple with three pieces of information:
##
## - In the first spot, the character itself.
## - In the second spot, the ordinal value of the character,
##   obtained using the ord() function (e.g. ord("a") -> 97).
## - In the third spot, what type of character it is: either
##   "letter", "number", or "punctuation".
##
##You may assume that anything that is not a letter (either
##upper or lower case) or a number is punctuation. You may
##also assume the ordinal will be between 32 (" ") and 126
##("~").


##Write your function here!

#def character_info(my_string):
#    ord_number = ord(my_string)
#    if ord_number >= 48 and ord_number <= 57:
#        character_type = "number"
#    elif ord_number >= 97 and ord_number <= 122:
#        character_type = "letter"
#    elif ord_number >= 91 and ord_number <= 96:
#        character_type = "punctuation"
#    return (my_string, ord_number, character_type)
        
##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print:
##('q', 113, 'letter')
##('7', 55, 'number')
##('`', 96, 'punctuation')
#print(character_info("q"))
#print(character_info("7"))
#print(character_info("`"))




##Write a function called modify_list. modify_list will
##take one parameter, a list. It should then modify the
##list in the following ways, in this order:
##
## - Sort the list (using the default sort method).
## - Reverse the order of the list.
## - Delete the last three items of the list.
## - Removes one instance the integer 7 from the list, if
##   it's present.
## - Double the values of the first and third items in
##   the list.
##
##It should then return the resulting list. You may assume
##the list will start with at least six items.
##
##Hint: Remember Python is 0-indexed. The second item
##does not have an index of 2.
##
##Hint 2: Remember, the list.remove() function removes items
##by value, not by index. Note also that if the item you're
##trying to remove is not found in the list, remove() will
##throw an error: so, you'll want to avoid that one way or
##another!


##Write your code here!

#def modify_list(my_list):
#    my_list.sort()
#    my_list.reverse()
#    del my_list[-3:]
#    try:
#        my_list.remove(7)
#    except:
#        pass
#    my_list[0] *= 2
#    my_list[2] *= 2
#    return my_list
    

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print:
##[178, 81, 75.0, 4, 3.141592653589793, 3]
#import math
#print(modify_list([7, 4, 3, 2.0, 81, 37.5, 89, math.pi, -2, math.e]))



##Write a function called multiply_strings. Multiply
##strings should have one parameter, a list of strings.
##It should return a modified list according to the
##following changes:
##
## - Every string stored at an even index should be
##   doubled.
## - Every string stored at an index that is a multiple
##   of 3 should be tripled.
## - Every other string should remain unchanged.
##
##These changes should "stack": the string stored at index
##6 should be duplicated six times (2 * 3).
##
##Then, return the new list. You may assume that 0 is a
##multiple of 2 and 3.
##
##Hint: To do this, you need to modify the values of the
##list using their indices, e.g. a_list[1]. If you're not
##using their indices, your answer won't work!


##Write your function here!

#def multiply_strings(list_of_strings):
#    for i in range(0, len(list_of_strings), 2):
#        list_of_strings[i] *= 2
#    for j in range(0, len(list_of_strings), 3):
#        list_of_strings[j] *= 3
#    return list_of_strings

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: 
##['AAAAAA', 'B', 'CC', 'DDD', 'EE', 'F', 'GGGGGG']
#test_list = ["A", "B", "C", "D", "E", "F", "G"]
#print(multiply_strings(test_list))



##Write a function called sum_lists. sum_lists should take
##one parameter, which will be a list of lists of integers.
##sum_lists should return the sum of adding every number from
##every list.
##
##For example:
##
## list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
## sum_list(list_of_lists) -> 67


##Add your code here!

#def sum_lists(list_of_lists):
#    summation = 0
#    for lists in list_of_lists:
#        for value in lists:
#            summation += value
#    return summation

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: 78
#list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#print(sum_lists(list_of_lists))



##We've learned a lot in this chapter. Let's try to use a lot
##of it for one final exercise.
##
##Write a function called sort_artists. sort_artists will
##take as input a list of tuples. Each tuple will have two
##items: the first item will be a string holding an artist's
##name, and the second will be an integer representing their
##total album sales (in millions).
##
##Return a tuple of two lists. The first list in the
##resulting tuple should be all the artists sorted
##alphabetically. The second list should be all the revenues
##sorted in descending numerical order.
##
##For example:
## artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
## sort_artists(artists) -> (["Elvis Presley", "Michael Jackson", "The Beatles"], [270.8, 211.5, 183.9])
##
##Notice that artists is a list of tuples (brackets first,
##then parentheses), but sort_artists outputs a tuple of
##lists (parentheses first, then brackets).


##Write your function here!

#def sort_artists(list_of_tuples):
#    list_of_artists = []
#    list_of_revenues = []
#    for artist_and_revenue in list_of_tuples:
#        list_of_artists.append(artist_and_revenue[0])
#        list_of_revenues.append(artist_and_revenue[1])
#    list_of_artists.sort()
#    list_of_revenues.sort()
#    list_of_revenues.reverse()
#    return (list_of_artists, list_of_revenues) 

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print:
##(['Elvis Presley', 'Michael Jackson', 'The Beatles'], [270.8, 211.5, 183.9])  
#artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
#print(sort_artists(artists))




##Write a function called "write_file" that accepts two 
##parameters: a filename and some data that will either 
##be an integer or a string to write. The function 
##should open the file and write the data to the file.
##
##Hints:
##
## - Don't forget to close the file when you're done!
## - If the data isn't a string already, you may need
##   to convert it, depending on the approach you
##   choose.
## - Remember, this code has no print statements, so
##   when you run it, don't expect to see any output
##   on the right! You could add print statements if
##   you want a confirmation the code is done running.
## - You can put the variable for the filename in the
##   same place where we put text like OutputFile.txt
##   in the videos.


##Write your function here!

#def write_file(filename, data):
#    file = open(filename, "w")
#    try:
#        file.write(data)
#    except TypeError:
#        data_as_string = str(data)
#        file.write(data_as_string)
#    file.close()
    

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print nothing. However, if you open WriteFileOutput.txt
##in the top left after running it, the contents of the
##file should be 1301.
#write_file("WriteFileOutput.txt", 1301)



##Write a function called "append_to_file" that accepts
##two parameters: a filename and some data that will
##be an integer or a string to write. The function 
##should open the file and add the data to the end of
##the file. Each new call to append_to_file should add
##the new contents on a new line.
##
##Hints:
##
## - Don't forget to close the file when you're done!
## - If the data isn't a string already, you may need
##   to convert it.
## - Remember, this code has no print statements, so
##   when you run it, don't expect to see any output
##   on the right! You could add print statements if
##   you want a confirmation the code is done running.
## - You can put the variable for the filename in the
##   same place where we put text like OutputFile.txt
##   in the videos.


##Write your function here!

#def append_to_file(filename, data):
#    file = open(filename, "a")
#    file.write(str(data) + "\n")
#    file.close()

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print nothing. However, if you open AppendToFileOutput.txt
##in the top left after running it, the contents of the
##file should be another instance of 1301 every time you
##run this file.
#append_to_file("AppendToFileOutput.txt", "1301")




##Write a function called "find_coffee" that expects a 
##filename as a parameter. The function should open the 
##given file and return True if the file contains the word 
##"coffee". Otherwise, the function should return False.
##
##Hint: look up the read() method if you want to do this
##more simply than you might do with readline().


##Write your function here!

#def find_coffee(filename):
#    file = open(filename, "r")
#    return "coffee" in file.read()

##You can test your function with the provided files named 
##"coffeeful.txt" and "coffeeless.txt". With their original
##text, the lines below should print True, then False. You
##may also edit the files by selecting them in the drop
##down in the top left to try your code with different
##input.
#print(find_coffee("coffeeful.txt"))
#print(find_coffee("coffeeless.txt"))



##Write a function called "load_file" that accepts one 
##parameter: a filename. The function should open the
##file and return the contents.#
##
## - If the contents of the file can be interpreted as
##   an integer, return the contents as an integer.
## - Otherwise, if the contents of the file can be
##   interpreted as a float, return the contents as a
##   float.
## - Otherwise, return the contents of the file as a
##   string.
##
##You may assume that the file has only one line.
##
##Hints:
##
## - Don't forget to close the file when you're done!
## - Remember, anything you read from a file is
##   initially interpreted as a string.


##Write your function here!

##Note: if you use read() on file more than once, it returns None after the first time. Best to use read() once and store in variable "value."
#def load_file(filename):
#    file = open(filename, "r")
#    value = file.read()
#    try:
#        content = int(value)
#    except ValueError:
#        try:
#            content = float(value)
#        except ValueError:
#            content = value
#    file.close()
#    return content
    

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print 123, followed by <class 'int'>.
#contents = load_file("LoadFromFileInput.txt")
#print(contents)
#print(type(contents))




##We've defined a list of tuples below. Each tuple follows
##the format: (name, home state).
##
##Create a dictionary called ta_dict in the space below, where
##the keys are each TA's name, and the values are their home
##state.

#ta_info = [("Joshua", "Georgia"),
#          ("Jackie", "Vermont"),
#          ("Marguerite", "Tennessee")]

##Add your code to create the dictionary as described!
##The first item in each tuple should be a key, and
##the second item in each tuple should be its value.
##Note that you may create this either by reading and
##using the ta_info list of tuples, or you can create
##the dictionary from scratch:


##Create your dictionary here!

#ta_dict = {ta_info[0][0] : ta_info[0][1], ta_info[1][0] : ta_info[1][1], ta_info[2][0] : ta_info[2][1]} 

##Now, create three variables: josh_val, jack_val, and
##marg_val. Set josh_val equal to Josh's dictionary value,
##then jack_val equal to Jackie's, then marg_val equal to
##Marguerite's. Remember how to properly access the value
##corresponding to a dictionary key!
##
##Make sure you use dictionary-access syntax to do this.
##Don't create the variables based on new values.


##Create your variables here!

#josh_val = ta_dict["Joshua"]
#jack_val = ta_dict["Jackie"]
#marg_val = ta_dict["Marguerite"]

##If your code works as intended, the following three lines
##will run and print Georgia, Vermont, and Tennessee:
#print(josh_val)
#print(jack_val)
#print(marg_val)



##Create a function called tup_to_dict. tup_to_dict should take one
##parameter: a list of tuples. You can assume each tuple in
##the list has exactly two values.
##
##The function should return a dictionary where the first item
##in each tuple is the key, and the second item in each tuple
##is the corresponding value.
##
##For example:
## colors = [("turquoise", "#40E0D0"), ("red", "#990000")]
## tup_to_dict(colors) -> {"turquoise":"#40E0D0", "red":"#990000"}
##
##Hint: the previous exercise is very similar; this just turns
##it into a function! All our tuples will be color name-color
##value pairs.


##Write your function here!

#def tup_to_dict(list_of_tuples):
#    dictionary = {}
#    for tup in list_of_tuples:
#        dictionary[tup[0]] = tup[1]
#    return dictionary

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print:  {'Turquoise':'#40E0D0', 'Red':'#990000'}
##
##Don't worry if it prints those in the reverse order; that's
##still correct!
#print(tup_to_dict([("Turquoise", "#40E0D0"), ("Red", "#990000")]))



##Write a function called students_present. students_present
##should take as input one parameter, a dictionary. The keys
##of the dictionary will be names, and the values will be one
##of three strings: "Here", "Present", or an empty string "".
##
##Return a list of the keys for whom the corresponding value
##is either "Here" or "Present".


##Add your code here!

#def students_present(dictionary):
#    present_students = []
#    for student in dictionary:
#        if dictionary[student] == "Here" or dictionary[student] == "Present":
#            present_students.append(student)
#    return present_students

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print (although the order of the keys may vary):
##["David", "Marguerite", "Joshua", "Erica"]

#student_list = {"David" : "Here", "Marguerite" : "Here",
#                "Jackie": "", "Joshua": "Present",
#                "Erica": "Here", "Daniel": ""}
#print(students_present(student_list))



##Write a function called name_counts. name_counts will take
##as input a list of full names. Each name will be two words
##separated by a space, like "David Joyner".
##
##The function should return a dictionary. The keys to the
##dictionary will be the first names from the list, and the
##values should be the number of times that first name
##appeared.
##
##HINT: Use split() to split names into first and last.


##Add your function here!

#def name_counts(list_of_names):
#    list_of_first_names = []
#    dictionary = {}
#    for name in list_of_names:
#        first_and_last = name.split(" ")
#        list_of_first_names.append(first_and_last[0])
#    for first_name in list_of_first_names:
#        if not first_name in dictionary:
#            dictionary[first_name] = 0
#        dictionary[first_name] += 1
#    return dictionary
    

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print (although the order of the keys may vary):
##{'Shelba': 5, 'Maren': 1, 'Nicol': 1, 'David': 2, 'Brenton': 2}
#name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
#             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
#             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
#             "Shelba Fry", "Maren Fry"]
#print(name_counts(name_list))



##Recall in the previous problem you counted the number of
##instances of a certain first name in a list of full names.
##You returned a dictionary with the name as the key, and the
##number of times it appeared as the value.
##
##Modify that code such that instead of having a count as the
##value, you instead have a list of the full names that had
##that first name. So, each key in the dictionary would still
##be a first name, but the values would be lists of names.
##Make sure to sort the list of names, too.
##
##Name this new function name_lists.


##Add your function here!

#def name_lists(name_list):
#    list_of_first_names = []
#    dictionary = {}
#    for name in name_list:
#        first_and_last = name.split(" ")
#        list_of_first_names.append(first_and_last[0])
#    for i in range(len(list_of_first_names)):
#        if not list_of_first_names[i] in dictionary:
#            dictionary[list_of_first_names[i]] = []
#        dictionary[list_of_first_names[i]].append(name_list[i])
#    return dictionary
    
##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print (although the order of the keys may vary):
##{'Shelba': ['Shelba Barthel', 'Shelba Crowley', 'Shelba Fernald', 'Shelba Fry', 'Shelba Odle'],
##'David': ['David Joyner', 'David Zuber'], 'Brenton': ['Brenton Joyner', 'Brenton Zuber'],
##'Maren': ['Maren Fry'], 'Nicol': ['Nicol Barthel']}

#name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
#             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
#             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
#             "Shelba Fry", "Maren Fry"]
#print(name_lists(name_list))



##Write a function called count_characters. count_characters
##should take as input a single string, and return a
##dictionary. In the dictionary, the keys should be
##characters, and the values should be the number of times
##each character appeared in the string.
##
##For example:
##
##  count_characters("aabbccc") -> {'a': 2, 'b': 2, 'c': 3}
##  count_characters("AaBbbb") -> {'A': 1, 'B': 1, 'a': 1, 'b': 3}
##
##You should not need to make any assumptions about the
##characters in the string: spaces, punctuation, line breaks,
##and any other characters should be handled automatically.
##You may count upper and lower case separately.


##Write your function here!

#def count_characters(my_string):
#    dictionary ={}
#    my_string = my_string.strip()
#    my_string = my_string.replace(".", "")
#    my_string = my_string.replace(",", "")
#    my_string = my_string.replace("'", "")
#    my_string = my_string.replace("\n", "")
#    my_string = my_string.replace(" ", "")
#    for character in my_string:
#        if not character in dictionary:
#            dictionary[character] = 0
#        dictionary[character] += 1
#    return dictionary
  

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print (although the order of the keys may vary):
##
##{'a': 2, 'b': 2, 'c': 3}
#print(count_characters("aabbccc"))
##print(count_characters("He thrusts his fists against the posts."))



##Write a function called find_range. find_range should take
##as input a string representing a filename. The file
##corresponding to that filename will be a list of integers,
##one integer per line. find_range should return a tuple
##containing the smallest and largest numbers in the file
##(the smallest first, then the largest).
##
##For example, in the dropdown in the top left you'll find a
##file named FindRangeInput.txt. The smallest number in that
##file is 2, and the largest is 37. So, if you called
##find_range("FindRangeInput.txt"), the function would return
##(2, 37), a tuple with two integers.
##
##You may assume that all lines in the file will contain a
##positive integer (greater than 0). There may be duplicates.
##
##Hint: Remember, if you loop through all the lines in a file
##then you have to close and reopen the file to read it again,
##or by use file.seek(0) to start from the top. However, you
##can do this problem without having to read the file twice.


##Write your function here!

#def find_range(filename):
#    file = open(filename, "r")
#    file_contents = file.read()
#    file_contents = file_contents.split()
#    minimum = 10**12
#    maximum = 0
#    for integer in file_contents:
#        if int(integer) < minimum:
#            minimum = int(integer)
#        if int(integer) > maximum:
#            maximum = int(integer)
#    return (minimum, maximum)
    

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: (2, 37)
#print(find_range("FindRangeInput.txt"))



##Write a function called pivot_library. pivot_library takes
##as input one parameter, a list of 3-tuples. Each tuple in
##the list has three items: the first item is a book title
##(a string), the second item is the book's author (a
##string), and the third item is the book's ISBN number (a
##string).
##
##pivot_library should return a dictionary. In the dictionary
##that it returns, the keys should be the ISBN numbers, and
##the values should be 2-item tuples. In each tuple, the first
##item should be the book title, and the second item should
##be the author's name.
##
##Hint: Unpack the tuple to variables first, then create the
##new dictionary item.
##
##For example:
##
## books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
##          ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
## pivot_library(books)
##   -> {"978-0-140-17739-8": ("Of Mice and Men", "John Steinbeck"),
##       "978-1-260-08227-2": ("Introduction to Computing", "David Joyner")}


##Write your function here!

#def pivot_library(list_of_tuples):
#    titles = []
#    authors = []
#    ISBNs = []
#    dictionary = {}
#    for i in range(len(list_of_tuples)):
#        titles.append(list_of_tuples[i][0])
#        authors.append(list_of_tuples[i][1])
#        ISBNs.append(list_of_tuples[i][2])
#    for j in range(len(ISBNs)):
#        dictionary[ISBNs[j]] = (titles[j], authors[j])
#    return dictionary

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print (although the order of the keys may vary):
##
##{"978-0-140-17739-8": ("Of Mice and Men", "John Steinbeck"), "978-1-260-08227-2": ("Introduction to Computing", "David Joyner")}
#books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"), ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
#print(pivot_library(books))




##Write a function called write_book_info. write_book_info
##will take as input two parameters: a string and a list of
##3-tuples.
##
##The string will represent the filename to which to write.
##
##Each 3-tuple in the list will contain three strings: a
##book title, the book's author, and the book's ISBN number.
##
##write_book_info should write the list of books to the file
##given by the filename using the following format:
##
## ISBN: Title by Author
##
##So, for this list:
##
## [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"),
##  ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
##
##The file printed would look like this:
##
## 978-0-140-17739-8: Of Mice and Men by John Steinbeck
## 978-1-260-08227-2: Introduction to Computing by David Joyner
##
##We've included Sample.txt to show you what a longer version
##of one of these files might look like.


##Write your function here!

#def write_book_info(filename, list_of_tuples):
#    file = open(filename, "w")
#    for tup in list_of_tuples:
#        file.write(tup[2] + ": " + tup[0] + " by " + tup[1] + "\n")
#    file.close()

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print nothing -- however, it should write the same contents
##as Sample.txt to Test.txt.
#books = [("Of Mice and Men", "John Steinbeck", "978-0-140-17739-8"), ("Introduction to Computing", "David Joyner", "978-1-260-08227-2")]
#write_book_info("Test.txt", books)



##APA citation style cites author names like this:
##
##  Last, F., Joyner, D., Burdell, G.
##
##Note the following:
##
## - Each individual name is listed as the last name, then a
##   comma, then the first initial, then a period.
## - The names are separated by commas, including the last
##   two.
## - There is no space or comma following the last period.
##
##Write a function called names_to_apa. names_to_apa should
##take as input one string, and return a reformatted string
##according to the style given above. You can assume that
##the input string will be of the following format:
##
##  First Last, David Joyner, and George Burdell
##
##You may assume the following:
##
## - There will be at least three names, with "and" before
##   the last name.
## - Each name will have exactly two words.
## - There will be commas between each pair of names.
## - The word 'and' will precede the last name.
## - The names will only be letters (no punctuation, special
##   characters, etc.), and first and last name will both be
##   capitalized.
##
##Hint: You can use the string replace() method to delete
##text from a string. For example, a_string.replace("hi", "")
##will delete all instances of "hi". There are multiple ways
##you might choose to use this.


##Write your function below!

#def names_to_apa(my_string):
#    new_string = ""
#    my_string = my_string.replace("and", "")
#    my_string = my_string.split(",")
#    for i in range(len(my_string)):
#        my_string[i] = my_string[i].strip()
#        my_string[i] = my_string[i].split()
#        my_string[i].reverse()
#        my_string[i][1] = my_string[i][1][0] + "."
#        if not i == len(my_string) - 1:
#            new_string += my_string[i][0] + ", " + my_string[i][1] + ", "
#        else:
#            new_string += my_string[i][0] + ", " + my_string[i][1]
#    return new_string

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: Last, F., Joyner, D., & Burdell, G.
#print(names_to_apa("First Last, David Joyner, and George Burdell"))




##In the game tic-tac-toe, two players take turns drawing
##Xs and Os on a 3x3 grid. If one player can place three of
##their symbols side-by-side in a row, column, or diagonal,
##they win the game.
##
##For example:
##
## X Wins:   X Wins:   X Wins:   No Winner:
## X|O|X     O|X|X     O|O|      X|O|O
## -+-+-     -+-+-     -+-+-     -+-+-
## O|O|X     X|O|      X|X|X     O|X|X
## -+-+-     -+-+-     -+-+-     -----
## O|X|X      | |O      | |      X|X|O
##
##Write a function called check_winner. check_winner will
##take one parameter as input, a 2D tuple (that is, a tuple
##of tuples). The 2D tuple represents the game board: each
##smaller tuple in the larger tuple is a row of the board,
##and each item in the smaller tuple is a spot on the
##board. There will always be three tuples in the larger
##tuple, and three items in each of the smaller tuples.
##
##Each item in the smaller tuple will always be one of three
##values: the string "X", the string "O", or the value None.
##
##check_winner should return one of three values: the string
##"X" if X has won the game; the string "O" if O has won the
##game; or the value None if there is no winner. None should
##NOT be the string "None"; it should be the value None,
##like the boolean values True and False.
##
##You may assume a player has won the game if and only if
##the board has three of their symbols in a row: you do not
##need to worry about whether the input is a valid game
##otherwise (e.g. a board of nine Xs still counts as X
##winning). You may assume that there will only be one
##winner per board.
##
##Hint: There are only eight possible places to win (three
##rows, three columns, two diagonals).
##
##Hint 2: If you're comfortable on time, you may want to
##check out the last problem before doing this one. It's
##only worth 1 point, but you might be able to design
##one solution that works for both problems!


##Write your function here!

#def check_winner(my_tuple):
#    boolean_matrix = [[None, None, None], 
#                      [None, None, None], 
#                      [None, None, None]]
#    for i in range(3):
#        for j in range(3):
#            if my_tuple[i][j] == "X":
#                boolean_matrix[i][j] = 1
#            elif my_tuple[i][j] == "O":
#                boolean_matrix[i][j] = -1
#            elif my_tuple[i][j] == None:
#                boolean_matrix[i][j] = 0
#    row_sums = []
#    column_sums = []
#    for i in range(3):
#        row_sums.append(sum(boolean_matrix[i]))
#        column_sums.append(sum(column(boolean_matrix, i)))
#    diagonal_sums = sum_up_diagonals(boolean_matrix)
#    if 3 in row_sums or 3 in column_sums or 3 in diagonal_sums:
#        return "X"
#    elif -3 in row_sums or -3 in column_sums or -3 in diagonal_sums:
#        return "O"
#    else:
#        return None
      
#def column(matrix, i):
#    return [row[i] for row in matrix]

#def sum_up_diagonals(li):
#    index = len(li)
#    first_dia =  sum(li[i][i]for i in range(index))
#    second_dia = sum(li[i][index-i-1]for i in range(index))
#    return [first_dia, second_dia]
        
##The code below shows how the tic-tac-toe tuples are
##created and tests your code with three games: one where
##X wins, one where O wins, and one where there is no winner.
##Remember, the line breaks in xwins and owins are optional:
##they're just to make the declarations more readable. They
##could be written the same as nowins.
#xwins = (("X", "O", "X"),
#         ("O", "O", "X"),
#         ("O", "X", "X"))
#owins = (("O", "X", "X"),
#         ("X", "O", None),
#         (None, None, "O"))
#nowins = (("X", "O", "O"),("O", "X", "X"),("X", "X", "O"))
##check_winner(nowins)
#print(check_winner(xwins))
#print(check_winner(owins))
#print(check_winner(nowins))



##Write a function called check_formula. The check_formula
##function should take as input one parameter, a string. It
##should return True if the string holds a correctly
##formatted arithmetic integer formula according to the rules
##below, or False if it does not.
##
##For this problem, here are the rules that define a
##correctly-formatted arithmetic string:
##
## - The only characters in the string should be digits or
##   the five arithmetic operators: +, -, *, /, and =. Any
##   other characters, including spaces, periods, commas,
##   or any letters, are not permitted.
## - There may not be any consecutive arithmetic operators.
##   Any arithmetic operator must have a number on either
##   side of it.
## - There must be an equals sign in the formula.
##
##You do not need to worry about negative numbers or
##parentheses, and you do not need to worry about whether
##the equation is accurate. You may also assume all the
##numbers in the string will be only one digit.
##
##Here are some examples of valid and invalid arithmetic
##formulas:
##
##   Valid     Invalid
##   5*3=5+2   5*3+5+2 (no equals)
##   5=7       5= (equals sign isn't in the middle)
##   5=2-5     50=-5 (consecutive arithmetic operators)
##   6/2=5/2   a=51 (illegal character)
##             -5=5+2 (starts with an operator)
##
##Hint: Remember, as soon as you find *one* thing wrong
##with the string, you know it's invalid and can return
##False. So, go character-by-character through the string
##checking everything that could be wrong. If you don't
##find anything wrong, return True!


##Write your function here!

#def check_formula(my_string):
#    if not "=" in my_string:
#        print("'=' not in my_string")
#        return False
#    for i in range(len(my_string)):
#        print(my_string[i])
#        if not my_string[i] in ["1","2","3","4","5","6","7","8","9","+","-","*","/","="]:
#            print("invalid character")
#            return False
#        elif (i == 0 or i == len(my_string) - 1) and my_string[i] in ["+","-","*","/","="]:
#            print("operator at beginning or end of string")
#            return False
#        elif my_string[i] in ["+","-","*","/","="] and my_string[i + 1] in ["+","-","*","/","="]:
#            print("consecutive operators")
#            return False
#    return True
   

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print True, then several Falses.
#print(check_formula("5*3=5+2"))
#print(check_formula("5*3+5+2"))
#print(check_formula("5="))
#print(check_formula("5=-5"))
#print(check_formula("a=5"))
#print(check_formula("-5=5+2"))

#print(str(None))



##Last problem, you implemented a function that could find if
##someone had won a particular game of tic-tac-toe based on a
##2D tuple representing the current game board.
##
##In this problem, you'll do the same thing, but for Connect
##4 instead of tic-tac-toe. Write another function called
##check_winner which takes as input a 2D list. It should
##return "X" if there are four adjacent "X" values anywhere
##in the list (row, column, diagonal); "O" if there are four
##adjacent "O" values anywhere in the list; and None if
##there are neither.
##
##Here are the ways Connect-4 is different from tic-tac-toe:
##
## - Connect-4 is played with 6 rows and 7 columns, not 3
##   rows and 3 columns.
## - You must have 4 in a row (or column or diagonal) to win
##   instead of 3.
## - You may only place pieces in the bottom-most empty
##   space in a column (e.g. you "drop" the pieces in the
##   column and they fall to the first empty spot). Note,
##   though, that this shouldn't affect your reasoning.
##
##To keep things simple, we'll still use "X" and "O" to
##represent the players, and None to represent empty spots.
##You may make the same assumptions as the previous
##problem: only one winner per board, no characters besides
##"X", "O", and None, and you don't have to worry about
##whether the board is actually a valid game of Connect 4.
##
##Hints:
## - Don't forget both kinds of diagonals!
## - This board is too large to check every possible place
##   for a winner: there are 69 places a player could win.
## - Remember, if you put a negative index in a list,
##   Python "wraps around" and checks the last value. You
##   may have to control for this.


##Write your function here!

#def check_winner(game_matrix):
#    all_rows_string = ""
#    all_columns_string = ""
#    all_diag_string_1 = ""
#    all_diag_string_2 = ""
#    for i in range(6):
#        for j in range(7):
#            all_rows_string += str(game_matrix[i][j])
#        all_rows_string += "\n"
#    for i in range(7):
#        for j in range(6):
#            all_columns_string += str(game_matrix[j][i])
#        all_columns_string += "\n"
#    for i in range(3, 6):
#        for j in range(i + 1):
#            all_diag_string_1 += str(game_matrix[i - j][j])
#        all_diag_string_1 += "\n"
#    for i in range(6, 9):
#        for j in range(i - 5, 7):
#            all_diag_string_1 += str(game_matrix[i - j][j])
#        all_diag_string_1 += "\n"
#    for i in range(2, -1, -1):
#        for j in range(6 - i):
#            all_diag_string_2 += str(game_matrix[i + j][j])
#        all_diag_string_2 += "\n"
#    for i in range(-1, -4, -1):
#        for j in range(7 + i):
#            all_diag_string_2 += str(game_matrix[j][j - i])
#        all_diag_string_2 += "\n"
#    if "XXXX" in all_rows_string or "XXXX" in all_columns_string or "XXXX" in all_diag_string_1 or "XXXX" in all_diag_string_2:
#        return "X"
#    elif "OOOO" in all_rows_string or "OOOO" in all_columns_string or "OOOO" in all_diag_string_1 or "OOOO" in all_diag_string_2:
#        return "O"
#    else:
#        return None
                   
              
    

##The code below tests your function on three Connect-4
##boards. Remember, the line breaks are not needed to create
##a 2D tuple; they're used here just for readability.
#xwins = ((None, None, None, None, None, None, None),
#         (None, None, None, None, None, None, None),
#         (None, None, None, None, "X" , None, None),
#         (None, None, None, "X" , "O" , "O", None),
#         (None, "O" , "X" , "X" , "O" , "X", None),
#         ("O" , "X" , "O" , "O" , "O" , "X" , "X"))
#owins = ((None, None, None, None, None, None, None),
#         (None, None, None, None, None, None, None),
#         ("O" , "O" , "O" , "O" , None, None, None),
#         ("O" , "X" , "X" , "X" , None, None, None),
#         ("X" , "X" , "X" , "O" , "X" , None, None),
#         ("X" , "O" , "O" , "X" , "O" , None, None))
#nowins =(("X" , "X" , None, None, None, None, None),
#         ("O" , "O" , None, None, None, None, None),
#         ("O" , "X" , "O" , "O" , None, "O" , "O" ),
#         ("O" , "X" , "X" , "X" , None, "X" , "X" ),
#         ("X" , "X" , "X" , "X" , "X" , "X" , "O" ),
#         ("X" , "O" , "O" , "X" , "X" , "X" , "O" ))

##check_winner(xwins)
#print(check_winner(xwins))
#print(check_winner(owins))
#print(check_winner(nowins))



##Write a function called average_rainfall. average_rainfall
##should have one parameter, a list of integers. The list
##represents daily rainfall measurements for a certain area.
##
##However, at some point in the list, there will be a -1.
##This indicates that you should stop averaging, and ignore
##any subsequent values.
##
##For example:
##
##average_rainfall([1, 2, 3, 4, 5, -1, 6, 7]) -> 3.0
##
##The function would only average 1, 2, 3, 4, and 5, and
##ignore any values after the -1.
##
##You may assume all the items in the list are integers,
##that -1 is guaranteed to occur somewhere in the list,
##and that -1 will not be the first item in the list.


##Add your code here!

#def average_rainfall(list_of_integers):
    
#    summation = 0
#    counter = 0
#    negative_one = False

#    while negative_one == False:
#        print(counter)
#        if list_of_integers[counter] == -1:
#            negative_one = True
#        else:
#            summation += list_of_integers[counter]
#            counter += 1
    
#    return summation / counter
        
       
##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: 3.0
#a_list = [1, 2, 3, 4, 5, -1, 6, 7]
#print(average_rainfall(a_list))



##Write a function called volume_and_area. volume_and_area
##will take in a dictionary. This dictionary is guaranteed to
##have three keys: "length", "width", and "height", whose
##values are integers representing three attributes of a
##rectangular prism (also known as a box).
##
##Modify this dictionary to add two keys: "volume" and "area".
##The values associated with these keys should be the volume
##and surface area of the box.
##
##The formula for volume is:
##  length * width * height
##
##The formula for surface area is:
##  2 * ((length * width) + (length*height) + (width*height))
##
##Because length, width, and height are integers, and because
##these formulas have no division, your results should be
##integers as well.


##Add your code here!

#def volume_and_area(dictionary):
    
#    length = dictionary["length"]
#    width = dictionary["width"]
#    height = dictionary["height"]
    
#    volume = length * width * height
#    surface_area = 2 * ((length * width) + (length*height) + (width*height))
    
#    dictionary["volume"] = volume
#    dictionary["area"] = surface_area
    
#    return dictionary

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print 6 and 22, each on a different line.
#rectangle = {"length": 1, "width": 2, "height": 3}
#rectangle = volume_and_area(rectangle)
##print(rectangle)
#print(rectangle["volume"])
#print(rectangle["area"])




##Write a function called imdb_dictionary. imdb_dictionary
##should have one parameter, a string representing a
##filename.
##
##On each row of the file will be a performer's name, then
##a semicolon, then a comma-separated list of movies the have
##been in. For example, one file's contents could be:
##
##Robert Downey Jr.; Avengers: Infinity War, Sherlock Holmes 3, Spider-Man: Homecoming
##Scarlett Johansson; Avengers: Infinity War, Isle of Dogs, Ghost in the Shell
##Elizabeth Olsen; Avengers: Infinity War, Kodachrome, Wind River, Ingrid Goes West
##
##You may assume that the only semi-colon will be after the
##performer's name, and that there will be no commas in the
##movie titles.
##
##Return a dictionary where the keys are each actor's name,
##and the values are alphabetically-sorted lists of the movies
##they have been in. For example, if imdb_dictionary was called
##on the file above, the output would be:
##{"Robert Downey Jr.": ["Avengers: Infinity War", "Sherlock Holmes 3", "Spider-Man: Homecoming"],
##"Scarlett Johansson": ["Avengers: Infinity War", "Ghost in the Shell", "Isle of Dogs"],
##Elizabeth Olsen": ["Avengers: Infinity War", "Ingrid Goes West", "Kodachrome", "Wind River"]}
##
##Make sure the list of movies is sorted alphabetically. Don't
##worry about the order the keys (names) appear in the dictionary.


##Add your code here!

#def imdb_dictionary(filename):
    
#    dictionary = {}
    
#    file = open(filename, "r")
#    file_text = file.read()
#    file_text = file_text.splitlines()
 
#    for i in range(len(file_text)):
#        file_text[i] = file_text[i].split(";")
#        file_text[i][1] = file_text[i][1].split(",")
#        for j in range(len(file_text[i][1])):
#            file_text[i][1][j] = file_text[i][1][j].strip()
#        file_text[i][1].sort()
#        dictionary[file_text[i][0]] = file_text[i][1]
    
#    return dictionary
    
        
##Below are some lines of code that will test your function.
##You can change the contents of some_performers.txt from
##the dropdown in the top left to test other inputs.
##
##If your function works correctly, this will originally
##print (although the order of the keys may vary):
##{"Robert Downey Jr.": ["Avengers: Infinity War", "Sherlock Holmes 3", "Spider-Man: Homecoming"], "Scarlett Johansson": ["Avengers: Infinity War", "Ghost in the Shell", "Isle of Dogs"], Elizabeth Olsen": ["Avengers: Infinity War", "Ingrid Goes West", "Kodachrome", "Wind River"]}
#print(imdb_dictionary("some_performers.txt"))




##Write a function called digit_count. digit_count should
##take as input a number, which could be either a float or an
##integer. It should return a dictionary whose keys are digits,
##and whose values are the number of times that digit appears
##in the number.
##
##The dictionary should NOT contain any numerals that do not
##occur at all in the number, and it should also note contain
##the decimal point character if the number is a decimal.
##
##For example:
##
##  digit_count(11223) -> {1: 2, 2: 2, 3: 1}
##  digit_count(3.14159) -> {3: 1, 1: 2, 4: 1, 5: 1, 9: 1}
##
##Hint: You should probably convert the number to a string to
##count the digits, but convert the individual digits back to
##integers to use as keys to the dictionary.

##Write your function here!

#def digit_count(number):
#    dictionary = {}
#    number = str(number)
#    if "." in number:
#        number = number.replace(".", "")
#    for digit in number:
#        if not int(digit) in dictionary:
#            dictionary[int(digit)] = 0
#        dictionary[int(digit)] += 1
#    return dictionary

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print (although the order of the keys may vary):
##
##{1: 2, 2: 2, 3: 1}
##{3: 1, 1: 2, 4: 1, 5: 1, 9: 1}
#print(digit_count(11223))
#print(digit_count(3.14159))




##Write a function called write_class_data. write_class_data
##will take as input two parameters: a string and a list of
##3-tuples.
##
##The string will represent the filename to which to write.
##
##Each 3-tuple in the list will contain three values:
##
## - A string representing the major of a college class (e.g.
##   "CS", "CHEM", "ENGL")
## - An integer representing a course number (e.g. 1301, 2241,
##   4001)
## - A string representing the name of a course (e.g.
##   "Introduction to Computing", "Organic Chemistry", etc.)
##
##write_class_data should write the list of classes to the file
##given by the filename using the following format:
##
## [major][number]: [class name]
##
##So, for this list:
##
## [("CS", 1301, "Introduction to Computing"),
##  ("CHEM", "1310", "General Chemistry")]
##
##The file printed would look like this:
##
## CS1301: Introduction to Computing
## CHEM1310: General Chemistry
##
##Note the specifics of that format: no space between the major
##and course number, no space between the course number and the
##colon, one space between the colon and the course name.
##
##We've included Sample.txt to show you what a longer version
##of one of these files might look like.


##Write your function here!

#def write_class_data(filename, list_of_tuples):
    
#    file = open(filename, "w")
    
#    for i in range(len(list_of_tuples)):
#        file.write(list_of_tuples[i][0] + str(list_of_tuples[i][1]) + ": " + list_of_tuples[i][2] + "\n")
    
#    file.close()

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print nothing -- however, it should write the same contents
##as Sample.txt to Test.txt.
#classes = [("CS", 1301, "Introduction to Computing"), ("CHEM", "1310", "General Chemistry")]
#write_class_data("Test.txt", classes)



##Write a function called first_to_last. first_to_last should
##take as input a string representing a filename. Inside the
##file will be some text on each line; some lines will contain
##integers, while others will contain strings of other
##characters.
##
##first_to_last should return a tuple containing the first and
##last strings in the file alphabetically. It should ignore any
##lines that contain integers.
##
##For example, in the dropdown in the top left you'll find a
##file named FirstLastInput.txt. Ignoring numerals, the first
##string alphabetically is appsp, and the last string
##alphabetically is zzffs. So, first_to_last("FirstLastInput.txt")
##would return the tuple ("appsp", "zzffs").
##
##You may assume that every line in the file contains either
##all numerals or all lower-case letters; there will be no lines
##with both numerals and letters, nor any capital letters.


##Write your function here!

#def first_to_last(filename):
    
#    file = open(filename, "r")
    
#    file_lines = file.readlines()
#    file_lines_no_numbers = []
#    for i in range(len(file_lines)):
#        file_lines[i] = file_lines[i].replace("\n", "")
#        if not file_lines[i][0] in "0123456789":
#            file_lines_no_numbers.append(file_lines[i])
#    file_lines_no_numbers.sort()
#    return (file_lines_no_numbers[0], file_lines_no_numbers[-1])
    

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: ("appsp", "zzffs")
#print(first_to_last("FirstLastInput.txt"))



##Write a function called complete_profile. complete_profile
##will take as input a dictionary. This dictionary will have
##four keys: first, middle, last, and title. The function
##should return a dictionary with those four keys, and three
##more: name, full_name, short_name. The values for those
##keys should be:
##
## - name: the first and last name, separated by a space
## - full_name: the title, first, middle, and last names,
##   with a space between each pair of strings
## - short_name: the first letter of the first name, a space,
##   and their last name
##
##For example:
##
## complete_profile({"first": "David", "middle": "Andrew",
##                   "last": "Joyner", "title": "Dr."})
##
## would return:
##
## {"first": "David", "middle": "Andrew", "last": "Joyner",
##  "title": "Dr.", "name": "David Joyner",
##  "full_name": "Dr. David Andrew Joyner",
##  "short_name": "D Joyner"}
##
##You may either modify the dictionary that is passed in,
##or create a new one. Either way, make sure to return the
##dictionary at the end of the function.

##Add your code here!

#def complete_profile(dictionary):
#    dictionary["name"] = dictionary["first"] + " " + dictionary["last"]
#    dictionary["full_name"] = dictionary["title"] + " " + dictionary["first"] + " " + dictionary["middle"] + " " + dictionary["last"]
#    dictionary["short_name"] = dictionary["first"][0] + " " + dictionary["last"]
#    return dictionary

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print "David Joyner", "Dr. David Andrew Joyner", and
##"D Joyner" each on a different line (without the quotes).
#prof = {"first": "David", "middle": "Andrew", "last": "Joyner", "title": "Dr."}
#prof = complete_profile(prof)
#print(prof["name"])
#print(prof["full_name"])
#print(prof["short_name"])



##In the game Rock-Paper-Scissors, two opponents
##simultaneously choose to throw either "Rock", "Paper",
##or "Scissors". Rock beats Scissors, Scissors beats Paper,
##and Paper beats Rock. If both players throw the same
##object, the round is a tie.
##
##Write a function called find_winner. find_winner will take
##as input a list of 2-tuples, each representing a round of
##Rock-Paper-Scissors. Each 2-tuple will contain two strings.
##Each string will be either "Rock", "Paper", or "Scissors".
##The first item in the 2-tuple will represent what Player 1
##chooses in each round, and the second item in the 2-tuple
##will represent what Player 2 chooses in each round.
##
##find_winner should return the string "Player 1 wins!" if
##Player 1 wins more games than Player 2. It should return the
##string "Player 2 wins!" if Player 2 wins more games than
##Player 1. It should return the string "It's a tie!" if the
##two players win an equal number of times. 
##
##The number of times the two players tie is irrelevant to the
##result: all that matters is who wins more rounds than the
##other.
##
##For example:
##
## find_winner([("Rock", "Rock"), ("Rock", "Scissors"),
##              ("Paper", "Rock"), ("Scissors", "Rock")])
##
##...would return "Player 1 wins!" because Player 1 wins
##two round and Player 2 wins one round.


##Write your function here!

#def find_winner(list_of_tuples):
#    player1_score = 0
#    player2_score = 0
#    for i in range(len(list_of_tuples)):
#        if list_of_tuples[i][0] == "Rock":
#            if list_of_tuples[i][1] == "Scissors":
#                player1_score += 1
#            elif list_of_tuples[i][1] == "Paper":
#                player2_score += 1
#        elif list_of_tuples[i][0] == "Paper":
#            if list_of_tuples[i][1] == "Rock":
#                player1_score += 1
#            elif list_of_tuples[i][1] == "Scissors":
#                player2_score += 1
#        elif list_of_tuples[i][0] == "Scissors":
#            if list_of_tuples[i][1] == "Paper":
#                player1_score += 1
#            elif list_of_tuples[i][1] == "Rock":
#                player2_score += 1
#    if player1_score > player2_score:
#        return "Player 1 wins!"
#    elif player2_score > player1_score:
#        return "Player 2 wins!"
#    else:
#        return "It's a tie!"
                

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print:
##Player 1 wins!
##Player 2 wins!
##It's a tie!
#p1_wins = [("Rock", "Rock"), ("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Rock")]
#p2_wins = [("Paper", "Rock"), ("Paper", "Paper"), ("Paper", "Scissors"), ("Rock", "Paper")]
#itsatie = [("Paper", "Paper"), ("Paper", "Rock"), ("Rock", "Paper"), ("Scissors", "Scissors")]
#print(find_winner(p1_wins))
#print(find_winner(p2_wins))
#print(find_winner(itsatie))



##-----------------------------------------------------------
##Write a function called no_you_pick. no_you_pick should
##have two parameters. The first parameter is a dictionary
##where the keys are restaurant names and the values are lists
##of attributes of those restaurants as strings, such as
##"vegetarian", "vegan", and "gluten-free".
##
##The second parameter is a list of strings representing of
##necessary attributes of the restaurant you select.
##
##Return a list of restaurants from the dictionary who each
##contain all the diet restrictions listed in the list,
##sorted alphabetically. If there are no restaurants that
##meet all the restrictions, return the string "Sorry, no
##restaurants meet your restrictions". Types of diet
##restrictions that exist in this question's universe are:
##vegetarian, vegan, kosher, gluten-free, dairy-free
##
##For example:
##grading_scale = {"blossom": ["vegetarian", "vegan", "kosher", "gluten-free", "dairy-free"], \
##                 "jacob's pickles": ["vegetarian", "gluten-free"], \
##                 "sweetgreen": ["vegetarian", "vegan", "gluten-free", "kosher"]}
##guests_diet = ["dairy-free"]
##no_you_pick(grading_scale, guests_diet) -> ["blossom"]


##Write your code here!

#def no_you_pick(dictionary, necessary_attributes):
#    good_restaurants = []
#    for restaurant in dictionary:
#        has_attribute = True
#        for attribute in necessary_attributes:
#            if not attribute in dictionary[restaurant]:
#                has_attribute = False
#        if has_attribute == True:
#            good_restaurants.append(restaurant)
#    return good_restaurants

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: blossom
#grading_scale = {"blossom": ["vegetarian", "vegan", "kosher", "gluten-free", "dairy-free"], \
#                 "jacob's pickles": ["vegetarian", "gluten-free"], \
#                 "sweetgreen": ["vegetarian", "vegan", "gluten-free", "kosher", "dairy-free"]}
#guests_diet = ["dairy-free", "kosher"]
#print(no_you_pick(grading_scale, guests_diet))




##Your goal in this question is to create a playlist (that is, a list of songs) by your friend's favorite artists.
##
##Write a function called playlist. playlist should have two parameters. The first parameter is a dictionary, where the keys are band names and the values are song names. The second parameter is a list of strings, where each string is an artist.
##
##playlist should return a list of all songs by the bands listed in the second parameter, sorted alphabetically. If there are no matching artists, return "I guess I don't mind ads on the radio that much"
##
##For example:
##artists_and_songs = {"Beyonce": ["Halo", "Run the World", "Irreplaceable"],\
##                     "Maroon 5": ["Sugar", "Payphone", "Memories"], "Harry Styles": \
##                     ["Sign of the Times", "Adore You", "Falling"], "AC/DC":\
##                     ["TNT", "It's a long way to the top", "Thunderstruck"]}
##friends_artists = ["Maroon 5", "AC/DC", "Tame Impala"]
##playlist(artists_and_songs, friends_artists) -> ["It's a long way to the top", "Memories", "Payphone", "Sugar", "TNT", "Thunderstruck"]


##Write your code here!

#def playlist(dictionary, list_of_artists):
#    list_of_songs = []
#    for artist in list_of_artists:
#        if artist in dictionary:
#            list_of_songs.extend(dictionary[artist])
#    list_of_songs.sort()
#    if list_of_songs == []:
#        return "I guess I don't mind ads on the radio that much"
#    return list_of_songs

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: ["It's a long way to the top", "Memories", "Payphone", "Sugar", "TNT", "Thunderstruck"]
#artists_and_songs = {"Beyonce": ["Halo", "Run the World", "Irreplaceable"],\
#                     "Maroon 5": ["Sugar", "Payphone", "Memories"], "Harry Styles": \
#                     ["Sign of the Times", "Adore You", "Falling"], "AC/DC":\
#                     ["TNT", "It's a long way to the top", "Thunderstruck"]}
#friends_artists = ["Maroon 5", "AC/DC", "Tame Impala"]
#print(playlist(artists_and_songs, friends_artists))




##You are going through your refrigerator at home and trying to determine whether you have the proper ingredients to cook a meal.
##
##Write a function called food_at_home. food_at_home should have one parameter, a list of foods in your house as strings. In order to cook a meal, the list must contain "cooking oil" and at least one other item. If this criteria is not met, return the string "I guess it's pizza tonight". If you do have cooking oil and at least one other food, return the string, "You do have food, your options are ... or ... or ...", where the ...s are replaced by the food names in the list in the order in which they appear. "cooking oil" should not be one of the foods listed under options.
##
##For example:
##food_list = ["chicken", "mixed veggies", "greens", "beans", "corn", "cooking oil"]
##food_at_home(food_list) -> "You do have food, your options are chicken or mixed veggies or greens or beans or corn"


##Write your code here!

#def food_at_home(foods_in_house):
#    if not "cooking oil" in foods_in_house or not len(foods_in_house) >= 2:
#        return "I guess it's pizza tonight"
#    else:
#        foods_in_house.remove("cooking oil")
#        return_statement = "You do have food, your options are "
#        for i in range(len(foods_in_house)):
#            if i < len(foods_in_house) - 1:
#                return_statement += foods_in_house[i] + " or "
#            else:
#                return_statement += foods_in_house[i]
#        return return_statement

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: You do have food, your options are chicken or mixed veggies or greens or beans or corn
#food_list = ["chicken", "mixed veggies", "greens", "beans", "corn", "cooking oil"]
#print(food_at_home(food_list))




##Write a class named "Number" with one attribute called 
##"value" which defaults to 0 and another attribute called 
##"even" which defaults to True.
##
##Next, create an instance of this class and assign it to
##a variable called "number_instance".
##
##Then, set the value attribute to 101 and the even
##attribute to False.


##Write your code here!

#class Number:
#    def __init__(self):
#        self.value = 0
#        self.even = True

#number_instance = Number()
#number_instance.value = 101
#number_instance.even = False

##Note that this exercise does not print anything by
##default. You're welcome to add print statements to debug
##your code when running it. Note that the autograder
##will check both your value for number_instance and your
##definition of the class Number.



##Rewrite the "Number" class from 5.1.2 Coding Exercise 2.
##This time, however, require arguments for value and
##even in the constructor. Then, inside the constructor,
##create new instance variables called value and even that
##copy the values of the arguments passed into the
##constructor.
##
##In other words, rewrite the Number class such that value
##and even behave the way studentName and enrolled behaved
##in the exercise above, and the way firstname and lastname
##behaved in video 5.1.4.1.
##
##Then, as before, create an instance of this class and
##assign it to a variable called "number_instance". value
##should again be set to 101 and even should be set to
##False.
##
##Hint: Remember, the way you initialize the instance will
##have to change, too, based on the changes to the
##constructor that we're requiring.


##Write your code here!

#class Number:
#    def __init__(self, value, even):
#        self.value = value
#        self.even = even

#number_instance = Number(101, False)
        
##Note that this exercise does not print anything by
##default. You're welcome to add print statements to debug
##your code when running it. Note that the autograder
##will check both your value for number_instance and your
##definition of the class Number.



##Imagine you're writing an exercise-tracking app like Fitbit
##or MyFitnessPal. Part of your app is that a user can log an
##exercise session by naming the exercise, the intensity, and
##the duration.
##
##Write a class called ExerciseSession. ExerciseSession
##should have a constructor that requires two strings and an
##integer: the strings represent the exercise name and the
##exercise intensity, which will be "Low", "Moderate", or
##"High". The integer will represent the length of the
##exercise session in minutes. These should be saved in the
##instance of the class.
##
##Then, add three getters to the class. The getters should
##be named get_exercise, get_intensity, and get_duration,
##and should return the exercise string, the exercise
##intensity, and the duration, respectively.
##
##The setters should be named set_exercise, set_intensity,
##and set_duration. Each should have one parameter (besides
##self), which should be stored as the new value of
##exercise, intensity, or duration. You may assume only
##valid values will be passed in.
##
##HINT: You don't have to do any logging like you saw in
##the video! That was just an example of one benefit of
##using getters and setters, but this problem does not ask
##you to do that.


##Add your code here!

#class ExerciseSession:
    
#    def __init__(self, exercise_name, intensity, duration):
#        self.exercise_name = exercise_name
#        self.intensity = intensity
#        self.duration = duration
        
#    def get_exercise(self):
#        return self.exercise_name
    
#    def get_intensity(self):
#        return self.intensity
    
#    def get_duration(self):
#        return self.duration
    
#    def set_exercise(self, new_exercise):
#        self.exercise_name = new_exercise
        
#    def set_intensity(self, new_intensity):
#        self.intensity = new_intensity
        
#    def set_duration(self, new_duration):
#        self.duration = new_duration

##If your code is implemented correctly, the lines below
##will run error-free. They will result in the following
##output to the console:
##Running
##Low
##60
##Swimming
##High
##30
#new_exercise = ExerciseSession("Running", "Low", 60)
#print(new_exercise.get_exercise())
#print(new_exercise.get_intensity())
#print(new_exercise.get_duration())
#new_exercise.set_exercise("Swimming")
#new_exercise.set_intensity("High")
#new_exercise.set_duration(30)
#print(new_exercise.get_exercise())
#print(new_exercise.get_intensity())
#print(new_exercise.get_duration())




##Previously, you wrote a class called ExerciseSession that
##had three attributes: an exercise name, an intensity, and a
##duration.
##
##Add a new method to that class called calories_burned.
##calories_burned should have no parameters (besides self, as
##every method in a class has). It should return an integer
##representing the number of calories burned according to the
##following formula:
##
## - If the intensity is "Low", 4 calories are burned per
##   minute.
## - If the intensity is "Medium", 8 calories are burned
##   per minute.
## - If the intensity is "High", 12 calories are burned per
##   minute.
##
##You may copy your class from the previous exercise and just
##add to it.


##Add your code here!

#class ExerciseSession:
    
#    def __init__(self, exercise_name, intensity, duration):
#        self.exercise_name = exercise_name
#        self.intensity = intensity
#        self.duration = duration
        
#    def get_exercise(self):
#        return self.exercise_name
    
#    def get_intensity(self):
#        return self.intensity
    
#    def get_duration(self):
#        return self.duration
    
#    def set_exercise(self, new_exercise):
#        self.exercise_name = new_exercise
        
#    def set_intensity(self, new_intensity):
#        self.intensity = new_intensity
        
#    def set_duration(self, new_duration):
#        self.duration = new_duration
        
#    def calories_burned(self):
#        if self.intensity == "Low":
#            return 4 * self.duration
#        elif self.intensity == "Medium":
#            return 8 * self.duration
#        elif self.intensity == "High":
#            return 12 * self.duration

##If your code is implemented correctly, the lines below
##will run error-free. They will result in the following
##output to the console:
##240
##360
#new_exercise = ExerciseSession("Running", "Low", 60)
#print(new_exercise.calories_burned())
#new_exercise.set_exercise("Swimming")
#new_exercise.set_intensity("High")
#new_exercise.set_duration(30)
#print(new_exercise.calories_burned())




##Classes can also have references to other instances of
##themselves. Consider this Person class, for example, 
##that allows for an instance of a father and mother
##to be given in the constructor.
##
##Create 3 instances of this class. The first should have 
##the name "Mr. Burdell" with an age of 53. The second
##instance should have a name of "Mrs. Burdell" with an age
##of 53 as well. Finally, make an instance with the name of
##"George P. Burdell" with an age of 25. This final instance
##should also have the father attribute set to the instance 
##of Mr. Burdell, and the mother attribute set to the 
##instance of Mrs. Burdell. Finally, store the instance of 
##George P. Burdell in a variable called george_p. (It does
##not matter what variable names you use for Mr. and Mrs.
##Burdell.)

#class Person:
#    def __init__(self, name, age, father=None, mother=None):
#        self.name = name
#        self.age = age
#        self.father = father
#        self.mother = mother

##Write your code here!

#mr_Burdell = Person("Mr. Burdell", 53)
#mrs_Burdell = Person("Mrs. Burdell", 53)
#george_p = Person("George P. Burdell", 25, father = mr_Burdell, mother = mrs_Burdell)


##The code below will let you test your code. It isn't used
##for grading, so feel free to modify it. As written, it
##should print George P. Burdell, Mrs. Burdell, and Mr.
##Burdell each on a separate line.
#print(george_p.name)
#print(george_p.mother.name)
#print(george_p.father.name)




##We've given you a class called "Song" that represents
##some basic information about a song. We also wrote a 
##class called "Artist" which contains some basic 
##information about an artist.
##
##Your job is to create three instances of the song class,
##called song_1, song_2, and song_3.
##
##song_1 should have the following attributes:
##   name = "You Belong With Me"
##   album = "Fearless"
##   year = 2008
##   artist.name = "Taylor Swift"
##   artist.label = "Big Machine Records, LLC"
##
##song_2 should have the following attributes:
##   name = "All Too Well"
##   album = "Red"
##   year = 2012
##   artist.name = "Taylor Swift"
##   artist.label = "Big Machine Records, LLC"
##
##song_3 should have the following attributes:
##   name = "Up We Go"
##   album = "Midnight Machines"
##   year = 2016
##   artist.name = "LiGHTS"
##   artist.label = "Warner Bros. Records Inc."
##
##Notice, though, that song_1 and song_2 have the same
##artist and label. That means they should each have the
##SAME instance of artist: do not create separate instances
##of artist for each song.
##
##When your code is done running, there should exist three
##variables: song_1, song_2, and song_3, according to the
##requirements above.

#class Artist:
#    def __init__(self, name, label):
#        self.name = name
#        self.label = label

#class Song:
#    def __init__(self, name, album, year, artist):
#        self.name = name
#        self.album = album
#        self.year = year
#        self.artist = artist
        

##Write your code here!

#artist_1 = Artist("Taylor Swift", "Big Machine Records, LLC")
#artist_2 = Artist("LiGHTS", "Warner Bros. Records Inc.")

#song_1 = Song("You Belong With Me", "Fearless", 2008, artist_1)
#song_2 = Song("All Too Well", "Red", 2012, artist_1)
#song_3 = Song("Up We Go", "Midnight Machines", 2016, artist_2)

##Feel free to add code to test your code below.




##Below are the two class definitions we supplied previously:
##Artist and Song.
##
##Write a function called "get_song_string". It should accept
##one argument which will be a Song object. It should return
##a string in the following format:
##
## "<song name>" - <artist name> (<song year>)
## e.g: 
## "You Belong With Me" - Taylor Swift (2008)
##
##The quotation marks around the song title should be *part*
##of the string.
##
##Hint: You're writing a function, not a method. That means
##the function get_song_string should not be inside either
##of these classes.

#class Artist:
#    def __init__(self, name, label):
#        self.name = name
#        self.label = label

#class Song:
#    def __init__(self, name, album, year, artist):
#        self.name = name
#        self.album = album
#        self.year = year
#        self.artist = artist

#def get_song_string(song):
#    return '"' + song.name + '" - ' + song.artist.name + " (" + str(song.year) + ")"
        
##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: "You Belong With Me" -Taylor Swift (2008)
#new_artist = Artist("Taylor Swift", "Big Machine Records, LLC")
#new_song = Song("You Belong With Me", "Fearless", 2008, new_artist)
#print(get_song_string(new_song))



##Let's implement the factorial function we saw in the
##previous video in Python!
##
##Our factorial function should take as input a number, and
##it should return the product of that number times every
##number between itself and 1.

##Let's start with the function definition. This function
##definition creates the function factorial with one
##parameter, n.

#def factorial(n):
#    #What do we want to do inside the function? Well, there
#    #are two cases. First, if n is 1, we just want to return
#    #1. After all, 1! is 1.
    
#    if n == 1:
#        return 1
    
#    #What if n doesn't equal 1, though? Then we want to
#    #return n times the factorial of (n - 1). After all,
#    #5! = 5 * 4!, 4! = 4 * 3!, etc.
    
#    else:
#        return n * factorial(n - 1)
    
#    #If n is greater than 1, then it multiplies 1 by the
#    #factorial of n - 1, as calculated with the same
#    #function. Every time factorial() runs, n decreases
#    #by 1, which guarantees that eventually, n will equal
#    #1.

##Now let's test it out! Run this file to see the results.
#print("5! is", factorial(5))
#print("10! is", factorial(10))

##Want to see more about how this works? Select the other
##file, FactorialwithPrints.py, from the drop-down in the
##top left to see a version of this that traces the output.




##We've written a function below called count_down(). This
##function takes an int parameter, start, and prints every
##number from that start to 0. The way we've written it uses
##recursion. Below that funtion, write a function that does
##the exact same thing, but do not use recursion.
##
##The purpose of this exercise is for you to recognize some
##example instances in which you can use recursion, and what
##differences can be seen in the actual code.
##
##Make sure to actually print 0 as the last number!

#def count_down(start):
#    #If we've reached 0 already, print 0 but do not call
#    #another copy
#    if start <= 0:
#        print(start)
    
#    #If we haven't reached 0 yet, print the current number,
#    #then call count_down with the current number minus 1.
#    else:
#        print(start)
#        count_down(start - 1)
        
##Do not modify the code above.
##Fill in the function below to do the same as the function
##above, but without recursion. You could use for loops,
##while loops, or some other approach.

#def count_down2(start):
#    #Add your code here!
#    for i in range(start, -1, -1):
#        print(i)


##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: 5, 4, 3, 2, 1, 0, each on their own line.
#count_down(5)
#count_down2(5)



##As before, our core function below hasn't changed. What
##has changed is that we've added print statements so we can
##see a bit about how the program is running.

#def fib(n):
#    if n == 1 or n == 2:
#        print("Found fib(", n, "): returning 1!", sep = "")
#        return 1
    
#    #As with the factorial function, we want to print every
#    #time we're about to create a new call to Fibonacci,
#    #and every time such a call is completed.
    
#    else:
#        print("Finding fib(", n, "): fib(", n - 1, ") + fib(", n-2, ")", sep = "")
#        result =  fib(n - 1) + fib(n - 2)
#        print("Found fib(", n, "): ", result, sep = "")
#        return result

##Now if we run this, we'll see a lot more output. Feel free
##to change this line to visualize different Fibonacci
##numbers.
#print("fib(5) is", fib(5))

##The output here is more complex; you may want to copy it
##into another window to read it.
##
##When fib(5) is first called, it wants to calculate fib(4)
##and fib(3). So, it calls fib(4) first, which demands fib(3)
##and fib(2). So, it calls fib(3), which demands fib(2) and
##fib(1). Those are both the base case, so both return 1.
##So, in the execution order, we see fib(5), then fib(4),
##then fib(3), then fib(2), then fib(1).
##
##Once fib(2) and fib(1) have run, then fib(3) can finish,
##and so the next statement printed is the result of fib(3).
##Once fib(3) is finished, then we can finish fib(4) by
##finding fib(2). fib(2) is again 1, so the next line is
##fib(2).
##
##Once fib(3) and fib(2) have finished, we can finish
##fib(4), so the next statement printed is the result of
##fib(4).
##
##Now that fib(4) is finished, we're all the way back to the
##first call, which wanted fib(4) + fib(3). Now, the rest of
##the execution is evaluating fib(3), which immediately
##demands fib(2) and fib(1). So, the next two lines are the
##results of fib(2) and fib(1). Once those are done, fib(3)
##is finished again.
##
##Now fib(4) and fib(3) are both finished, so the very first
##line can end: fib(4) + fib(3) = 3 + 2 = 5.



##We've started a recursive function below called
##exponent_calc(). It takes in two integer parameters, base
##and expo. It should return the mathematical answer to
##base^expo. For example, exponent_calc(5, 3) should return
##125: 5^3 = 125.
##
##The code is almost done - we have our base case written.
##We know to stop recursing when we've reached the simplest
##form. When the exponent is 0, we return 1, because anything
##to the 0 power is 1. But we are missing our recursive call!
##
##Fill in the marked line with the recursive call necessary
##to complete the function. Do not use the double-asterisk
##operator for exponentiation. Do not use any loops.
##
##Hint: Notice the similarity between exponentiation and
##factorial:
##  4! = 4! = 4 * 3!, 3! = 3 * 2!, 2! = 2 * 1
##  2^4 = 2 * 2^3, 2^3 = 2 * 2^2, 2^2 = 2 * 2^1, 2^1 = 2 * 2^0

#def exponent_calc(base, expo):
#    if expo == 0:
#        return 1
#    else:
#        return base * exponent_calc(base, expo - 1)

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: 125
#print(exponent_calc(5, 3))



##We've written the function, sort_with_bubbles, below. It takes
##in one list parameter, lst. However, there are two problems in
##our current code:
## - There's a missing line
## - There's a semantic error (the code does not raise an
##   error message, but it does not perform correctly)
##
##Find and fix these problems! Note that you should only need
##to change or add code where explicitly indicated.
##
##Hint: If you're stuck, use an example input list and trace
##the code and how it modifies your list on paper. For
##example, try writing out what happens to the following list:
##
##  [34, 16, 2, 78, 4, 6, 1]

#def sort_with_bubbles(lst):
#    #Set swap_occurred to True to guarantee the loop runs once
#    swap_occurred = True
    
#    #Run the loop as long as a swap occurred the previous time
#    while swap_occurred:
        
#        #Start off assuming a swap did not occur
#        swap_occurred = False
        
#        #For every item in the list except the last one...
#        for i in range(len(lst) - 1):

#            #If the item should swap with the next item...
#            if lst[i] > lst[i + 1]:

#                #Then, swap them! But these lines aren't
#                #quite right: fix this code!
#                temp = lst[i]
#                lst[i] = lst[i + 1]
#                lst[i + 1] = temp

#                swap_occurred = True

#    return lst

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: [1, 2, 3, 4, 5]
#print(sort_with_bubbles([5, 3, 1, 2, 4]))




##We've written the function, sort_with_select, below. It takes
##in one list parameter, a_list. Our version of selection sort
##involves finding the minimum value and moving it to an
##earlier spot in the list.
##
##However, some lines of code are blank. Complete these lines
##to complete the selection_sort function. You should only need
##to modify the section marked 'Write your code here!'

#def sort_with_select(a_list):
    
#    #For each index in the list...
#    for i in range(len(a_list)):
        
#        #Assume first that current item is already correct...
#        minIndex = i

#        #For each index from i to the end...
#        for j in range(i + 1, len(a_list)):
            
#            #Complete the reasoning of this conditional to
#            #complete the algorithm! Remember, the goal is
#            #to find the lowest item in the list between
#            #index i and the end of the list, and store its
#            #index in the variable minIndex.
#            #
#            #Write your code here!
            
#            if a_list[j] < a_list[j - 1]:
#                minIndex = j

#        #Save the current minimum value since we're about
#        #to delete it
#        minValue = a_list[minIndex]
        
#        #Delete the minimum value from its current index
#        del a_list[minIndex]
        
#        #Insert the minimum value at its new index
#        a_list.insert(i, minValue)

#    #Return the resultant list
#    return a_list
	

##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print: [1, 2, 3, 4, 5]
#print(sort_with_select([5, 3, 1, 2, 4]))




##Let's implement Mergesort! This is a complex problem
##because it applies recursion to sorting algorithms, but
##it's also by far the most efficient sorting algorithm we'll
##cover.

##First, we need a function definition: MergeSort should take
##as input one list.

#def mergesort(lst):
    
#    #Then, what does it do? mergesort should recursively
#    #run mergesort on the left and right sides of lst until
#    #it's given a list only one item. So, if lst has only
#    #one item, we should just return that one-item list.
    
#    if len(lst) <= 1:
#        return lst
    
#    #Otherwise, we should call mergesort separately on the
#    #left and right sides. Since each successive call to
#    #mergesort sends half as many items, we're guaranteed
#    #to eventually send it a list with only one item, at
#    #which point we'll stop calling mergesort again.
#    else:

#        #Floor division on the length of the list will
#        #find us the index of the middle value.
#        midpoint = len(lst) // 2

#        #lst[:midpoint] will get the left side of the
#        #list based on list slicing syntax. So, we want
#        #to sort the left side of the list alone and
#        #assign the result to the new smaller list left.
#        left = mergesort(lst[:midpoint])

#        #And same for the right side.
#        right = mergesort(lst[midpoint:])

#        #So, left and right now hold sorted lists of
#        #each half of the original list. They might
#        #each have only one item, or they could each
#        #have several items.

#        #Now we want to compare the first items in each
#        #list one-by-one, adding the smaller to our new
#        #result list until one list is completely empty.

#        newlist = []
#        while len(left) and len(right) > 0:

#            #If the first number in left is lower, add
#            #it to the new list and remove it from left
#            if left[0] < right[0]:
#                newlist.append(left[0])
#                del left[0]

#            #Otherwise, add the first number from right
#            #to the new list and remove it from right
#            else:
#                newlist.append(right[0])
#                del right[0]

#        #When the while loop above is done, it means
#        #one of the two lists is empty. Because both
#        #lists were sorted, we can now add the remainder
#        #of each list to the new list. The empty list
#        #will have no items to add, and the non-empty
#        #list will add its items in order.

#        newlist.extend(left)
#        newlist.extend(right)

#        #newlist is now the sorted version of lst! So,
#        #we can return it. If this was a recursive call
#        #to mergesort, then this sends a sorted half-
#        #list up the ladder. If this was the original
#        #call, then this is the final sorted list.

#        return newlist

##Let's try it out!
#print(mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))

##It works! To see more about how it works, check out
##MergesortwithPrints.py. To get a succinct version of
##this algorithm, checkout MergesortShort.py.




##Let's implement a binary search using a loop! For now,
##our search will just return True if the item is found,
##False if it's not.

##Like our linear search, our binary search needs to
##parameters: a list to search, and an item to search for.

#def binary_search(searchList, searchTerm):

#    #First, the list must be sorted.
#    searchList.sort()

#    #Now, each iteration of the loop, we want to narrow
#    #down the part of the list to look at. So, we need to
#    #keep track of the range we've narrowed down to so
#    #far. Initially, that will be the entire list, from
#    #the first index to the last.
    
#    min = 0
#    max = len(searchList) - 1
    
#    #Now, we want to loop as long as our range has any
#    #numbers left to investigate. As long as there is
#    #more than one number between minimum and maximum,
#    #we're not done searching.
    
#    while min <= max:

#        #We want to check the middle item of the
#        #current range, which is the average of the
#        #current minimum and maximum index. For
#        #example, if min was 5 and max was 15, our
#        #middle number would be at index 5. We'll
#        #use floor division because indices must be
#        #integers.
#        currentMiddle = (min + max) // 2

#        #If the term in the middle is the term we're
#        #looking for, we're done!
#        if searchList[currentMiddle] == searchTerm:
#            return True

#        #If not, we want to check if the term we're
#        #looking for should come earlier or later.

#        #If the term we're looking for is less than
#        #the current middle, then search the first
#        #half of the list:
#        elif searchTerm < searchList[currentMiddle]:
#            max = currentMiddle - 1

#        #If the term we're looking for is greater
#        #than the current middle, search the second
#        #half of the list:
#        else:
#            min = currentMiddle + 1

#        #Each iteration of the loop, one of three
#        #things happens: the term is found, max
#        #shrinks, or min grows. Eventually, either
#        #the term will be found, or min will be
#        #equal to max.

#    #If the search term was found, this line will
#    #never be reached because the return statement
#    #will end the function. So, if we get this
#    #far, then the search term was not found, and
#    #we can return False.
#    return False

##Let's try it out!
#intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
#print("23 is in intlist:", binary_search(intlist, 23))
#print("50 is in intlist:", binary_search(intlist, 50))

##Want to see something else interesting? Because of
##the way Python handles types, this exact same
##function works for any sortable data type. Check
##it out with strings:
#strlist = ["David", "Joshua", "Marguerite", "Jackie"]
#print("David is in strlist:", binary_search(strlist, "David"))
#print("Lucy is in strlist:", binary_search(strlist, "Lucy"))

##Or with dates!
#from datetime import date
#datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
#print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
#print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))


##Now, go see how it works with recursion instead of loops
##in RecursiveBinarySearch.py! Or, print how this works with
##LoopingBinarySearchwithPrints.py.



##Create a class called RightTriangle. RightTriangle should
##have two attributes (instance variables): opposite and
##adjacent. Make sure the variable names match those words.
##Both will be floats.
##
##RightTriangle should have a constructor with two required
##parameters, one for each of those attributes (opposite and
##adjacent, in that order).
##
##RightTriangle should also have a method called
##find_hypotenuse. find_hypotenuse should calculate the
##hypotenuse of the triangle based on the current values for
##opposite and adjacent.
##
##hypotenuse should NOT be an attribute of the class;
##instead, hypotenuse should be calculated and returned live
##when the method find_hypotenuse is called.
##
##The find_hypotenuse method should have NO parameters
##besides self. Instead, it should calculate the hypotenuse
##based on the current values for the opposite and adjacent
##attributes.
##
##Hint: In other words: opposite and adjacent will be
##attributes similar to guacamole and cheese in the Burrito
##class from Problem Set 5.1. find_hypotenuse will be a
##method similar to the get_cost method from the Burrito
##class.
##
##Hint 2: The formula for hypotenuse is the square root of
##opposite squared plus adjacent squared. The easiest way to
##find the square root is to use the exponent operator to
##raise the sum to the 0.5 power (e.g. sum**0.5).


##Write your class here!

#class RightTriangle:
    
#    def __init__(self, opposite, adjacent):
#        self.opposite = opposite
#        self.adjacent = adjacent
        
#    def find_hypotenuse(self):
#        return (self.opposite ** 2 + self.adjacent ** 2) ** (1 / 2)

##The code below will test your function. If it works, it
##should print 3.0, 4.0, and 5.0 in that order.
#test_triangle = RightTriangle(3.0, 4.0)
#print(test_triangle.opposite)
#print(test_triangle.adjacent)
#print(test_triangle.find_hypotenuse())



##Remember that Fibonacci's sequence is a sequence of numbers
##where every number is the sum of the previous two numbers.
##
##There exists a variant of Fibonacci's sequence called
##Fibonacci's multiplicative sequence. Fibonacci's
##multiplicative sequence is identical to Fibonacci's
##sequence, except that each number is the PRODUCT of the
##previous two numbers instead of the sum. Let's call these
##FibMult numbers.
##
##In order to make this interesting, we set the first two
##FibMult numbers to 1 and 2. So, the 1st FibMult number is
##1, and the second FibMult number is 2.
##
##So, here are the first few FibMult numbers:
##
##         n  = 1 2 3 4 5  6   7    8       9          10
## FibMult(n) = 1 2 2 4 8 32 256 8192 2097152 17179869184
##
##The sequence gets large fast!
##
##Write the function fib_mult using recursion. fib_mult
##takes as input an integer, and returns the FibMult
##number corresponding to that integer. For example:
##
## - fib_mult(1) = 1
## - fib_mult(2) = 2
## - fib_mult(3) = 2
## - fib_mult(9) = 2097152
## - fib_mult(12) = 618970019642690137449562112
##
##fib_mult MUST be implemented recursively.
##
##Hint: You will actually have two separate base cases,
##one for n = 1 and one for n = 2.


##Write your code here!

#def fib_mult(integer):
    
#    if integer == 1:
#        return 1
    
#    elif integer == 2:
#        return 2
    
#    else:
#        return fib_mult(integer - 1) * fib_mult(integer - 2)
    

##The lines below will test your code. If your funciton is
##correct, they will print 1, 2, 2, and 2097152.
#print(fib_mult(1))
#print(fib_mult(2))
#print(fib_mult(3))
#print(fib_mult(9))

#print(3 // 2)



# #Write a function called inverted_sort. inverted_ should
# #take as input a list of integers, and return as output a
# #list with the integers sorted from HIGHEST to LOWEST.
# #
# #You may use any sorting algorithm you want: bubble, merge,
# #insertion, selection, a new sort that you learned on your
# #own, or even one you created yourself. You may use loops,
# #or you may use recursion.
# #
# #You may not use Python's native list sort or reverse 
# #methods; you must write your own sort.


# #Write your function here!

# def inverted_sort(list_of_integers):
    
#    #print("Splitting list: " + str(list_of_integers))

#    new_list = []

#    if len(list_of_integers) == 1:
#        return list_of_integers
#    else:
#        midpoint = len(list_of_integers) // 2
#        list_1 = inverted_sort(list_of_integers[:midpoint])
#        list_2 = inverted_sort(list_of_integers[midpoint:])
#        #print(list_1, list_2)
#        while len(list_1) > 0 and len(list_2) > 0:
#            if list_1[0] > list_2[0]:
#                new_list.append(list_1[0])
#                list_1.remove(list_1[0])
#            elif list_2[0] > list_1[0]:
#                new_list.append(list_2[0])
#                list_2.remove(list_2[0])
#        new_list.extend(list_1)
#        new_list.extend(list_2)

#        #print(new_list)

#        return new_list
    

# #The code below will test your function. Feel free to
# #modify it. As written originally, it will print the list:
# # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# #print(inverted_sort([1,2,3]))
# print(inverted_sort([5, 4, 10, 1, 7, 2, 3, 6, 8, 9, 122, 334, 20009]))




#class Student:
    
#    def __init__(self, first_name, last_name):
#        self.first_name = first_name
#        self.last_name = last_name

#list_of_students = [Student("Franklin","Joyner"), Student("Jesse","Luna"), Student("Ashtyn","Simpson"), Student("Cody","Simpson"), \
#    Student("Ashtyn","White")]

#def check_attendance(list_of_students, first_name, last_name): 

#    middle_index = len(list_of_students) // 2
#    #print(middle_index)

#    if len(list_of_students) == 0:
#        return False

#    if list_of_students[middle_index].first_name == first_name and list_of_students[middle_index].last_name == last_name:
#        return True

#    elif list_of_students[middle_index].last_name > last_name or (list_of_students[middle_index].last_name == last_name \
#                                                                  and list_of_students[middle_index].first_name > first_name):
#        #print("eliminating top half of list")
#        return check_attendance(list_of_students[:middle_index], first_name, last_name)
        
#    elif list_of_students[middle_index].last_name < last_name or (list_of_students[middle_index].last_name == last_name \
#                                                                  and list_of_students[middle_index].first_name < first_name):
#        #print("eliminating bottom half of list")
#        return check_attendance(list_of_students[middle_index + 1:], first_name, last_name)

#print(check_attendance(list_of_students, "Ashtyn", "White"))



# #Write a function called add_to_dictionary. add_to_dictionary
# #should have three parameters: a dictionary, a potential new
# #key, and a potential new value.
# #
# #add_to_dictionary should add the given key and value to the
# #dictionary if the key is of a legal type to be used as a
# #dictionary key.
# #
# #If the key is a legal type to be used as a dictionary key,
# #return the resultant dictionary.
# #
# #If the key is _not_ a legal type to be used as a dictionary
# #key, return the string "Error!"
# #
# #Remember, only immutable types can be used as dictionary
# #keys. If you don't remember which types are immutable or
# #how to check a value's type, don't fret: there's a way
# #to do this without checking them directly!


# #Write your function here!

# def add_to_dictionary(dictionary, new_key, new_value):
#     try:
#         dictionary[new_key] = new_value
#         return dictionary
#     except TypeError:
#         return "Error!"

# #Below are some lines of code that will test your function.
# #You can change the value of the variable(s) to test your
# #function with different inputs.
# #
# #If your function works correctly, this will originally
# #print:
# #{1: "a", 2: "b", 3: "c", 4: "d"}
# #Error!
# a_dictionary = {1: "a", 2: "b", 3: "c"}
# print(add_to_dictionary(a_dictionary, 4, "d"))
# print(add_to_dictionary(a_dictionary, [4, 5, 6], "e"))