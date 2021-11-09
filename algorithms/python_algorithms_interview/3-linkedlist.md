# 연결리스트

- 연결리스트는 데이터 요소의 선형 집합으로 데이터의 순서가 메모리에 물리적인 순서대로 저장되지는 않는다.

연결리스트는 가장 기본이 되는 대표적인 선형 자료구조 중 하나로 다양한 추상 자료형 구현이 기반이 된다. 동적으로 새로운 노드를 삽입하거나 삭제하기가 간편하며, 연결 구조를 통해 물리 메모리를 연속적으로 사용하지 않아도 되기 때문에 관리도 쉽다.

특정 인덱스에 접근하기 위해서는 전체를 순서대로 읽어야 하므로 상수 시간에 접근할 수 없다. 탐색에는 O(n)이 소모된다. 반면 삭제, 추출하는 작업은 O(1)에 가능하다.



### 펠린드롬 연결 리스트

- 연결리스트가 펠린드롬 구조인지 판별하라.

> __예제__
>
> - 입력: 1-> 2
> - 출력: false



__풀이 1. 리스트 변환__

- 펠린드롬 여부를 판별하기 위해서는 앞뒤로 모두 추출할 수 있는 자료구조가 필요하다. 따라서 이 문제는 연결리스트를 파이썬의 리스트로 변환하여 리스트의 기능을 이용하면 쉽게 풀이 할 수 있을 것이다.



```python
def solution(head):
    q = []
    
    if not head:
        return False
    
    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next
        
    # 펠린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
        
    return True
```



__풀이 2. 데크를 이용한 최적화__

- 리스트에선 q.pop(0)은 O(n) 시간복잡도를 가진다. 따라서 최적화를 위해선 데크가 필요하다.

```python
def solution(head):
    q = collections.deque()
    
    if not head:
        return False
    
    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next
        
    # 펠린드롬 판별
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
        
    return True
```



__풀이 3. 런너를 이용한 우아한 풀이__

- 2개의 노드씩 건너뛰는 빠른 런너와 노드 1개씩 건너뛰는 느린 런너를 각각 출발시키면, 빠른 런너가 끝에 다다를때 느린 런너는 정확히 중간 지점에 도달하게 될 것이다. 느린 런너는 중간까지 이동하면서 역순으로 연결리스트 rev를 만들어간다. 이제 중간에 도달한 느린 런너가 나머지 경로를 이동할 때 역순으로 만든 연결 리스트의 값들과 일치하는지 확인해나가면 된다.

```python
def solution(head):
    rev = None
    slow = fast = head
    # 런너를 이용해 역순 연결리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    # 노드의 갯수가 홀수 일 때 slow가 중앙을 벗어나냐함
    if fast:
        slow = slow.next
    
    while rev and rev.val == slow.val:
        slow, rev = slow.val, rev.val
    
    return not rev
```



> __런너 기법__
> 런너는 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법이다. 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다.



### 두 정렬 리스트의 병합

- 정렬되어 있는 두 연결 리스트를 합쳐라.

> __예제__
>
> - 입력: 1->2->4, 1->3->4
> - 출력: 1->-1>2->3->4->4



__풀이 1. 재귀 구조로 연결__

- 정렬된 리스트라는 점이 중요하다. 병합정렬처럼 하나씩 비교하면서 리턴한다.

```python
def solution(l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.solution(l1,next, l2)
    return l1
```



### 역순 연결리스트

- 연결 리스트를 뒤집어라

> __예제__
>
> - 입력: 1->2->3->4->5->NULL
> - 출력: 5->4->3->2->1->NULL



__풀이 1. 재귀구조로 뒤집기__

- 연결리스트를 뒤집는 문제는 매우 일반적이면서도 활용더가 높은 문제로, 실무에서도 빈번하게 쓰인다.



```python
def solution(head):
    def reverse(node, prev = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    
    return reverse(head)
```



__풀이 2. 반복구조로 뒤집기__

