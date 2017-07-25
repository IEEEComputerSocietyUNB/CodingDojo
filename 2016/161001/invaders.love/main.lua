	------------------- FUNÇÕES BÁSICAS
-- Executa apenas uma vez
function love.load()
	local joysticks = love.joystick.getJoysticks()
	playerOne = joysticks[1]
	playerTwo = joysticks[2]

	nave = criarNave (200, 350);
	nave2 = criarNave(400, 350);
	aliens = criarAliens (5);
	tiros = criarTiros ();
	deslocamento = criarDeslocamentos ();

	tempoBase = 0;
end

-- Executa enquanto a janela estiver aberta,
-- reservada para a atualização dos dados
function love.update(dt)
    atualizarNave (dt);

    atualizarSaida ();

    atualizarTiros ();

    atualizarAliens ();
end

-- Executa enquanto a janela estiver aberta,
-- reservada para o desenho em tela
function love.draw()
    -- Desenhando a nave
		if nave then
    	love.graphics.draw (nave.imagem, nave.x, nave.y, 0, 1, 1);
		end
		if nave2 then
			love.graphics.draw (nave2.imagem, nave2.x, nave2.y, 0, 1, 1);
		end

    -- Desenhando os aliens
    for ind, alienaux in pairs(aliens.alien) do
			love.graphics.draw(aliens.imagem, alienaux.x, alienaux.y, 0, 1, 1);
		end

    --  Desenhando os tiros
    for i, tiroaux in pairs(tiros.tiro) do
        love.graphics.rectangle("fill", tiroaux.x, tiroaux.y, tiros.larg, tiros.alt)
    end
end

------------------- FUNÇÕES DE CRIAÇÃO
-- Criação de uma nova nave
function criarNave (x, y)
    local novaNave = {};

    novaNave.imagem = love.graphics.newImage ('art/spacer.png');
    novaNave.x = x;
    novaNave.y = y;

    return novaNave;
end

-- Criação de um novo alien
function criaAlien(qnt)
	local novoAlien = {};

  novoAlien.x = 100 * qnt;
	novoAlien.y = 100;

	return novoAlien;
end

-- Criação do grupo de Aliens
function criarAliens (qnt)
    local novosAliens = {};

    novosAliens.imagem = love.graphics.newImage ('art/invader.png');
    novosAliens.alien = {};

    for ind = 1, qnt do
        table.insert(novosAliens.alien, criaAlien(ind));
    end

    return novosAliens;
end

-- Criação de um novo tiro
function criarTiro(x, y)
	local novoTiro = {};

  novoTiro.x = x;
	novoTiro.y = y - 5;

	return novoTiro;
end

-- Criação do grupo de Tiros
function criarTiros ()
    local novoTiros = {};

    novoTiros.tiro = {};
    novoTiros.som = love.audio.newSource ('art/shoot-laser.wav', "stream");
    novoTiros.larg = 4;
    novoTiros.alt = 8;
    novoTiros.reload = 15;

    return novoTiros;
end

-- Criação de um novo conjunto de deslocamento
function criarDeslocamentos ()
    local novoDeslocamento = {};

    novoDeslocamento.nave = 5;
    novoDeslocamento.alien = .2;
    novoDeslocamento.tiro = 12;
		novoDeslocamento.naveJoystick = 300;

    return novoDeslocamento;
end

