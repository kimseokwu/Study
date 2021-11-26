# 슬라이딩 윈도우

- 슬라이딩 윈도우란 고정 사이즈의 윈도우가 이동하면서 윈도우 내에 있는 데이터를 이용해 문제를 풀이하는 알고리즘을 말한다.
- 정렬된 배열을 대상으로 하는 투 포인터와 달리 슬라이딩 윈도우는 정렬 여부와 관계 없이 활용된다는 차이가 있다.



### 최대 슬라이딩 윈도우

- 배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 오른쪽 끝까지 이동하면서 최대 슬라이딩 윈도우를 구하라.

> __예제__
>
> - 입력: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
> - 출력: [3, 3, 5, 5, 6, 7]



__풀이 1. 큐를 이용한 최적화__

- 슬라이딩 윈도우에서 최댓값을 추출하려면 어떠한 알고리즘이든 결국 한번 이상은 봐야하기 때문에 O(n)의 시간이 든다.
- 따라서 가급적 최댓값 계산을 최소화하기 위해 이전의 최댓값을 저장해뒀다가 한칸씩 이동할 때 새 값에 대해서만 더 큰 값인지 확인하고 최댓값이 윈도우에서 빠지게 되는 경우만 다시 전체를 계산하는 형태로 개선한다.

```python
def solution(nums, k):
    result = []
    window = collections.deque()
    current_max = float('-inf')
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue
        
        # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v
        
        result.append(current_max)
        
        # 최댓값이 윈도우에서 빠지면 초기화
        if current_max == window.popleft():
            current_max = float('-inf')
    return result
```



### 부분 문자열이 포함된 최소 윈도우

- 문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라

> __예제__
>
> - 입력: S = "ADOBECODEBANC", T = "ABC"
> - 출력: "BANC"



__풀이 1. 투 포인터, 슬라이딩 윈도우로 최적화__

- 우측으로 슬라이딩 윈도우를 이동시키면서 좌우 포인터의 크기를 좁혀 나가는 투 포인터로 풀이할 수 있다.

```python
def solution(s, t):
    need = collections.Counter(s)
    missing = len(t)
    left = start = end = 0
    
    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1
        
        # 필요 문자가 0이면 왼쪽 포인터 이동 판단
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            
            if not end or right - left <= end - start:
                start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]
```



__풀이 2. Counter로 좀 더 편리한 풀이__

- 필요한 문자의 개수를 직접 계산하지 않고 Counter의 기능을 이용해 풀이한다. missing == 0 대신  Counter의 AND 연산으로 비교한다.



```python
def solution(s, t):
    t_count = collections.Counter(t)
    current_count = collections.Counter()
    
    start = float('-inf')
    end = float('inf')
    
    left = 0
    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        current_count[char] += 1
        
        # AND 연산 결과로 왼쪽 포인터 이동 판단
        while current_count & t_count == t_count:
            if right - left < end - start:
                start, end = left, right
            current_count[s[left]] -= 1
            left += 1
            
    return s[start:end] if end - start <= len(s) else ''
```

- 그러나 아쉽게도 이 풀이는 너무 느리게 실행된다. Counter끼리 AND 연산으로 비교하는 과정이 내부적으로 매우 무거운 연산이기 때문이다.



### 가장 긴 반복 문자 대체

- 대문자로 구성된 문자열 s가 주어졌을 때 k번만큼의 변경으로 만들 수 있는, 연속으로 반복된 문자열의 가장 긴 길이를 출력하라.

> __예제__
>
> - 입력: s = "AAABBC", k = 2
> - 출력: 5
> - 설명: B를 A로 각각 2번 변경하면 길이 5인 AAAAA를 만들 수 있다.



__풀이 1. 투 포인터, 슬라이딩 윈도우, Counter를 모두 이용__

- 이 문제는 오른쪽 포인터가 계속 우측으로 이동한다는 점에서 슬라이딩 윈도우 문제이지만 왼쪽 포인터를 계속 좁혀서 범위를 조절해 나간다는 점에서는 투포인터와 결합된 문제이다.
- 오른쪽 포인터에서 왼쪽 포인터 위치를 뺀다음, 윈도우 내 출현 빈도가 가장 높은 문자의 수를 뺀 값이 k와 같을 수 있는 수 중 가장 큰 최댓값이라 정의할 수 있다.

```python
def solution(s, k):
    left = right = 0
    counts = collections.Counter()
    for right in range(1, len(s) + 1):
        counts[s[right - 1]] += 1
        # 가장 흔하게 등장하는 문자 탐색
        max_char_n = counts.most_common(1)[0][1]
        
        # k 초과시 왼쪽 포인터 이동
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    return right - left
```

- 길이의 최댓값을 구하는 과정은 생략할 수 있다. 최댓값이 된 상태에서는 오른쪽 포인터가 한 칸 이동하면 왼쪽 포인터도 따라서 이동하게 되면서 값은 바뀌지 않기 때문이다.