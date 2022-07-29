-- Out of those counties with at least 25000 residents,
-- retrieve the pair that had the absolute closest
-- population in 2018
-- 1.1 marks: <11 operators
-- 1.0 marks: <12 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer

SELECT `county1`.`name`, `pop1`.`population`, `county2`.`name`, `pop2`.`population`
FROM `counties`.`CountyPopulation` AS `pop1`
  JOIN `counties`.`County` AS `county1` 
    ON (`pop1`.`county` = `county1`.`fips`)
  JOIN `counties`.`County` AS `county2`
    ON (`county1`.`state` = `county2`.`state`)
  JOIN `counties`.`CountyPopulation` AS `pop2`
    ON (`county2`.`fips` = `pop2`.`county`)
WHERE `pop1`.`year` = 2018
  AND `pop1`.`year` = `pop2`.`year`
  AND `pop1`.`population` >=25000
  AND `pop2`.`population` >= `pop1`.`population`
  AND `pop1`.`county` <> `pop2`.`county`
ORDER BY `pop2`.`population` - `pop1`.`population` ASC
LIMIT 1;
