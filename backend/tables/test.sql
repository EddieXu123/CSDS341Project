-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 07, 2020 at 04:18 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `Academics`
--

CREATE TABLE `Academics` (
  `User_ID` int(11) NOT NULL,
  `major` char(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `AcademicYear` int(11) DEFAULT NULL,
  `GPA` decimal(4,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Academics`
--

INSERT INTO `Academics` (`User_ID`, `major`, `AcademicYear`, `GPA`) VALUES
(77, 'Computer Science', 2022, '4'),
(78, 'Computer Science', 2022, '3');

-- --------------------------------------------------------

--
-- Table structure for table `Class`
--

CREATE TABLE `Class` (
  `ClassName` char(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ClassNum` int(11) NOT NULL,
  `ClassDept` char(30) COLLATE utf8_unicode_ci NOT NULL,
  `ClassSem` char(30) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Interests`
--

CREATE TABLE `Interests` (
  `interests` char(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `USER_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Interests`
--

INSERT INTO `Interests` (`interests`, `USER_ID`) VALUES
('Skiing, coding, driving', 77),
('driving, skiing, coding', 78);

-- --------------------------------------------------------

--
-- Table structure for table `Login_Info`
--

CREATE TABLE `Login_Info` (
  `Email_address` char(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Password` char(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Security_PIN` int(11) DEFAULT NULL,
  `User_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Login_Info`
--

INSERT INTO `Login_Info` (`Email_address`, `Password`, `Security_PIN`, `User_ID`) VALUES
('eddie@gmail.com', 'Password', NULL, 77),
('newUser@gmail.com', 'Pass', NULL, 78);

-- --------------------------------------------------------

--
-- Table structure for table `Student`
--

CREATE TABLE `Student` (
  `User_ID` int(11) NOT NULL,
  `First_Name` char(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Last_Name` char(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `DOB` char(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `gender` char(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `PhoneNum` char(15) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Student`
--

INSERT INTO `Student` (`User_ID`, `First_Name`, `Last_Name`, `DOB`, `gender`, `PhoneNum`) VALUES
(77, 'Eddie', 'Xu', '08/02/2000', 'Male', '609-391-1823'),
(78, 'Guy', 'Fieri', '08/20/1999', 'Female', '504-315-3620');

-- --------------------------------------------------------

--
-- Table structure for table `Takes`
--

CREATE TABLE `Takes` (
  `User_ID` int(11) NOT NULL,
  `ClassNum` int(11) NOT NULL,
  `ClassDept` char(20) COLLATE utf8_unicode_ci NOT NULL,
  `ClassSem` char(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Takes`
--

INSERT INTO `Takes` (`User_ID`, `ClassNum`, `ClassDept`, `ClassSem`) VALUES
(77, 2, 'Computer Science', 'Spring'),
(78, 2, 'Computer Science', 'Spring');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Academics`
--
ALTER TABLE `Academics`
  ADD PRIMARY KEY (`User_ID`);

--
-- Indexes for table `Class`
--
ALTER TABLE `Class`
  ADD PRIMARY KEY (`ClassNum`,`ClassDept`,`ClassSem`);

--
-- Indexes for table `Interests`
--
ALTER TABLE `Interests`
  ADD PRIMARY KEY (`USER_ID`);

--
-- Indexes for table `Login_Info`
--
ALTER TABLE `Login_Info`
  ADD PRIMARY KEY (`User_ID`);

--
-- Indexes for table `Student`
--
ALTER TABLE `Student`
  ADD PRIMARY KEY (`User_ID`);

--
-- Indexes for table `Takes`
--
ALTER TABLE `Takes`
  ADD PRIMARY KEY (`User_ID`,`ClassNum`,`ClassDept`,`ClassSem`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Login_Info`
--
ALTER TABLE `Login_Info`
  MODIFY `User_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
