x = 1
y = 4
bin_x = bin(x)[2:]
bin_y = bin(y)[2:]
while len(bin_x) > len(bin_y):
  bin_y = bin_y.zfill(len(bin_x))
bin_x = bin_x.zfill(len(bin_y))
dif = 0
for i in range(len(bin_x)):
  if bin_x[i] != bin_y[i]:
    dif += 1
print dif 

'''
def hamming_distance(x,y):
  return bin(x^y).count("1")
'''