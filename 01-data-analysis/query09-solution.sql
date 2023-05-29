-- Show all counties ordered by their total
-- number of employees across all industries
-- 1.1 marks: <5 operators
-- 1.0 marks: <6 operators
-- 0.8 marks: correct answer


SELECT `county`.*
FROM `county`
  JOIN `CountyIndustries`
    ON (`county`.`fips` = `CountyIndustries`.`county`)
GROUP BY `county`.`fips`
ORDER BY SUM(`employees`) ASC;
