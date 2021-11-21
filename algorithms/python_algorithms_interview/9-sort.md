# 정렬

- 정렬 알고리즘은 목록의 요소를 특정 순서대로 넣는 알고리즘이다. 대개 숫자식 순서와 사전식 순서로 정렬한다.



__버블 정렬__

```
Bubblesort(A)
	for i from 1 to A.length
		for j from 0 to A.length - 1
			if A[j] > A[j + 1]
				swap a[j] with a[j + 1]
```

- 이 알고리즘은 n번의 라운드로 이뤄져있으며, 각 라운드마다 배열의 아이템을 한 번씩 죽 모두 살펴본다.
- 배열 전체를 살펴보는 것을 n번 하기 때문에 시간 복잡도는 항상 O(n^2)이다.



__병합 정렬__

- 최선과 최악 모두 O(n log n)으로 일정한 알고리즘이다.
- 대부분의 경우 퀵 정렬보다는 느리지만 일정한 실행 속도뿐 만 아니라 안정 정렬이라는 점에서 여전히 상용 라이브러리에 많이 쓰이고 있다.
- 분할 정복으로 배열을 더 이상 쪼갤 수 없을 때까지 분할한 후, 분할이 끝나면 정렬하면서 정복해 나간다.



__퀵 정렬__

- 피벗을 기준으로 좌우를 나누는 특징 때문에 파티션 교환 정렬이라고도 불리운다.
- 병합 정렬과 마찬가지로 분할 정복 알고리즘이며 여기에 피벗이라는 개념을 통해 피벗보다 작으면 왼쪽, 크면 오른쪽과 같은 방식으로 파티셔닝 하면서 쪼개 나간다.

- 로무토 파티션은 항상 맨 오른쪽의 피벗을 택하는 단순한 방식으로 최초의 퀵 정렬 알고리즘보다 훨씬 더 이해하기 쉽다.

```python
# lo = 왼쪽 끝, hi = 오른쪽 끝
def Quicksort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]
        return left
    
    if lo < hi:
        pivot = partition(lo, hi)
        Quicksort(A, lo, pivot - 1)
        Quicksort(A, pivot + 1, hi)
```

- 퀵 정렬은 매우 빠르고 효율적이지만 최악의 경우, 이미 정렬된 배열이 입력값으로 들어왔을 경우 O(n^2)가 된다.



__안정 정렬 vs 불안정 정렬__

- 안정 정렬 알고리즘은 중복된 값을 입력 순서와 동일하게 정렬한다.
- 입력값이 유지되는 안정 정렬 알고리즘이 불안정 정렬 알고리즘보다 유용하다.
- 대표적으로 병합 정렬, 버블 정렬이 안정 정렬이며 퀵정렬은 불안정 정렬이다. 따라서 실무에서는 병합 정렬이 여전히 활발히 쓰이고 있으며, 파이썬의 기본 정렬 알고리즘으로는 병합 정렬과 삽입 정렬을 휴리스틱하게 조합한 팀소트를 사용한다.



### 리스트 정렬

- 연결 리스트를 O(n log n)에 정렬하라.

> __예제__
>
> - 입력: 4 -> 2 -> 1 -> 3
> - 출력: 1 -> 2 -> 3 -> 4



__풀이 1. 병합 정렬__

- 연결 리스트 입력에 대해서는 파이썬에서 정렬할 수 있는 별도의 함수를 제공하지 않기 때문에 직접 정렬 알고리즘을 구현해야 한다.
- 연결 리스트는 특성상 피벗을 고정된 위치로 지정할 수밖에 없고 입력값에 따라 성능의 편차가 심하므로 병합정렬로 구현한다.
- 병합 정렬의 분할 정복을 위해서는 중앙을 분할해야 하므로 런너 기법을 사용한다.

```python
def MergeTwoLists(l1, l2):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = MergeTwoLists(l1.next, l2)
    
    return l1 or l2

def sortLists(head):
    if not (head or head.next):
        return head
    
    # 런너 기법 활용
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    half.next = None
    
    # 분할 재귀 호출
    l1 = self.sortLists(head)
    l2 = self.sortLists(slow)
    
    return self.mergeTwoLists(l1, l2)
```





### 구간 병합

- 겹치는 구간을 병합하라.

> __예제__
>
> - 입력: [[1, 3], [2, 6], [8,10], [15, 18]]
> - 출력:[[1, 6], [8, 10], [15, 18]]



__풀이 1. 정렬하여 병합__

- 이 문제를 풀기 위해 먼저 정렬을 수행한다. 정렬 순서는 첫번째 값을 기준으로 한다.
- 그 후 현재 아이템의 시작이 이전 아이템의 끝과 겹치게 되면 최댓값을 기준으로 병합하는 형태로 반복해 나간다.

```python
def solution(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for i in intervals:
        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(i[1], merged[-1][1])
        else:
            merged += i,
    return merged
```



__콤마 연산자__

- 기본적인 추가 연산의 경우 요소를 이어붙인다. 

```python
a = [1]
b = [2, 3]
a += b
a
# [1, 2, 3]
```



- 콤마를 넣으면 중첩리스트가 된다. 콤마는 대괄호를 부여한 것과 동일한 역할을 한다.

```python
a = [1]
b = [2, 3]
a += b,
a
# [1, [2, 3]]
```



### 삽입 정렬 리스트

- 연결 리스트를 삽입 정렬로 정렬하라



