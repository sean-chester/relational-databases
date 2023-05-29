-- Retrieve the name of all counties, ordered alphabetically,
-- whose male population is less than its annual precipitation in cm
-- 1.1 marks: <5 operators
-- 1.0 marks: <6 operators
-- 0.8 marks: correct answer


SELECT `county`.`name`, CAST(`precip` * 2.54 AS UNSIGNED) AS `precip_cm`, `population` AS `male_pop`
FROM `County`
  JOIN `GenderBreakdown`
    ON (`County`.`fips` = `GenderBreakdown`.`county`)
WHERE `County`.`precip` * 2.54 > `GenderBreakdown`.`population`
  AND `gender` = 'male'
ORDER BY `county`.`name`;
