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
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8mb3 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`account_status`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`account_status` ;

CREATE TABLE IF NOT EXISTS `mydb`.`account_status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`account_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`account_type` ;

CREATE TABLE IF NOT EXISTS `mydb`.`account_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`account`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`account` ;

CREATE TABLE IF NOT EXISTS `mydb`.`account` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `account_type_id` INT NOT NULL,
  `account_status_id` INT NOT NULL,
  `number` VARCHAR(45) NOT NULL,
  `credentials` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `balance` INT NOT NULL,
  `creditscore` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_account_account_type1_idx` (`account_type_id` ASC) VISIBLE,
  INDEX `fk_account_account_status1_idx` (`account_status_id` ASC) VISIBLE,
  CONSTRAINT `fk_account_account_status1`
    FOREIGN KEY (`account_status_id`)
    REFERENCES `mydb`.`account_status` (`id`),
  CONSTRAINT `fk_account_account_type1`
    FOREIGN KEY (`account_type_id`)
    REFERENCES `mydb`.`account_type` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`account_access_status`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`account_access_status` ;

CREATE TABLE IF NOT EXISTS `mydb`.`account_access_status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`card_status`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`card_status` ;

CREATE TABLE IF NOT EXISTS `mydb`.`card_status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`card_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`card_type` ;

CREATE TABLE IF NOT EXISTS `mydb`.`card_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`card_pattern`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`card_pattern` ;

CREATE TABLE IF NOT EXISTS `mydb`.`card_pattern` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `pattern_path` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`card`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`card` ;

CREATE TABLE IF NOT EXISTS `mydb`.`card` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `account_id` INT NOT NULL,
  `card_type_id` INT NOT NULL,
  `card_status_id` INT NOT NULL,
  `card_pattern_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `creation_date` DATETIME NOT NULL,
  `number` VARCHAR(20) NOT NULL,
  `cvv` VARCHAR(5) NOT NULL,
  `pin` VARCHAR(5) NOT NULL,
  `secret_word` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_card_card_type1_idx` (`card_type_id` ASC) VISIBLE,
  INDEX `fk_card_card_status1_idx` (`card_status_id` ASC) VISIBLE,
  INDEX `fk_card_account1_idx` (`account_id` ASC) VISIBLE,
  INDEX `account_id_Index` (`account_id` ASC) INVISIBLE,
  INDEX `number_Index` (`number` ASC) VISIBLE,
  CONSTRAINT `fk_card_account1`
    FOREIGN KEY (`account_id`)
    REFERENCES `mydb`.`account` (`id`),
  CONSTRAINT `fk_card_card_status1`
    FOREIGN KEY (`card_status_id`)
    REFERENCES `mydb`.`card_status` (`id`),
  CONSTRAINT `fk_card_card_type1`
    FOREIGN KEY (`card_type_id`)
    REFERENCES `mydb`.`card_type` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`client`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`client` ;

