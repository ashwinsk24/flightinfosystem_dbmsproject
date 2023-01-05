-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 05, 2023 at 10:22 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fms`
--

-- --------------------------------------------------------

--
-- Table structure for table `flights`
--

CREATE TABLE `flights` (
  `fid` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `flightno` varchar(50) NOT NULL,
  `airline` varchar(50) NOT NULL,
  `origin` varchar(50) NOT NULL,
  `destination` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `schd` time NOT NULL,
  `time` time NOT NULL,
  `status` varchar(50) NOT NULL,
  `terminal` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `flights`
--

INSERT INTO `flights` (`fid`, `email`, `flightno`, `airline`, `origin`, `destination`, `date`, `schd`, `time`, `status`, `terminal`) VALUES
(1, 'ash@outlook.com', 'EK531', 'Emirates', 'Dubai', 'Cochin', '2023-01-04', '13:55:00', '13:55:00', 'ARRIVED', 'T1'),
(2, 'ash@outlook.com', 'AI916', 'Air India', 'Cochin', 'Sharjah', '2023-01-05', '12:15:00', '12:15:00', 'DEPARTED', 'T3'),
(3, 'ash@outlook.com', 'QR514', 'Qatar Airways', 'Doha', 'Cochin', '2023-01-04', '20:20:00', '20:19:00', 'BOARDING', 'T1');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `name`, `email`) VALUES
(1, 'ashwin', 'ash@gmail.com'),
(2, 'ashwin2', 'ash2@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
(1, 'ash@outlook.com', 'ash@outlook.com', 'pbkdf2:sha256:260000$5oogrjtbQLxhd79g$1cac32772eeb534d74510027920eed19afbcc42d3b23fc8547dd7ccaa0eb7b7d'),
(2, 'ash', 'ashevents24@gmail.com', 'pbkdf2:sha256:260000$b0A0P97UcBGbDhLp$9a43672ec933a71dae3434ba3ca72fd45f8844d5becbb8c35751deb9db025490'),
(3, 'admin', 'testerash@gmail.com', 'pbkdf2:sha256:260000$989f3ngn10i4hd9m$44aa0fcd64ca787805e0ab2e159fda6e823839355e9cc4b8e07959d3239a6ce9');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `flights`
--
ALTER TABLE `flights`
  ADD PRIMARY KEY (`fid`),
  ADD UNIQUE KEY `flightno` (`flightno`),
  ADD KEY `email` (`email`) USING BTREE,
  ADD KEY `origin` (`origin`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `flights`
--
ALTER TABLE `flights`
  MODIFY `fid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
