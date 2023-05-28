-- Retrieve the state with the median number of
-- employees in 'Education Services'
-- 1.1 marks: < 10 operators
-- 1.0 marks: < 11 operators
-- 0.8 marks: correct answer

SELECT `counties`.`State`.`abbr`, SUM(`employees`) AS `TotalEmployees`
FROM `counties`.`County`
  JOIN `counties`.`CountyIndustries`
    ON (`fips` = `county`)
  JOIN `counties`.`Industry`
    ON (`industry` = `id`)
  JOIN `counties`.`State`
    ON (`state` = `counties`.`State`.`id`)
WHERE `counties`.`Industry`.`name` = 'Educational services'
GROUP BY `state`
ORDER BY sum(`employees`) DESC
LIMIT 25,1;
