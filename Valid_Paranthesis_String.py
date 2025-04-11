# string consists of (, ), *
# * can be replaced by ( or ) and that has to be valid or can be made valid
# like simply chekcing, can you make it valid or not

def valid_paranthesis(s:str)->bool:
    open_count = 0
    close_count = 0

    for ch in s:
        if ch =='(':
            open_count += 1
        elif ch == ')':
            open_count -= 1
            if open_count < 0:
                return False
        else:
            close_count+=1
        
        if close_count < open_count:
            return False

    # at last, open count should be zero then only its valid paranthesis        
    return open_count == 0

s="((*)"
print("The decision is:",valid_paranthesis(s))