-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 01, 2024 at 12:43 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user_register`
--

-- --------------------------------------------------------

--
-- Table structure for table `complaints`
--

CREATE TABLE `complaints` (
  `id` int(40) NOT NULL,
  `userName` varchar(40) NOT NULL,
  `userEmail` varchar(50) NOT NULL,
  `ownerName` varchar(50) NOT NULL,
  `ownerEmail` varchar(30) NOT NULL,
  `propertyName` varchar(50) NOT NULL,
  `complaint` varchar(255) NOT NULL,
  `status` varchar(30) NOT NULL DEFAULT 'new',
  `cdate` date DEFAULT NULL,
  `solution` varchar(255) NOT NULL,
  `rdate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `complaints`
--

INSERT INTO `complaints` (`id`, `userName`, `userEmail`, `ownerName`, `ownerEmail`, `propertyName`, `complaint`, `status`, `cdate`, `solution`, `rdate`) VALUES
(1, 'dinsesh', 'nandhustark3000@gmail.com', 'Nandhualan', 'nandhualan108@gmail.com', 'Pandi Pg', 'Rats problem solve it soon', 'solved', '2024-02-27', 'ok i will solve it soon', '2024-02-27'),
(2, 'dinsesh', 'nandhustark3000@gmail.com', 'Nandhualan', 'nandhualan108@gmail.com', 'Kesave apartments', 'Lift is not working ', 'solved', '2024-02-27', 'Ok sir problem is fixed', '2024-02-27'),
(3, 'dinsesh', 'nandhustark3000@gmail.com', 'Nandhualan', 'nandhualan108@gmail.com', 'Pandi PG', 'Lots of problems in property', 'new', '2024-02-27', '', NULL),
(4, 'dinsesh', 'nandhustark3000@gmail.com', 'Nandhualan', 'nandhualan108@gmail.com', 'Kesave aparments', 'this is an testing complaint', 'new', '2024-02-29', '', NULL),
(5, 'dinsesh', 'nandhustark3000@gmail.com', 'Nandhualan', 'nandhualan108@gmail.com', 'Pandi PG', 'booking problems', 'new', '2024-03-01', '', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `forgot_pass`
--

CREATE TABLE `forgot_pass` (
  `id` int(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `forgot_pass`
--

INSERT INTO `forgot_pass` (`id`, `Name`, `Email`, `password`, `status`) VALUES
(1, 'dinsesh', 'nandhustark3000@gmail.com', '987', 'Approve'),
(2, 'dinsesh', 'nandhustark3000@gmail.com', '987', 'new');

-- --------------------------------------------------------

--
-- Table structure for table `ownerregform`
--

CREATE TABLE `ownerregform` (
  `id` int(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` int(255) NOT NULL,
  `email` varchar(30) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  `pincode` int(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `district` varchar(30) NOT NULL,
  `profile` varchar(20) NOT NULL,
  `identity` varchar(30) NOT NULL,
  `password` varchar(50) NOT NULL,
  `p_type` varchar(30) NOT NULL,
  `p_location` varchar(30) NOT NULL,
  `p_document` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL DEFAULT 'new',
  `username` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ownerregform`
--

INSERT INTO `ownerregform` (`id`, `name`, `phone`, `email`, `dob`, `gender`, `address`, `pincode`, `state`, `district`, `profile`, `identity`, `password`, `p_type`, `p_location`, `p_document`, `status`, `username`) VALUES
(1, 'Nandhualan', 923654987, 'nandhualan108@gmail.com', '2024-02-04', 'male', 'Nagapattinam  newary post office', 123654, 'Tamil Nadu', 'Nagapattinam', 'p1.jpeg', 'document.png', 'DH@POAQZUY', 'PG', 'Nagapattinam', 'document.png', 'Approve', 'OWNERDH0001'),
(2, 'Nandhustark', 721654987, 'nandhustark3000@gmail.com', '2024-02-11', 'male', 'Mayiladuthurai nayakkar stree', 321654, 'Tamil Nadu', 'Mayiladuthurai', 'p2.jpeg', 'document.png', 'DH@POAQZUZ', 'house', 'Mayiladuthurai ', 'document.png', 'new', 'OWNERDH0002'),
(3, 'pandikumar', 947483647, 'pandikumar652001@gmail.com', '2024-02-02', 'male', 'Nilgris amman kovil near by', 12345, 'Tamil Nadu', 'Nilgiris', 'p3.jpeg', 'document.png', 'DH@WKQ2YQ0', 'PG', 'Nilgiris', 'document.png', 'Approve', 'OWNERDH0003'),
(4, 'testing', 947483647, 'nandhustark3000@gmail.com', '2024-02-10', 'male', 'Nilgiris police station near', 123456, 'Tamil Nadu', 'Nilgiris', 'p4.jpeg', 'document.png', 'DH@R73R1VQ', 'house', 'Nilgiris', 'document.png', 'new', 'OWNERDH0004'),
(6, 'Surendhar', 2147483647, 'surendhar.duplessis79@gmail.co', '2024-02-04', 'male', 'Dindigul post office near by', 321654, 'Tamil Nadu', 'Dindigul', 'p5.jpeg', 'document.png', 'DH@FBOICKQ', 'house', 'Dindigul', 'document.png', 'Approve', 'OWNERDH0005'),
(7, 'Raja', 736549870, 'sugeshrahul1304@gmail.com', '2024-02-10', 'male', 'dindugal near', 123456, 'Tamil Nadu', 'Dindigul', 'p6.jpeg', 'document.png', 'DH@R5Q28SP', 'house', 'Dindugul', 'document.png', 'Approve', 'OWNERDH0007');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `id` int(40) NOT NULL,
  `uid` int(10) NOT NULL,
  `propertyType` varchar(40) NOT NULL,
  `propertyName` varchar(40) NOT NULL,
  `uname` varchar(40) NOT NULL,
  `uemail` varchar(50) NOT NULL,
  `owname` varchar(50) NOT NULL,
  `owemail` varchar(50) NOT NULL,
  `rent` int(20) NOT NULL,
  `payed` int(20) NOT NULL,
  `date` varchar(10) NOT NULL,
  `month` varchar(20) NOT NULL,
  `status` varchar(30) NOT NULL DEFAULT 'unpaid',
  `payment_date` date NOT NULL,
  `property_status` varchar(30) NOT NULL,
  `paymentMethod` varchar(50) NOT NULL,
  `cardno` int(30) NOT NULL,
  `cvv` int(10) NOT NULL,
  `expiryDate` varchar(50) NOT NULL,
  `cardAmount` int(30) NOT NULL,
  `upid` varchar(30) NOT NULL,
  `net_accno` int(30) NOT NULL,
  `net_ifsc` varchar(30) NOT NULL,
  `payment_status` varchar(30) NOT NULL,
  `vacate_status` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`id`, `uid`, `propertyType`, `propertyName`, `uname`, `uemail`, `owname`, `owemail`, `rent`, `payed`, `date`, `month`, `status`, `payment_date`, `property_status`, `paymentMethod`, `cardno`, `cvv`, `expiryDate`, `cardAmount`, `upid`, `net_accno`, `net_ifsc`, `payment_status`, `vacate_status`) VALUES
(1, 2, 'Apartment', 'Kesave aparments', 'dinsesh', 'nandhustark3000@gmail.com', 'Nandhualan', 'nandhualan108@gmail.com', 5400, 5400, '1', 'March', 'paid', '2024-03-01', 'Approve', 'gpay', 0, 0, '', 0, 'fdfdsfd22', 0, '', 'Approve', 'vacant'),
(2, 1, 'Apartment', 'Kesave aparments', 'Nandhu', 'nandhualan108@gmail.com', 'Nandhualan', 'nandhualan108@gmail.com', 5400, 0, '1', 'March', 'unpaid', '0000-00-00', 'Approve', '', 0, 0, '', 0, '', 0, '', '', 'vacant'),
(3, 1, 'Apartment', 'Kesave aparments', 'Nandhu', 'nandhualan108@gmail.com', 'Nandhualan', 'nandhualan108@gmail.com', 5400, 5400, '1', 'March', 'paid', '2024-03-01', 'Approve', 'gpay', 0, 0, '', 0, '121212ff', 0, '', 'Approve', 'vacant'),
(4, 2, 'House', 'hari Jolaya', 'dinsesh', 'nandhustark3000@gmail.com', 'Nandhustark', 'nandhustark3000@gmail.com', 6000, 0, '1', 'March', 'unpaid', '0000-00-00', 'Approve', '', 0, 0, '', 0, '', 0, '', '', 'occupied'),
(5, 2, 'Pg', 'Pandi PG', 'dinsesh', 'nandhustark3000@gmail.com', 'Nandhualan', 'nandhualan108@gmail.com', 2000, 0, '1', 'March', 'unpaid', '0000-00-00', 'Approve', '', 0, 0, '', 0, '', 0, '', '', 'occupied'),
(6, 1, 'Apartment', 'Marveleous', 'Nandhu', 'nandhualan108@gmail.com', 'Nandhustark', 'nandhustark3000@gmail.com', 7300, 0, '1', 'March', 'unpaid', '0000-00-00', 'request', '', 0, 0, '', 0, '', 0, '', '', 'occupied');

-- --------------------------------------------------------

--
-- Table structure for table `payment_history`
--

CREATE TABLE `payment_history` (
  `id` int(10) NOT NULL,
  `uid` int(10) NOT NULL,
  `uname` varchar(30) NOT NULL,
  `propertyName` varchar(30) NOT NULL,
  `propertyType` varchar(30) NOT NULL,
  `owname` varchar(30) NOT NULL,
  `payed` int(10) NOT NULL,
  `date` varchar(20) NOT NULL,
  `payed time` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `payment_method` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment_history`
--

INSERT INTO `payment_history` (`id`, `uid`, `uname`, `propertyName`, `propertyType`, `owname`, `payed`, `date`, `payed time`, `payment_method`) VALUES
(1, 2, 'dinsesh', 'Pg', 'Pandi PG', 'Nandhualan', 2000, '2024-02-26', '2024-02-26 11:54:09.688215', ''),
(2, 1, 'Nandhu', 'Apartment', 'Marveleous', 'Nandhustark', 7300, '2024-02-29', '2024-02-29 11:37:45.373159', 'netbanking'),
(3, 1, 'Nandhu', 'Pg', 'Pandi PG', 'Nandhualan', 2000, '2024-03-01', '2024-03-01 05:58:26.700762', 'netbanking'),
(4, 2, 'dinsesh', 'Apartment', 'Kesave aparments', 'Nandhualan', 5400, '2024-03-01', '2024-03-01 06:28:01.156875', 'gpay'),
(5, 1, 'Nandhu', 'Apartment', 'Kesave aparments', 'Nandhualan', 5400, '2024-03-01', '2024-03-01 06:41:11.853186', 'gpay');

-- --------------------------------------------------------

--
-- Table structure for table `property`
--

CREATE TABLE `property` (
  `id` int(40) NOT NULL,
  `propertyName` varchar(50) NOT NULL,
  `ownerName` varchar(50) NOT NULL,
  `mobile` int(20) NOT NULL,
  `propertyType` varchar(30) NOT NULL,
  `email` varchar(40) NOT NULL,
  `plotNo` varchar(50) NOT NULL,
  `availableBhk` int(50) NOT NULL,
  `state` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `pincode` int(10) NOT NULL,
  `rent` int(20) NOT NULL,
  `deposit` int(20) NOT NULL,
  `facilities` varchar(30) NOT NULL,
  `description` varchar(255) NOT NULL,
  `landmark` varchar(100) NOT NULL,
  `address` varchar(255) NOT NULL,
  `vacancies` varchar(20) NOT NULL,
  `pImage` varchar(20) NOT NULL,
  `pimage2` varchar(20) NOT NULL,
  `pimage3` varchar(20) NOT NULL,
  `status` varchar(30) NOT NULL DEFAULT 'new',
  `remaining_bhk` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `property`
--

INSERT INTO `property` (`id`, `propertyName`, `ownerName`, `mobile`, `propertyType`, `email`, `plotNo`, `availableBhk`, `state`, `city`, `pincode`, `rent`, `deposit`, `facilities`, `description`, `landmark`, `address`, `vacancies`, `pImage`, `pimage2`, `pimage3`, `status`, `remaining_bhk`) VALUES
(1, 'Pandi PG', 'Nandhualan', 549873210, 'Pg', 'nandhualan108@gmail.com', '13-Bca', 2, 'Tamil Nadu', 'Mayiladuthurai', 123456, 2000, 15000, 'food', 'Fine Property ', 'gh -hospital', 'ukadamm', 'vacant', 'apartment.png', 'apartment1.png', 'apartment2.jpg', 'Approve', 1),
(2, 'Kesave aparments', 'Nandhualan', 1234567890, 'Apartment', 'nandhualan108@gmail.com', '90-dfa', 3, 'Tamil Nadu', 'Mayiladuthurai', 123456, 5400, 20000, 'wifi_food', 'Large space so many members can stay', 'co office', 'Mayiladuthurai neary by', 'vacant', 'apartment2.jpg', 'apartment1.png', 'apartment.png', 'Approve', 3),
(3, 'hari Jolaya', 'Nandhustark', 2147483647, 'House', 'nandhustark3000@gmail.com', '25-jhg', 2, 'Tamil Nadu', 'Perambalur', 321654, 6000, 12088, 'food', 'best property for 4 members family', 'collector office', 'Perambalur with gh hospital', 'vacant', 'apartment.png', 'apartment1.png', 'apartment2.jpg', 'Approve', 1),
(4, 'Janani Apartments', 'Surendhar', 2147483647, 'Apartment', 'surendhar.duplessis79@gmail.co', '12-JH', 2, 'Tamil Nadu', 'Mayiladuthurai', 321654, 8000, 50000, 'wifi_food', 'Large space with futureistice apartments', 'ploice station', 'salem', 'vacant', 'apartment2.jpg', 'apartment1.png', 'apartment.png', 'Approve', 2),
(5, 'Marveleous', 'Nandhustark', 2147483647, 'Apartment', 'nandhustark3000@gmail.com', '13-NUV', 2, 'Tamil Nadu', 'Karur', 321987, 7300, 20000, 'food', 'Good Looking apartment and lots of advantages', 'Techvolt oposite', 'Covai', 'vacant', 'apartment2.jpg', 'bgimg.jpg', 'house3.png', 'Approve', 1),
(6, 'Karthigai House', 'pandikumar', 654987123, 'House', 'pandikumar652001@gmail.com', 'E3-Fa', 2, 'Tamil Nadu', 'Krishnagiri', 980767, 5000, 23000, 'food', 'most suitable for family and well organized', 'police station', 'Krishnagiri police station Opposite', 'vacant', 'house1.png', 'apartment.png', 'house3.png', 'Approve', 2),
(7, 'Vidyalaya Housed', 'pandikumar', 2147483647, 'House', 'pandikumar652001@gmail.com', 'mn-45B', 3, 'Tamil Nadu', 'Perambalur', 987423, 3400, 23000, 'wifi_food', 'Hospitals and schools are near by', 'Viya School Oposite', 'Perambalur', 'vacant', 'house2.jpg', 'pg3.jpg', 'apartment.png', 'Approve', 3),
(8, 'Jolly Pg', 'Surendhar', 2147483647, 'Pg', 'surendhar.duplessis79@gmail.co', '14-hgb', 1, 'Tamil Nadu', 'Vellore', 123654, 9500, 25000, 'wifi_food', 'All fecilities are available and lots of rooms are available', 'water office opposite', 'vellor water office near by', 'vacant', 'house2.jpg', 'apartment.png', 'house3.png', 'Approve', 1),
(9, 'sugesh Houses', 'Raja', 1239085647, 'House', 'sugeshrahul1304@gmail.com', 'wd-67', 2, 'Tamil Nadu', 'Virudhunagar', 952365, 4500, 14000, 'wifi', 'Most suitable for three members family', 'gh-hospital', 'virudhunagar post office near by', 'vacant', 'house1.png', 'apartment.png', 'three.png', 'Approve', 2),
(10, 'beautiful Sugesh Houses', 'Raja', 2147483647, 'House', 'sugeshrahul1304@gmail.com', 'uj-78h', 1, 'Tamil Nadu', 'Pudukkottai', 951357, 6500, 20000, 'wifi', 'well organized and simple house ', 'It center opposite', 'Pudukkottai near by', 'vacant', 'one.png', 'pg1.jpg', 'three.png', 'Approve', 1),
(11, 'sugesh Apartments', 'Raja', 2147483647, 'Apartment', 'sugeshrahul1304@gmail.com', '12-bhu', 2, 'Tamil Nadu', 'Tiruvarur', 23165, 6000, 23000, 'wifi_food', 'Good for Company based organization', 'It Park', 'tiruvarur', 'vacant', 'house3.png', 'pg2.jpg', 'pg2.jpg', 'Approve', 1),
(12, 'Nandhalala pg', 'Nandhualan', 987654321, 'Pg', 'nandhualan108@gmail.com', '12-BHG', 2, 'Tamil Nadu', 'Nilgiris', 645987, 2000, 12000, 'wifi_food', 'Clean Area with large space', 'Gh Oposite', 'Nilgiris Gh Hospital ', 'vacant', 'pg1.jpg', 'pg2.jpg', 'pg3.jpg', 'Approve', 2),
(13, 'Jayam Houses', 'Nandhualan', 2147483647, 'House', 'nandhualan108@gmail.com', '14-ghy', 3, 'Tamil Nadu', 'Krishnagiri', 987456, 6000, 25000, 'food', 'Near by school and play grounds', 'Police station near by', 'Krishnagiri', 'vacant', 'fbg.jpg', 'pg3.jpg', 'apartment.png', 'new', 3),
(14, 'techvolt company', 'pandikumar', 2147483647, 'Apartment', 'pandikumar652001@gmail.com', '12-ghy', 2, 'Tamil Nadu', 'Pudukkottai', 321654, 6000, 23000, 'wifi_food', 'Best suitable for companys', 'GH-hospital', 'Nayakkar street pudukkottai', 'vacant', 'house3.png', 'three.png', 'apartment1.png', 'new', 2);

-- --------------------------------------------------------

--
-- Table structure for table `purchased_property`
--

CREATE TABLE `purchased_property` (
  `id` int(30) NOT NULL,
  `propertyName` varchar(40) NOT NULL,
  `ownerName` varchar(50) NOT NULL,
  `mobile` int(15) NOT NULL,
  `propertyType` varchar(20) NOT NULL,
  `owner_email` varchar(30) NOT NULL,
  `user_email` varchar(30) NOT NULL,
  `plotNo` varchar(30) NOT NULL,
  `availableBhk` int(50) NOT NULL,
  `state` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `pincode` int(10) NOT NULL,
  `rent` int(20) NOT NULL,
  `deposit` int(20) NOT NULL,
  `facilities` varchar(30) NOT NULL,
  `description` varchar(255) NOT NULL,
  `landmark` varchar(30) NOT NULL,
  `address` varchar(255) NOT NULL,
  `vacancies` varchar(30) NOT NULL,
  `pimage1` varchar(30) NOT NULL,
  `pimage2` varchar(30) NOT NULL,
  `pimage3` varchar(30) NOT NULL,
  `rentpayed` int(20) NOT NULL DEFAULT 0,
  `status` varchar(20) NOT NULL DEFAULT 'request',
  `balance` int(20) NOT NULL,
  `date` varchar(10) NOT NULL,
  `month` varchar(10) NOT NULL,
  `uname` varchar(30) NOT NULL,
  `umobile` int(30) NOT NULL,
  `uprofile` varchar(30) NOT NULL,
  `vacate_date` date NOT NULL,
  `vacate_status` varchar(30) NOT NULL,
  `remaining_bhk` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `purchased_property`
--

INSERT INTO `purchased_property` (`id`, `propertyName`, `ownerName`, `mobile`, `propertyType`, `owner_email`, `user_email`, `plotNo`, `availableBhk`, `state`, `city`, `pincode`, `rent`, `deposit`, `facilities`, `description`, `landmark`, `address`, `vacancies`, `pimage1`, `pimage2`, `pimage3`, `rentpayed`, `status`, `balance`, `date`, `month`, `uname`, `umobile`, `uprofile`, `vacate_date`, `vacate_status`, `remaining_bhk`) VALUES
(1, 'Kesave aparments', 'Nandhualan', 1234567890, 'Apartment', 'nandhualan108@gmail.com', 'nandhustark3000@gmail.com', '90-dfa', 3, 'Tamil Nadu', 'Mayiladuthurai', 123456, 5400, 20000, 'wifi_food', 'Large space so many members can stay', 'co office', 'Mayiladuthurai neary by', 'vacant', 'apartment2.jpg', 'apartment1.png', 'apartment.png', 0, 'Approve', 5400, '1', 'March', 'dinsesh', 1236549870, 'NANDHAKUMAR.jpg', '2024-03-01', 'Approve', 3),
(2, 'Kesave aparments', 'Nandhualan', 1234567890, 'Apartment', 'nandhualan108@gmail.com', 'nandhualan108@gmail.com', '90-dfa', 3, 'Tamil Nadu', 'Mayiladuthurai', 123456, 5400, 20000, 'wifi_food', 'Large space so many members can stay', 'co office', 'Mayiladuthurai neary by', 'vacant', 'apartment2.jpg', 'apartment1.png', 'apartment.png', 0, 'Approve', 5400, '1', 'March', 'Nandhu', 1236549870, '3437.jpg', '2024-03-01', 'Approve', 2),
(3, 'Kesave aparments', 'Nandhualan', 1234567890, 'Apartment', 'nandhualan108@gmail.com', 'nandhualan108@gmail.com', '90-dfa', 3, 'Tamil Nadu', 'Mayiladuthurai', 123456, 5400, 20000, 'wifi_food', 'Large space so many members can stay', 'co office', 'Mayiladuthurai neary by', 'vacant', 'apartment2.jpg', 'apartment1.png', 'apartment.png', 0, 'Approve', 5400, '1', 'March', 'Nandhu', 1236549870, '3437.jpg', '2024-03-01', 'Approve', 2),
(4, 'hari Jolaya', 'Nandhustark', 2147483647, 'House', 'nandhustark3000@gmail.com', 'nandhustark3000@gmail.com', '25-jhg', 2, 'Tamil Nadu', 'Perambalur', 321654, 6000, 12088, 'food', 'best property for 4 members family', 'collector office', 'Perambalur with gh hospital', 'occupied', 'apartment.png', 'apartment1.png', 'apartment2.jpg', 0, 'Approve', 6000, '1', 'March', 'dinsesh', 1236549870, 'NANDHAKUMAR.jpg', '0000-00-00', '', 1),
(5, 'Pandi PG', 'Nandhualan', 549873210, 'Pg', 'nandhualan108@gmail.com', 'nandhustark3000@gmail.com', '13-Bca', 2, 'Tamil Nadu', 'Mayiladuthurai', 123456, 2000, 15000, 'food', 'Fine Property ', 'gh -hospital', 'ukadamm', 'occupied', 'apartment.png', 'apartment1.png', 'apartment2.jpg', 0, 'Approve', 2000, '1', 'March', 'dinsesh', 1236549870, 'NANDHAKUMAR.jpg', '0000-00-00', '', 1),
(6, 'Marveleous', 'Nandhustark', 2147483647, 'Apartment', 'nandhustark3000@gmail.com', 'nandhualan108@gmail.com', '13-NUV', 2, 'Tamil Nadu', 'Karur', 321987, 7300, 20000, 'food', 'Good Looking apartment and lots of advantages', 'Techvolt oposite', 'Covai', 'vacant', 'apartment2.jpg', 'bgimg.jpg', 'house3.png', 0, 'request', 7300, '1', 'March', 'Nandhu', 1236549870, '3437.jpg', '0000-00-00', '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `userregform`
--

CREATE TABLE `userregform` (
  `id` int(20) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `Phone` int(20) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Dob` date NOT NULL,
  `Address` varchar(60) NOT NULL,
  `Pincode` int(10) NOT NULL,
  `State` varchar(30) NOT NULL,
  `City` varchar(30) NOT NULL,
  `Profession` varchar(30) NOT NULL,
  `photo` varchar(20) NOT NULL,
  `MarriedState` varchar(20) NOT NULL,
  `Identity` varchar(20) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Reg_time` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userregform`
--

INSERT INTO `userregform` (`id`, `Name`, `Gender`, `Phone`, `Email`, `Dob`, `Address`, `Pincode`, `State`, `City`, `Profession`, `photo`, `MarriedState`, `Identity`, `Password`, `Reg_time`) VALUES
(1, 'Nandhu', 'male', 1236549870, 'nandhualan108@gmail.com', '2024-02-17', 'fdfdfd', 123456, 'Tamil Nadu', 'Madurai', 'Lawyer', '3437.jpg', 'married', '8.jpg', '123', '2024-02-09 08:35:07.281794'),
(2, 'dinsesh', 'male', 1236549870, 'nandhustark3000@gmail.com', '0000-00-00', 'Krishnagiri', 123456, 'Tamil Nadu', 'Krishnagiri', 'Bussiness', 'NANDHAKUMAR.jpg', 'unmarried', '621123.jpg', '987', '2024-02-26 16:46:57.479230');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `complaints`
--
ALTER TABLE `complaints`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `forgot_pass`
--
ALTER TABLE `forgot_pass`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ownerregform`
--
ALTER TABLE `ownerregform`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payment_history`
--
ALTER TABLE `payment_history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `property`
--
ALTER TABLE `property`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `purchased_property`
--
ALTER TABLE `purchased_property`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userregform`
--
ALTER TABLE `userregform`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `complaints`
--
ALTER TABLE `complaints`
  MODIFY `id` int(40) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `forgot_pass`
--
ALTER TABLE `forgot_pass`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `ownerregform`
--
ALTER TABLE `ownerregform`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `id` int(40) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `payment_history`
--
ALTER TABLE `payment_history`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `property`
--
ALTER TABLE `property`
  MODIFY `id` int(40) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `purchased_property`
--
ALTER TABLE `purchased_property`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `userregform`
--
ALTER TABLE `userregform`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