```python
def solution(head):
    node, prev = head, None
    
    while node:
        next, node.next = node.next, head
        prev, node = node, next
        
    return prev
```



### 두 수의 덧셈

- 역순으로 저장된 연결 리스트의 숫자를 더하라.

> __예제__
>
> - 입력: (2->4->3) + (5->6->4)
> - 출력: 7->0->8



__풀이 1. 전가산기 구현__

- 전가산기는 입력값 A와 B, 자리올림수 3가지 입력으로 합과 다음 자리 올림수 여부를 결정한다. 입력값 A, B는 오른쪽으로는 XOR 게이트를 통과한 결과가 나아가고, 아래로는 AND 게이트를 통과한 결과가 나아간다. 그렇게 합과 다음 자리 올림수 위치에 도달한 결과가 진리표다. 덧셈 연산을 수행하는 논리회로의 원리다.

|  A   |  B   | carry in | sum  | carry out |
| :--: | :--: | :------: | :--: | :-------: |
|  0   |  0   |    0     |  0   |     0     |
|  0   |  0   |    1     |  1   |     0     |
|  0   |  1   |    0     |  1   |     0     |
|  0   |  1   |    1     |  0   |     1     |
|  1   |  0   |    0     |  1   |     0     |
|  1   |  0   |    1     |  0   |     1     |
|  1   |  1   |    0     |  0   |     1     |
|  1   |  1   |    1     |  1   |     1     |

```python
def solution(l1, l2):
    root = head = ListNode(0)
    
    carry = 0
    while l1 or l2 or carry:
        sum = 0
        # 두 입력값의 합 계산
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
            
        # 몫(자리 올림수)과 나머지(값) 계산
        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

	return root.next    
```



### 페어의 노드 스왑

- 연결리스트를 입력받아 페어 단위로 스왑하라

> __예제__
>
> - 입력: 1->2->3->4
> - 출력: 2->1->4->3



__풀이 1. 값만 교환__

- 연결리스트의 노드를 변경하는 게 아닌 노드 구조는 그대로 유지하 되 값만 병경하는 방법이다. 실용성과는 다소 거리가 있다.

```python
def solution(head):
    cur = head
    
    while cur and cur.next:
        # 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next
        
    return head
```



__풀이 2. 반복구조로 풀이__

- 1->2->3->4->5->6인 연결리스트가 있을 경우 3->4를 4->3으로 바꾸려면 그 앞인 2가 가리키는 연결리스트와 5로 연결되는 연결리스트도 다 같이 변경해야 한다.

- ```python
  b = a.next
  a.next = b.next
  b.next = a
  ```

- 이처럼 b가 a를 가리키고 a는 b의 다음을 가리키도록 변경한다. 그러나 아직 a의 이전 노드가 b를 가리키지는 못한다.

- ```python
  prev.next = b
  a = a.next
  prev = prev.next.next
  ```

- a의 이전 노드 prev가 b를 가리키게 하고 다음 비교를 위해 prev는 두칸 앞으로 이동한다. 그리고 다시 다음번 교환을 진행한다.

```python
def solution(head):
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        # b가 a(head)를 가리키도록 할당
        b = head.next
        head.next = b.next
        b.next = head
        
        # prev가 b를 가리키도록 할당
        prev.next = b
        
        # 다음번 비교를 위해 이동
        head = head.next
        prev = prev.next.next
    
    return root.next
```



__풀이 3. 재귀 구조로 스왑__

- 재귀로는 훨씬 더 깔끔하게 풀이할 수 있다.

```python
def solution(head):
    if head and head.next:
        p = head.next
        # 스왑된 값 리턴 받음
        head.next = solution(p.next)
        p.next = head
        return p
    return head
```



# 홀짝 연결 리스트

- 연결리스트를 홀수 ㅗㄴ드 다음에 짝수 노드가 오도록 재구성하라. 공간복잡도 O(n), 시간복잡도 O(n)에 풀이하라.
