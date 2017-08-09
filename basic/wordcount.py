# Written using python 3.6.2
#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def parse_words(filename):
  f = open(filename, 'rU') #read-only universal
  dict = {} #dictionary of words
  for line in f:
    line = line.lower() #lowercase
    words = line.split() #split into words by whitespace delimiter
    for word in words:
      if word in dict:
        dict[word] += 1 #add 1 if in dictionary
      else:
        dict[word] = 1 #base-case: not in dictionary, add it
  f.close()
  return dict
  
def print_words(filename):
  words_dict = parse_words(filename)
  sort_by_count = sorted(words_dict.keys()) #sort dictionary by key
  for key in sort_by_count:
    print (key + ': ' + str(words_dict[key]))
  return
  
def get_count_in_tuple(count_tuple):
  return count_tuple[1]
  
def print_top(filename):
  words_dict = parse_words(filename)
  # Sorts tuples in reverse, so the largest counts are first.
  word_count_tuples = sorted(words_dict.items(), key=get_count_in_tuple, reverse=True)
  
  # Print the first 20
  for item in word_count_tuples[:20]:
    #print (item[0], item[1])
    #print ('{0: <16}'.format(item[0]) + str(item[1]))
    #print ('{{0: <{}}}'.format(12).format(item[0]), str(item[1]))
    print("%-10s %d" % (item[0], item[1]))
  return

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
