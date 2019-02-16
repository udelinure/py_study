arrayOfAnswer = [] 
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
dic = {}
for i in cpdomains:
  count, domain = i.split()
  count = int(count)
  eachdomain = domain.split('.')
  for i,j in enumerate(eachdomain):
    value = ".".join(eachdomain[i:])
    if value not in dic:
      dic[value] = count
    else:
      dic[value] += count
for key,value in dic.iteritems():
  ans = str(value) + " " +str(key)
  arrayOfAnswer.append(str(ans))
print arrayOfAnswer 
