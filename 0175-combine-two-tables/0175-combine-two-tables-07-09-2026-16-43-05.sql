-- Write your PostgreSQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state
from Person p
left join Address a
ON p.personId = a.personId

