-- Show which county has the largest relative population decrease
-- from 2010 to 2019.
-- 1.1 marks: <11 operators
-- 1.0 marks: <13 operators
-- 0.9 marks: <16 operators
-- 0.8 marks: correct answer

SELECT `name`
     , pop1.population AS `2010`
     , pop2.population AS `2019`
     , `abbr`, 100 * (`pop1`.`population` - `pop2`.`population`) / `pop1`.`population` AS `Loss (%)`
FROM `counties`.`CountyPopulation` AS `pop1`
  JOIN `counties`.`CountyPopulation` AS `pop2`
    ON (`pop1`.`county` = `pop2`.`county`)
  JOIN `counties`.`County`
    ON (`pop1`.`county` = `fips`)
  JOIN `counties`.`State`
    ON (`state` = `id`)
WHERE `pop1`.`year` = 2010
  AND `pop2`.`year` = 2019
ORDER BY `Loss (%)` DESC
LIMIT 1;
