names = ["Mike","john","steve"]
names_iterator = iter(names)

for i in range(len(names)):
    print(next(names_iterator))



names = ["Mike","John","steve"]
for name in names:
    print(name)
