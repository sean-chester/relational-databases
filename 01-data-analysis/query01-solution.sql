-- Retrieve the name of all counties, ordered alphabetically,
-- that had a six-figure average income and voted Republican in 2020
-- 1.1 marks: < 8 operators
-- 1.0 marks: < 9 operators
-- 0.8 marks: correct answer

SELECT `county`.`name`
FROM `county`
  JOIN `ElectionResult`
    ON (`county`.`fips` = `ElectionResult`.`county`)
WHERE `ElectionResult`.`year` = 2020
  AND `county`.`avg_income` >= 100000
  AND `county`.`avg_income` < 1000000
  AND `gop` > `dem`
ORDER BY `county`.`name`;
