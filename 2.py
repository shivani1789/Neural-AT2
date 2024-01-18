
def wordCount():
    file1=open("input.txt","r")
    file2=open("output.txt","w")
    count={}
    for line in file1:
        w=line.strip().split(" ")
        for i in w:
            if(i in count):
                count[i]=count[i]+1 
            else: 
                 count[i]=1
    for i in count:
        file2.write(i+ ": "+str (count[i]));
        file2.write("\n")
    print(count)
        
        # count[l]
        

wordCount()
