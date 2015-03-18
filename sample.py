aaa = []
ab=open("/home/alina/Desktop/Exercise/testing_file.txt", 'r')
for line in ab:
	c=line.split(' ')
	aaa.append(c[0])
ab.close()

print aaa
ac=open("/home/alina/Desktop/Exercise/edited.txt", 'w')
for a in aaa:
	ac.write(a)
	ac.write('\n')
ac.close

