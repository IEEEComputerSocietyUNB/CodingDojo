-- Isto eh um comentario

-- # Tipos basicos
print("Tipos basicos: ")
local a_boolean = true
local another_boolean = false
local und = a_boolean and another_boolean
local oder = a_boolean or another_boolean
local number = 2
local another_number = 5
print("5 / 2 = " .. another_number / number) -- todos os numeros sao ponto flutuante!
local a_string = "hello"
local my_name = "joe"
local classic_string = a_string .. " " .. my_name .. "!"
print(classic_string)

-- # Estruturas de controle
print("Exemplo de if:")
if number > 3 then
    print(number)
elseif another_number ~= 5 then
    print(another_number)
else
    print("wtf dude")
end

print("For example:")
for i = 1, another_number do
    print("  " .. i)
end

print("Exemplo de while:")
local j = 0
while j < 10 do
    print("  " .. j)
    j = j + 3
end

function sayHello(name)
    return "hallo " .. name .. "!"
end

-- # Tabelas
local tabela = { }
local lista = { }

for i = 1, 10 do
    table.insert(lista, i*2)
end

for i, it in ipairs(lista) do
    print("# " .. i .. ": " .. it)
end
print("Tamanho da lista: " .. (#lista))

tabela["nome"] = "Joe"
tabela.idade = 22

print("Tabela:")
for key, value in pairs(tabela) do
    print("  " .. key .. ": " .. value)
end
tabela.idade = nil
print("Tabela:")
for key, value in pairs(tabela) do
    print("  " .. key .. ": " .. value)
end

tabela.poder = sayHello
print(tabela.poder(tabela.nome))
