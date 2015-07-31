-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: kmbdd
-- ------------------------------------------------------
-- Server version	5.5.44-0+deb8u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add activite audit',7,'add_activiteaudit'),(20,'Can change activite audit',7,'change_activiteaudit'),(21,'Can delete activite audit',7,'delete_activiteaudit'),(22,'Can add impact vuln',8,'add_impactvuln'),(23,'Can change impact vuln',8,'change_impactvuln'),(24,'Can delete impact vuln',8,'delete_impactvuln'),(25,'Can add difficulte exploit vuln',9,'add_difficulteexploitvuln'),(26,'Can change difficulte exploit vuln',9,'change_difficulteexploitvuln'),(27,'Can delete difficulte exploit vuln',9,'delete_difficulteexploitvuln'),(28,'Can add rapport',10,'add_rapport'),(29,'Can change rapport',10,'change_rapport'),(30,'Can delete rapport',10,'delete_rapport'),(31,'Can add mot clef',11,'add_motclef'),(32,'Can change mot clef',11,'change_motclef'),(33,'Can delete mot clef',11,'delete_motclef'),(34,'Can add vulnerabilite',12,'add_vulnerabilite'),(35,'Can change vulnerabilite',12,'change_vulnerabilite'),(36,'Can delete vulnerabilite',12,'delete_vulnerabilite'),(37,'Can add echeance reco',13,'add_echeancereco'),(38,'Can change echeance reco',13,'change_echeancereco'),(39,'Can delete echeance reco',13,'delete_echeancereco'),(40,'Can add difficulte reco',14,'add_difficultereco'),(41,'Can change difficulte reco',14,'change_difficultereco'),(42,'Can delete difficulte reco',14,'delete_difficultereco'),(43,'Can add recommandation',15,'add_recommandation'),(44,'Can change recommandation',15,'change_recommandation'),(45,'Can delete recommandation',15,'delete_recommandation');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$Ej8wo84gBNlp$4STJDxDsS5F5V0BQfVBJNOU2d84WWU4ApaOInFdjnIA=','2015-07-23 16:01:00',1,'hdl','','','hugoss1@hotmail.fr',1,1,'2015-07-20 07:13:57');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-07-20 07:22:57','1','aucun impact',1,'',8,1),(2,'2015-07-20 07:23:18','1','difficultee = 3',1,'',9,1),(3,'2015-07-20 07:23:39','1','X12-2009',1,'',10,1),(4,'2015-07-20 07:23:50','1','XSS',1,'',11,1),(5,'2015-07-20 07:24:04','1','audit de conf',1,'',7,1),(6,'2015-07-20 07:24:28','1','courte',1,'',13,1),(7,'2015-07-20 07:24:48','1','ça va',1,'',14,1),(8,'2015-07-20 07:25:57','1','bla description detaillée client...',1,'',12,1),(9,'2015-07-20 07:31:03','2','moyen',1,'',8,1),(10,'2015-07-20 07:31:15','2','difficultee = 2',1,'',9,1),(11,'2015-07-20 07:31:38','2','FR89-YT',1,'',10,1),(12,'2015-07-20 07:31:46','2','SQLi',1,'',11,1),(13,'2015-07-20 07:32:03','2','conf code',1,'',7,1),(14,'2015-07-20 07:33:00','2','on a le temps',1,'',13,1),(15,'2015-07-20 07:33:15','2','cher',1,'',14,1),(16,'2015-07-20 07:33:23','2','detruit tout...',1,'',12,1),(17,'2015-07-20 12:26:26','2','detruit tout <script>alert(0)</script>...',2,'Changed description.',12,1),(18,'2015-07-22 09:41:50','2','detruit tout <script>alert(0)</script>...',3,'',12,1),(19,'2015-07-22 09:41:50','1','bla description detaillée client...',3,'',12,1),(20,'2015-07-22 10:03:59','3','Mineur',1,'',8,1),(21,'2015-07-22 11:14:54','4','Notable',1,'',8,1),(22,'2015-07-22 11:15:23','5','Critique',1,'',8,1),(23,'2015-07-22 11:17:25','6','Majeur',1,'',8,1),(24,'2015-07-22 11:21:13','3','Mineur',2,'Changed description_detaillee.',8,1),(25,'2015-07-22 11:22:23','6','Majeur',2,'Changed description_detaillee.',8,1),(26,'2015-07-22 11:24:23','3','difficultee = 1',1,'',9,1),(27,'2015-07-22 11:25:20','4','difficultee = 2',1,'',9,1),(28,'2015-07-22 11:25:59','5','difficultee = 3',1,'',9,1),(29,'2015-07-22 11:26:35','6','difficultee = 4',1,'',9,1),(30,'2015-07-22 11:27:43','3','Code source',1,'',7,1),(31,'2015-07-22 11:27:58','4','Architecture',1,'',7,1),(32,'2015-07-22 11:28:12','5','Configuration',1,'',7,1),(33,'2015-07-22 11:28:44','6','Test d\'intrusion',1,'',7,1),(34,'2015-07-22 11:29:27','7','Test d\'intrusion interne',1,'',7,1),(35,'2015-07-22 11:29:47','8','Test d\'intrusion externe',1,'',7,1),(36,'2015-07-22 13:58:34','3','test',1,'',11,1),(37,'2015-07-22 13:59:26','3','test',3,'',11,1),(38,'2015-07-22 15:53:49','3','SIB007',1,'',10,1),(39,'2015-07-22 15:54:53','4','OBE002',1,'',10,1),(40,'2015-07-22 15:55:45','5','SF2001',1,'',10,1),(41,'2015-07-22 15:56:32','6','CNE025',1,'',10,1),(42,'2015-07-22 16:00:04','7','NAT001',1,'',10,1),(43,'2015-07-22 16:00:43','8','FIM004',1,'',10,1),(44,'2015-07-22 16:01:21','9','PBX001',1,'',10,1),(45,'2015-07-22 16:02:57','10','C35002-3',1,'',10,1),(46,'2015-07-22 16:04:38','11','FIM005',1,'',10,1),(47,'2015-07-22 16:05:02','10','C35002-3',2,'Changed auditeurs_impliques.',10,1),(48,'2015-07-22 16:05:37','8','FIM004',2,'Changed auditeurs_impliques.',10,1),(49,'2015-07-22 16:05:57','6','CNE025',2,'Changed auditeurs_impliques.',10,1),(50,'2015-07-22 16:06:19','3','SIB007',2,'No fields changed.',10,1),(51,'2015-07-22 16:07:03','12','AGE001',1,'',10,1),(52,'2015-07-22 16:07:42','13','ARE010',1,'',10,1),(53,'2015-07-22 16:08:14','14','ATO010',1,'',10,1),(54,'2015-07-22 16:08:43','15','CDA001',1,'',10,1),(55,'2015-07-22 16:09:21','16','CNE028',1,'',10,1),(56,'2015-07-22 16:09:59','17','COD001',1,'',10,1),(57,'2015-07-22 16:10:37','18','CRO001',1,'',10,1),(58,'2015-07-22 16:11:13','19','DIE001',1,'',10,1),(59,'2015-07-22 16:11:50','20','DIG001',1,'',10,1),(60,'2015-07-22 16:12:36','21','FIM007',1,'',10,1),(61,'2015-07-22 16:13:10','22',' FIM007-1',1,'',10,1),(62,'2015-07-22 16:13:49','23','IMP002',1,'',10,1),(63,'2015-07-22 16:14:20','24','ORA001-5',1,'',10,1),(64,'2015-07-22 16:14:54','25','PBX001-1',1,'',10,1),(65,'2015-07-22 16:15:24','26','PBX002',1,'',10,1),(66,'2015-07-22 16:16:02','27','SIE001',1,'',10,1),(67,'2015-07-22 16:16:43','28','C35002-4',1,'',10,1),(68,'2015-07-22 16:17:09','29','BRO001',1,'',10,1),(69,'2015-07-22 16:17:48','30','SAO001',1,'',10,1),(70,'2015-07-22 16:18:14','31','SOS001',1,'',10,1),(71,'2015-07-22 16:18:51','32','CNI001',1,'',10,1),(72,'2015-07-22 16:19:17','33','PBX001-2',1,'',10,1),(73,'2015-07-22 16:19:51','34','CNE031',1,'',10,1),(74,'2015-07-22 16:20:29','35','CNE035',1,'',10,1),(75,'2015-07-22 16:20:56','36','IPL001',1,'',10,1),(76,'2015-07-22 16:21:35','37','FLA001-2',1,'',10,1),(77,'2015-07-22 16:21:59','38','REN001',1,'',10,1),(78,'2015-07-22 16:22:25','39','SF2002',1,'',10,1),(79,'2015-07-22 16:22:56','40','ATE001',1,'',10,1),(80,'2015-07-22 16:23:26','41','CHD001',1,'',10,1),(81,'2015-07-22 16:24:01','42','CHD002',1,'',10,1),(82,'2015-07-22 16:24:44','43','CMG001',1,'',10,1),(83,'2015-07-22 16:25:06','44','DET002',1,'',10,1),(84,'2015-07-22 16:25:23','45','IPL002',1,'',10,1),(85,'2015-07-22 16:25:49','46','ELR001',1,'',10,1),(86,'2015-07-22 16:26:11','47','GAL001',1,'',10,1),(87,'2015-07-22 16:26:32','48','GTT001',1,'',10,1),(88,'2015-07-22 16:26:57','49','IMP004',1,'',10,1),(89,'2015-07-22 16:27:20','50','PBX004',1,'',10,1),(90,'2015-07-22 16:27:54','51','PBX005',1,'',10,1),(91,'2015-07-22 16:28:11','52','PPA001',1,'',10,1),(92,'2015-07-22 16:28:42','53','SIE003',1,'',10,1),(93,'2015-07-22 16:29:08','54','SEL001',1,'',10,1),(94,'2015-07-22 16:29:39','55','TRA001',1,'',10,1),(95,'2015-07-22 16:30:11','56','VAL001',1,'',10,1),(96,'2015-07-22 16:30:39','57','AUV001-1',1,'',10,1),(97,'2015-07-23 09:05:55','22','FIM007-1',2,'Changed nom_rapport.',10,1),(98,'2015-07-23 16:21:38','1','<script>',1,'',11,1),(99,'2015-07-23 16:23:04','1','<script>',3,'',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'home','activiteaudit'),(9,'home','difficulteexploitvuln'),(14,'home','difficultereco'),(13,'home','echeancereco'),(8,'home','impactvuln'),(11,'home','motclef'),(10,'home','rapport'),(15,'home','recommandation'),(12,'home','vulnerabilite'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-07-17 15:05:01'),(2,'auth','0001_initial','2015-07-17 15:05:03'),(3,'admin','0001_initial','2015-07-17 15:05:03'),(4,'contenttypes','0002_remove_content_type_name','2015-07-17 15:05:03'),(5,'auth','0002_alter_permission_name_max_length','2015-07-17 15:05:03'),(6,'auth','0003_alter_user_email_max_length','2015-07-17 15:05:04'),(7,'auth','0004_alter_user_username_opts','2015-07-17 15:05:04'),(8,'auth','0005_alter_user_last_login_null','2015-07-17 15:05:04'),(9,'auth','0006_require_contenttypes_0002','2015-07-17 15:05:04'),(10,'home','0001_initial','2015-07-17 15:05:04'),(11,'home','0002_auto_20150715_1241','2015-07-17 15:05:06'),(12,'home','0003_auto_20150715_1522','2015-07-17 15:05:08'),(13,'home','0004_auto_20150715_1527','2015-07-17 15:05:08'),(14,'home','0005_auto_20150715_1530','2015-07-17 15:05:09'),(15,'home','0006_auto_20150715_1531','2015-07-17 15:05:09'),(16,'home','0007_auto_20150715_1532','2015-07-17 15:05:10'),(17,'home','0008_auto_20150716_1245','2015-07-17 15:05:11'),(18,'home','0009_vulnerabilite_activites_liees','2015-07-17 15:05:11'),(19,'sessions','0001_initial','2015-07-17 15:05:12'),(20,'home','0010_auto_20150720_0712','2015-07-20 07:12:43'),(21,'home','0011_auto_20150720_0719','2015-07-20 07:20:02'),(22,'home','0012_auto_20150722_0953','2015-07-22 09:53:12'),(23,'home','0013_auto_20150722_1354','2015-07-22 13:54:10');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('53nr06xl87nn71bqdzb52w9zi0pqr3mj','ODRkYjFlM2Q1OGEzMmYyMWZkYTA0MGQ2YzBmM2Y0ODRjZWRlOGY2YTp7Il9hdXRoX3VzZXJfaGFzaCI6IjVjYTcxNjNhYWM4NDYwY2MxZTc5Zjg0MGRiYTY2OTMzNTk4Mjc0MDMiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-08-06 16:01:01');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuln_activiteaudit`
--

DROP TABLE IF EXISTS `vuln_activiteaudit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vuln_activiteaudit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom_activite` varchar(255) NOT NULL,
  `activiteParente_id` int(11),
  PRIMARY KEY (`id`),
  KEY `vuln_activiteaudit_d5518988` (`activiteParente_id`),
  CONSTRAINT `hom_activiteParente_id_581e5a44f23cd4a9_fk_vuln_activiteaudit_id` FOREIGN KEY (`activiteParente_id`) REFERENCES `vuln_activiteaudit` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuln_activiteaudit`
--

LOCK TABLES `vuln_activiteaudit` WRITE;
/*!40000 ALTER TABLE `vuln_activiteaudit` DISABLE KEYS */;
INSERT INTO `vuln_activiteaudit` VALUES (3,'Code source',NULL),(4,'Architecture',NULL),(5,'Configuration',NULL),(6,'Test d\'intrusion',NULL),(7,'Test d\'intrusion interne',6),(8,'Test d\'intrusion externe',6);
/*!40000 ALTER TABLE `vuln_activiteaudit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuln_difficulteexploitvuln`
--

DROP TABLE IF EXISTS `vuln_difficulteexploitvuln`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vuln_difficulteexploitvuln` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `niveau` int(11) NOT NULL,
  `description_acte_volontaire` longtext NOT NULL,
  `description_acte_involontaire` longtext NOT NULL,
  `description_niveau` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuln_difficulteexploitvuln`
--

LOCK TABLES `vuln_difficulteexploitvuln` WRITE;
/*!40000 ALTER TABLE `vuln_difficulteexploitvuln` DISABLE KEYS */;
INSERT INTO `vuln_difficulteexploitvuln` VALUES (3,1,'Très improbable :\r\n< 1% de chances de survenance sur l’année','Très difficile :\r\nLa menace est réalisable à condition que la source puisse disposer de la complicité de plusieurs acteurs ainsi que de compétences poussées ou de moyens couteux qui ne se trouvent pas habituellement en possession de la source considérée','Extrêmement rare'),(4,2,'Peu vraisemblable :\r\n< 10% de chances de survenance sur l’année','Faisable :\r\nLa menace est réalisable à condition que la source puisse disposer de la complicité de plusieurs acteurs ainsi que de compétences poussées ou de moyens couteux ','Rare'),(5,3,'Probable : \r\nEntre 10% et 50% de chances de survenance sur l’année','Facile :\r\nLa menace est réalisable à condition que la source puisse disposer de droits supplémentaires (ou d\'une seule complicité)','Possible'),(6,4,'Très probable :\r\n> 50% de chances de survenance sur l’année','Très facile :\r\nLa menace est réalisable par des moyens standards ou des connaissances de base qui sont à la portée de tous','Fréquent');
/*!40000 ALTER TABLE `vuln_difficulteexploitvuln` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuln_difficultereco`
--

DROP TABLE IF EXISTS `vuln_difficultereco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vuln_difficultereco` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `niveau` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `cout_homme_mois` double NOT NULL,
  `cout_initial_euros` double NOT NULL,
  `cout_recurrent_euros` double NOT NULL,
  `description_detaillee` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuln_difficultereco`
--

LOCK TABLES `vuln_difficultereco` WRITE;
/*!40000 ALTER TABLE `vuln_difficultereco` DISABLE KEYS */;
/*!40000 ALTER TABLE `vuln_difficultereco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuln_echeancereco`
--

DROP TABLE IF EXISTS `vuln_echeancereco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vuln_echeancereco` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `niveau` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `description_detaillee` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuln_echeancereco`
--

LOCK TABLES `vuln_echeancereco` WRITE;
/*!40000 ALTER TABLE `vuln_echeancereco` DISABLE KEYS */;
/*!40000 ALTER TABLE `vuln_echeancereco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuln_impactvuln`
--

DROP TABLE IF EXISTS `vuln_impactvuln`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vuln_impactvuln` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `niveau` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `description_detaillee` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuln_impactvuln`
--

LOCK TABLES `vuln_impactvuln` WRITE;
/*!40000 ALTER TABLE `vuln_impactvuln` DISABLE KEYS */;
INSERT INTO `vuln_impactvuln` VALUES (3,1,'Mineur','IF : dizaine ou centaine d’euros annuels\r\nRéputation / image : pas d’impact en dehors de l\'entreprise.\r\nRéglementaire : sanction interne.\r\nAtteinte à la vie des personnes : alerte sans arrêt de travail'),(4,2,'Notable','IF : milliers d’euros annuels\r\nRéputation / image : impact localisé, sur peu de partenaires\r\nRéglementaire : Corruption des données de traçabilité, mention dans une affaire civile ou pénale, pénalités contractuelles\r\nAtteinte à la vie des personnes : arrêt de travail de courte durée'),(5,3,'Critique','IF : dizaine ou centaine de milliers d’euros annuels\r\nRéputation / image : impact national, sur les tutelles et sur de nombreux partenaires \r\nRéglementaire : Non-respect de la loi et de la réglementation (CNIL notamment). Atteinte à la vie privée. Perte de traçabilité sur un processus critique. Enquête administrative. Condamnation ou amende. Pénalités contractuelles fortes.\r\nAtteinte à la vie des personnes : arrêt de travail de longue durée / séquelles'),(6,4,'Majeur','IF : millions d’euros annuels\r\nRéputation / image : visibilité par le public\r\nRéglementaire : Non-respect majeur de la loi et de la réglementation (CNIL notamment). Perte de traçabilité sur un processus très critique. Atteinte massive à la vie privée. Condamnation pénale d’un agent ou de l’organisme. Pénalités contractuelles maximum.\r\nAtteinte à la vie des personnes : Décès');
/*!40000 ALTER TABLE `vuln_impactvuln` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuln_motclef`
--

DROP TABLE IF EXISTS `vuln_motclef`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vuln_motclef` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vuln_motclef_nom_20c3988c7a94fcb8_uniq` (`nom`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuln_motclef`
--

LOCK TABLES `vuln_motclef` WRITE;
/*!40000 ALTER TABLE `vuln_motclef` DISABLE KEYS */;
/*!40000 ALTER TABLE `vuln_motclef` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuln_rapport`
--

DROP TABLE IF EXISTS `vuln_rapport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vuln_rapport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom_rapport` varchar(255) NOT NULL,
  `date_rapport` date NOT NULL,
  `auditeurs_impliques` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuln_rapport`
--

LOCK TABLES `vuln_rapport` WRITE;
/*!40000 ALTER TABLE `vuln_rapport` DISABLE KEYS */;
INSERT INTO `vuln_rapport` VALUES (3,'SIB007','2013-09-01','mor, dkr, dln'),(4,'OBE002','2013-10-01','yde'),(5,'SF2001','2013-11-01','arn, mor'),(6,'CNE025','2013-11-12','trt, fgy'),(7,'NAT001','2013-11-22','trt, tvz, mor'),(8,'FIM004','2013-12-11','trt, tvz, yde, she\r\n'),(9,'PBX001','2013-12-21','yde, tvz'),(10,'C35002-3','2014-01-01','tvz, mor'),(11,'FIM005','2014-01-08','cmy, dkr, dln'),(12,'AGE001','2014-01-15','arn, mor, tvz'),(13,'ARE010','2014-01-22','arn, jld'),(14,'ATO010','2014-02-01','trt, arn, mor'),(15,'CDA001','2014-02-08','tvz, mor'),(16,'CNE028','2014-03-22','trt,gbt, mor'),(17,'COD001','2014-02-22','tvz,mor, dln'),(18,'CRO001','2014-03-01','arn,mor'),(19,'DIE001','2014-03-08','arn,mor'),(20,'DIG001','2014-03-22','mor, dln'),(21,'FIM007','2014-04-01','yde, dln'),(22,'FIM007-1','2014-05-01','yde, dln'),(23,'IMP002','2014-05-15','yde, tvz,mor'),(24,'ORA001-5','2014-06-01','yde'),(25,'PBX001-1','2014-06-15','yde'),(26,'PBX002','2014-07-01','yde'),(27,'SIE001','2014-07-01','arn, mor'),(28,'C35002-4','2014-07-15','arn, mor'),(29,'BRO001','2014-08-01','jle'),(30,'SAO001','2014-09-01','arn, trt, mor'),(31,'SOS001','2014-10-01','tvz'),(32,'CNI001','2014-11-01','yde, jle, she'),(33,'PBX001-2','2014-12-01','yde'),(34,'CNE031','2014-12-15','trt, dln'),(35,'CNE035','2015-01-01','jle, mor'),(36,'IPL001','2015-01-15','yde'),(37,'FLA001-2','2015-02-01','tvz, mor,tvz, jle'),(38,'REN001','2015-02-15','yde'),(39,'SF2002','2015-03-01','mor'),(40,'ATE001','2015-03-10','gfn'),(41,'CHD001','2015-03-20','glt, jle'),(42,'CHD002','2015-04-01','glt, jle'),(43,'CMG001','2015-04-03','glt, gfn'),(44,'DET002','2015-04-15','trt'),(45,'IPL002','2015-04-30','yde'),(46,'ELR001','2015-05-01','yde, chy'),(47,'GAL001','2015-05-10','yde, fgy'),(48,'GTT001','2015-05-20','gcu, jld'),(49,'IMP004','2015-06-01','mor'),(50,'PBX004','2015-06-10','yde'),(51,'PBX005','2015-06-20','yde, gfn'),(52,'PPA001','2015-06-30','tvz'),(53,'SIE003','2015-06-15','trt'),(54,'SEL001','2015-06-25','cmy, dln'),(55,'TRA001','2015-07-05','cbn, mvt, glt'),(56,'VAL001','2015-07-15','arn, tvz'),(57,'AUV001-1','2015-07-15','yde, dco, she');
/*!40000 ALTER TABLE `vuln_rapport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuln_recommandation`
--

DROP TABLE IF EXISTS `vuln_recommandation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vuln_recommandation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `explication` longtext NOT NULL,
  `cout_reco_id` int(11) NOT NULL,
  `echeance_id` int(11) NOT NULL,
  `vuln_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vuln_recomm_echeance_id_1781e494c0b82094_fk_vuln_echeancereco_id` (`echeance_id`),
  KEY `vuln_recommandation_71e81e85` (`vuln_id`),
  KEY `vuln_reco_cout_reco_id_b950279fb181088_fk_vuln_difficultereco_id` (`cout_reco_id`),
  CONSTRAINT `vuln_recommand_vuln_id_63b5834e5f726c65_fk_vuln_vulnerabilite_id` FOREIGN KEY (`vuln_id`) REFERENCES `vuln_vulnerabilite` (`id`),
  CONSTRAINT `vuln_recomm_echeance_id_1781e494c0b82094_fk_vuln_echeancereco_id` FOREIGN KEY (`echeance_id`) REFERENCES `vuln_echeancereco` (`id`),
  CONSTRAINT `vuln_reco_cout_reco_id_b950279fb181088_fk_vuln_difficultereco_id` FOREIGN KEY (`cout_reco_id`) REFERENCES `vuln_difficultereco` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuln_recommandation`
--

LOCK TABLES `vuln_recommandation` WRITE;
/*!40000 ALTER TABLE `vuln_recommandation` DISABLE KEYS */;
/*!40000 ALTER TABLE `vuln_recommandation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuln_vulnerabilite`
--

DROP TABLE IF EXISTS `vuln_vulnerabilite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vuln_vulnerabilite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` longtext NOT NULL,
  `estBoiteNoire` tinyint(1) NOT NULL,
  `difficulte_exploit_id` int(11) NOT NULL,
  `impact_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `D3e277b17c829d06381dc50b43522308` (`difficulte_exploit_id`),
  KEY `vuln_vulnerabili_impact_id_28de3b9d3c4f022_fk_vuln_impactvuln_id` (`impact_id`),
  CONSTRAINT `D3e277b17c829d06381dc50b43522308` FOREIGN KEY (`difficulte_exploit_id`) REFERENCES `vuln_difficulteexploitvuln` (`id`),
  CONSTRAINT `vuln_vulnerabili_impact_id_28de3b9d3c4f022_fk_vuln_impactvuln_id` FOREIGN KEY (`impact_id`) REFERENCES `vuln_impactvuln` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuln_vulnerabilite`
--

LOCK TABLES `vuln_vulnerabilite` WRITE;
/*!40000 ALTER TABLE `vuln_vulnerabilite` DISABLE KEYS */;
/*!40000 ALTER TABLE `vuln_vulnerabilite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuln_vulnerabilite_activites_liees`
--

DROP TABLE IF EXISTS `vuln_vulnerabilite_activites_liees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vuln_vulnerabilite_activites_liees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vulnerabilite_id` int(11) NOT NULL,
  `activiteaudit_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vulnerabilite_id` (`vulnerabilite_id`,`activiteaudit_id`),
  KEY `vuln_v_activiteaudit_id_d5ce5fa16283157_fk_vuln_activiteaudit_id` (`activiteaudit_id`),
  CONSTRAINT `vuln_v_activiteaudit_id_d5ce5fa16283157_fk_vuln_activiteaudit_id` FOREIGN KEY (`activiteaudit_id`) REFERENCES `vuln_activiteaudit` (`id`),
  CONSTRAINT `vuln__vulnerabilite_id_2a9cafe34234fef5_fk_vuln_vulnerabilite_id` FOREIGN KEY (`vulnerabilite_id`) REFERENCES `vuln_vulnerabilite` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuln_vulnerabilite_activites_liees`
--

LOCK TABLES `vuln_vulnerabilite_activites_liees` WRITE;
/*!40000 ALTER TABLE `vuln_vulnerabilite_activites_liees` DISABLE KEYS */;
/*!40000 ALTER TABLE `vuln_vulnerabilite_activites_liees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuln_vulnerabilite_mots_clefs`
--

DROP TABLE IF EXISTS `vuln_vulnerabilite_mots_clefs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vuln_vulnerabilite_mots_clefs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vulnerabilite_id` int(11) NOT NULL,
  `motclef_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vulnerabilite_id` (`vulnerabilite_id`,`motclef_id`),
  KEY `vuln_vulnerabilit_motclef_id_2844ece6261fc1c4_fk_vuln_motclef_id` (`motclef_id`),
  CONSTRAINT `vuln_vulnerabilit_motclef_id_2844ece6261fc1c4_fk_vuln_motclef_id` FOREIGN KEY (`motclef_id`) REFERENCES `vuln_motclef` (`id`),
  CONSTRAINT `vuln__vulnerabilite_id_5b4391d643f44888_fk_vuln_vulnerabilite_id` FOREIGN KEY (`vulnerabilite_id`) REFERENCES `vuln_vulnerabilite` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuln_vulnerabilite_mots_clefs`
--

LOCK TABLES `vuln_vulnerabilite_mots_clefs` WRITE;
/*!40000 ALTER TABLE `vuln_vulnerabilite_mots_clefs` DISABLE KEYS */;
/*!40000 ALTER TABLE `vuln_vulnerabilite_mots_clefs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vuln_vulnerabilite_rapports_ou_on_a_trouve_la_vuln`
--

DROP TABLE IF EXISTS `vuln_vulnerabilite_rapports_ou_on_a_trouve_la_vuln`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vuln_vulnerabilite_rapports_ou_on_a_trouve_la_vuln` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vulnerabilite_id` int(11) NOT NULL,
  `rapport_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vulnerabilite_id` (`vulnerabilite_id`,`rapport_id`),
  KEY `vuln_vulnerabilit_rapport_id_3eda61670ec041f4_fk_vuln_rapport_id` (`rapport_id`),
  CONSTRAINT `vuln_vulnerabilit_rapport_id_3eda61670ec041f4_fk_vuln_rapport_id` FOREIGN KEY (`rapport_id`) REFERENCES `vuln_rapport` (`id`),
  CONSTRAINT `vuln__vulnerabilite_id_7f198a5f88c37eac_fk_vuln_vulnerabilite_id` FOREIGN KEY (`vulnerabilite_id`) REFERENCES `vuln_vulnerabilite` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vuln_vulnerabilite_rapports_ou_on_a_trouve_la_vuln`
--

LOCK TABLES `vuln_vulnerabilite_rapports_ou_on_a_trouve_la_vuln` WRITE;
/*!40000 ALTER TABLE `vuln_vulnerabilite_rapports_ou_on_a_trouve_la_vuln` DISABLE KEYS */;
/*!40000 ALTER TABLE `vuln_vulnerabilite_rapports_ou_on_a_trouve_la_vuln` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-29 11:52:33
