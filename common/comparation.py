def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
answer = raw_input("input the number u want to compare with 5  ")       
print greater_less_equal_5(answer)


'''print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)'''