__풀이 1. 삽입 정렬__

- 삽입정렬은 정렬을 해야 할 대상과 정렬을 끝낸 대상, 두 그룹으로 나눠 진행한다. head는 정렬을 해야 할 대상이며 cur는 정렬을 끝낸 대상으로 정한다. 다음과 같이 정렬을 해야할 대상 head를 반복한다.

```python
cur = parent = ListNode(None)
while head:
    while cur.next and cur.next.val < head.val:
        cur = cur.next
```

- 먼저 cur과 parent는 빈 노드로 정한다. cur엔 정렬을 끝낸 연결 리스트를 추가해줄 것이고, parent는 계속 그 위치에 두어 사실상 루트를 가리키게 한다.
- 정렬을 끝낸 cur는 이미 정렬된 상태이므로 정렬을 해야 할 대상 head와 비교하면서 더 작다면 계속 cur.next로 이동한다. 그 후 cur에 삽입될 위치를 찾았다면 cur 연결리스트에 추가한다.
- cur 위치 다음에 head가 들어가고 head.next에는 cur.next를 연결해서 계속 이어지게 한다. 그리고 다음번 head는 head.next로 차례를 이어 받는다. 이후에는 cur = parent를 통해 다시 처음으로 되돌아가며 차례대로 다시 비교하게 된다.

- 다음번 head도 cur보다 크다면 처음으로 돌아갈 필요가 없으므로 필요한 경우에만 포인터가 돌아가도록 한다.

```python
def insertionSortList(head):
    cur = parent = ListNode(None)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next
            
        cur.next, head.next, head = head, cur.next, head.next
        
        # 필요한 경우에만 cur 포인터가 되돌아가도록 처리
        if head and cur.val > head.val:
        	cur = parent
        
    return cur.next
```





### 가장 큰 수

- 항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라.

> __예제__
>
> - 입력: [10, 2]
> - 출력: "210"



__풀이 1. 삽입 정렬__

- 맨 앞에서부터 자릿수 단위로 비교해서 크기 순으로 정렬한다. 즉 9는 30보다 맨 앞자리 수가 크므로 9가 더 파에 와야한다. 

```python
class solution():
    # 문제에 적합한 비교 함수
    @staticmethod
    def to_swap(n1, n2):
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    def largestNumber(nums):
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1
```





### 유효한 애너그램

- t가 s의 애너그램인지 판별하라.

> __예제__
>
> - 입력: s = "anagram", t = '"nagaram"
> - 출력: True



__풀이 1. 정렬을 이용한 비교__

- 애너그램  여부를 판별하려면 양족 문자열을 모두 정렬하고 그 상태가 일치하는지 확인하면 된다.

```python
def solution(s, t):
    return sorted(s) == sorted(t)
```





### 색 정렬

- 빨간색을 0, 흰색을 1, 파란색을 2라 할 때, 순서대로 인접하는 제자리 정렬을 수행하라.

> __예제__
>
> - 입력: [2, 0, 2, 1, 1, 0]
> - 출력: [0, 0, 1, 1, 2, 2]



__풀이 1. 네덜란드 국기 문제를 응용한 풀이__

- 이 문제는 다익스트라가 제안한 네덜란드 국기 문제와 동일한 문제로, 퀵 정렬의 개선 아이디어와도 관련이 깊다.
- 네덜란드 국기 색깔인 붉은색, 흰색, 파란색을 세 부분으로 대입해 분할하는 것으로서, 피벗보다 작은 부분, 같은 부분, 큰 부분 이렇게 세 부분으로 분할하려 기존 퀵 정렬의 두 부분 분할에 비해 개선하는 방안을 제시하는 것이다.
- 네덜란드 국기 문제의 수도코드는 다음과 같다.

```
three-way-partition(A : array of values, mid : value):
	i = 0
	j = 0
	k = size of A
	
	while j < k:
		 if A[j] < mid:
		 	swap A[i] and A[j]
			i += 1
			j += 1
		 else if A[j] > mid:
		 	k -= 1
		 	swap A[j] and A[k]
		 else:
		 	j += 1
```

- i와 k로 영역을 점점 좁혀가면서 mid에 해당하는 값을 모은다.



```python
def solution(nums):
    red, white, blue = 0, 0, len(nums)
    
    while white < blue:
        if nums[white] < 1:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] > 1:
            blue -= 1
            nums[white], nums[blue] = nums[blue], nums[white]
        else:
            white += 1
```





### 원점에 K번째로 가까운 점

- 평면상에 points 목록이 있을 때, 원점 (0, 0)에서 K번 가까운 점 목록을 순서대로 출력하라. 평면상 두 점의 거리는 유클리드 거리로 한다.

> __예제__
>
> - 입력: points = [[1, 3], [-2, 2]], K = 1
> - 출력: [[-2, 2]]



__풀이 1. 유클리드 거리의 우선순위 큐 순서__

- 유클리드 거리를 계산에 heap에 push한 뒤 k번 추출하여 리턴한다.
- 유클리드 거리에 math.sqrt()는 하지 않아도 결과는 같으므로 생략한다.

```python
def solution(points, k):
    heap = []
    for x, y in points:
        dist = x**2 + y**2
        heapq.heappush(heap, (dist, x, y))
    
    result = []
    for _ in range(k):
        (dist, x, y) = heapq.heappop()
        result.append((x, y))
    
    return result
```

