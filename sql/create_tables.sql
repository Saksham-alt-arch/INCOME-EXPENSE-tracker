CREATE TABLE `transactions` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Date_` date DEFAULT NULL,
  `Description_` varchar(100) DEFAULT NULL,
  `Type_` varchar(15) DEFAULT NULL,
  `Amount_` decimal(7,2) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `total_balance` (
  `descr` varchar(30) DEFAULT NULL,
  `Balance` decimal(12,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `total_income` (
  `descr` varchar(25) DEFAULT NULL,
  `amount` decimal(15,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `total_expense` (
  `descr` varchar(25) DEFAULT NULL,
  `amount` decimal(20,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `total_everything` (
  `Month_` varchar(25) DEFAULT NULL,
  `Balance` decimal(25,2) DEFAULT NULL,
  `Income` decimal(25,2) DEFAULT NULL,
  `Expense` decimal(25,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

