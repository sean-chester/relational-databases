-- Show which industries in which states (except DC)
-- employed at least 7.5% of the state's 2019 population,
-- ordered by the total payroll for that industry
-- in that state.
-- 1.1 marks: <26 operators
-- 1.0 marks: <30 operators
-- 0.9 marks: <35 operators
-- 0.8 marks: correct answer


SELECT `abbr`
     , `counties`.`Industry`.`name`
     , `Total Payrolls`
     , ( 100 * `Total Employees` / `Total Population` ) AS `% of Population`
FROM (
    SELECT `state`
         , `industry`
         , SUM(`payroll`) AS `Total Payrolls`
         , SUM(`employees`) AS `Total Employees`
    FROM `counties`.`CountyIndustries`
      JOIN `counties`.`County`
        ON (`counties`.`CountyIndustries`.`county` = `fips`)
    GROUP BY `state`, `industry` ) AS `EmpData`
  JOIN (
      SELECT `state`, SUM( `population` ) AS `Total Population`
      FROM `counties`.`County`
        JOIN `counties`.`CountyPopulation`
          ON (`fips` = `counties`.`CountyPopulation`.`county`)
      WHERE `year` = 2019
      GROUP BY `state` ) As `PopData`
    ON (`EmpData`.`state` = `PopData`.`state`)
  JOIN `counties`.`State`
    ON (`EmpData`.`state` = `counties`.`State`.`id`)
  JOIN `counties`.`Industry`
    ON (`industry` = `counties`.`Industry`.`id`)
WHERE `EmpData`.`Total Employees` > .075 * `PopData`.`Total Population`
  AND `abbr` <> 'DC'
GROUP BY `EmpData`.`state`, `EmpData`.`industry`
ORDER BY `Total Payrolls` DESC;
