-- Determine which counties have a larger area (in square kilometres)
-- than average income (in USD) and more precipitation (in inches)
-- than the average annual temperature (in Farenheit).
-- 1.1 marks: <3 operators
-- 1.0 marks: <4 operators
-- 0.8 marks: correct answer

SELECT *
FROM `counties`.`County`
WHERE `precip` > `temp`
  AND `sq_km` > `avg_income`;
