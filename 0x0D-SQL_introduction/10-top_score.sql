-- script to select entries by score and name
-- highest score should be on top

SELECT score, name FROM second_table
	ORDER BY score DESC;
