# 스택, 큐

- 스택과 큐는 프로그래밍이라는 개념이 탄생할 때 부터 사용된 가장 고전적인 자료구조 중 하나로 그 중에서도 스택은 거의 모든 애플리케이션을 만들 때 사용되는 자료구조다.
- 스택은 후입선출, 큐는 선입선출
- 파이썬은 리스트가 사실상 스택의 모든 연산을 지원하고 큐는 데크 자료구조형을 사용한다.

-  꽉 찬 스택에 요소를 삽입하고자 할 때 스택에 요소가 넘쳐서 에러가 발생하는 것을 스택오버플로우라고 한다.



### 유효한 괄호

- 괄호로 된 입력값이 올바른지 판별하라.

> __예제__
>
> - 입력: ()[]{}
> - 출력: True



__풀이 1. 스택 일치 여부 판별__

- 스택에 푸시를 하고, 스택에서 팝한 결과가 매핑 테이블 결과와 매칭되는지 확인하면 된다.

```python
def solution():
    stack = []
    table = {
        ')':'(',
        '}':'{'.
        ']':'['
    }
    
    # 스택 이용 예외 처리 및 일치 여부 판별
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    
    return len(stack) == 0
```





### 중복 문자 제거

- 중복된 문자를 제외하고 사전식 순서로 나열하라.

> __예제__
>
> - 입력: 'bcabc'
> - 출력: 'abc'



__풀이 1. 스택을 이용한 문자제거__

- 문자를 앞에서부터 하나씩 차례대로 쌓아나간다. 만약 현재 문자 char가 스택에 쌓여있는 문자이고 뒤에 다시 붙일 문자가 남아 있다면 쌓아둔걸 꺼내서 없앤다. 카운팅에는 collections.Counter()를 사용한다.

```python
def solution(s):
    counter, seen, stack = collections.Counter(s), set(), []
    
    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
   
	return ''.join(stack)
```



### 일일 온도

- 매일의 화씨 온도 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.

> __예제__
>
> - 입력: [73, 74, 75, 71, 69, 72, 76, 73]
> - 출력: [1, 1, 4, 2, 1, 1, 0, 0]



__풀이 1. 스택 값 비교__

- 빗물 트래핑과 유사한 방법으로 풀이할 수 있다.
- 현재의 인덱스를 계속 스택에 쌓아두다가, 이전보다 상승하는 지점에서 현재 온도와 스택에 쌓아둔 인덱스 지점의 온도 차이를 비교해서 더 높다면 다음과 같이 스택의 값을 pop()으로 꺼내고 현재 인덱스와 스택에 쌓아둔 인덱스의 차이를 정답으로 처리한다.

```python
def solution(T):
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        # 현재 온도가 스택값보다 높다면 정답 처리
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    
    return answer
```



# 데크, 우선순위 큐

__데크__

- deque는 double ended queue의 줄임말로 글자 그대로 양쪽끝을 모두 추출할 수 있는 큐를 일반화한 형태의 추상자료형이다.
- collections.deque는 이중 연결 리스트로 구현되어 있다.



__우선순위 큐__

- 우선순위 큐는 어떠한 특정 조건에 따라 우선순위가 가장 높은 요소가 추출되는 자료형이다. 대표적으로 최댓값 추출을 들 수 있다.
- 정렬 알고리즘을 사용하면 우선순위 큐를 만들 수 있다. 단순 정렬보다는 힙 정렬등의 좀 더 효율적인 방법을 활용한다.
- 최단경로를 탐색하는 다익스트라 알고리즘 등 우선순위 큐는 다양한 분야에 활용되며 힙 자료구조와도 관련이 깊다.



### k개 정렬 리스트 병합

- k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라.

> __예제__
>
> - 입력: [1->4->5, 1->3->4, 2->6]
> - 출력: 1->1->2->3->4->4->5->6



__풀이 1. 우선순위 큐를 이용한 리스트 병합__

- 파이썬에서는 대부분의 우선순위 큐 풀이에 거의 항상 heapq 모듈을 사용한다.
- 연결리스트 노드를 heap에 push한 뒤, heappop을 이용해 최소 노드를 추출해서 result에 붙인다. 그 후 다음 노드를 다시 heap에 push한다.

```python
def solution(list):
    root = result = ListNode(None)
    heap = []
    
    # 각 연결리스트의 루트를 힙에 저장
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
    
    # 힙 추출 이후 다음 노드는 다시 저장
    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]
        
        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
    
    return root.next
```

