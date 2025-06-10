-- Insert data into Plano table
INSERT INTO Plano (IDPlano, PlaName, Plapreco, TelaSimult, ResolucaoMax) VALUES
('001', 'PADRÃO COM ANÚNCIOS', '20.9', 2, '1080p'),
('002', 'PADRÃO', '44.9', 2, '1080p'),
('003', 'PREMIUM', '59.9', 4, '4K+HDR'),
('004', 'BÁSICO', '14.9', 1, '720p'),
('005', 'FAMILIAR', '49.9', 6, '1080p');

-- Insert data into Titulo table
INSERT INTO Titulo (IDTitulo, TitName, Sinopse, AnoEstreia) VALUES
('001', 'Shrek', 'Nesta alegre comédia de animação, um ogro e um burro se unem para salvar uma princesa de um dragão.', 2001),
('002', 'Titanic', 'Um artista pobre e uma jovem rica se apaixonam a bordo do Titanic, mas precisam enfrentar um destino trágico.', 1997),
('003', 'Vingadores: Ultimato', 'Os heróis sobreviventes se unem para restaurar o equilíbrio do universo após o estalo de Thanos.', 2019),
('004', 'Interestelar', 'Um grupo de astronautas embarca em uma missão para encontrar um novo lar para a humanidade.', 2014),
('005', 'Divertida Mente', 'Dentro da mente de uma garota, cinco emoções trabalham juntas para ajudá-la a lidar com mudanças na vida.', 2015),
('006', 'Jojo''s Bizarre Adventure', 'Em vários períodos históricos, diferentes gerações da família Joestar, todas com o mesmo apelido, enfrentam alguns vilões com poderes sobrenaturas', 2012),
('007', 'Brooklyn Nine-Nine', 'Com a chegada de um novo capitão exigente, o despreocupado detetive do Brooklyn, Jake Peralta, deve aprender a respeitar as regras e a trabalhar em equipe.', 2013),
('008', 'Stranger Things', 'Quando um garoto desaparece, a cidade toda participa nas buscas. Mas o que encontram são segredos, forças sobrenaturais e uma menina.', 2015),
('009', 'Archer', 'Ele é um espião elegante e usa vários apetrechos modernos, mas também tem um tanto de problema. Para Sterling Archer, a missão mais difícil é simplesmente conseguir trabalhar.', 2009),
('010', 'Avatar - A lenda de Aang', 'Os irmãos Katara e Sokka acordam o jovem Aang de uma longa hibernação e descobrem que ele é um Avatar, com poderes que podem derrotar a Nação do Fogo.', 2005),
('011', 'O Senhor dos Anéis: A Sociedade do Anel', 'Um hobbit embarca em uma jornada para destruir um anel poderoso.', 2001),
('012', 'Matrix', 'Um hacker descobre a verdade sobre sua realidade e seu papel na guerra contra seus controladores.', 1999),
('013', 'Forrest Gump', 'Um homem com QI baixo vive grandes momentos da história dos EUA.', 1994),
('014', 'O Rei Leão', 'Um jovem leão foge de seu reino apenas para aprender o verdadeiro significado da responsabilidade e da bravura.', 1994),
('015', 'Jurassic Park', 'Um parque temático com dinossauros clonados se transforma em um pesadelo.', 1993),
('016', 'Gladiador', 'Um general romano busca vingança após ser traído.', 2000),
('017', 'Clube da Luta', 'Dois homens formam um clube secreto de luta.', 1999),
('018', 'A Origem', 'Um ladrão invade sonhos para roubar segredos.', 2010),
('019', 'O Poderoso Chefão', 'A saga de uma família mafiosa nos EUA.', 1972),
('020', 'Pulp Fiction', 'Histórias interligadas de crime em Los Angeles.', 1994),
('021', 'A Bela e a Fera', 'Uma jovem se apaixona por uma fera em um castelo encantado.', 1991),
('022', 'Toy Story', 'Brinquedos ganham vida quando os humanos não estão por perto.', 1995),
('023', 'Homem-Aranha: No Aranhaverso', 'Miles Morales descobre o multiverso dos Homens-Aranha.', 2018),
('024', 'Pantera Negra', 'O rei de Wakanda luta para proteger seu povo.', 2018),
('025', 'La La Land', 'Um músico e uma atriz buscam sucesso em Los Angeles.', 2016),
('026', 'O Grande Gatsby', 'Um milionário misterioso busca reconquistar seu amor perdido.', 2013),
('027', 'Coringa', 'A origem do icônico vilão de Gotham.', 2019),
('028', 'O Lobo de Wall Street', 'A ascensão e queda de um corretor da bolsa.', 2013),
('029', 'Os Incríveis', 'Uma família de super-heróis tenta viver uma vida normal.', 2004),
('030', 'Divulgação', 'Um executivo enfrenta acusações de assédio sexual.', 1994),
('031', 'O Código Da Vinci', 'Um simbologista desvenda um mistério religioso.', 2006),
('032', 'O Menino do Pijama Listrado', 'A amizade improvável entre dois meninos durante a Segunda Guerra.', 2008),
('033', 'A Teoria de Tudo', 'A vida do físico Stephen Hawking.', 2014),
('034', 'O Jogo da Imitação', 'Alan Turing tenta decifrar códigos nazistas.', 2014),
('035', 'Bird Box', 'Uma mãe tenta proteger seus filhos de uma ameaça invisível.', 2018),
('036', 'O Irlandês', 'Um matador de aluguel relembra seu passado.', 2019),
('037', 'Roma', 'A vida de uma empregada doméstica na Cidade do México.', 2018),
('038', 'O Poço', 'Prisioneiros lutam por comida em uma prisão vertical.', 2019),
('039', 'Enola Holmes', 'A irmã mais nova de Sherlock Holmes desvenda um mistério.', 2020),
('040', 'Lupin', 'Um ladrão inspirado em Arsène Lupin busca vingança.', 2021),
('041', 'Dark', 'Mistérios de viagem no tempo em uma pequena cidade alemã.', 2017),
('042', 'The Witcher', 'Um caçador de monstros luta para encontrar seu lugar em um mundo turbulento.', 2019),
('043', 'Breaking Bad', 'Um professor de química vira fabricante de metanfetamina.', 2008),
('044', 'Better Call Saul', 'A origem do advogado Saul Goodman.', 2015),
('045', 'Narcos', 'A ascensão e queda de Pablo Escobar.', 2015),
('046', 'House of Cards', 'Um político ambicioso manipula seu caminho até o topo.', 2013),
('047', 'The Crown', 'A história do reinado da Rainha Elizabeth II.', 2016),
('048', 'Black Mirror', 'Antologia sobre tecnologia e sociedade.', 2011),
('049', 'The Mandalorian', 'Um caçador de recompensas viaja pela galáxia.', 2019),
('050', 'The Boys', 'Super-heróis corruptos enfrentam vigilantes.', 2019),
('051', 'The Umbrella Academy', 'Irmãos adotivos com superpoderes tentam salvar o mundo.', 2019),
('052', 'Lucifer', 'O diabo tira férias em Los Angeles.', 2016),
('053', 'Anne with an E', 'Uma órfã encontra um novo lar em Avonlea.', 2017),
('054', 'Peaky Blinders', 'Uma família de gângsteres na Inglaterra pós-guerra.', 2013),
('055', 'Sense8', 'Oito desconhecidos compartilham uma conexão mental.', 2015),
('056', 'Elite', 'Alunos de uma escola de elite se envolvem em mistérios.', 2018),
('057', 'Vis a Vis', 'Uma mulher enfrenta desafios em uma prisão feminina.', 2015),
('058', 'La Casa de Papel', 'Um grupo realiza o maior assalto da história.', 2017),
('059', '3%', 'Jovens competem por uma vida melhor em uma sociedade dividida.', 2016),
('060', 'The Good Place', 'Uma mulher tenta se tornar uma pessoa melhor após a morte.', 2016);

