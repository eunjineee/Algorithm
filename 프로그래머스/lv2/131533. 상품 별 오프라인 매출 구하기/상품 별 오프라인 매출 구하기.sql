-- 코드를 입력하세요
SELECT PRODUCT_CODE, SUM(PRICE * SALES_AMOUNT) AS SALES
# SELECT *
FROM PRODUCT JOIN OFFLINE_SALE
ON PRODUCT.PRODUCT_ID = OFFLINE_SALE.PRODUCT_ID
GROUP BY PRODUCT.PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE;
# ORDER BY PRODUCT_CODE;