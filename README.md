# Description
다음 두가지 버켓팅 방법에 따른 impression, click, unique imp, click을 비교해주는 시뮬레이션입니다.
- 유저별로 지정된 Bucket의 광고들만 할당하는 경우와 (User Bucketing)
- 요청별로 랜덤한 Bucket의 광고들을 할당하는 경우 (Request Bucketing)
  
# Constants
```
NUMBER_OF_GROUPS = 3
NUMBER_OF_PEOPLE_IN_GROUP = 100
IMPRESSION_MAX_PER_GROUP = 1000
CPU = 2
```

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

# Analysis
## Q1. CTR이 늘어난 이유
- 기존: User Bucketing의 경우 CTR 상위 유저들은 CPU의 제약을 받아 최대 2번까지밖에 클릭을 할 수 있었습니다.
- 현재: Request Bucketing의 경우 이 유저들에게 여러 그룹의 광고들을 할당할 수 있기 때문에 최대 6번까지 클릭을 할 수 있습니다.
- 따라서 CTR이 늘어나게 됩니다.

## Q2. Unique Impression 이 늘어난 이유
- 기존: User Bucketing의 경우 최대 각 그룹에 속하는 유저 수만큼의 Unique Impression을 가질 수 있었습니다.
- 현재: Request Bucketing의 경우 최대 전체 유저 수만큼의 Unique Impression을 가질 수 있습니다.
- 따라서 Unique Impression이 늘어나게 됩니다.
- 동일한 예산으로 타겟팅을 일부만 한 경우와 전체를 한 경우로 치환해서 생각하면 Unique Impression이 늘어나는 이유를 보다 쉽게 이해할 수 있습니다.
  
## Q3. Unique Click이 늘어난 이유
- Q2와 동일한 원리로 설명이 가능합니다. 동일한 예산으로 타겟팅을 일부만 한 경우보다 전체로 바꾼 경우에 Unique Click이 늘어나게 됩니다.

## Q4. 각 유저별로 사용하는 광고비가 늘어났으니 Unique 값은 줄어야 하는 것이 아닌가?
- 실제로 기존보다 더 많은 광고비를 사용하는 유저도 다른 그룹의 Unique 값으로 잡히기 때문에 그렇지 않습니다.
- 예시를 들어보겠습니다.
  - X라는 유저는 기존 User Bucketing에서는 A그룹에 할당되었습니다.
    - 이 유저는 해당 그룹에서 5번 할당 받았고 그 중 2번 클릭을 하였습니다.
    - 이 유저는 A그룹의 Unique Impression과 Click에 각각 1을 기여하게 됩니다.
  - 이번에는 Request Bucketing에서 X 유저를 생각해봅시다.
    - 이 유저는 A, B, C 그룹을 통틀어 10번 할당받았고 그 중 4번 클릭을 하였습니다.
    - 이 유저는 A, B, C 세 그룹에 Unique Impression을 3, Unique CLick을 3만큼 기여하게 됩니다.
  - 따라서 실제 유저가 사용하는 광고비는 늘어났으나(2배) Unique Impression, Click에는 이보다 더 큰 기여(3배)를 하게 됩니다.  
