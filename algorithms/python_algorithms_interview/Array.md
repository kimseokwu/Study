- 배열은 값 또는 변수 엘리먼트의 집합으로 구성된 구조로, 하나 이상의 인덱스 또는 키로 식별된다.
- 자료구조는 크게 메모리 공간 기반의 연속 방식과 포인터 기반의 연결 방식으로 나뉜다.
- 배열은 연속 방식의 가장 기본이 되는 자료형이다.
- 메모리의 크기를 지정하지 않고 자동으로 리사이징하는 배열을 동적 배열이라고 한다.
- 파이썬에서는 리스트가 동적 배열이다. 정적 배열은 따로 제공하지 않는다.

- 동적 배열의 원리는 미리 초깃값을 작게 잡아 배열을 생성하고, 데이터가 꽉 채워지면 늘려주고 모두 복사하는 방식이다.

# 두수의 합
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

입력: nums = [2, 7, 11, 15], target = 9
출력 : [0, 1]

## <풀이 1> 브루트 포스로 계산

- 브루트 포스는 배열을 두번 반복하면서 모든 조합을 더해서 일일히 확인해보는 방식이다.

```python
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
    return [i, j]
```

## <풀이 2> in을 이용한 탐색

```python
def twoSum(nums, target):
    for i, n in enumerate(nums):
        complement = target - n
            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)]
```

- in 연산의 시간 복잡도는 O(n)이기 때문에 전체 시간복잡도는 브루트 포스와 동일한 O(n^2)이지만 in 연산은 파이썬의 내부 함수로 구현되었기 때문에 훨씬 빨리 실행된다.


## <풀이 3> 첫번째 수를 뺀 결과 키 조회

```python
def twoSums(nums, target):
    nums_map = {}
    #키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    #타겟에서 첫번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in num_map and i != num_map[target - num]:
            return [i, num_map[target - num]]
```

- 두번째 수를 인덱스로 하고 인덱스는 값으로 바꿔서 딕셔너리로 저장해두면, 나중에 두번째 수를 키로 조회해서 정답을 즉시 찾아낼 수 있을 것이다.

## <풀이 4> 조회 구조 개선

```python
def twoSum(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i 
        if target-num in nums_map:
            return [nums_map[target - num], i]
```

- 딕셔너리 저장과 조회를 두개의 for문에서 하나의 for문으로 합쳐서 처리했다.

# 빗물 트래핑
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라

입력 : [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
출력 : 6

## <풀이 1> 투 포인터 활용
- 가장 높이가 높은 막대를 왼쪽과 오른쪽을 가르는 장벽으로 사용한다.

```python
def trap(height):
    if not height:
        return 0
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right += 1
    retrun volume
```

## <풀이 2> 스택 쌓기

- 스택에 쌓아 나가면서 현재 높이가 이전 높이보다 높을 때 변곡점을 기준으로 격차 만큼 물 높이를 채운다.

```python
def trap(height):
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
    volume += distance + waters

    stack.append(i)
    return volume
```

# 세 수의 합
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

입력: nums = [-1, 0, 1, 2, -1, -4]
출력 [[-1, 0, 1], [-1, -1, 2]]

## <풀이 1> 브루트 포스로 계산
- 시간복잡도가 O(n^3)으로 타임아웃

## <풀이 2> 투 포인터로 합 계산

- 리스트를 정렬하고 시작한다.
- i를 축으로 하고 중복된 값을 건너뛰게 한다.
- 합이 0보다 크면 오른쪽 포인터를, 0보다 작으면 왼쪽 포인터를 움직인다.

```python
def threeSum(nums):
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너 뛰기
        if i  > 0 and num[i] == nums[i -1]:
            continue
        # 간격을 좁혀나가며 합 계산
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
```

- 투포인터는 대개 시작접과 끝점 또는 왼쪽 포인터와 오른쪽 포인터 두 지점을 기준으로 하는 문제 풀이 전략이다.
- 일반적으로 배열이 정렬되어 있을 때 좀 더 유용하다.

# 배열 파티션

n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라
입력 : [1, 4, 3, 2]
출력 : 4

설명 : n은 2가 되며 최대 합은 4이다.
min(1, 2) + min(3, 4) = 4

## <풀이 1> 오름차순 풀이
- 앞에서부터 오름차순으로 페어를 집어 넣으면 항상 최대값을 유지할 수 있다.

```python
def arrayPairSum(nums):
sum = 0
pair = []
nums.sort()

for n in nums:
pair.append(n)
if len(pair) == 2:
sum += min(pair}
pair = []

return sum
```

## <풀이 2> 짝수 번째 값 계산

- 리스트 변수를 생략할 수 있도록 짝수 번째 값을 더한다.

```python
def arrayPairSum(nums):
sum = 0
nums.sort()

for i, n in enumerate(nums);
if i % 2 == 0:
sum += n

return sum
```


## <풀이 3> 파이썬다운 방식
- 슬라이싱을 이용하면 단 한줄로 풀이가 가능하다.

```python
def arrayPairSum(nums):
    return sum(sorted(nums)[::2])
```

# 자신을 제외한 배열의 곱
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라

입력: [1, 2, 3, 4]
출력: [24, 12, 8, 6]
* 주의: 나눗셈을 하지 않고 O(n)에 풀이하라.

## <풀이 1> 왼족 곱셈 결과에 오른쪽 값을 차례대로 곱셈
- 제약사항 때문에 미리 전체 곱셈 값을 구해놓고 각 항목별로 자기 자신을 나눠서 풀이하는 방법은 안된다.
- 자기 자신을 제외하고 왼쪽의 곱셈 결과와 오른쪽의 곱셈 결과를 곱하면 된다.

```python
def productExceptSelf(nums):
out = []
p = 1
# 왼쪽 곱셈
for i in range(0, len(nums)):
out.append(p)
p = p * nums[i]
p = 1
# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
for i in range(len(nums) - 1, 0 - 1, -1):
out[i] = out[i] * p
p = p * nums[i]
return out
```

# 주식을 사고팔기 가장 좋은 시점
한 번의 거래로 낼 수 있는 최대 이익을 산출하라

입력: [7, 1, 5, 3, 6, 4]
출력: 5
설명 : 1일 때 사서 6일 때 팔면 5의 이익을 얻는다.

## <풀이 1> 저점과 현재 값과의 차이 계산

```python
def maxProfit(prices):
import sys
profit = 0
min_price = sys.maxsize

#최솟값과 최댓값을 계속 갱신
for price in prices:
min_price = min(min_price, price)
profit = max(profit, price - min_price)

return profit
```

- sys.maxsize를 이용하면 시스템이 지정할 수 있는 가장 높은 값, 가장 낮은 값을 활용할 수 있다.

```python
mx = -sys.maxsize
mn = sys.maxsize
```

- float()를 사용해 다음과 같이 무한대 값을 지정하는 방법도 있다.

```python
mx = float(‘-inf’)
mn = float(‘inf’)
```