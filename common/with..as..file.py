with open("text.txt", "r+") as my_file:
  my_file.write("hello python")
print my_file.closed
if my_file.closed == False:
  my_file.close()
print my_file.closed
f = open("text.txt","r+")
print f.read()
