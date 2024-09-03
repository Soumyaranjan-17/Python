import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))


print(mpg[:3])
print()
print(len(mpg))
print(mpg[1]["manufacturer"])
print(mpg[0].keys())
print(sum(float(d["cty"]) for d in mpg)/len(mpg))