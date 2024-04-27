-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER ##
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN userId INT)
BEGIN
    DECLARE total_weight INT;
    SELECT SUM(weight) INTO total_weight FROM projects;

    UPDATE users
    SET average_score = (
        SELECT (SUM(corrections.score * projects.weight) / total_weight)
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = userId
    )
    WHERE users.id = userId;
END ##
DELIMITER ;

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER ##
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE user_cursor CURSOR FOR 
        SELECT id FROM users;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN user_cursor;
    user_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

        CALL ComputeAverageWeightedScoreForUser(user_id);
    END LOOP;

    -- Close cursor
    CLOSE user_cursor;
END ##
DELIMITER ;
