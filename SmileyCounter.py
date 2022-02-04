def count_smileys(arr):
    happy,count=[[":",";"],["-","~"],[")","D"]],0
    for i in arr:
        rules=[len(list(i))==2,list(i)[0] in happy[0],list(i)[-1] in happy[2],list(i)[1] in happy[1],len(list(i))==3]
        if all(rules[:3]) or all(rules[1:]):
            count+=1
    return count
