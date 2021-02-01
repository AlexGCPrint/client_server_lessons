import chardet
rawdata = open('test_file', "rb").read()
result = chardet.detect(rawdata)
charenc = result['encoding']

print(charenc)