-- Insert data into Genero table
INSERT INTO Genero (IDGenero, GenName) VALUES
('001', 'Ação'),
('002', 'Comédia'),
('003', 'Terror'),
('004', 'Romance'),
('005', 'Drama'),
('006', 'Suspense'),
('007', 'Ficção Científica'),
('008', 'Aventura'),
('009', 'Documentário'),
('010', 'Anime'),
('011', 'Animação'),
('012', 'Sitcom');

-- Insert data into PertenceA table (note: column order corrected to match DDL)
INSERT INTO PertenceA (IDGenero, IDTitulo) VALUES
('002', '001'),
('011', '001'),
('004', '002'),
('005', '002'),
('001', '003'),
('008', '003'),
('007', '004'),
('008', '004'),
('011', '005'),
('001', '006'),
('010', '006'),
('002', '007'),
('012', '007'),
('003', '008'),
('007', '008'),
('012', '009'),
('001', '009'),
('008', '010'),
('011', '010');

-- Insert data into Filme table
INSERT INTO Filme (IDTitulo, Duracao) VALUES
('001', '90min'),
('002', '195min'),
('003', '181min'),
('004', '169min'),
('005', '95min');

-- Insert data into Serie table
INSERT INTO Serie (IDTitulo) VALUES
('006'),
('007'),
('008'),
('009'),
('010');

