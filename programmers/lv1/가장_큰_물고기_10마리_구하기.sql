-- 코드를 작성해주세요
select ID, LENGTH
from FISH_INFO
order by LENGTH desc, ID asc
limit 10;

-- where 절에서만 and 사용
-- order by절에서는 , 사용