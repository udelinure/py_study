def count(sequence, item):
  number = 0
  for letter in sequence:
    if letter == item:
      number += 1
  return number
