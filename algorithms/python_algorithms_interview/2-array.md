# 배열

- 배열은 값 또는 변수 엘리먼트의 집합으로 구성된 구조로, 하나 이상의 인덱스 또는 키로 식별된다.

자료구조는 크게 메모리 공간 기반의 연속 방식과 포인터 기반의 연결 방식으로 나뉜다. 배열은 연속방식의 가장 기본이 되는 자료형이다. 연결 방식의 가장 기본이 되는 자료형은 연결 리스트다. 추상자료형(abstract data type)의 실제 구현 대부분은 배열 또는 연결리스트를 기반으로 한다. 스택은 연결리스트로 구현하고 큐는 배열로 구현한다.

배열은 어느 위치에나 O(1)에 조회가 가능하다는 장점이 있다. 그러나 배열은 고정된 크기 만큼의 연속된 메모리 할당이므로 너무 작은 영역을 할당하여 모자라거나 너무 많은 영역을 할당해서 낭비가 될 때도 있다. 이러한 고민을 해결하고자 크기를 지정하지 않고 자동으로 리사이징하는 배열인 동적 배열이 등장했다. 파이썬에선 리스트가 바로 동적 배열 자료형이다.

동적 배열의 원리는 미리 초깃값을 작게 잡아 배열을 생성하고, 데이터가 추가되면서 꽉 채워지면 늘려주고 모두 복사하는 식이다. 대개는 더블링이라 하며 2배씩 늘려주게 된다.

동적 배열은 정적 배열과 달리 크기를 지정할 필요가 없어 매우 편리하게 활용할 수 있으며 조회 또한 기존의 배열과 동일하게 O(1)에 가능하다 그러나 더블링이 필요할 만큼 공간이 차게 되면 기존 데이터를 복사하는 작업이 필요하므로 O(n) 비용이 발생한다.



### 두수의 합

- 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

> __예제__
>
> - 입력: nums = [2, 7, 11, 5], target = 9
> - 출력: [0, 1]



__풀이 1.  브루트 포스로 계산__

- 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식인 브루트 포스를 이용한다.
- 이 경우 시간복잡도는 O(n^2)이다.

```python
def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```



__풀이 2. in을 이용한 탐색__

- target - n이 존재하는지 탐색하는 문제로 변경해보자.
- in의 시간복잡도는 O(n)이고 따라서 전체 시간복잡도는 이전과 동일하지만 in 연산이 더 가볍고 빠르다.

```python
def solution(nums, target):
    for i, n in enumerate(nums):
        if target - n in nums[i + 1:]:
            returm [nums.index(n), nums[i+1:].index(target - n) + (i + 1)]
```



__풀이 3. 첫번째 수를 뺀 결과 키 조회__

```python
def solution(nums, target):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
        
    # 타겟에서 첫번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - n in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - n]]
```

- 딕셔너리는 조회가 평균적으로 O(1)에 가능하다. 전체 시간복잡도는 O(n)이 된다



### 빗물 트래핑

- 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

> __예제__
>
> - 입력: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
> - 출력: 6



__풀이 1. 투 포인터를 최대로 이동__

- 투 포인터나 스택을 이용하면 O(n)으로 풀이가 가능하다.
- 가장 높은 막대를 살펴본다. 높고 낮음과 무관하게 전체 부피에 영향을 끼치지않으면서 그저 왼쪽과 오른쪽을 가르는 장벽 역할을 한다.
- 최대 높이의 막대까지 각각 좌우 기둥 최대 높이 left_max, right_max가 현재 높이와의 차이만큼 물 높이 volume을 더해 나간다.
- 낮은 쪽은 그만큼 항상 채워질 것이기 때문에 좌우 어느쪽이든 낮은 쪽은 높은 쪽을 향해서 포인터가 가운데로 점점 이동한다. 오른쪽이 크다면 left += 1로 이동하고 왼쪽이 크다면 right -= 1로 오른쪽이 이동한다. 이렇게 하면 가장 높이가 높은 막대, 즉 최대 지점에서 좌우 포인터가 만나게 되며 O(n)에 풀이가 가능하다.

```python
def solution(height):
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        
        # 더 높은 쪽을 향해 투포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    
    return volume
```



__풀이 2. 스택 쌓기__

- 높이를 스택에 쌓아가면서 현재 높이가 이전 높이보다 높을 때, 즉 꺾이는 부분 변곡점을 기준으로 격차만큼 물 높이 volume을 채운다. 이전 높이는 고정된 형태가 아니라 들쑥날쑥하기 때문에 계속 스택으로 채워나가다가 변곡점을 만날 때마다 스택에서 하나씩 꺼내면서 이전과 차이만큼 물 높이를 채워 나간다.

