-- Retrieve alphabetically by name
-- all counties that have the first four letters of
-- their name in common
-- (Ensure that there are no duplicate pairs.)
-- 1.1 marks: <4 operators
-- 1.0 marks: <5 operators
-- 0.8 marks: correct answer

SELECT `C1`.`name`, `C2`.`name`
FROM `County` AS `C1`
  JOIN `County` AS `C2`
    ON (LEFT(`C1`.`name`, 4) = LEFT(`C2`.`name`, 4)
      AND `C1`.`fips` < `C2`.`fips`)
ORDER BY `C1`.`name`, `C2`.`name`;
