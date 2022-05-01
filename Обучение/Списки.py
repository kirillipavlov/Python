def update_dictionary (d, key, value):
    if key in d.keys():
        d[key] += [value]
    elif key * 2 in d.keys():
        d[key * 2] += [value]
    else:
        d.update({key * 2 : [value]})
d={}
#d = {3 : [20]}
update_dictionary(d, 3, 345)
update_dictionary(d, 4, 680)
update_dictionary(d, 6, 234)
print (d)