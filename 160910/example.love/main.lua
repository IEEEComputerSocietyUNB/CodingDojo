function love.load()
    dimension = 16

    -- Criando o personagem
    me = { }
    -- me.img = love.graphics.newImage("art/")
    me.x = 20
    me.y = 20

    -- Criando o ambiente
    they = { }
    they.x = 100
    they.y = 100

end

function love.update()
    

    -- Atualizando o personagem

    -- Atualizando o ambiente
    they.x = 100 + 100 * math.sin()
    they.y = 100 + 100 * math.sin()
end

function love.draw()
    -- Desenhando o personagem

    -- Desenhando o ambiente
end
