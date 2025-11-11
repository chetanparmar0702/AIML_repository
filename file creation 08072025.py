f = open('demo.txt', 'w')
f.write('created a file')
f.close()

f=open('demo.txt', 'a')
f.write('\ncreated a second line')
f.close()

f=open('demo.txt', 'r')
line1=f.read()
print(line1)
f.close()

f=open('demo.txt', 'r')
line2=f.readlines()
print(line2)
f.close()



