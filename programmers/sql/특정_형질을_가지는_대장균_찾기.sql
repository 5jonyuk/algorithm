select COUNT(*) as COUNT
from ECOLI_DATA
where
GENOTYPE != 0 AND
GENOTYPE % 8 != 0 AND
(GENOTYPE % 4) NOT IN (2,3);

-- 비트 마스킹
-- select COUNT(*) as COUNT
-- from ECOLI_DATA
-- where
-- GENOTYPE & 2 = 0 AND
-- (GENOTYPE & 1 <> 0 OR GENOTYPE & 4 <> 0)

-- <> 와 != 은 같은 의미이나 sql에서는 <>을 더 많이 씀