```python
def solution(height):
    stack = []
    volume = 0
    
    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다.
            top = stack.pop()
            
            if not len(stack):
                break
        
            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume
```





__세 수의 합__

- 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

> __예제__
>
> - 입력: nums = [-1, 0, 1, 2, -1, -4]
> - 출력: [[-1, 0, 1], [-1, -1, 2]]



__풀이 1. 투 포인터로 합 계산__

- i를 축으로 하고 중복된 값이 나오면 건너뛴다. i의 다음 지점과 마지막 지점을 left, right로 설정하고 간격을 좁혀가면서 sum을 계산한다. sum이 0보다 작다면 값을 키워야하므로 left를 우측으로 이동하고 0보다 크다면 값을 줄여야하므로 right를 좌측으로 이동한다.
- sum = 0이면 정답이므로 결과를 result에 저장한다. 추가한 다음은 left, right 양 옆으로 동일한 값이 있을 수 있으므로 left += 1, right -= 1을 반복해서 스킵 처리한다. 마지막으로 left를 한 칸 우측으로 right를 한 칸 왼쪽으로 더 이동하고 다음으로 넘긴다.

```python
def solution(nums):
    result = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0인 경우이므로 정답 및 스킵 처리
                result.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    
    return result
```



### 배열 파티션 1

- n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

> __예제__
>
> - 입력: [1, 4, 3, 2]
> - 출력: 4



__풀이 1. 오름차순 풀이__

- 페어의 min을 합산했을 때 최대를 만드는 것은 결국 min()이 되도록 커야한다는 뜻이고 뒤에서부터 내림차수능로 집어 넣으면 항상 min()  페어를 유지할 수 있다. 이 문제에서 배열 입력값은 항상 2n개일 것이므로 앞에서부터 오름차순으로 집어 넣어도 결과는 똑같을 것이다.

```python
def solution(nums):
    sum = 0
    pair = []
    nums.sort()
    
    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
            
    return sum
```



__풀이 2. 짝수번째 값 계산__

- 일일히 페어에 대해 값을 구하지 않아도 짝수 번째 값을 더하면 될 것 같다. 정렬된 상태에서는 짝수 번째 항상 작은 값이 위치하기 때문이다.

```python
def solution(nums):
    return sum(sorted(nums)[::2])
```





### 자신을 제외한 배열의 곱

- 배열을 입력받아 output[i]가 자신을 제외한 나머지 요소의 곱셈 결과가 되도록 출력하라. 나눗셈을 하지 않고 O(n)에 풀이하라.

> __예제__
>
> - 입력: [1, 2, 3, 4]
> - 출력: [24, 12, 8, 6]

__풀이 1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈__

- 자기 자신을 제외하고 왼쪽의 곱셈 결과와 오른쪽의 곱셈 결과를 곱해야한다.
- 왼쪽부터 곱해서 result에 추가한다. 곱셈 결과는 그대로 out 리스트 변수에 담기게 되며, 마지막 값 곰셈으 ㄹ제외하여 결과는 [1, 1, 2, 6]이 된다.
- 그 후 왼쪽 곱셈 결과에 오른쪽 마지막 값부터 차례대로 곱해 나간다.

```python
def solution(nums):
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = p * out[i]
        p = p * nums[i]
        
    return out
```



### 주식을 사고 팔기 가장 좋은 시점

- 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

> __예제__
>
> - 입력: [7, 1, 5, 3, 6, 4]
> - 출력: 5



__풀이 1. 저점과 현재 값과의 차이 계산__

- 포인터가 우측으로 이동하면서 이전 상태의 저점을 기준으로 가격 차이를 계산하고 만약 클 경우 최댓값을 계속 교체해나가는 형태로 O(n) 풀이가 가능하다.

- 최솟값 변수는 시스템의 최솟값으로 지정한다. 어떤 값이 들어오든 바로 교체될 수 있기 때문이다.

- 이 문제는 최대 서브 배열 문제와도 유사하다. 그 문제는 카데인 알고리즘이라는 방법으로 O(n)에 풀이가 가능하다. 마찬가지로 여기서도 카데인 알고리즘을 응용해 O(n)으로 풀이하였다.

  

```python
def solution(prices):
    profit = 0
    min_price = sys.maxsize
    
    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
        
    return profit
```

