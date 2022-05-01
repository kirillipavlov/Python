def update_dictionary (d, key, value):
    key += key * (key not in d)
    #print(key, key not in d)
    d[key] = d.get(key, []) + [value]
d={}
#d = {3 : [20]}
update_dictionary(d, 3, 345)
update_dictionary(d, 4, 680)
update_dictionary(d, 6, 234)
print (d)