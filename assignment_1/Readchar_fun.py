file = open("readtext.txt","r",encoding='utf-8')
data = file.read()

maxlengthword = 0
wordcount = 0
for i, value in enumerate(data.split()):
    wordcount = len(value)
    if(maxlengthword < wordcount):
        maxlengthword=wordcount
print("Find the length of total read character is :",len(data))
print("in text file found longest word count is :", maxlengthword)
charSet = set(data)
count = 0
for set in charSet:
    for char in data:
        if char == set :
            count +=1
    print(set,"------>",count, end="  ")
    count = 0
print("jdg")