-- Insert data into Usuario table
INSERT INTO Usuario (IDUsuario, UserName, DataNasc, Email, Senha, IDPlanoAssinado) VALUES
('001', 'Beatriz', '1989-03-29', 'Bia@yahoo.com', 'beatriz123?', '004'),
('002', 'Fidel', '2002-12-02', 'fidel@gmail.com', 'Senha_Fidel2', '005'),
('003', 'Melissa', '2003-03-26', 'melissa@gmail.com', 'M3liss4!', '003'),
('004', 'Bruno', '2004-03-12', 'bruno@gmail.com', 'Bruno_Senha4', '002'),
('005', 'Estefania', '2010-09-04', 'estefania@outock.com', '>3Stefani4<', '001');

-- Insert data into Perfil table
INSERT INTO Perfil (IDPerfil, IDUsuario, ProfileName) VALUES
('001', '001', 'Bia'),
('002', '001', 'Mãe'),
('003', '001', 'Pai'),
('004', '002', 'Fidel'),
('005', '002', 'Infantil'),
('006', '003', 'Ação e aventura'),
('007', '003', 'Sessão pipoca'),
('008', '003', 'Maratonas'),
('009', '003', 'Dramalover'),
('010', '003', 'Nerds'),
('011', '004', 'Clássicos'),
('012', '004', 'Noveleira'),
('013', '004', 'Bruno'),
('014', '005', 'Desenhos');

-- Insert data into Visualizacao table
INSERT INTO Visualizacao (IDVisualizacao, IDPerfil, VisuData, Progresso) VALUES
('001', '001', '2024-12-24', '07:58:00'),
('002', '002', '2025-01-24', '01:25:32'),
('003', '002', '2025-02-08', '03:26:00'),
('004', '003', '2025-02-20', '00:40:08'),
('005', '004', '2024-12-16', '16:43'),
('006', '004', '2025-01-09', '07:48:00'),
('007', '005', '2024-12-23', '01:44:00'),
('008', '005', '2024-12-24', '19:11'),
('009', '005', '2025-01-09', '07:05:00'),
('010', '007', '2025-02-12', '11:54'),
('011', '008', '2025-01-25', '02:00:00'),
('012', '009', '2024-12-05', '06:11:00'),
('013', '009', '2024-12-08', '00:30:40'),
('014', '010', '2025-01-05', '16:11'),
('015', '012', '2024-12-18', '00:37:42'),
('016', '012', '2024-12-20', '00:13:38'),
('017', '012', '2025-01-23', '01:01:00'),
('018', '014', '2024-12-01', '14:29:00'),
('019', '014', '2025-01-06', '00:01:09');

