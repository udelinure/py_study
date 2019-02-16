def fizz_count(x):
  count = 0
  for string in x:
    if string == "fizz":
      count = count+1
  return count
print fizz_count(['fizz', 'fizz', 'fizz', 8, 'fizz', 'fIzZ'])
