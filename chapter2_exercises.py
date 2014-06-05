# Exercises for chapter 2:

# Name: Patrick Brand

# 2.1: Numbers with a leading zero end up interpreted as octals. 

# 2.2: The statements themselves don't actually output--the print statements need to be invoked. x + 1 does not change the stored value of x since there's no assignment
# (x = x + 1)

5
x = 5
x + 1

print '5'
print 'x = 5'
print 'x + 1'
print x

# 2.3 

width = 17
height = 12.0
delimiter = '.'

# guesses:
# 1. 8.5 ; incorrect guess because this wasn't a float
# 2. 8.5 ; correct
# 3. 4.0 ; correct
# 4. 15 ; incorrect because multiplication happens first, duh
# 5. ..... ; correct

print width / 2
print width / 2.0
print height / 3
print 1 + 2 * 5
print delimiter * 5

# 2.4 

# 1 

print 4 / 3 * 3.14159 * 5 ** 3 # I know this is incorrect, but I can't figure out how to get it anywhere near the correct answer, which I know from Google's implementation of the formula is around 523.6 
# 2 

bookstore_cost = 24.95 - (24.95 * .4)
first_shipping_cost = 3.0
second_shipping_cost = 0.75
books_bookstore_cost = bookstore_cost * 60.0
shipping_cost = first_shipping_cost + (second_shipping_cost * 59.0)
total_cost = books_bookstore_cost + shipping_cost

print total_cost # $945.50

# 3 

start_time = (3600 * 6) + (52 * 60)
print start_time
easy_mile = (8 * 60) + 15
tempo_mile = (7 * 60) + 12
run_time = (easy_mile * 2) + (tempo_mile * 3)
print run_time
total_time = start_time + run_time
print total_time

minutes = total_time / 60
hours = total_time / 3600

print 'final arrival at' + str(hours) + ':' + str(minutes)  