def is_anagram(list_str1,list_str2):
        list_str1=list(list_str1)
        list_str1.sort()
        list_str2=list(list_str2)
        list_str2.sort()
        return(list_str1==list_str2)
print (is_anagram('anagram','nagaram'))
print(is_anagram('cat','rat'))

