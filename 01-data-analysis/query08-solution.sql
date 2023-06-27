-- Retrieve alphabetically the abbreviations of the states
-- in which one can find the ten counties that had the
-- largest (absolute) increase in employed persons
-- between 2008 and 2016.
-- 1.02 marks: <11 operators
-- 1.00 marks: <12 operators
-- 0.90 marks: <14 operators
-- 0.80 marks: correct answer

SELECT DISTINCT `State`.`abbr`
FROM `State`
NATURAL JOIN
  (SELECT `County`.`state` AS `id`
   FROM `CountyLabourStats` AS `2016Stats`
     JOIN `County`
       ON (`County`.`fips` = `2016Stats`.`county`
       AND `2016Stats`.`year` = 2016)
     JOIN `CountyLabourStats` AS `2008Stats`
       ON (`County`.`fips` = `2008Stats`.`county`
       AND `2008Stats`.`year` = 2008)
   ORDER BY `2016Stats`.`employed` - `2008Stats`.`employed` DESC
   LIMIT 10) As `CountyDifferences`
ORDER BY `State`.`abbr`;
