------------------- FUNÇÕES BÁSICAS
-- Executa apenas uma vez
function love.load()
    nave = criarNave ();

    aliens = criarAliens (5);

    tiros = criarTiros ();

    deslocamento = criarDeslocamentos ();

    tempoBase = 0;
end

-- Executa enquanto a janela estiver aberta,
-- reservada para a atualização dos dados
function love.update()
    atualizarNave ();

    atualizarSaida ();

    atualizarTiros ();

    atualizarAliens ();
end

-- Executa enquanto a janela estiver aberta,
-- reservada para o desenho em tela
function love.draw()
    -- Desenhando a nave
    love.graphics.draw (nave.imagem, nave.x, nave.y, 0, 1, 1);

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
function criarNave ()
    local novaNave = {};

    novaNave.imagem = love.graphics.newImage ('art/spacer.png');
    novaNave.x = 300;
    novaNave.y = 350;

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
function criarTiro()
	local novoTiro = {};

    novoTiro.x = nave.x;
	novoTiro.y = nave.y;

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

    novoDeslocamento.nave = 1;
    novoDeslocamento.alien = .2;
    novoDeslocamento.tiro = 12;

    return novoDeslocamento;
end

------------------- FUNÇÕES DE ATUALIZAÇÃO
-- Atualiza o estado da nave
function atualizarNave ()
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
end

-- Atualizar o estado da aplicação
function atualizarSaida ()
	if love.keyboard.isDown('escape') then
		love.event.quit();
	end
end

-- Atualizar o estado dos tiros
function atualizarTiros ()
    if (love.keyboard.isDown('k') and (tempoBase == 0)) then
        love.audio.play (tiros.som);
		table.insert(tiros.tiro, criarTiro());
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
