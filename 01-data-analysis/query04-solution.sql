-- Retrieve alphabetically all states in which
-- every county has a name not found anywhere else
-- in the US
-- 1.1 marks: <8 operators
-- 1.0 marks: <9 operators
-- 0.8 marks: correct answer

SELECT `abbr`
FROM `counties`.`State`
WHERE `id` NOT IN (
    SELECT `l`.`state`
    FROM `counties`.`County` AS `l`
      JOIN `counties`.`County` AS `r`
        ON (`l`.`name` = `r`.`name`)
    WHERE `l`.`fips` <> `r`.`fips` )
ORDER BY `abbr`;
