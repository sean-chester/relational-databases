-- Retrieve by life expectancy all
-- counties that have no industry data
-- 1.1 marks: <6 operators
-- 1.0 marks: <8 operators
-- 0.8 marks: correct answer

SELECT *
FROM `counties`.`County`
WHERE `fips` NOT IN (
	SELECT `county`
	FROM `counties`.`CountyIndustries`)
ORDER BY `life_expectancy`;
