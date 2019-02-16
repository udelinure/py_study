def check_bit4(input1):
  if input1 >= 8:
    if str(bin(input1))[-4] == "1":
      return "on"
    return "off"
  return "off"
print check_bit4(0b1000)




'''
def check_bit4(input1):
  return "on" if input1&8 else "off"
print check_bit4(0b1000)
'''
