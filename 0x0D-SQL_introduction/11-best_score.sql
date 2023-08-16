-- script that selects the scores >= 10
-- results are ordered by score (top first)
SELECT score, name FROM second_table
	WHERE 	score >= 10
	ORDER BY score DESC
