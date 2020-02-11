def writeFile(client_data):
    f = open('text.txt','a')
    f.write(client_data)
    f.write('\n')