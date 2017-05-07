
#write a Pig Latin translator in Python
import enchant
d = enchant.Dict("en_US")
print 'Welcome to the Pig Latin Translator!'
word = raw_input('Enter the word in English:     ')
if len(word) > 0 and d.check(word) == True:
    new_word = word[1:]+word[0]+'ay'
else:
    print 'wrong entry'
    
print new_word
