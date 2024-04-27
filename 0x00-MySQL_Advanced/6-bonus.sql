-- DOC
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER ##
CREATE PROCEDURE AddBonus(
    IN userId INT,
    IN projectName VARCHAR(255),
    IN Score INT)
BEGIN
    IF (SELECT id FROM projects WHERE name = projectName) IS NULL THEN
        INSERT INTO projects (name) VALUES (projectName);
    END IF;
    INSERT INTO corrections (user_id, project_id, score)  
    VALUES(userId, (SELECT id FROM projects WHERE name = projectName), Score);
END ##
DELIMITER ;
