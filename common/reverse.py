def reverse(text):
  result = []
  for i in range(0,len(text)):
    result.append(text[i-(2 * i + 1)]) 
  result = "".join(result)
  return result


'''
my_list = range(1, 11)

# Add your code below!
backwards = my_list[-1::-1]
print backwards


to_one_hundred = range(101)
# Add your code below!

backwards_by_tens = to_one_hundred[-1::-10]
print backwards_by_tens
'''