# Exercises for chapter 3:

# Name: Patrick Brand

import math

# 3.1: error is NameError: "name 'repeat_lyrics' is not defined"

# 3.2: works okay (output repeats once, presumably because print_lyrics() is not actively called until after it's defined... even if that's out of order

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

repeat_lyrics() 

# 3.3 

def right_justify(s):
    length = len(s)
    indent_num = 70 - length
    indent_spaces = indent_num * ' '
    print indent_spaces + s
    
right_justify('allen')

# 3.4 

def do_twice(f, s):
    f(s)
    f(s)

def print_twice(s):
    print s
    print s
    
def do_four(f, s):
    print 'calling do_four()'
    do_twice(f, s)
    do_twice(f, s)

do_twice(print_twice, 'spam')
do_four(print_twice, 'spam')