start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()

print square_list

'''


1.
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# Use index() to find "duck"
print duck_index
# Your code here!
animals.insert(duck_index,"cobra")

print animals # Observe what prints after the insert operation


2.
animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]



3.
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("1")
suitcase.append("2")
suitcase.append("3")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase
'''