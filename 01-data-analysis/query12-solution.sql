-- Retrieve alphabetically the names of industries that
-- employ at least five million workers across
-- the US, excluding California.
-- 1.1 marks: <9 operators
-- 1.0 marks: <11 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer

SELECT `counties`.`Industry`.`name`
FROM `counties`.`CountyIndustries`
  JOIN `counties`.`County`
    ON (`fips` = `county`)
  JOIN `counties`.`State`
    ON (`state` = `counties`.`State`.`id`)
  JOIN `counties`.`Industry`
    ON (`industry` = `counties`.`Industry`.`id`)
WHERE `abbr` <> 'CA'
GROUP BY `counties`.`Industry`.`name`
HAVING sum(employees) >= 5000000
ORDER BY `counties`.`Industry`.`name`;
