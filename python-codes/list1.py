#!/usr/bin/python 

# name:		match_ends
# function:	Given a list of string, returns the count of 
#		number of string with string length of 2 or
#		more and the first and last characters of 
#		the string are the same.
# args:		words

def match_ends(words):
    count = 0
    for word in words:
    	if len(word) >= 2 and word[0:1] == word[-1:]:
    	    count = count+1
    return count

# name:		front_x
# function:	Given a list of string, return a list with strings
#		in sorted order, except all the strings that begin
#    	        with x first.
# args:		words

def front_x(words):
    a_list = []
    b_list = []
    for word in words:
    	if word[0:1] == 'x':
    	    a_list.append(word)
    	else:
    	    b_list.append(word)
    return sorted(a_list) + sorted(b_list)

# name: 	last
# function:	extract the last element from a tuple -- used for
#    	    	custom sorting below.
# args: 	tuple_element

def first(tuple_element):
  return tuple_element[0]

# name:		sorted_first()
# function :    given a list of non-empty tuples, return a list sorted
#               in increasing order by the first element in each tuple
# args:         words

def sorted_first(words):
    return sorted(words, key=first)

def main():
    words = ['aba','mgm','aaa','a','aa']
    count = match_ends(words)
    print count
    words = ['xyz', 'xabc', 'aa', 'mxm', 'abx', 'x']
    newlist = front_x(words)
    print newlist
    words = [(1,2),(3,7),(5,9),(7,0),(1,10),(9,9)]
    sorted_tuples = sorted_first(words)
    print sorted_tuples

if __name__=='__main__':
   main()
