#!/usr/bin/env python
# /usr/bin/env : Find correct location and version of python as per PATH

# https://www.youtube.com/watch?v=N4mEzFDjqtA

''' To use Multiple Line Comment
    use 3'
'''
print "Hello World!!"

name = "Rahul!"
age  = 25
# printf type printing
print("Name = %s Agne : %d" % (name, age))

'''
    Python Built-in Data Types
    1. Number : int, float, long, complex
    2. String : str, unicode
    3. List   : list []
    4. Tuples : tuple ()
    5. Dict/map : dict {}
'''
int_num = int(23.5)
float_num = float(23.5)
long_num  = long(0xffffffffffffffff)
complex_num = complex(5,4);

print(int_num, float_num, long_num, complex_num);

print( "5.1 // 2 (floored) integer division  x and y = " , (5.1 // 2))
print( "5.1 / 2 division of x and y = " , (5.1 / 2))

str_name = str("hi this is string")
str_multiline = ''' hi this is multiple
                    Wow
                '''
print(str_multiline)
unicode_name = unicode("Hi  this is unicode name")

print(str_name)
print(unicode_name)

# concat string
print ( str_name + str_multiline );
big_string  = "%s BBBBB %s" % (str_name, str_multiline);
print(big_string);


list_num = [1,2,3,4,5]
tuple_num = (1,2,3,4,5)

print(list_num)
print(tuple_num)

dic_map = { 'A' : 1,
            'B' : 2,
            'C' : 3,
          }
print(dic_map)
print(dic_map.keys())
print(dic_map.values())
