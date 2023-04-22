DROP TRIGGER IF EXISTS payments_after_insert;

DELIMITER $$
CREATE TRIGGER payments_after_insert
	AFTER INSERT ON payments
	FOR EACH ROW
BEGIN
	UPDATE invoices
	SET payment_total = payment_total + NEW.amount
    WHERE invoice_id = NEW.invoice_id;
    
    INSERT
    INTO payments_audit
    VALUES (NEW.client_id , NEW.date , NEW.amount , 'insert' , NOW());
END $$
DELIMITER ;

/*
INSERT INTO payments	-- 测试一下触发器
VALUES (DEFAULT , 5 , 3 , '2019-01-01' , 10 , 1)
;
*/