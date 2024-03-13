# Description
유저별로 지정된 Bucket의 광고들만 할당하는 경우와 (User Bucketing)
요청별로 랜덤한 Bucket의 광고들을 할당하는 경우 (Request Bucketing) 의 impression, click, unique imp, click을 비교해주는 시뮬레이션입니다.

# Constants
NUMBER_OF_GROUPS = 3
NUMBER_OF_PEOPLE_IN_GROUP = 100
IMPRESSION_MAX_PER_GROUP = 1000
CPU = 2

# Results
```
User Bucketing
--------------------------------------------------
Group   Imp     Click   Unique Imp      Unique Click
0       1000    170     100             91
1       1000    169     100             90
2       1000    169     100             90
--------------------------------------------------
Total   3000    508     300             271


Request Bucketing
--------------------------------------------------
Group   Imp     Click   Unique Imp      Unique Click
0       1000    365     289             224
1       1000    342     290             216
2       1000    360     286             222
--------------------------------------------------
Total   3000    1067    865             662
```
