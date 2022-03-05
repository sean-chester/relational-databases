# CSC 370 - SQL Golf

## Assignment Goals

In this assignment you will:

  * demonstrate data analysis skills with SQL

    + write SQL queries with increasing complexity to extract desired information from a relational database
    + optimise SQL queries towards simplicity

## Task

[Code Golf](https://www.barrymichaeldoyle.com/code-golf/) is a sort of recreational programming activity in which one tries to implement functionality using as few characters as possible. The general goal is to think of alternative solutions to a problem and it derives its name from the sport of _golf_, in which one tries to minimise the number of whacks with an iron shaft to put a tiny ball in a far-flung hole. In this assignment, you will try not just to write SQL queries that are correct, but that also are "minimal." 

As an example, imagine that you have two relations: *Employee(<ins>employee_id</ins>, employee_name, dept_id)* and *Department(<ins>dept_id</ins>, dept_name)* and you would like to find the names of all employees in a department named "Shipping & Receiving". A simple solution would be:

```sql
SELECT `employee_name`
FROM `Employee`
    NATURAL JOIN `Department`
WHERE `dept_name` LIKE 'Shipping \& Receiving';
```

Certainly, another "correct" solution would be:

```sql
SELECT `employee_name`
FROM `Employee`
WHERE `dept_id` IN (
    SELECT `dept_id`
    FROM `Department`
    WHERE `dept_name` LIKE 'Shipping \& Receiving' );
```

Both queries retrieve the same result, but the second query is unnecessarily complex, or at the very least non-idiomatic. I hope that you prefer the first solution. Even if not, this assignment is designed to encourage you to write the first query by rewarding you inversely to the number of times any of the following tokens appears in your SQL query:

  * SELECT (i.e., projection operator)
  * FROM (i.e., the table- or index-scan operator)
  * , (i.e., the cross product operator)
  * JOIN (i.e., a theta-, natural, or outer join or per MySQL an intersection)
  * UNION (i.e., the bag union operator)
  * DISTINCT (i.e., the duplicate elimination operator)
  * GROUP (i.e., the group-by operator)
  * ORDER (i.e., the sort operator)
  * HAVING (i.e., the selection operator applied to groups)
  * WHERE (i.e., the selection operator applied to tuples)
  * LIMIT (i.e., the MySQL top-k operator)

This gives us a metric by which to claim the first query is better: it only uses 4 instances of the above set of operators (SELECT, FROM, JOIN, and WHERE), whereas the second query uses 6 instances (2×SELECT, 2×FROM, 2×WHERE). This is the metric that you should aim to minimise with the SQL queries that you submit. You would receive more marks for the first query than the second one.

It is important to remember that this is an exercise in code simplification and creative thinking, not in performance optimisation. Although you are trying to minimise the number of operator references, SQL is a _declarative language_ and there is no specific reason to assume that the first example query will run faster than the second one. However, simple and idiomatic code is easier for compilers to optimise, so there could be tangential performance benefits to striving for simpler—or at least shorter—queries.
_The real intent here is to leverage an assumed correlation between this "golf score" metric and the quality of a SQL query to encourage you to write better SQL_.

You are given instructions to create (optionally) a MySQL database. Moreover, you are given twenty `.sql` files that are unfortunately empty except for a comment indicating their intended query and their mapping between "SQL Golf" scores (i.e., total instances of the aforementioned operators/tokens) and grade. For example, the above problem would be represented by the following `example.sql` file:

```sql
-- Find the names of all employees in a department named "Shipping & Receiving"
-- 1.1 marks: <4 operators
-- 1.0 marks: <6 operators
-- 0.8 marks: correct answer

-- Replace this comment line with the actual query
```

Alongside the `.sql` file will be a `.tsv` file showing the expected result, which you can use for testing.


## Submission

You should submit all of the `.sql` files without renaming them, but after replacing the final comment line with an actual SQL query that achieves the stated objective. Ordinarily, you should submit twenty `.sql` files, though it is okay to submit fewer files if you do not have a solution for all twenty tests.

## Evaluation

Your grade on the assignment will be the sum of your scores on each query, scaled up by a factor of 20/14. This could be in excess of 20 (i.e., full marks), particularly if you minimise your queries more effectively than the teaching team has. However, to receive any marks on a particular query, you *must* produce the correct result, including attribute names. We will ascertain this by performing a `diff` between the corresponding `.tsv` file and your query results on an up-to-date MySQL instance prior to counting operators.

Above, the first query would score 1.0 marks and the second query would score 0.8 marks. If you can answer the query with fewer operator instances than the first query, you would score 1.1 marks. The following query would obtain 0.0 marks, even though the number of operators is small, because it does not produce the same result (namely, it doesn't filter by department):

```sql
SELECT `employee_name`
FROM `Employee`;
```

_Note that we have manipulated our testing dataset to avoid hard-coded solutions. You should not make assumptions (e.g., of uniqueness or non-nulls) that are not supported by the data model in the CREATE TABLE statements above_.

## Dataset

For this assignment, we will use [the data dump from one of the Stack Exchanges](https://archive.org/download/stackexchange): fittingly, the one for _Code Golf_. If you want to run the queries before submitting them, you should follow the instrutions below to create a local database.

First, download and extract the entire data dump from here: https://archive.org/download/stackexchange/codegolf.stackexchange.com.7z. 

To [load the XML data into a MySQL database](https://dev.mysql.com/doc/refman/8.0/en/load-xml.html), you first need to create a database with the same structure. Open an instance of MySQL and execute the following DDL queries:

```sql
-- Create and switch to a new database for this project
DROP DATABASE IF EXISTS `code_golf`;
CREATE DATABASE `code_golf`;
USE `code_golf`;

-- Construct tables into which the data will be imported
-- You may want to keep the order of these tables because of FK references
CREATE TABLE `User`( `Id` INT
                   , `Reputation` INT NOT NULL DEFAULT 100
                   , `CreationDate` DATETIME NOT NULL
                   , `DisplayName` VARCHAR(60) NOT NULL DEFAULT 'Foo'
                   , `LastAccessDate` DATETIME NOT NULL
                   , `WebsiteUrl` VARCHAR(255) 
                   , `Location` VARCHAR(120)
                   , `AboutMe` TEXT
                   , `Views` INT NOT NULL DEFAULT 0
                   , `Upvotes` INT 
                   , `Downvotes` INT
                   , `AccountId` INT
                   , PRIMARY KEY( `Id` ) );

CREATE TABLE `Badge`( `Id` INT
                     , `UserId` INT NOT NULL
                     , `Name` VARCHAR(30) NOT NULL
                     , `Date` DATETIME NOT NULL
                     , `Class` SMALLINT NOT NULL
                     , `TagBased` ENUM('True', 'False') NOT NULL
                     , PRIMARY KEY( `Id` )
                     , FOREIGN KEY( `UserId` ) REFERENCES `User`( `Id` ) );

CREATE TABLE `Tag`( `Id` INT
                  , `TagName` VARCHAR(30) NOT NULL
                  , `Count` INT NOT NULL
                  , `ExcerptPostId` INT NOT NULL
                  , `WikiPostId` INT NOT NULL
                  , PRIMARY KEY( `Id` ) );

CREATE TABLE `Post`( `Id` INT
                   , `PostTypeId` INT NOT NULL
                   , `ParentId` INT
                   , `CreationDate` DATETIME NOT NULL
                   , `Score` INT NOT NULL DEFAULT 0
                   , `Body` LONGTEXT
                   , `OwnerUserId` INT 
                   , `LastEditorUserId` INT
                   , `LastEditDate` DATETIME
                   , `LastActivityDate` DATETIME NOT NULL
                   , `CommentCount` INT NOT NULL DEFAULT 0
                   , `ContentLicense` VARCHAR(30) NOT NULL DEFAULT 'CC BY-SA 2.5'
                   , PRIMARY KEY( `Id` )
                   , FOREIGN KEY( `ParentId` ) REFERENCES `Post`( `Id` )
                   , FOREIGN KEY( `OwnerUserId` ) REFERENCES `User`( `Id` )
                   , FOREIGN KEY( `LastEditorUserId` ) REFERENCES `User`( `Id` ) );

CREATE TABLE `Link`( `Id` INT
                   , `PostId` INT NOT NULL
                   , `RelatedPostId` INT NOT NULL
                   , `CreationDate` DATETIME NOT NULL
                   , `LinkTypeId` INT NOT NULL
                   , PRIMARY KEY( `Id` )
--                   , FOREIGN KEY( `PostId` ) REFERENCES `Post`( `Id` )         -- violated by actual data
--                   , FOREIGN KEY( `RelatedPostId` ) REFERENCES `Post`( `Id` )  -- violated by actual data
                   );

CREATE TABLE `Vote`( `Id` INT
                   , `PostId` INT NOT NULL
                   , `VoteTypeId` INT NOT NULL
                   , `CreationDate` DATETIME NOT NULL
                   , PRIMARY KEY( `Id` )
--                   , FOREIGN KEY( `PostId` ) REFERENCES `Post`( `Id` ) -- violated by actual data
                   ); 

CREATE TABLE `Comment`( `Id` INT
                      , `PostId` INT NOT NULL
                      , `Score` INT NOT NULL DEFAULT 0
                      , `Text` TEXT NOT NULL
                      , `CreationDate` DATETIME NOT NULL
                      , `UserId` INT 
                      , `ContentLicense` VARCHAR(30) NOT NULL DEFAULT 'CC BY-SA 2.5'
                      , PRIMARY KEY( `Id` )
                      , FOREIGN KEY( `PostId` ) REFERENCES `Post`( `Id` )
                      , FOREIGN KEY( `UserId` ) REFERENCES `User`( `Id` ) );

```

Finally, you can load all the XML files directly into the database by executing the following statements:

```sql
USE `code_golf`;

-- You will likely find it easiest to move the files to the following directory
-- and change '/var/lib/mysql-files/' in the paths below to the result of this
-- SHOW VARIABLES query.
-- https://stackoverflow.com/q/32737478/2769271
SHOW VARIABLES LIKE "secure_file_priv";

-- Finally, load data into each of the tables
-- Again, ensure that you maintain this order
-- for the sake of referential integrity
LOAD XML INFILE '/var/lib/mysql-files/Users.xml'
INTO TABLE `User`
ROWS IDENTIFIED BY '<row>';

LOAD XML INFILE '/var/lib/mysql-files/Badges.xml'
INTO TABLE `Badge`
ROWS IDENTIFIED BY '<row>';

LOAD XML INFILE '/var/lib/mysql-files/Tags.xml'
INTO TABLE `Tag`
ROWS IDENTIFIED BY '<row>';

LOAD XML INFILE '/var/lib/mysql-files/Posts.xml'
INTO TABLE `Post`
ROWS IDENTIFIED BY '<row>';

LOAD XML INFILE '/var/lib/mysql-files/Votes.xml'
INTO TABLE `Vote`
ROWS IDENTIFIED BY '<row>';

LOAD XML INFILE '/var/lib/mysql-files/Comments.xml'
INTO TABLE `Comment`
ROWS IDENTIFIED BY '<row>';

LOAD XML INFILE '/var/lib/mysql-files/PostLinks.xml'
INTO TABLE `Link`
ROWS IDENTIFIED BY '<row>';

```

## Queries

The queries are available in two locations:

  * You can access them on [the public-facing GitHub repo](https://github.com/sean-chester/relational-databases) for this course's assignments. The advantages to this source are that it is the freshest (first place updates are pushed) and that you can directly check out the code with `git`, which might be an easier toolchain
  * You can access them by downloading the compressed tarball (that will soon be) attached to this assignment description and unpack it locally.

Remember to edit and upload the `.sql` files and to use the `.tsv` files to check the correctness of your solutions.


## Sources

You are permitted to use sources that you find on the Internet, so long as it is clear that the source existed prior to the creation of this assignment and you provide a citation in your source code. For example, GitHub and StackOverflow content is permitted, so long as they are clearly dated prior to the beginning of this semester. If you do not include a citation in your source code, your work will be considered plagiarism.

You should, however, work through the assignment on your own. You are welcome to prepare for the assignment with peers in the class by working through the ungraded worksheets together.

## Illness Policy

The end date for the assignment is three days later than the due date. This is expected to provide sufficient contingency for most minor illnesses and you should submit by the due date rather than the end date if you are not constrained by illness. Submissions will not be accepted even a couple minutes after the end of the illness buffer period (visible as the _end date_ of the assignment in Brightspace).

Support for the assignment _will not be provided_ during the illness buffer. You are encouraged to ask questions early.

In the event that three days contingency is insufficient, you could contact the instructor in advance of the due date with a brief explanation. If you have submitted all previous, graded assignments, then your quiz for this module will be used as the assessment for these learning outcomes. If, on the other hand, you have a missing assignment due to, for example, prior illness this semester, then a well-justified second absence longer than three days we be accommodated with a make-up assessment in the form of an individual, closed, recorded oral exam over Zoom conducted by the instructor. The use of make-up assessments will help to ensure that there are sufficiently many assessment activities (at least 80% of the grade) for each student to accurately reflect their achievement in this course.

You are encouraged to submit your preliminary progress one week and again three days prior to the assignment deadline to document progress in case of illness. These preliminary submissions can, of course, be overwritten by your final submission.

## Summary

I hope that this assignment is a fun way to learn and/or practice the SQL query language. Good luck!
