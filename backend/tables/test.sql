-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 29, 2020 at 06:23 PM
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
  `GPA` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

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
  `PhoneNum` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Takes`
--

CREATE TABLE `Takes` (
  `User_ID` int(11) NOT NULL,
  `ClassNum` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

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
  ADD PRIMARY KEY (`User_ID`,`ClassNum`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
