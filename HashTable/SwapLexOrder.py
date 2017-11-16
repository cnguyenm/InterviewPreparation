"""
Given a string str and array of pairs that indicates which indices in the string can be swapped, 
return the lexicographically largest string that results from doing the allowed swaps. 
You can swap indices any number of times.

Example

For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
swapLexOrder(str, pairs) = "dbca".

By swapping the given indices, 
you get the strings: "cbda", "cbad", "dbac", "dbca".
The lexicographically largest string in this list is "dbca".
"""


# s: string
# p: pairs, [[1,4], [3,4]]
def swapLexOrder(s, pairs):
    
    # component list, [(1,3,4),(2)]
    compo_list = []
    has_add = 0
   
    # add to component dict
    for p in pairs:
        
        has_add = 0
        
        
        # if compo_list is empty
        if (len(compo_list) == 0):
            t = set()
            t.add(p[0])
            t.add(p[1])
            compo_list.append(t)
            continue
        
        # if compo_list is not empty
        for i in range(len(compo_list)):
            
            # if exist in one components
            if (p[0] in compo_list[i] or p[1] in compo_list[i]):
                compo_list[i].add(p[0])
                compo_list[i].add(p[1])
                has_add = 1
                break
                
        # if compo_list not have any components, which contains pairs
        if (has_add == 0):
            t = set()
            t.add(p[0])
            t.add(p[1])
            compo_list.append(t)
    
    print("Component List: " + str(compo_list))
    
    # union the component
    x = []
    has_union = 0
    for i in range(len(compo_list)):
        
        has_union = 0
        
        # if x has a compo share element
        for j in range(len(x)):
            if (bool(x[j] & compo_list[i])):
                x[j] = x[j].union(compo_list[i])
                has_union = 1
                break
                
        # if x does not share any        
        if (has_union == 0):
            x.append(compo_list[i])
    
    compo_list = x
    
    # sort the component
    compo_str = []      # ['a','c','d']
    compo_index = []    # [0, 2, 3]
    s_list = list(s)
    for compo in compo_list:
        
        # get char from original string
        compo_index = list(compo)
        for i in compo_index:
            compo_str.append(s[i-1])
            
        # sort    
        compo_str = sorted(compo_str, reverse=True)
        
        print(compo_str)
        
        # add back to string
        compo_index = sorted(compo_index)
        j = 0
        for i in compo_index:
            s_list[i-1] = compo_str[j]
            j += 1
        
        print("".join(s_list))
        # reset
        compo_str = []
        
        
    s = "".join(s_list)
    return s    

def main():
    
    s = "acxrabdz"
    p = [[1,3], 
         [6,8], 
         [3,8], 
         [2,7]]
    
    swapLexOrder(s, p)

main()
