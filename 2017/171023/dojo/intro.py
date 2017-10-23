def escolaridade(idade):
    if idade < 10:
        return 'fundamental'
    elif (idade >= 10) and (idade < 18):
        return 'medio'
    else:
        return 'superior'

entrada = input()
print('hello ' + entrada)
a = 7
b = 3
print(a+b)
print(a-b)
print(a*b)
print(b/a)
print(b//a)
i = 23
print('voce tem ' + str(i) + ' anos e esta no ensino ' + escolaridade(i))
print('olar ' * 3)
print(len([1,2,3]))
