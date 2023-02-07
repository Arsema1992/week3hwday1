#Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups 
#(return None for names with no first and last name, or names that aren't properly capitalized)
#"""
#Expected Output
#Abraham Lincoln
#Andrew P Garfield
#Connor Milliken
#Jordan Alexander Williams
#None
#None
#"""
import re
f = open('./regex_test.txt')
my_data= f.readlines()
data_pattern = re.compile('([A-Z][a-zA-Z]+[])(A-Z) ([A-Z][a-zA-Z]+)')
for data in my_data:
    if data_pattern.match(data):
        print(data)
    else:
        print('none')