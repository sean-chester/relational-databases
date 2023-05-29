-- Retrieve the total payrolls for all counties that had a population of
-- less than 500 in 2011. Ensure you don't miss any counties.
-- Order the results by descending total payrolls.
-- Hint: you may find the COALESCE function useful.
-- 1.1 marks: <7 operators
-- 1.0 marks: <8 operators
-- 0.9 marks: <11 operators
-- 0.8 marks: correct answer

SELECT `County`.`name` AS `County`, COALESCE(SUM(`payroll`), 0) AS `Total Payroll`
FROM `CountyPopulation`
  JOIN `County`
    ON (`County`.`fips` = `CountyPopulation`.`county`)
  LEFT OUTER JOIN `CountyIndustries`
    ON (`County`.`fips` = `CountyIndustries`.`county`)
WHERE `year` = 2011
  AND `population` < 500
GROUP BY `County`.`fips`
ORDER BY `Total Payroll` DESC;
