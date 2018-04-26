def is_sorted(list_1,list_2): 
	list_1=list(list_1)
        list_1.sort()
        list_2=list(list_2)
        list_2.sort()
        return(list_1==list_2)
print (is_sorted([1,2,2]))
print (is_sorted(['b','a']))

