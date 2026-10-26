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
  `id` INT AUTO_INCREMENT NOT NULL,
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
    ON DELETE cascade
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ship_weight_class1`
    FOREIGN KEY (`weight_class_id`)
    REFERENCES `mydb`.`weight_class` (`id`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`user` ;

CREATE TABLE IF NOT EXISTS `mydb`.`user` (
  `id` INT AUTO_INCREMENT NOT NULL,
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
  `id` INT AUTO_INCREMENT NOT NULL,
  `date` DATETIME NULL,
  `user_id` INT NOT NULL,
  `payed` BIT NULL,
  `completed` BIT NULL,
  PRIMARY KEY (`id`, `user_id`),
  INDEX `fk_order_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mydb`.`user` (`id`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`order_has_ship`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`order_has_ship` ;

CREATE TABLE IF NOT EXISTS `mydb`.`order_has_ship` (
  `order_id` INT AUTO_INCREMENT NOT NULL,
  `ship_id` INT NOT NULL,
  `order_start` DATETIME NULL,
  `order_end` DATETIME NULL,
  PRIMARY KEY (`order_id`, `ship_id`),
  INDEX `fk_order_has_ship_ship1_idx` (`ship_id` ASC) VISIBLE,
  INDEX `fk_order_has_ship_order1_idx` (`order_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_has_ship_order1`
    FOREIGN KEY (`order_id`)
    REFERENCES `mydb`.`order` (`id`)
    ON DELETE cascade
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_has_ship_ship1`
    FOREIGN KEY (`ship_id`)
    REFERENCES `mydb`.`ship` (`id`)
    ON DELETE cascade
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



-- ------------------------------------------------
--              Inserting data here
-- ------------------------------------------------

INSERT INTO `mydb`.`user` 
	(`id`, `login`, `password`, `gmail`)
VALUES
	(1, 'Pablo', 'Pablo123', 'pablo@gmail.com'),
    (2, 'Marta', 'pass', 'martavarh@gmail.com'),
    (3, 'Andrij', '228', 'andrij@gmail.com')
;
    
    
INSERT INTO `mydb`.`ship_type`
	(`id`, `name`, `color`)
VALUES
	(1, 'Пасажирський', 'var(--bs-teal)'),
	(2, 'Транспортний', 'var(--bs-yellow)'),
	(3, 'Рибальський', 'var(--bs-primary)')
;
    
    
INSERT INTO `mydb`.`weight_class`
	(`id`, `name`, `color`)
VALUES
	(1, 'Легкий', 'var(--bs-teal)'),
	(2, 'Середній', 'var(--bs-warning)'),
	(3, 'Тяжкий', 'var(--bs-danger)')
;


INSERT INTO `mydb`.`ship`
    (`id`, `header_title`, `passengers`, `weight`, `description`, `price_hour`, `price_day`, `image_src`, `ship_type_id`, `weight_class_id`)
VALUES
    (1, '1Катер', 10, 52, 'Сучасний швидкісний катер для комфортних екскурсій, прибережних прогулянок та пасажирських перевезень невеликих груп.', 40, 400, './img/катер.jpg', 1, 2),
    (2, '2Контейнеровоз', 20, 1000, 'Потужне великотоннажне вантажне судно, призначене для масштабних морських перевезень стандартних контейнерів і важких вантажів.', 8000, 80000, './img/контейнеровоз.webp', 2, 3),
    (3, '3Рибальський човен', 5, 6, 'Надійне промислове судно з необхідним оснащенням для морської риболовлі, тралення та роботи у прибережних водах.', 10, 100, './img/рибальський човен.jpg', 3, 1)
;


INSERT INTO `mydb`.`order`
    (`id`, `date`, `user_id`, `payed`, `completed`)
VALUES
    (1, '2026-06-01 10:00:00', 1, 1, 1),
    (2, '2026-06-05 14:30:00', 2, 1, 0),
    (3, '2026-06-10 09:15:00', 3, 0, 0)
;


INSERT INTO `mydb`.`order_has_ship`
    (`order_id`, `ship_id`, `order_start`, `order_end`)
VALUES
    (1, 1, '2026-06-01 11:00:00', '2026-06-01 15:00:00'),
    (1, 3, '2026-06-02 08:00:00', '2026-06-02 14:00:00'),
    
    (2, 2, '2026-06-06 08:00:00', '2026-06-08 08:00:00'),
    (2, 1, '2026-06-07 10:00:00', '2026-06-07 18:00:00'),
    
    (3, 3, '2026-06-11 06:00:00', '2026-06-11 18:00:00')
;
