def duplicate_count(text):
    text=text.lower()
    dict_str={}
    count=0
    for letter in text:
        if letter in dict_str:
            dict_str[letter]+=1
        else:
            dict_str[letter]=1
    for i in dict_str:
        if dict_str[i]>1:
            count+=1
    return count
     
