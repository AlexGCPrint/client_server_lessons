import yaml

data = {
    '1' : ['1', '2', '3'],
    '2' : 2,
    '3' : {
        '1😂' : '1',
        '2💶' : '2',
        '3€' : '3'
    }
}

with open('file.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=True, allow_unicode=True)

with open('file.yaml') as f:
    yaml_data = yaml.load(f, Loader=yaml.FullLoader)

if yaml_data == data:
    print('Данные совпали')
else:
    print('Данные не совпали')