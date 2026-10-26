SELECT * FROM mydb.ship 
	WHERE 
		(1 OR header_title = '1Катер') 
		AND (1 OR header_title LIKE '%судно%' OR description LIKE '%судно%') 
        AND (1 OR ship_type_id = 2) 
        AND (1 OR weight_class_id = 1);