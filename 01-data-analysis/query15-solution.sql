-- Show the percentage of counties that have more
-- females than males.
-- 1.1 marks: <8 operators
-- 1.0 marks: <10 operators
-- 0.9 marks: <13 operators
-- 0.8 marks: correct answer


SELECT `x` / `y` AS `Fraction`
FROM (
	SELECT COUNT(*) AS `x`
	FROM `counties`.`GenderBreakdown` as `m`
	  JOIN `counties`.`GenderBreakdown` as `f`
	    ON (`m`.`county` = `f`.`county`)
	WHERE `m`.`population` < `f`.`population`
	  AND `m`.`gender` = 'male'
	  AND `f`.`gender` = 'female'
	) AS `Filtered`
  , (
    SELECT COUNT(*) AS `y`
    FROM `counties`.`County`
    ) AS `Total`;
