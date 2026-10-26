-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`ship_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`ship_type` ;

CREATE TABLE IF NOT EXISTS `mydb`.`ship_type` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `color` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`weight_class`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`weight_class` ;

CREATE TABLE IF NOT EXISTS `mydb`.`weight_class` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `color` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ship`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`ship` ;

CREATE TABLE IF NOT EXISTS `mydb`.`ship` (
  `id` INT NOT NULL,
  `header_title` VARCHAR(45) NULL,
  `passengers` INT NULL,
  `weight` DOUBLE NULL,
  `description` VARCHAR(500) NULL,
  `price_hour` INT NULL,
  `price_day` INT NULL,
  `image_src` VARCHAR(45) NULL,
  `ship_type_id` INT NOT NULL,
  `weight_class_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ship_ship_type_idx` (`ship_type_id` ASC) VISIBLE,
  INDEX `fk_ship_weight_class1_idx` (`weight_class_id` ASC) VISIBLE,
  CONSTRAINT `fk_ship_ship_type`
    FOREIGN KEY (`ship_type_id`)
    REFERENCES `mydb`.`ship_type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ship_weight_class1`
    FOREIGN KEY (`weight_class_id`)
    REFERENCES `mydb`.`weight_class` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`user` ;

CREATE TABLE IF NOT EXISTS `mydb`.`user` (
  `id` INT NOT NULL,
  `login` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `gmail` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`order`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`order` ;

CREATE TABLE IF NOT EXISTS `mydb`.`order` (
  `id` INT NOT NULL,
  `date` DATETIME NULL,
  `user_id` INT NOT NULL,
  `payed` BIT NULL,
  `completed` BIT NULL,
  PRIMARY KEY (`id`, `user_id`),
  INDEX `fk_order_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`order_has_ship`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`order_has_ship` ;

CREATE TABLE IF NOT EXISTS `mydb`.`order_has_ship` (
  `order_id` INT NOT NULL,
  `ship_id` INT NOT NULL,
  `order_start` DATETIME NULL,
  `order_end` DATETIME NULL,
  PRIMARY KEY (`order_id`, `ship_id`),
  INDEX `fk_order_has_ship_ship1_idx` (`ship_id` ASC) VISIBLE,
  INDEX `fk_order_has_ship_order1_idx` (`order_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_has_ship_order1`
    FOREIGN KEY (`order_id`)
    REFERENCES `mydb`.`order` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_has_ship_ship1`
    FOREIGN KEY (`ship_id`)
    REFERENCES `mydb`.`ship` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
