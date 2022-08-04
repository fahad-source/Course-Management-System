-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 06, 2022 at 08:29 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `saad`
--

-- --------------------------------------------------------

--
-- Table structure for table `coursework`
--

CREATE TABLE `coursework` (
  `m_id` int(11) NOT NULL,
  `c_id` int(11) NOT NULL,
  `c_des` varchar(100) NOT NULL,
  `due_date` date NOT NULL,
  `time` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `coursework`
--

INSERT INTO `coursework` (`m_id`, `c_id`, `c_des`, `due_date`, `time`) VALUES
(676, 0, 'djjks', '2022-07-06', '6:59 AM'),
(6, 1, 'jsjajksdjk', '0007-05-22', '6:59 AM'),
(1, 10, '20', '0000-00-00', '67'),
(1, 20, '20', '0000-00-00', '67'),
(24, 123, 'sjjsj', '2022-07-06', '6:59 AM'),
(5, 431, 'fahad', '0007-05-22', '7:59 AM'),
(24, 1234, 'sjjsj', '2022-07-06', '6:59 AM'),
(676, 2113, 'sahjshdj', '2022-07-08', '6:59 AM'),
(676, 2323, 'sjsdjsdj', '2022-07-15', '6:59 AM'),
(676, 23434, 'sdfeer', '2022-07-07', '6:59 AM'),
(676, 34343, 'sdhhaj', '2022-07-12', '3:59 AM'),
(676, 123445, 'dfddfg', '2022-07-26', '6:59 AM');

-- --------------------------------------------------------

--
-- Table structure for table `module`
--

CREATE TABLE `module` (
  `m_id` int(11) NOT NULL,
  `m_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `module`
--

INSERT INTO `module` (`m_id`, `m_name`) VALUES
(0, 'cdcsdcd'),
(1, 'semister 1'),
(5, 'ssd'),
(6, 'ssd'),
(24, 'check'),
(146, 'ali raza'),
(676, 'shajshshahshsjjh');

-- --------------------------------------------------------

--
-- Table structure for table `requirement`
--

CREATE TABLE `requirement` (
  `id` int(11) NOT NULL,
  `c_id` int(11) NOT NULL,
  `c_req` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `coursework`
--
ALTER TABLE `coursework`
  ADD PRIMARY KEY (`c_id`),
  ADD KEY `fk_m_key` (`m_id`);

--
-- Indexes for table `module`
--
ALTER TABLE `module`
  ADD PRIMARY KEY (`m_id`);

--
-- Indexes for table `requirement`
--
ALTER TABLE `requirement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `c_id` (`c_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `requirement`
--
ALTER TABLE `requirement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `coursework`
--
ALTER TABLE `coursework`
  ADD CONSTRAINT `fk_m_key` FOREIGN KEY (`m_id`) REFERENCES `module` (`m_id`);

--
-- Constraints for table `requirement`
--
ALTER TABLE `requirement`
  ADD CONSTRAINT `requirement_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `coursework` (`c_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
