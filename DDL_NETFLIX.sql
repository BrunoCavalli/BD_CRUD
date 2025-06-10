CREATE TABLE Plano
(
  IDPlano CHAR(3) NOT NULL,
  PlaName VARCHAR NOT NULL,
  Plapreco VARCHAR NOT NULL,
  TelaSimult INT NOT NULL,
  ResolucaoMax VARCHAR NOT NULL,
  PRIMARY KEY (IDPlano)
);

CREATE TABLE Titulo
(
  IDTitulo CHAR(3) NOT NULL,
  TitName VARCHAR NOT NULL,
  Sinopse VARCHAR NOT NULL,
  AnoEstreia INT NOT NULL,
  PRIMARY KEY (IDTitulo)
);

CREATE TABLE Genero
(
  IDGenero CHAR(3) NOT NULL,
  GenName VARCHAR NOT NULL,
  PRIMARY KEY (IDGenero)
);

CREATE TABLE PertenceA
(
  IDGenero CHAR(3) NOT NULL,
  IDTitulo CHAR(3) NOT NULL,
  PRIMARY KEY (IDGenero, IDTitulo),
  FOREIGN KEY (IDGenero) REFERENCES Genero(IDGenero),
  FOREIGN KEY (IDTitulo) REFERENCES Titulo(IDTitulo)
);

CREATE TABLE Filme
(
  Duracao VARCHAR NOT NULL,
  IDTitulo CHAR(3) NOT NULL,
  PRIMARY KEY (IDTitulo),
  FOREIGN KEY (IDTitulo) REFERENCES Titulo(IDTitulo)
);

CREATE TABLE Serie
(
  IDTitulo CHAR(3) NOT NULL,
  PRIMARY KEY (IDTitulo),
  FOREIGN KEY (IDTitulo) REFERENCES Titulo(IDTitulo)
);

CREATE TABLE Usuario
(
  IDUsuario CHAR(3) NOT NULL,
  DataNasc DATE NOT NULL,
  UserName VARCHAR NOT NULL,
  Email VARCHAR NOT NULL,
  Senha  VARCHAR NOT NULL,
  IDPlanoAssinado CHAR(3) NOT NULL,
  PRIMARY KEY (IDUsuario),
  FOREIGN KEY (IDPlanoAssinado) REFERENCES Plano(IDPlano),
  UNIQUE (Email)
);

CREATE TABLE Perfil
(
  IDPerfil CHAR(3) NOT NULL,
  ProfileName VARCHAR NOT NULL,
  IDUsuario CHAR(3) NOT NULL,
  PRIMARY KEY (IDPerfil),
  FOREIGN KEY (IDUsuario) REFERENCES Usuario(IDUsuario)
);

CREATE TABLE Visualizacao
(
  VisuData DATE NOT NULL,
  Progresso VARCHAR NOT NULL,
  IDVisualizacao CHAR(3) NOT NULL,
  IDPerfil CHAR(3) NOT NULL,
  PRIMARY KEY (IDVisualizacao),
  FOREIGN KEY (IDPerfil) REFERENCES Perfil(IDPerfil)
);

CREATE TABLE Temporada
(
  NumTemp INT NOT NULL,
  TempName VARCHAR NOT NULL,
  IDTitulo CHAR(3) NOT NULL,
  PRIMARY KEY (NumTemp, IDTitulo),
  FOREIGN KEY (IDTitulo) REFERENCES Serie(IDTitulo)
);

CREATE TABLE VisFilme
(
  IDTitulo CHAR(3) NOT NULL,
  IDVisualizacao CHAR(3) NOT NULL,
  PRIMARY KEY (IDVisualizacao),
  FOREIGN KEY (IDTitulo) REFERENCES Filme(IDTitulo),
  FOREIGN KEY (IDVisualizacao) REFERENCES Visualizacao(IDVisualizacao)
);

CREATE TABLE Episodio
(
  NumEp INT NOT NULL,
  EpName VARCHAR NOT NULL,
  EpDuracao VARCHAR NOT NULL,
  NumTemp INT NOT NULL,
  IDTitulo CHAR(3) NOT NULL,
  PRIMARY KEY (NumEp, NumTemp, IDTitulo),
  FOREIGN KEY (NumTemp, IDTitulo) REFERENCES Temporada(NumTemp, IDTitulo)
);

CREATE TABLE VisEpisodio
(
  NumEp INT NOT NULL,
  NumTemp INT NOT NULL,
  IDTitulo CHAR(3) NOT NULL,
  IDVisualizacao CHAR(3) NOT NULL,
  PRIMARY KEY (IDVisualizacao),
  FOREIGN KEY (NumEp, NumTemp, IDTitulo) REFERENCES Episodio(NumEp, NumTemp, IDTitulo),
  FOREIGN KEY (IDVisualizacao) REFERENCES Visualizacao(IDVisualizacao)
);
