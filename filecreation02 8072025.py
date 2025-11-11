f = open('demo1.txt', 'w')
f.write('Hi how are you')
f.close()

f=open('demo1.txt', 'a')
f.write('\ngood to see you')
f.close()

f=open('demo1.txt', 'r')
line=f.readlines()
line[0]= 'Hi my name is Chetan\n'
f.close()
f=open('demo1.txt','w')
f.writelines(line)
f.close()

f=open('demo1.txt', 'a')
f.write('\nthankyou')
f.close()

f=open('demo1.txt', 'r')
line=f.readlines()
line[2]= 'Goodbye\n'
f.close()
f=open('demo1.txt','w')
f.writelines(line)
f.close()

f=open('demo1.txt', 'r')
line1=f.read()
print(line1)
f.close()

