def ParseFileByName(fileName):
    with open(fileName) as f:
        content = []
        for line in f:
            words = line.strip().split(' ')
            content.append(words)
    if(len(content) == 0):
        return Exception("file is empty")
    else:
        return content
def WriteSearchedArraysInFile(fileName,searchedWord,array):
    with open("file2.txt", "w") as file:
        for el in array:
            if searchedWord in el:
                for elem in el:
                    file.write(elem + " ")
                file.write("\n")

