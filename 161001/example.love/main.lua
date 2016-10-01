function love.load()
    dimension = 16
    relogio = love.timer.getTime()

    -- Criando o personagem
    me = { }
    me.img = love.graphics.newImage("art/spacer.png")
    me.x = 20
    me.y = 20

    -- Criando o ambiente
    they = { }
    they.img = love.graphics.newImage("art/invader.png")
    they.x = 100
    they.y = 100
end

function love.update()
    agora = love.timer.getTime() - relogio
	
    -- Atualizando o personagem
    if love.keyboard.isDown("right") then
        me.x = me.x + 5
    end
    if love.keyboard.isDown("left") then
        me.x = me.x - 5
    end
    if love.keyboard.isDown("up") then
        me.y = me.y - 5
    end
    if love.keyboard.isDown("down") then
        me.y = me.y + 5
    end

    -- Atualizando o ambiente
    they.x = 100 + 50 * math.sin(2 * math.pi * agora / 2)
    they.y = 100 + 50 * math.sin(2 * math.pi * agora / 2)
end

function love.draw()
    -- love.graphics.draw( drawable, x, y, r, sx, sy, ox, oy, kx, ky )
    -- Desenhando o personagem
    love.graphics.draw(me.img, me.x, me.y, 0, 1, 1)

    -- Desenhando o ambiente
     love.graphics.draw(they.img, they.x, they.y, 0, 1, 1)

     -- Desenhando um quadradinho
     love.graphics.setColor(255, 150, 150)
     love.graphics.rectangle("fill", 300, 350, 30, 40)
end
