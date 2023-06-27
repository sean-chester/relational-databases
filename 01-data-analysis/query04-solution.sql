-- Consider the industry with the most employees
-- nationwide. Retrieve alphabetically all counties
-- that have fewer than 10 employees in that industry
-- (ignoring those with no data on it).
-- 1.02 marks: <10 operators
-- 1.00 marks: <12 operators
-- 0.80 marks: correct answer


SELECT `County`.`name` AS `County`
FROM `County`
  JOIN `CountyIndustries`
    ON (`County`.`fips` = `CountyIndustries`.`county`)
WHERE `industry` = (
  SELECT `industry`
  FROM `CountyIndustries`
  GROUP BY `industry`
  ORDER BY SUM(`employees`) DESC
  LIMIT 1)
  AND `employees` < 10
ORDER BY `County`.`name`;
