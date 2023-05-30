-- Retrieve the five states
-- that had the largest (relative) increase in
-- votes for the democrat party from 2016 to 2020
-- 1.02 marks: <8 operators
-- 1.00 marks: <10 operators
-- 0.80 marks: correct answer

SELECT `State`.`abbr` AS `State`, (SUM(`2020Result`.`dem`) - SUM(`2016Result`.`dem`)) / SUM(`2016Result`.`dem`) AS `VoteChange`
FROM `State`
  JOIN `County`
    ON (`State`.`id` = `County`.`state`)
  JOIN `ElectionResult` AS `2020Result`
    ON (`2020Result`.`county` = `county`.`fips`
    AND `2020Result`.`year` = 2020)
  JOIN `ElectionResult` AS `2016Result`
    ON (`2016Result`.`county` = `county`.`fips`
    AND `2016Result`.`year` = 2016)
GROUP BY `State`.`id`
ORDER BY `VoteChange` DESC
LIMIT 5;
