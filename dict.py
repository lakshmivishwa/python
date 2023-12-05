d= {101:"lakshmi", 102:"sonal", 103:"Rajashree"}
for k in d:
    print(k,":", d[k])

d[104]="Radhika" # will add the key and data  
print(d)

d[102]="Radhika" # will change 102's value
print(d)

# del d[102] #delete data

# # methods

# d.keys()
# d.values()
# d.items()


# for t in d.items():
#     k=t[0]
#     d=t[1]
#     print(k,d)

s=sorted(d)
print(s)

d= {a:a**2 for a in range(1,8,1)}
print(d)