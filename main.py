def parseFileByName(fileName):
    with open(fileName) as f:
        content = []
        for line in f:
            words = line.strip().split(' ')
            content.append(words)
    if(len(content) == 0):
        return Exception("file is empty")
    else:
        return content
