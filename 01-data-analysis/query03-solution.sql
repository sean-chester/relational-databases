-- Retrieve the names of all counties, ordered by id,
-- that had either less than USD $1M of total payroll in "Real Estate"
-- or no data on that industry altogether.
-- 1.1 marks: <9 operators
-- 1.0 marks: <11 operators
-- 0.8 marks: correct answer

SELECT `County`.`name`, `County`.`fips`
FROM `County`
WHERE `county`.`fips` NOT IN
  (SELECT `county`
   FROM `CountyIndustries`
     JOIN `Industry`
       ON (`Industry`.`id` = `CountyIndustries`.`industry`)
   WHERE `industry`.`name` LIKE '%real estate%'
     AND `payroll` >= 1000000)
ORDER BY `county`.`fips`;
