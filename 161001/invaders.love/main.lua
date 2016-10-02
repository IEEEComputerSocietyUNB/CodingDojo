function love.load()
	nave = { }
	nave.imagem = love.graphics.newImage('art/spacer.png')
	
	nave.x = 300
	nave.y = 350
	tempoinicial = 0
	tiros = {} -- lista de tiros
	tiro = {}
	tiro.larg = 4
	tiro.alt = 8
	aliens = {}
	
	for i =1,5 do
		table.insert(aliens,criaAlien(i))
	end
	
	incremento = 5
end

function criaAlien(i)
	local alienzin = {}
	alienzin.x = 100*i
	alienzin.y = 100
	alienzin.imagem = love.graphics.newImage('art/invader.png')
	return alienzin
end

function love.update()
	
	--movimento personagem
	if love.keyboard.isDown('a') then
		if nave.x > 1 then
			nave.x = nave.x - incremento
		end
	end
	if love.keyboard.isDown('d') then
		if nave.x < 584 then
			nave.x = nave.x + incremento
		end
	end
	if love.keyboard.isDown('w') then
		if nave.y > 1 then
			nave.y = nave.y - incremento
		end
	end
	if love.keyboard.isDown('s') then
		if nave.y < 384 then
			nave.y = nave.y + incremento
		end
	end
	if love.keyboard.isDown('escape') then
		love.event.quit()
	end
	-- tiro
		
	if love.keyboard.isDown('k') and tempoinicial==0 then 	
		table.insert(tiros, atira())
	end
	-- Tiro Update
	for i, tiroaux in pairs(tiros) do
		tiros[i].y = tiroaux.y  - incremento
		for j, alienaux in pairs(aliens) do
			if compara(tiroaux.x, alienaux.x) then
				tiros[i] = nil -- apagar do item
				aliens[j] = nil -- apagar do item
			end
		end
		
	end
	tempoinicial=tempoinicial+1
	if tempoinicial>=5 then
		tempoinicial=0
	end
	--Anda alienzin
	for i, alienaux in pairs(aliens) do
		aliens[i].y = alienaux.y  + 1
	end
	
	
end

function love.draw()
	love.graphics.draw(nave.imagem, nave.x, nave.y, 0, 1, 1)
	
	for i, tiroaux in pairs(tiros) do
		love.graphics.rectangle("fill", tiroaux.x, tiroaux.y, tiro.larg, tiro.alt)
	end
	for i, alienaux in pairs(aliens) do
		love.graphics.draw(alienaux.imagem, alienaux.x, alienaux.y, 0, 1, 1)
	end	
end
	
function atira()
	local tiro = { }
	tiro.x = nave.x
	tiro.y = nave.y
	return tiro
end

function compara (tiroX, invaderX)
	return invaderX <= tiroX and
		invaderX + 16 >= tiroX
end