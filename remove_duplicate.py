def remove_duplicates(alist):
  if alist == []:
    return alist
  alist = sorted(alist)
  result = [alist[0]]
  for i in range(1,len(alist)):
    if alist[i] != alist[i-1]:
      result.append(alist[i])
  return result



'''
def remove_duplicate(alist):
  return list(set(alist))
'''