-- Insert data into Temporada table
INSERT INTO Temporada (IDTitulo, NumTemp, TempName) VALUES
('006', 1, 'Phantom Blood'),
('006', 2, 'Battle Tendency'),
('007', 1, 'Temporada 1'),
('007', 2, 'Temporada 2'),
('008', 1, 'Stranger Things'),
('008', 2, 'Stranger Things 2'),
('009', 1, 'Temporada 1'),
('009', 2, 'Temporada 2'),
('010', 1, 'Avatar - A lenda de Aang: Livro 1'),
('010', 2, 'Avatar - A lenda de Aang: Livro 2');

-- Insert data into Episodio table
INSERT INTO Episodio (IDTitulo, NumTemp, NumEp, EpName, EpDuracao) VALUES
('006', 1, 1, 'Dio, o Invasor', '23min'),
('006', 1, 2, 'Uma Carta do Passado', '23min'),
('006', 1, 3, 'Minha Juventude com Dio', '23min'),
('006', 2, 1, 'JoJo em Nova Iorque', '23min'),
('006', 2, 2, 'O Mestre do Jogo', '23min'),
('006', 2, 3, 'O Homem do Pilar', '23min'),
('007', 1, 1, 'Novo capitão', '22min'),
('007', 1, 2, 'O funeral', '21min'),
('007', 1, 3, 'O palpite do Boyle', '21min'),
('007', 2, 1, 'Infiltrado', '21min'),
('007', 2, 2, 'Achocolatado', '21min'),
('007', 2, 3, 'A competição', '21min'),
('008', 1, 1, 'Capítulo um: O desaparecimento de Will Byers', '49min'),
('008', 1, 2, 'Capítulo dois: A estranha da Maple Street', '56min'),
('008', 1, 3, 'Capítulo três: Caramba', '52min'),
('008', 2, 1, 'Capítulo um: Mad Max', '48min'),
('008', 2, 2, 'Capítulo dois: Gostosura ou travessura, aberração', '56min'),
('008', 2, 3, 'Capítulo três: O girino', '51min'),
('009', 1, 1, 'Piloto: Caçando um espião duplo', '21min'),
('009', 1, 2, 'Dia de treino', '21min'),
('009', 1, 3, 'Diversidade', '20min'),
('009', 2, 1, 'Moça suíça', '21min'),
('009', 2, 2, 'ISIS à venda', '21min'),
('009', 2, 3, 'Teste de paternidade', '21min'),
('010', 1, 1, 'The Boy in the Iceberg: The Avatar Returns: Parte 1', '23min'),
('010', 1, 2, 'The Avatar Returns: Parte 1', '23min'),
('010', 1, 3, 'The Southern Air Temple', '24min'),
('010', 2, 1, 'O estado avatar', '24min'),
('010', 2, 2, 'A caverna dos dois amantes', '24min'),
('010', 2, 3, 'Retorno a Omashu', '24min');

-- Insert data into VisFilme table
INSERT INTO VisFilme (IDVisualizacao, IDTitulo) VALUES
('002', '001'),
('004', '004'),
('007', '001'),
('013', '002'),
('015', '003'),
('016', '004'),
('019', '005');

-- Insert data into VisEpisodio table
INSERT INTO VisEpisodio (IDVisualizacao, IDTitulo, NumTemp, NumEp) VALUES
('001', '009', 2, 1),
('003', '008', 1, 2),
('005', '007', 1, 3),
('006', '009', 2, 2),
('008', '010', 1, 3),
('009', '008', 1, 1),
('010', '010', 2, 2),
('011', '007', 1, 2),
('012', '006', 2, 3),
('014', '010', 2, 3),
('017', '008', 1, 2),
('018', '010', 1, 1);