lines_seen = set()
outfile = open('C:/Users/adminlocal/Desktop/example.txt', "w")
infile = open('C:/Users/adminlocal/Downloads/duplicate.txt', "r")
print ("The file bar.txt is as follows")
for line in infile:
    print(line)
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print ("The file foo.txt is as follows")
for line in open('C:/Users/adminlocal/Desktop/example.txt', "r"):
    print (line)
