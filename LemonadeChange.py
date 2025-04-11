def LemonadeChange(arr):
    five = 0
    ten = 0
    # twenty_bill = 0 we dont need this bcoz we'll not be returning this 20 bill
    for i in range(len(arr)):
        if arr[i] == 5:
            five = five + 1
        elif arr[i] == 10:
            if five:
                five = five - 1
                ten = ten + 1
            else:
                return False
        else:
            if ten and five:
                ten = ten - 1
                five = five - 1
            elif five >= 3:
                five = five - 3
            else:
                return False
    return True


print(LemonadeChange([5, 5, 5, 10, 20])) 
print(LemonadeChange([5, 5, 10, 10, 20]))
                
             

