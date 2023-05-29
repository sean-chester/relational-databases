-- Retrieve alphabetically the abbreviations of all states in which
-- every county has a (relative) difference between
-- male and female populations strictly within 10%.
-- 1.1 marks: <9 operators
-- 1.0 marks: <11 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer

SELECT `State`.`abbr` AS `State`
FROM `State`
WHERE `id` NOT IN
(SELECT `County`.`state`
FROM `GenderBreakdown` AS `Boys`
  JOIN `GenderBreakdown` AS `Girls`
    ON (`Boys`.`county` = `Girls`.`county`
    AND `Boys`.`gender` = 'male'
    AND `Girls`.`gender` = 'female')
  JOIN `County`
    ON (`Boys`.`county` = `County`.`fips`)
WHERE ABS(`Boys`.`population` - `Girls`.`population`) / (`Boys`.`population` + `Girls`.`population`) >= .1 )
ORDER BY `abbr`;
