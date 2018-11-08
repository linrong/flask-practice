drop database if exists flask;
create database flask;
use flask;
DROP TABLE IF EXISTS `PasteFile`;
CREATE TABLE `PasteFile` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `filename` varchar(5000) NOT NULL,
    `filehash` VARCHAR(128) NOT NULL,
    `filemd5` VARCHAR(128) NOT NULL,
    `uploadtime` DATETIME NOT NULL,
    `mimetype` VARCHAR(256) NOT NULL,
    `size` INT(11) unsigned NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `filehash` (`filehash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8; 
