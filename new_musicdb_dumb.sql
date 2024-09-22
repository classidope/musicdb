-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: musicdb
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `songs`
--

DROP TABLE IF EXISTS `songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `artist` varchar(100) NOT NULL,
  `title` varchar(150) NOT NULL,
  `mood` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_song` (`artist`,`title`,`mood`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs`
--

LOCK TABLES `songs` WRITE;
/*!40000 ALTER TABLE `songs` DISABLE KEYS */;
INSERT INTO `songs` VALUES (1,'Acid Bath','The Bones Of Babydolls','depressing'),(2,'Agalloch','Falling Snow','reflective'),(3,'Anathema','One Last Goodbye','reflective'),(4,'Anthrax','Caught In A Mosh','energetic'),(5,'Behemoth','Blow Your Trumpets Gabriel','aggressive'),(6,'Black Sabbath','Planet Caravan','mellow'),(7,'Bolt Thrower','The IVth Crusade','depressing'),(8,'Candlemass','Epicus Doomicus Metallicus','epic'),(9,'Cannibal Corpse','Hammer Smashed Face','aggressive'),(34,'Clairo','Bubble Gum','Fretting'),(32,'Cults','Gilded Lily','Fretting'),(36,'Duster','Stars Will Fall','Fretting'),(10,'Dying Fetus','Pissing in the Mainstream','aggressive'),(11,'Immolation','Kingdom of Conspiracy','aggressive'),(12,'Led Zeppelin','Going to California','mellow'),(13,'Metallica','Enter Sandman','energetic'),(14,'My Dying Bride','The Dreadful Hours','depressing'),(15,'Napalm Death','Scum','aggressive'),(16,'Opeth','Ghost of Perdition','reflective'),(17,'Opeth','Harvest','reflective'),(18,'Pantera','Walk','energetic'),(19,'Paradise Lost','Gothic','depressing'),(20,'Pink Floyd','Wish You Were Here','mellow'),(21,'Porcupine Tree','Arriving Somewhere But Not Here','reflective'),(22,'Sepultura','Roots Bloody Roots','energetic'),(33,'sign crushes motorist','Better','Fretting'),(23,'Slayer','Raining Blood','energetic'),(24,'Sodom','Agent Orange','agressive'),(25,'The Doors','Riders on the Storm','mellow'),(26,'Tool','Lateralus','mellow'),(27,'Xasthur','Screaming at Forgotten Tears','depressing'),(28,'Xasthur','Telepathic with the Deceased','depressing'),(35,'Yot Club','YKWIM?','Fretting');
/*!40000 ALTER TABLE `songs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-22 16:53:50
