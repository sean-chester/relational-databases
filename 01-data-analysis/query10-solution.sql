-- Retrieve for each state the average payroll
-- in the "mining" sector (total vs number of counties),
-- ordered by that average payroll
-- Hint: you may need the COALESCE function
-- 1.02 marks: <15 operators
-- 1.00 marks: <18 operators
-- 0.80 marks: correct answer


SELECT `State`.`abbr`, COALESCE(CAST( `StateMining` / `NumCounties` AS SIGNED), 0) AS `AvgPayroll`
FROM `State`
  LEFT OUTER JOIN (
    SELECT `County`.`state`, SUM(`payroll`) AS `StateMining`
    FROM `County`
      JOIN `CountyIndustries`
        ON (`CountyIndustries`.`county` = `County`.`fips`)
      JOIN `Industry`
        ON (`Industry`.`id` = `CountyIndustries`.`industry`)
    WHERE `Industry`.`name` LIKE '%mining%'
    GROUP BY `County`.`state`) AS `CountyMining`
    ON (`CountyMining`.`state` = `State`.`id`)
  LEFT OUTER JOIN (
    SELECT `County`.`state`, COUNT(*) AS `NumCounties`
    FROM `County`
      JOIN `State`
        ON (`County`.`state` = `State`.`id`)
    GROUP BY `County`.`state`) As `CountyCounts`
    ON (`CountyCounts`.`state` = `State`.`id`)
ORDER BY `AvgPayroll` DESC;