------------------- FUNÇÕES DE ATUALIZAÇÃO
-- Atualiza o estado da nave
function atualizarNave (dt)
    -- Para a esquerda
	if love.keyboard.isDown('a') then
		if nave.x > 0 then
			nave.x = nave.x - deslocamento.nave;
		end

    -- Para a direita
	elseif love.keyboard.isDown('d') then
		if nave.x < 583 then
			nave.x = nave.x + deslocamento.nave;
		end
	end

	if playerOne and nave then
		--movimento da nave
		if playerOne:isGamepadDown("dpleft") then
			if nave.x > 0 then
				nave.x = nave.x - deslocamento.naveJoystick * dt
			end
		elseif playerOne:isGamepadDown("dpright") then
			if nave.x < 583 then
				nave.x = nave.x + deslocamento.naveJoystick * dt
			end
		end

		if playerOne:isGamepadDown("dpup") then
			if nave.y > 1 then
				nave.y = nave.y - deslocamento.naveJoystick * dt
			end
		elseif playerOne:isGamepadDown("dpdown") then
			if nave.y < 383 then
				nave.y = nave.y + deslocamento.naveJoystick * dt
			end
		end
	end

	if playerTwo and nave2 then
		--movimento da nave
		if playerTwo:isGamepadDown("dpleft") then
			if nave2.x > 0 then
				nave2.x = nave2.x - deslocamento.naveJoystick * dt
			end
		elseif playerTwo:isGamepadDown("dpright") then
			if nave2.x < 583 then
				nave2.x = nave2.x + deslocamento.naveJoystick * dt
			end
		end

		if playerTwo:isGamepadDown("dpup") then
			if nave2.y > 1 then
				nave2.y = nave2.y - deslocamento.naveJoystick * dt
			end
		elseif playerTwo:isGamepadDown("dpdown") then
			if nave2.y < 383 then
				nave2.y = nave2.y + deslocamento.naveJoystick * dt
			end
		end
	end

end

-- Atualizar o estado da aplicação
function atualizarSaida ()
	if love.keyboard.isDown('escape') then
		love.event.quit();
	end

	if (playerOne and playerOne:isGamepadDown("back")) then
		love.event.quit();
	end
end

-- Atualizar o estado dos tiros
function atualizarTiros ()
    if (love.keyboard.isDown('k') and (tempoBase == 0)) then
        love.audio.play (tiros.som);
				table.insert(tiros.tiro, criarTiro(nave.x, nave.y));
		end

		if (playerOne and playerOne:isGamepadDown("b") and (tempoBase == 0)) then
			love.audio.play (tiros.som);
			table.insert(tiros.tiro, criarTiro(nave.x, nave.y));
		end

		if (playerTwo and playerTwo:isGamepadDown("b") and (tempoBase == 0)) then
			love.audio.play (tiros.som);
			table.insert(tiros.tiro, criarTiro(nave2.x, nave2.y));
		end
    -- Atualizando posição
    atualizarPosicaoTiros ();

    recarregarArma ();
end

-- Atualizar o estado dos aliens
function atualizarAliens ()
    --Anda alienzin
    for i, alienaux in pairs(aliens.alien) do
        aliens.alien[i].y = alienaux.y  + deslocamento.alien;
    end
end

------------------- FUNÇÕES DE CONTROLE
-- Atualização da posição dos tiros
function atualizarPosicaoTiros ()
    for i, tiroaux in pairs(tiros.tiro) do
        tiros.tiro[i].y = tiroaux.y  - deslocamento.tiro;

        for j, alienaux in pairs(aliens.alien) do
            if compara(tiroaux, alienaux) then
                tiros.tiro[i] = nil;
                aliens.alien[j] = nil;
            end
        end

				if nave2 and compara(tiroaux, nave2) then
						tiros.tiro[i] = nil;
						nave2 = nil;
				end

				if nave and compara(tiroaux, nave) then
						tiros.tiro[i] = nil;
						nave = nil;
				end
    end
end

-- Recarga da pistola automática, para o tiro
function recarregarArma ()
    tempoBase = tempoBase + 1;

    if tempoBase >= tiros.reload then
        tempoBase = 0;
    end
end

-- Comparação de dois objetos, se ocupam o mesmo espaço
function compara (objeto1, objeto2)
    return (avaliarX(objeto1, objeto2) and avaliarY(objeto1, objeto2))
end

-- Avaliar alinhamento em relação ao eixo Ox
function avaliarX(objeto1, objeto2)
    return ((objeto2.x >= objeto1.x) or ((objeto2.x + 16) >= objeto1.x))
            and ((objeto2.x <= (objeto1.x + 16)) or ((objeto2.x + 16) <= (objeto1.x + 16)));
end

-- Avaliar alinhamento em relação ao eixo Oy
function avaliarY(objeto1, objeto2)
    return ((objeto2.y >= objeto1.y) or ((objeto2.y + 16) >= objeto1.y))
            and ((objeto2.y <= (objeto1.y + 16)) or ((objeto2.y + 16) <= (objeto1.y + 16)));
end
