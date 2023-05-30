-- Retrieve the name of all counties, ordered alphabetically, in Texas
-- that have seen at least 2.5% population growth every year on record
-- 1.02 marks: <9 operators
-- 1.00 marks: <12 operators
-- 0.80 marks: correct answer

SELECT `County`.`name` AS `County`
FROM `County`
  JOIN `State`
    ON (`State`.`id` = `County`.`state`)
  JOIN `CountyPopulation` AS `Year1`
    ON (`County`.`fips` = `Year1`.`county`)
  JOIN `CountyPopulation` AS `Year2`
    ON (`County`.`fips` = `Year2`.`county`
    AND `Year1`.`year` + 1 = `Year2`.`year`)
WHERE `State`.`abbr` = 'TX'
GROUP BY `County`.`fips`
HAVING MIN((`Year2`.`population` - `Year1`.`population`) / `Year1`.`population` >= 0.025)
ORDER BY `county`.`name`;
