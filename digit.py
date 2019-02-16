def digit_sum(n):
  sum = 0
  n = str(n)
  for digit in n:
    sum += int(digit)
  return sum
