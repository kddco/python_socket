def read_SendFile():
    f = open('text.txt', 'r')
    getText = f.read()
    print('檔案內容:', getText)
    return getText