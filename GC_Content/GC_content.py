#find GC content of brca1 gene
#brca1 gene is the one for breast cancer
#download the FASTA format of the gene from NCBI

with open('brca1.txt','r') as GC:
    #set the values to zero
    a=t=c=g=0
    #skip the header which is first line
    GC.readline()
    for line in GC:
        #make all the char lower case
        line=line.lower()
        #break #this break statement print only the first line and break the loop
        #again using for loop for each line
        #this reads each character in each line
        for char in line:
            if char=='g':
                g+=1 #increase the value of g with 1 if the letter in gene is g
            if char=='c':
                c+=1
            if char=='a':
                a+=1
            if char=='t':
                t+=1
    print('the number of g in GC is:' + str(g))
    print('the number of c in GC is:' + str(c))
    print('the number of a in GC is:' + str(a))
    print('the number of t in GC is:' + str(t))

    gc=(g+c+0.)/(g+c+a+t+0.)
    print(str(gc))
