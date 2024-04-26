-- script that creates a trigger that decreases the quantity of an item after adding a new order
-- Quantity in the table items can be negative.

DROP TRIGGER IF EXISTS check_quantity;

DELIMITER ##
CREATE TRIGGER check_quantity
AFTER INSERT on orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END ##
DELIMITER ;
