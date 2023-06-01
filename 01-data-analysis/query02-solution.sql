-- Order by total payroll all states
-- that have fewer than 50 counties with payroll data
-- and at least ten industries of payroll data
-- 1.02 marks: <11 operators
-- 1.00 marks: <12 operators
-- 0.90 marks: <14 operators
-- 0.80 marks: correct answer


SELECT `State`.`abbr`, SUM(`County Payroll`) AS `State Payroll`
FROM `State`
  NATURAL JOIN
    (SELECT `County`.`state` AS `id`, `County`.`fips` AS `county`, SUM(`payroll`) AS `County Payroll`
     FROM `CountyIndustries`
       JOIN `County`
         ON (`County`.`fips` = `CountyIndustries`.`county`)
     GROUP BY `County`.`fips`
     HAVING COUNT(*) >= 10) AS `CountyLevelData`
GROUP BY `State`.`id`
HAVING COUNT(*) < 50
ORDER BY `State Payroll` DESC;
