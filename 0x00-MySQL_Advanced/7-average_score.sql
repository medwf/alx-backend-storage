-- script that creates a stored procedure ComputeAverageScoreForUser
-- store the average score for a student. Note: An average score can be a decimal

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER ##
CREATE PROCEDURE ComputeAverageScoreForUser(IN Id INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections WHERE user_id = Id)
    WHERE users.id = Id;
END ##
DELIMITER ;
