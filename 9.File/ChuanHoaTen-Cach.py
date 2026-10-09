f1=open("ChuanHoaTen-Cach.input.txt", "r")
f2=open("ChuanHoaTen-Cach.output.txt", "w")
for line in f1:
    line=(' '.join(line.split())).title()
    f2.write(line)
f1.close()
f2.close()