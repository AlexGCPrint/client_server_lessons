args = ['разработка', 'администрирование', 'protocol', 'standard']
for arg in args:
    arg_encode = arg.encode('utf-8')
    print(type(arg_encode))
    print(arg_encode)
    arg_decode = arg_encode.decode('utf-8')
    print(arg_decode)
    print(type(arg_decode))
    print('*' * 25)

