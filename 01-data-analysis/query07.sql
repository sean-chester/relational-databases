-- Retrieve all states who had more counties
-- that voted democratic than the median state did,
-- ordered alphabetically.
-- (You can assume that there are 51 states.)
-- 1.1 marks: <11 operators
-- 1.0 marks: <12 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer


SELECT `State`.`abbr`
FROM `State`
  NATURAL JOIN
    (SELECT `County`.`state` AS `id`
     FROM `County`
       JOIN `ElectionResult`
         ON (`County`.`fips` = `ElectionResult`.`county`)
     WHERE `dem` > `gop`
     GROUP BY `County`.`state`
     ORDER BY COUNT(*) DESC
     LIMIT 25) AS `wrong_order`
ORDER BY `State`.`abbr`;
