--create table trainer

CREATE TABLE `trainer` (
  `id_trainer` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `start_date` varchar(10) NOT NULL,
  PRIMARY KEY (`id_trainer`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci 

--create table pokemon
CREATE TABLE `pokemon` (
  `id_pokemon` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_pokemon`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci

--create table pokedex
CREATE TABLE `pokedex` (
  `id_pokedex` int(11) NOT NULL AUTO_INCREMENT,
  `id_trainer` int(11) NOT NULL,
  `id_pokemon` int(11) NOT NULL,
  `catch_date` varchar(10) NOT NULL,
  PRIMARY KEY (`id_pokedex`),
  KEY `id_trainer` (`id_trainer`),
  KEY `id_pokemon` (`id_pokemon`),
  CONSTRAINT `pokedex_ibfk_1` FOREIGN KEY (`id_trainer`) REFERENCES `trainer` (`id_trainer`),
  CONSTRAINT `pokedex_ibfk_2` FOREIGN KEY (`id_pokemon`) REFERENCES `pokemon` (`id_pokemon`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci