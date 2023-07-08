-- 코드를 입력하세요
SELECT USER_ID,PRODUCT_ID
from ONLINE_SALE 
Group by USER_ID,PRODUCT_ID
Having count(*) >= 2
order by USER_ID,PRODUCT_ID DESC;