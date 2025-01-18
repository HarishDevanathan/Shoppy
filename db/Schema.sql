-- MySQL dump 10.13  Distrib 9.1.0, for macos13.7 (arm64)
--
-- Host: localhost    Database: project_db
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `name` varchar(100) DEFAULT NULL,
  `brand` varchar(100) DEFAULT NULL,
  `product_id` varchar(16) NOT NULL,
  `id` varchar(11) NOT NULL,
  `discountpercentage` int DEFAULT NULL,
  `discountprice` int DEFAULT NULL,
  `imagepath` varchar(200) DEFAULT NULL,
  `productdesc` varchar(500) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `units_sold` int DEFAULT NULL,
  `rating_count` int DEFAULT NULL,
  `smdesc` varchar(100) DEFAULT NULL,
  `shipping` int DEFAULT NULL,
  `mrp` int DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  KEY `id` (`id`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user_data` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('water bottle','tupperware','SQUF10527400','02-12345678',30,3500,'SQUF10527400.jpg','this is a water bottle',5,25,60,2000,'plastic',3,5000),('water bottle','signoraware','VNZJ33302041','02-12345678',30,3500,'VNZJ33302041.jpg','this is set of 9 water bottles',5,20,50,1000,'set of 9 bottles',3,5000);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_data`
--

DROP TABLE IF EXISTS `user_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_data` (
  `username` varchar(100) NOT NULL,
  `passw` varchar(500) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phno` varchar(15) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `doj` date DEFAULT NULL,
  `id` varchar(11) DEFAULT NULL,
  `cart` json DEFAULT NULL,
  `orders` json DEFAULT NULL,
  `wallet` int DEFAULT NULL,
  `owned_products` json DEFAULT NULL,
  `hist` json DEFAULT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phno` (`phno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_data`
--

LOCK TABLES `user_data` WRITE;
/*!40000 ALTER TABLE `user_data` DISABLE KEYS */;
INSERT INTO `user_data` VALUES ('Ganesh','scrypt:32768:8:1$S2lqZs4PBLjLdnU7$edd24fa10a37e034f18bdb53f19e05aadb4ef3e39b49dc562d6b0644fa1645a9825018dc4b91c2386dfde9bae8fb3864117a3bba33050247858b9556a918a0ac','abcd@gmail.com','+91-1234567890','no 17','2025-01-14','02-12345678',NULL,NULL,1000,'[\"VNZJ33302041\"]',NULL);
/*!40000 ALTER TABLE `user_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-18 21:59:21
