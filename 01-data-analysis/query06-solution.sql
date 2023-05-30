-- Retrieve alphabetically all pairs of counties (along with their ids)
-- that have the same name but voted for different parties
-- in 2020
-- 1.02 marks: <7 operators
-- 1.00 marks: <8 operators
-- 0.90 marks: <9 operators
-- 0.80 marks: correct answer

SELECT `C1`.`fips`, `C1`.`name`, `C2`.`fips`, `C2`.`name`
FROM `County` AS `C1`
  JOIN `County` AS `C2`
    ON (`C1`.`name` = `C2`.`name`
    AND `C1`.`fips` < `C2`.`fips`)
  JOIN `ElectionResult` AS `E1`
    ON (`E1`.`county` = `C1`.`fips`)
  JOIN `ElectionResult` AS `E2`
    ON (`E2`.`county` = `C2`.`fips`)
WHERE `E1`.`year` = 2020
  AND `E2`.`year` = 2020
  AND (`E1`.`dem` - `E1`.`gop`) * (`E2`.`dem` - `E2`.`gop`) < 1
ORDER BY `C1`.`name`, `C2`.`name`;
