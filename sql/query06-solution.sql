-- Retrieve by increasing snowfall the number of employees
-- in 'Mining, quarrying, and oil and gas extraction' for all
-- counties that have the words 'iron', 'ore', or 'mineral'
-- in their name.
-- 1.1 marks: <13 operators
-- 1.0 marks: <15 operators
-- 0.9 marks: <20 operators
-- 0.8 marks: correct answer

SELECT `name`, `abbr`, `employees`
FROM `counties`.`County`
  JOIN `counties`.`State`
    ON (`state` = `id`)
  LEFT OUTER JOIN (
  	  SELECT `county`, `employees`
  	  FROM `counties`.`CountyIndustries`
  	    JOIN `counties`.`Industry`
  	      ON (`industry` = `id`)
  	    WHERE `name` = 'Mining, quarrying, and oil and gas extraction') AS `unnamed`
    ON (`fips` = `county`)
WHERE `name` LIKE '%iron%'
   OR `name` LIKE '%coal%'
   OR `name` LIKE '%mineral%'
ORDER BY `snow`;
