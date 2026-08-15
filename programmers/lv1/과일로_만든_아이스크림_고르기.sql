select ii.FLAVER
from FIRST_HARF fh
join ICECREAM_INFO ii on fh.FLAVER = ii.FLAVER
where fh.TOTAL_ORDER > 3000 AND
ii.INGREDIENT_TYPE = 'fruit_based'
ORDER by fh.TOTAL_ORDER desc;