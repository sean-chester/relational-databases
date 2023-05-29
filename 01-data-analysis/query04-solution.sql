-- Retrieve alphabetically by abbreviation all states in which
-- no county that receives snowfall has a life expectancy over 80
-- (you can assume that every state has at least one county)
-- 1.1 marks: <7 operators
-- 1.0 marks: <8 operators
-- 0.8 marks: correct answer

SELECT `state`.*
FROM `State`
  JOIN `County`
    ON (`County`.`state` = `State`.`id`)
WHERE `snow` > 0
GROUP BY `state`.`id`
HAVING MAX(`life_expectancy`) <= 80
ORDER BY `abbr`;
