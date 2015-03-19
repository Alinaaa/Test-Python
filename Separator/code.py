firstname = []
lastname = []
middlename = []
infile=open('Name.txt','r')
for line in infile:
	splitname= line.split(' ')
	firstname.append(splitname[0])
	lastname.append(splitname[len(splitname)-1].rstrip())
	if len(splitname) >= 3:
		middlename.append(splitname[len(splitname)-2].rstrip())
	else:
		middlename.append(' ')

infile.close

print firstname
print lastname
print middlename

counter=0

outfile =open('Separated_name','w')
for counter  in xrange(len(firstname)):
	outfile.write (firstname[counter])
	outfile.write(',')
	outfile.write (lastname[counter])
	outfile.write(',')
	outfile.write (middlename[counter])
	outfile.write('\n')
outfile.close




