#Importing a temparay file 
import tempfile
#Creating a temparay file 
tempFile = tempfile.TemporaryFile()

tempFile.write(b" Writing some text in to the temparay file ")
tempFile.seek(0)
print(tempFile.read())