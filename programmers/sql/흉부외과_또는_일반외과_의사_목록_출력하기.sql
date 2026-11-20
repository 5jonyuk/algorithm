select 
    DR_NAME,
    DR_ID,
    MCDP_CD,
    HIRE_YMD
from DOCTOR
WHERE MCDP_CD == CS || MCDP_CD == GS
ORDER BY HIRE_YMD desc, DR_NAME asc;