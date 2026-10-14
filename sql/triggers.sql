CREATE DEFINER=`root`@`localhost` TRIGGER `after_insert_on_transactions` 
AFTER INSERT ON `transactions` 
FOR EACH ROW 
UPDATE total_balance
SET Balance = Balance + (new.Amount_)
WHERE descr = "description"

CREATE DEFINER=`root`@`localhost` TRIGGER `after_incinsrt_ontrans` 
AFTER INSERT ON `transactions` 
FOR EACH ROW 
UPDATE total_income
SET amount = amount + NEW.Amount_
WHERE descr = "income" AND NEW.Type_ = "Income"

CREATE DEFINER=`root`@`localhost` TRIGGER `after_expinsrt_ontrans` 
AFTER INSERT ON `transactions` 
FOR EACH ROW 
UPDATE total_expense
SET amount = amount + ( NEW.Amount_)
WHERE descr = "expense" AND NEW.Type_ = "Expense"