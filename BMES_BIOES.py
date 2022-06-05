f = open(r'./output/BMES.txt', 'r', encoding='utf-8')
f1 = open(r'./output/BIOES.txt', 'w+', encoding='utf-8')
str1 = []

for line in f.readlines():
    # print(list(line))
    if line != "\n":
        line1 = line.split()
        str2 = line1[0]
        for i in range(1, len(line1)):
            line2 = list(line1[i])
            if line2[0] == "M":
                line2[0] = "I"
            str3 = ''
            for i in line2:
                str3 = str3 + i
            str2 = str2 + ' ' + str3
        print(str2)
        str1.append(str2)
    else:
        str1.append(line)
for j in str1:
    f1.write(j)
    f1.write("\n")