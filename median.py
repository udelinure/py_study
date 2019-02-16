def median(alist):
  if alist == []:
    return False
  alist = sorted(alist)
  if len(alist) % 2 == 0:
    return (alist[len(alist)/2] + alist[len(alist)/2-1])/2.0
  return alist[len(alist)/2]
