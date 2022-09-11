-- Given the Contacts table below, write a SQL statement to get all contacts that have both
-- email and phone values populated
SELECT * from `contacts` 
WHERE `email` <> '' AND `phone` <> '';

-- Given the Users table below, write a SQL statement to get the count of users per groupId
SELECT count(id) as 'count', groupId
FROM `users`
GROUP BY `groupId`;
 
-- Given the Customers and Orders table below, write a SQL statement to get the
-- customerName, orderId and orderDate in a single dataset
SELECT c.customerName, o.orderId, o.orderDate
FROM `customers` c, `orders` o
WHERE c.id = o.customerId;