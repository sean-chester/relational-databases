-- Retrieve in descending order of labour force size
-- all counties that had unemployment rates over 10%
-- in the 2008 census.
-- Hint: Unemployment rate = unemployment / labour force
-- 1.1 marks: <9 operators
-- 1.0 marks: <10 operators
-- 1.0 marks: <15 operators
-- 0.8 marks: correct answer

SELECT `name`, `abbr`, `labour_force`, 100 * `unemployed` / `labour_force` AS `Unemployment Rate`
FROM `counties`.`CountyLabourStats`
  JOIN `counties`.`County`
    ON (`county` = `fips`)
  JOIN `counties`.`State`
    ON (`state` = `id`)
WHERE `year` = 2008
  AND `unemployed` / `labour_force` > .1
ORDER BY `labour_force` DESC;
