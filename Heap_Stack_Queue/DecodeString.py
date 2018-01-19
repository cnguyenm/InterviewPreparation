
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    
    return False

# @param s <string>
def decodeString(s):
    
    # check
    if (s == None):
        return None
        
    if (len(s) == 0):
        return s
    
    # stack to store char
    stack = []
    
    # var to decode
    temp = ''
    count = '' # change to number later
    
    # loop
    for i in s:
        
        if (i == ']'):
            # get last item in stack
            # temp is <string>
            temp = stack.pop() 
            
            # continue pop until see '['
            while(stack[-1] != '['):
                temp = stack.pop() + temp
            
            # get count
            stack.pop() #remove '['
            
            # pop until not number anymore
            count = stack.pop()
            while ( len(stack) > 0 and is_number(stack[-1]) ):
                count = stack.pop() + count
            
            
            # decode
            temp = temp * int(count)
            
            # add temp back to stack
            stack.append(temp)
        
        # if normal case
        else:
            stack.append(i)
            
    # put stack together
    return "".join(stack)
     
def main():
    s = "z1[y]zzz2[abc]"
    print( decodeString(s) )
    
main()