CREATE TABLE IF NOT EXISTS `mydb`.`client` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `middlename` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(15) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `rnokpp` VARCHAR(45) NOT NULL,
  `fop` VARCHAR(45) NOT NULL,
  `photolink` VARCHAR(200) NOT NULL,
  `date_registered` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `phone_Index` (`phone` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`client_account`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`client_account` ;

CREATE TABLE IF NOT EXISTS `mydb`.`client_account` (
  `account_id` INT NOT NULL,
  `client_id` INT NOT NULL,
  `account_access_status_id` INT NOT NULL,
  PRIMARY KEY (`account_id`, `client_id`),
  INDEX `fk_account_has_client_client1_idx` (`client_id` ASC) VISIBLE,
  INDEX `fk_account_has_client_account1_idx` (`account_id` ASC) VISIBLE,
  INDEX `fk_client_account_account_access_status1_idx` (`account_access_status_id` ASC) VISIBLE,
  CONSTRAINT `fk_account_has_client_account1`
    FOREIGN KEY (`account_id`)
    REFERENCES `mydb`.`account` (`id`),
  CONSTRAINT `fk_account_has_client_client1`
    FOREIGN KEY (`client_id`)
    REFERENCES `mydb`.`client` (`id`),
  CONSTRAINT `fk_client_account_account_access_status1`
    FOREIGN KEY (`account_access_status_id`)
    REFERENCES `mydb`.`account_access_status` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`client_secret_data`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`client_secret_data` ;

CREATE TABLE IF NOT EXISTS `mydb`.`client_secret_data` (
  `client_id` INT NOT NULL,
  `residence` VARCHAR(100) NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  `is_on_fraud_watch` BIT(1) NOT NULL,
  `war_veteran` BIT(1) NOT NULL,
  PRIMARY KEY (`client_id`),
  INDEX `fk_client_secret_data_client1_idx` (`client_id` ASC) VISIBLE,
  CONSTRAINT `fk_client_secret_data_client1`
    FOREIGN KEY (`client_id`)
    REFERENCES `mydb`.`client` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `mydb`.`transaction`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`transaction` ;

CREATE TABLE IF NOT EXISTS `mydb`.`transaction` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `account_id` INT NOT NULL,
  `reciever_account_id` INT NOT NULL,
  `datetime` DATETIME NOT NULL,
  `amount` INT NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_transaction_account1_idx` (`account_id` ASC) INVISIBLE,
  INDEX `datetime_Index` (`datetime` DESC) INVISIBLE,
  INDEX `reciever_Index` (`reciever_account_id` ASC) INVISIBLE,
  INDEX `sender_Index` (`account_id` ASC) VISIBLE,
  CONSTRAINT `fk_transaction_account1`
    FOREIGN KEY (`account_id`)
    

    REFERENCES `mydb`.`account` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;






-- ------------------------------------------------
--              Inserting data here
-- ------------------------------------------------

INSERT INTO `mydb`.`client` 
  (`id`, `name`, `surname`, `middlename`, `phone`, `email`, `rnokpp`, `fop`, `photolink`, `date_registered`) 
VALUES
  (1, 'Petro', 'Marik', 'Bobrov', '0671234567', 'bober@gmail.com', '0984562368', '782152689', 'photo/folder/1.png', '2018-02-14 14:22:01'),
  (2, 'Oksana', 'Shevchenko', 'Ivanivna', '0671234567', 'o.shevchenko@gmail.com', '3124567890', '432156789', 'photo/folder/2.png', '2018-05-14 10:20:00'),
  (3, 'Taras', 'Bondarenko', 'Mykolayovych', '0509876543', 't.bond@ukr.net', '2987654321', '876543210', 'photo/folder/3.png', '2019-11-23 14:45:30'),
  (4, 'Yulia', 'Kovalchuk', 'Vasylivna', '0935554433', 'kovalchuk.y@meta.ua', '3256987410', '192837465', 'photo/folder/4.png', '2020-02-01 09:15:00'),
  (5, 'Andrii', 'Tkachenko', 'Olehovych', '0684443322', 'a.tkach@gmail.com', '3045678912', '564738291', 'photo/folder/5.png', '2020-08-19 16:30:12'),
  (6, 'Iryna', 'Melnyk', 'Serhiivna', '0972221100', 'iryna.melnyk@outlook.com', '2891234567', '918273645', 'photo/folder/6.png', '2021-03-10 11:05:45'),
  (7, 'Dmytro', 'Kravchenko', 'Volodymyrovych', '0663339988', 'dkravch@gmail.com', '3312345678', '827364519', 'photo/folder/7.png', '2021-07-25 18:22:00'),
  (8, 'Nataliia', 'Boyko', 'Yuriyivna', '0738887766', 'nat.boyko@ukr.net', '3156789123', '374658291', 'photo/folder/8.png', '2022-01-15 13:40:50'),
  (9, 'Maksym', 'Rudenko', 'Andriyovych', '0951112233', 'm.rudenko@gmail.com', '3423456789', '647382910', 'photo/folder/9.png', '2022-09-04 15:10:00'),
  (10, 'Olena', 'Moroz', 'Pavlivna', '0969990011', 'olena.moroz@meta.ua', '2789123456', '519283746', 'photo/folder/10.png', '2023-04-18 08:55:20'),
  (11, 'Serhii', 'Lytvyn', 'Borysovych', '0634447788', 's.lytvyn@gmail.com', '3567891234', '283746519', 'photo/folder/11.png', '2023-10-30 17:00:15');
  
INSERT INTO `mydb`.`client_secret_data` 
  (`client_id`, `residence`, `description`, `is_on_fraud_watch`, `war_veteran`)
VALUES
  (1, 'Kyiv, Khreshchatyk St, 15, apt. 12', 'VIP corporate client, high priority support requested.', b'0', b'0'),
  (2, 'Lviv, Horodotska St, 44, apt. 8', 'Requires signed paper receipts for accounting.', b'0', b'0'),
  (3, 'Odesa, Deribasivska St, 10, apt. 3', 'Frequent international wire transfers, requires identity verification.', b'0', b'0'),
  (4, 'Dnipro, Dmytra Yavornytskoho Ave, 78, apt. 45', 'Suspicious activity reported on multiple accounts in early 2021.', b'1', b'0'),
  (5, 'Kharkiv, Sumska St, 25, apt. 19', 'Discounts applied for IT-consulting services.', b'0', b'0'),
  (6, 'Zaporizhzhia, Sobornyi Ave, 112, apt. 5', 'Veteran benefits verified and active.', b'0', b'1'),
  (7, 'Vinnytsia, Soborna St, 33, apt. 14', 'Flagged for multiple chargeback disputes in 2022.', b'1', b'0'),
  (8, 'Poltava, Sobornosti St, 50, apt. 22', 'Standard contract, prompt monthly payments.', b'0', b'0'),
  (9, 'Chernihiv, Myru Ave, 61, apt. 7', 'Combat veteran, priority public service discount applied.', b'0', b'1'),
  (10, 'Ivano-Frankivsk, Nezalezhnosti St, 18, apt. 2', 'Corporate cardholder, no issues detected.', b'0', b'0'),
  (11, 'Lutsk, Voli Ave, 9, apt. 31', 'Secondary contact point for regional logistics team.', b'0', b'0');
  
INSERT INTO `mydb`.`account_access_status` (`id`, `name`)
VALUES
  (1, 'Active'),
  (2, 'Suspended'),
  (3, 'Blocked'),
  (4, 'Pending Verification'),
  (5, 'Closed');
  

-- -----------------------------------------------------
-- 1. Dictionary / Lookup Tables
-- -----------------------------------------------------

INSERT INTO `mydb`.`account_type` (`id`, `name`) VALUES
  (1, 'Checking'),
  (2, 'Savings'),
  (3, 'Business / FOP'),
  (4, 'Credit Line'),
  (5, 'Deposit');

INSERT INTO `mydb`.`account_status` (`id`, `name`) VALUES
  (1, 'Active'),
  (2, 'Frozen'),
  (3, 'Dormant'),
  (4, 'Closed');

INSERT INTO `mydb`.`card_type` (`id`, `name`) VALUES
  (1, 'Debit Visa'),
  (2, 'Debit Mastercard'),
  (3, 'Credit Visa'),
  (4, 'Credit Mastercard'),
  (5, 'Virtual / Internet');

INSERT INTO `mydb`.`card_status` (`id`, `name`) VALUES
  (1, 'Active'),
  (2, 'Temporarily Blocked'),
  (3, 'Permanently Blocked (Lost/Stolen)'),
  (4, 'Expired');

INSERT INTO `mydb`.`card_pattern` (`id`, `name`, `pattern_path`) VALUES
  (1, 'Classic Blue', 'patterns/blue.png'),
  (2, 'Dark Obsidian', 'patterns/dark.png'),
  (3, 'Gold Metallic', 'patterns/gold.png'),
  (4, 'Minimalist White', 'patterns/white.png');

-- -----------------------------------------------------
-- 2. Accounts
-- -----------------------------------------------------

INSERT INTO `mydb`.`account` 
  (`id`, `account_type_id`, `account_status_id`, `number`, `credentials`, `name`, `balance`, `creditscore`) 
VALUES
  (1,  3, 1, 'UA213052990000026001111111111', 'CR-00101', 'Petro FOP Main', 185000, 780),
  (2,  1, 1, 'UA353052990000026202222222222', 'CR-00201', 'Oksana Primary Checking', 42300, 740),
  (3,  1, 1, 'UA483052990000026203333333333', 'CR-00301', 'Taras Everyday Checking', 12850, 690),
  (4,  4, 2, 'UA513052990000026204444444444', 'CR-00401', 'Yulia Overdraft Line', -4500, 520),
  (5,  3, 1, 'UA643052990000026005555555555', 'CR-00501', 'Andrii IT Services', 340000, 810),
  (6,  2, 1, 'UA773052990000026206666666666', 'CR-00601', 'Iryna Reserve Savings', 95000, 760),
  (7,  1, 1, 'UA893052990000026207777777777', 'CR-00701', 'Dmytro Standard Card', 8200, 590),
  (8,  1, 1, 'UA923052990000026208888888888', 'CR-00801', 'Nataliia Daily Expenses', 27400, 715),
  (9,  2, 1, 'UA143052990000026209999999999', 'CR-00901', 'Maksym Savings Vault', 150000, 800),
  (10, 1, 1, 'UA273052990000026201010101010', 'CR-01001', 'Olena Personal Account', 31900, 750),
  (11, 3, 1, 'UA393052990000026001112131415', 'CR-01101', 'Serhii Logistics Settlement', 210000, 730);

-- -----------------------------------------------------
-- 3. Client Account Junction (Many-to-Many Linking)
-- (Maps client_id 1..11 to account_id 1..11, with account 1 shared)
-- -----------------------------------------------------

INSERT INTO `mydb`.`client_account` (`account_id`, `client_id`, `account_access_status_id`) VALUES
  (1,  1,  1), -- Petro: Primary Owner (Active)
  (1,  2,  1), -- Oksana: Authorized Accountant on Petro's FOP
  (2,  2,  1), -- Oksana: Owner
  (3,  3,  1), -- Taras: Owner
  (4,  4,  2), -- Yulia: Suspended Access
  (5,  5,  1), -- Andrii: Owner
  (6,  6,  1), -- Iryna: Owner
  (7,  7,  1), -- Dmytro: Owner
  (8,  8,  1), -- Nataliia: Owner
  (9,  9,  1), -- Maksym: Owner
  (10, 10, 1), -- Olena: Owner
  (11, 11, 1); -- Serhii: Owner

-- -----------------------------------------------------
-- 4. Payment Cards
-- -----------------------------------------------------

INSERT INTO `mydb`.`card` 
  (`id`, `account_id`, `card_type_id`, `card_status_id`, `card_pattern_id`, `name`, `creation_date`, `number`, `cvv`, `pin`, `secret_word`) 
VALUES
  (1,  1,  2, 1, 1, 'Petro Corporate MC',      '2021-01-15 10:00:00', '4149491122334401', '412', '1984', 'Dnipro'),
  (2,  2,  1, 1, 2, 'Oksana Debit Visa',       '2021-03-20 11:30:00', '5168752233445502', '829', '4321', 'Carpathians'),
  (3,  3,  2, 1, 1, 'Taras MC Standard',       '2021-06-12 14:15:00', '4149493344556603', '109', '7744', 'Odesa'),
  (4,  4,  3, 2, 3, 'Yulia Credit Gold',       '2021-08-01 09:00:00', '4149494455667704', '654', '1122', 'Kashtan'),
  (5,  5,  1, 1, 3, 'Andrii Platinum Visa',    '2021-09-18 16:45:00', '5168755566778805', '331', '9081', 'Kharkiv'),
  (6,  6,  5, 1, 4, 'Iryna Virtual Shopping',  '2022-02-10 12:20:00', '4149496677889906', '942', '5566', 'Summer'),
  (7,  7,  2, 3, 1, 'Dmytro Debit (Lost)',     '2022-04-05 15:10:00', '5168757788990007', '215', '3412', 'Horizon'),
  (8,  8,  1, 1, 2, 'Nataliia Everyday Visa',  '2022-07-22 17:35:00', '4149498899001108', '773', '6789', 'Poltava'),
  (9,  9,  4, 1, 3, 'Maksym World Elite MC',   '2022-11-03 13:00:00', '5168759900112209', '480', '2024', 'Desna'),
  (10, 10, 5, 1, 4, 'Olena Digital Pass',      '2023-01-19 18:40:00', '4149490011223310', '167', '8123', 'Hoverla'),
  (11, 11, 2, 1, 2, 'Serhii Business MC',      '2023-05-14 10:25:00', '5168751122334411', '593', '4490', 'Lutsk');


-- -----------------------------------------------------
-- 5. Transactions
-- -----------------------------------------------------

INSERT INTO `mydb`.`transaction` 
  (`id`, `account_id`, `reciever_account_id`, `datetime`, `amount`, `description`) 
VALUES
  (1,  1,   5, '2024-01-10 09:15:00',  85000, 'Incoming client payment for software services invoice #104'),
  (2,  1,   5, '2024-01-15 00:01:00',   -150, 'Monthly corporate banking maintenance fee'),
  (3,  2,   8,  '2024-01-18 14:32:10',  -1240, 'Silpo Supermarket grocery purchase'),
  (4,  3,   2,  '2024-01-20 18:05:44',  -3000, 'ATM cash withdrawal at PrivatBank ATM #4012'),
  (5,  4,   1,  '2024-01-22 11:20:15',  -4500, 'Peer-to-peer mobile transfer to card 4149****1122'),
  (6,  5,   3,  '2024-02-01 10:00:00', 120000, 'Upwork incoming wire transfer USD/UAH conversion'),
  (7,  6,   9,  '2024-02-05 16:45:00',  25000, 'Internal funds transfer from external bank deposit'),
  (8,  7,   4,  '2024-02-08 20:11:33',   -890, 'WOG gas station fuel payment'),
  (9,  8,   7,  '2024-02-14 19:25:00',  -2150, 'Epicentr shopping mall purchase'),
  (10, 9,  11,  '2024-02-20 13:10:00',  50000, 'Transfer received from Rudenko M. consulting contract'),
  (11, 10, 11, '2024-02-24 15:40:22',   -450, 'Apotheka purchases'),
  (12, 11, 10, '2024-02-28 17:05:00', -18000, 'Supplier settlement payment for spare truck parts');



DELIMITER //


DROP TRIGGER IF EXISTS `check_card_pattern_exists_before_insert`//
DROP TRIGGER IF EXISTS `check_card_pattern_exists_before_update`//


CREATE TRIGGER `check_card_pattern_exists_before_insert`
BEFORE INSERT ON `mydb`.`card`
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM `mydb`.`card_pattern` WHERE `id` = NEW.card_pattern_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: this card pattern does not exist';
    END IF;
END//


CREATE TRIGGER `check_card_pattern_exists_before_update`
BEFORE UPDATE ON `mydb`.`card`
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM `mydb`.`card_pattern` WHERE `id` = NEW.card_pattern_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: this card pattern does not exist';
    END IF;
END//


DROP PROCEDURE IF EXISTS `sp_insert_account`//

CREATE PROCEDURE `sp_insert_account` (
    IN p_account_type_id INT,
    IN p_account_status_id INT,
    IN p_number VARCHAR(45),
    IN p_credentials VARCHAR(45),
    IN p_name VARCHAR(45),
    IN p_balance INT,
    IN p_creditscore INT,
    OUT p_new_id INT
)
BEGIN
    INSERT INTO `account` (
        `account_type_id`, 
        `account_status_id`, 
        `number`, 
        `credentials`, 
        `name`, 
        `balance`, 
        `creditscore`
    ) 
    VALUES (
        p_account_type_id, 
        p_account_status_id, 
        p_number, 
        p_credentials, 
        p_name, 
        p_balance, 
        p_creditscore
    );
    
    SET p_new_id = LAST_INSERT_ID();
END//


DELIMITER ;


