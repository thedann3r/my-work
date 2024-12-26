# count = 0
# while count <= 100:
#     print(count)
#     count += 25

# for i in range(1,100,1):
#     print(i)

marks = [12,13,15,19,21]

perc = list()

for mark in marks:
    total = (mark*100) / 30
    perc.append(total)
print(min(perc))