pyg = 'ay'

original = raw_input('Enter a word:  ')
word = original.lower()
first = word[0]
new_word = "%s%s%s" % (word,first,pyg)
new_word = new_word[1:len(new_word)]
print new_word
if len(original) > 0 and original.isalpha():
  print original
else:
  print 'ur input has some problems'
