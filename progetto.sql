-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Ott 19, 2023 alle 15:37
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `progetto`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `dipendente`
--

CREATE TABLE `dipendente` (
  `id_d` int(11) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `cognome` varchar(20) NOT NULL,
  `eta` int(11) NOT NULL,
  `pos_lavorativa` varchar(20) NOT NULL,
  `data_nascita` date NOT NULL,
  `stipendio` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `dipendente`
--

INSERT INTO `dipendente` (`id_d`, `nome`, `cognome`, `eta`, `pos_lavorativa`, `data_nascita`, `stipendio`) VALUES
(1, 'Gianluca', 'Lugli', 18, 'Dottore', '2005-01-24', 321);

-- --------------------------------------------------------

--
-- Struttura della tabella `zona_lavoro`
--

CREATE TABLE `zona_lavoro` (
  `id_z` int(11) NOT NULL,
  `nome_zona` varchar(20) NOT NULL,
  `numero_clienti` int(11) NOT NULL,
  `distretto` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `zona_lavoro`
--

INSERT INTO `zona_lavoro` (`id_z`, `nome_zona`, `numero_clienti`, `distretto`) VALUES
(1, 'Foggia', 12, 'A');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendente`
--
ALTER TABLE `dipendente`
  ADD PRIMARY KEY (`id_d`);

--
-- Indici per le tabelle `zona_lavoro`
--
ALTER TABLE `zona_lavoro`
  ADD PRIMARY KEY (`id_z`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendente`
--
ALTER TABLE `dipendente`
  MODIFY `id_d` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT per la tabella `zona_lavoro`
--
ALTER TABLE `zona_lavoro`
  MODIFY `id_z` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
