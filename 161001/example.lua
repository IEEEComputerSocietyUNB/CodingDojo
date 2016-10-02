local modulo = require("module")

-- Comentário!

-- # Tipos básicos
verdadeiro = true
falso = false
local numero = 5
local outro_numero = 13
print(outro_numero / numero)
print(verdadeiro and falso)
print(verdadeiro or falso)
classic_string = 'hello '
my_name = 'joe'
my_name = 5
yet_classic_string = classic_string .. my_name
print(yet_classic_string)
print(my_name)

-- # Estruturas de controle
if falso then
	print('oops')
elseif verdadeiro and falso then
	print('oops again')
else
	print('ok!')
end

i = 1
while i < 10 do
	print(i * 2)
	i = modulo.somar(i, 1)
end

-- # Tabelas
tabela = { }
lista = { }

print('# LISTA')
-- Inserindo valores na lista
for i = 1, 10 do
	table.insert(lista, i)
end
-- Printando a lista
print("tabela:")
for i, valor in pairs(lista) do
	print(i .. '. ' .. valor)
end
-- Atualizando os valores da lista
for i, valor in pairs(lista) do
	lista[i] = valor + 1 
end
-- Printando a nova lista
print("tabela:")
for i, valor in pairs(lista) do
	print(i .. '. ' .. (valor))
end
print("...")


tabela["indice"] = 1
tabela.ind = 2
-- tabela["ind"] = 2


tabela.func = function(name)
	return "hello " .. name
end
print(tabela.func("frank"))

tabela.indice = nil -- apagar do item
for i, valor in pairs(tabela) do
	print(i .. '. ' .. (valor))
end
