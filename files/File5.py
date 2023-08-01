try:
   fin= open("students.txt", "r+")
        # print()
except:
    print("file is open")
 
# f=fin.read() 
print(fin.read()) 
input()
        # # f=fin.readlines()
        # print(f)
f1= open("students.txt","a") 
print()
sur=input("sur: ")
name=input("name: ")
mark=input("mark: ")
tmp=sur+" "+name+" "+str(mark) +"\n"
        # f1.write(tmp)
print(f1.write(tmp))
input()

def removeLine(fileIn, fileOut, lineNumber):
        with open(fileIn) as fr:
            lines = fr.readlines()
    
            counter=1 # position pointer 
    
            with open(fileOut, 'w') as fw:
                for line in lines:
                    if counter != lineNumber:
                        fw.write(line)
                    counter += 1
 
myFile='students.txt'
resultFile='result.txt'
newFile1=sorted('students.txt')
print(newFile1)
    
removeLine(myFile, resultFile, 2)

def replaceTextInFile(fileName,originText,newText):
        with open(fileName) as fileHandler:
            data = fileHandler.read()
            data = data.replace(originText, newText)
    
        with open(fileName,'w') as fileHandler:
            fileHandler.write(data)
    
def readFromFile(fileName):
        with open(fileName) as fileHandler:
            data = fileHandler.read()
            print(data)
        
myFile='students.txt'
    
        
print("Original file content:")
        
readFromFile(myFile)
    
replaceTextInFile(myFile,'Ivanova','Morozova')
    
print("New file content:")
readFromFile(myFile)
print()

# except:
#     pass
# finally:
#     fin.close()
#     f1.close()