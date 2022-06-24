-- Show which industries in which states (except DC)
-- employed at least 7.5% of the state's 2019 population,
-- ordered by the total payroll for that industry
-- in that state.
-- 1.1 marks: <13 operators
-- 1.0 marks: <15 operators
-- 0.9 marks: <20 operators
-- 0.8 marks: correct answer


SELECT `abbr`
     , `counties`.`Industry`.`name`
     , SUM(`payroll`) AS `Total Payrolls`
     , ( 100 * SUM(`employees`) / SUM( `population` ) ) AS `% of Population`
FROM `counties`.`CountyIndustries`
  JOIN `counties`.`County`
    ON (`counties`.`CountyIndustries`.`county` = `fips`)
  JOIN `counties`.`State`
    ON (`state` = `counties`.`State`.`id`)
  JOIN `counties`.`Industry`
    ON (`industry` = `counties`.`Industry`.`id`)
  JOIN `counties`.`CountyPopulation`
    ON (`fips` = `counties`.`CountyPopulation`.`county`)
WHERE `year` = 2019
  AND `abbr` <> 'DC'
GROUP BY `state`, `industry`
HAVING SUM(`employees`) > .075 * SUM( `population` ) 
ORDER BY `Total Payrolls` DESC;
