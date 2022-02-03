def pig_it(text):
    text=text.split()
    txt=""
    for i in text:
        if ord(i[0]) in range(65,123):
            temp=i[0]+"ay "
            txt+=i[1:]+temp
        else:
            txt+=i
    return txt.strip()
