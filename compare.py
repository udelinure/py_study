def findMinAndMax(list):
    if list is None or list == []:
        min = max = None
    else:
        min = max = list[0]
        for one in list:
            if one < min:
                min = one
            if one > max:
                max = one
    res = (min,max)
    return res
def comparation(list):
    max_number = max(list[:])
    min_muber = min(list[:])
    return max_number,min_muber
string = raw_input("pls in put the numbers:(eg:0,1,2,3) ")
string_list = string.split(',')  #save the string into array
list = map(int,string_list) #transfer string to int
print findMinAndMax(list)
print comparation(list)