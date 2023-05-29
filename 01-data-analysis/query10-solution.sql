-- Retrieve alphabetically the name of all industries
-- for which there no more than 2000 counties with data
-- 1.1 marks: <6 operators
-- 1.0 marks: <8 operators
-- 0.8 marks: correct answer

SELECT `Industry`.`name` AS `Industry`
FROM `CountyIndustries`
  JOIN `Industry`
    ON (`Industry`.`id` = `CountyIndustries`.`industry`)
GROUP BY `Industry`.`id`
HAVING COUNT(*) <= 2000
ORDER BY `Industry`.`name`;
