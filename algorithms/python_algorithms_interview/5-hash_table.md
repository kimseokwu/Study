# 해시 테이블

- 해시테이블 또는 해시맵은 키를 값에 매핑할 수 있는 구조인, 연관 배열 추상 자료형을 구현하는 자료구조다.
- 해시 테이블의 가장 큰 특징은 대부분의 연산이 분할 상환 분석에 따른 시간 복잡도가 O(1)이라는 점이다. 덕분에 데이터 양과 관계없이 빠른 성능을 기대할 수 있다는 장점이 있다.



__해시__

- 해시 함수란 임의 크기 데이터를 고정 크기 값으로 매핑하는 데 사용할 수 있는 함수를 말한다.
- 해시 테이블을 인덱싱하기 위해 이처럼 해시 함수를 사용하는 것을 해싱이라 하며, 해싱은 정보를 가능한 빠르게 저장하고 검색하기 위해 사용하는 중요한 기법 중 하나다. 최적의 검색이 필요한 분야에 사용된다.



__로드 팩터__

- 로드팩터란 해시 테이블에 저장된 데이터 개수 n을 버킷의 개수 k로 나눈 것이다.
- 일반적으로 로드 팩터가 증가할 수록 해시 테이블의 성능은 점점 감소하게 된다.



### 보석과 돌

- J는 보석이며 S는 갖고 있는 돌이다. S에는 보석이 몇개나 있을까? 대소문자는 구분한다.

> __예제__
>
> - 입력: J = 'aA', S = 'aAAbbbb'
> - 출력: 3



__풀이 1. 해시 테이블을 이용한 풀이__

- 이 문제는 갖고 있는 돌 S의 각각의 개수를 모두 헤아린다음, J의 각 요소를 키로 하는 각 개수를 합산하면 풀이할 수 있다. 따라서 해시 테이블로 풀이할 수 있는 전형적인 문제이다.

```python
def solution(J, S):
    freqs = collections.Counter(S)
    count = 0
    
    for char in J:
        count += freqs[char]
    
    return count
```





__풀이 2. 파이썬다운 방식__

- 해시 테이블과는 관련이 없지만, 이 문제는 파이썬 다운 방식으로 단 한줄로 계산할 수 있다.

```python
def solution(J, S):
    return sum(s in J for s in S)
```



### 중복 문자 없는 가장 긴 부분 문자열

- 중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라.

> __예제__
>
> - 입력: 'abcabcbb'
> - 출력: 3 (정답은 abc로 길이는 3이다.)



__풀이 1. 슬라이딩 윈도우와 투 포인터로 사이즈 조절__

- 슬라이딩 윈도우로 한 칸씩 우측으로 이동하면서 윈도우 내에 모든 문자가 중복이 없도록 투 포인터로 윈도우 사이즈를 조절하면서 풀이한다.
- 포인터 두개 모두 왼족에서 출발한다. 각각 왼쪽 시작점에서 출발해 두 번째 포인터는 계속 오른쪽으로 확장한다.
- 여기서 만약 이미 등장한 문자라면 used에 있을 것이고 이 경우 첫 번째 포인터인 start를 used[char] + 1 위치로 갱신한다.
- 처음 보는 문자인 경우 매번 max()로 부분 문자열의 길이를 확인하면서 더 큰 값인 경우 갱신한다.

```python
def solution(s):
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        # 이미 등장했던 문자라면 start 위치 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1
        else: # 최대 부분 문자열 길이 갱신
            max_length = max(max_length, index - start + 1)
            
        # 현재 문자의 위치 삽입
        used[char] = index
        
    return max_length
```



### 상위 k 빈도 요소

- 상위 k번 이상 등장하는 요소를 추출하라

> __예제__
>
> - 입력: nums = [1, 1, 1, 2, 2, 3], k = 2
> - 출력: [1, 2]



__풀이 1. Counter를 이용한 음수 순 추출__

- 요소의 값을 키로 하는 해시 테이블을 만들고 여기에 빈도수를 저장한 다음, 우선순위 큐를 이용해 상위 k번만큼 추출하면 k번 이상 등장하는 요소를 손쉽게 추출할 수 있다.
- heap에 삽입하는 방법은 두가지가 있는데, 첫째는 일반적인 파이썬의 리스트에 모두 삽입한 다음 마지막에 heapify()를 하는 방식과 매번 heappush()를 하는 방식이다.

```python
def solution(nums, k):
    freqs = collections.Counter(nums)
    freqs_heap = []
    # 힙에 음수로 삽입
    for f in freqs:
        heapq.heappush(freqs_heap, (-freq[f], f))
    
    topk = list()
    # k번 만큼 추출, 최소 힙이므로 가장 작은 음수 순으로 추출
    
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
        
    return topk
```



__풀이 2. 파이썬다운 방식__

- Counter에는 most_common()이라는 빈도 수가 높은 순서대로 아이템을 추출하는 기능을 제공한다.
- 여기서는 파이썬의 2가지 기능인 zip()과 *를 더 활용해본다.



```python
def solution(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]
```



