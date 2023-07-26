DROP DATABASE IF EXISTS `assignment2`;
CREATE DATABASE `assignment2`;
USE `assignment2`;

-- Tables for confirmSuperkey()

CREATE TABLE R1( `e` INT
	           , `f` INT AUTO_INCREMENT
	           , `g` INT
	           , `h` INT
	           , PRIMARY KEY(`f`)
	           );

CREATE TABLE R2( `e` INT
	           , `f` INT AUTO_INCREMENT
	           , `g` INT
	           , `h` INT
	           , PRIMARY KEY(`f`)
	           );

CREATE TABLE R3( `e` INT
	           , `f` INT AUTO_INCREMENT
	           , `g` INT DEFAULT 3
	           , `h` INT
	           , PRIMARY KEY(`f`, `g`)
	           );

CREATE TABLE R4( `e` INT
	           , `f` INT AUTO_INCREMENT
	           , `g` INT UNIQUE DEFAULT 4
	           , `h` INT
	           , PRIMARY KEY(`f`)
	           );

-- Tables for confirmForeignKey()

CREATE TABLE R6( `x` INT AUTO_INCREMENT
	           , `y` INT
	           , `z` INT
	           , PRIMARY KEY(`x`)
	           );
CREATE TABLE S6( `v` INT AUTO_INCREMENT
	           , `w` INT
	           , `x` INT
	           , PRIMARY KEY(`v`)
	           , FOREIGN KEY(`x`)
	               REFERENCES `R6`(`x`)
	           );

DROP USER IF EXISTS 'student'@'localhost';
CREATE USER IF NOT EXISTS 'student'@'localhost' IDENTIFIED BY 'stud3nt';
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON `assignment2`.* TO 'student'@'localhost';
SHOW GRANTS FOR 'student'@'localhost';
