- 연결리스트는 선형 자료구조 중 하나로 다양한 추상 자료형 구현의 기반이 된다.
- 삽입과 삭제가 간편하다.
- 물리 메모리를 연속적으로 사용하지 않아도 되기 때문에 관리하기도 쉽다.
- 연결리스트는 리스트와 달리 특정 인덱스에 접근하기 위해 전체를 순서대로 읽어야 한다. 따라서 O(n)의 시간이 걸린다.
- 그러나 삽입과 삭제에는 O(1)의 시간이 걸린다.

# 팰린드롬 연결 리스트
연결 리스트가 팰린 드롬 구조인지 판별하라

입력 : 1->2
출력 : False

입력 : 1 -> 2 -> 2 -> 1
출력 : True

## <풀이 1> 리스트 변환
- 연결 리스트 입력 값을 파이썬의 리스트로 변환해 풀이

```python
def isPalindrome(head):
  q = []
  if not head:
    return True

  node = head
  # 리스트 변환
  while node is not None:
    q.append(node.val)
    node = node.next

  # 팰린드롬 판별
  while len(q) > 1:
    if q.pop(0) != q.pop():
      return False

  return True
```


## <풀이 2> 데크를 이용한 최적화
- 파이썬의 데크는 이중 연결 리스트 구조로 양쪽 방향 모두 추출하는데 시간 복잡도 O(1)에 실행된다.

```python
def isPalindrome(head):
  q = collections.deque()
  if not head:
    return True

  node = head
  # 리스트 변환
  while node is not None:
    q.append(node.val)
    node = node.next

  # 팰린드롬 판별
  while len(q) > 1:
    if q.popleft() != q.pop():
      return False

  return True
```

## <풀이 3> 런너를 이용한 우아한 풀이
- 두칸씩 뛰는 빠른 런너와 한칸씩 뛰는 느린 런너를 사용한다.

```python
def isPalindrome(head):
  rev = None
  slow = fast = head
  # 런너를 이용해 역순 연결 리스트 구성
  while fast and fast.next:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next
    if fast:
      slow = slow.next

  # 펠린드롬 여부 확인
  while rev and rev.val == slow.val:
    slow, rev = slow.next, rev.next
  return not rev
```

* rev, rev.next, slow = slow, rev, slow.next를 2줄로 풀어쓰면 코드가 작동하지 않는다. slow가 rev를 참조하기 때문이다.

# 두 정렬 리스트의 병합
정렬되어 있는 두 연결 리스트를 합쳐라

입력: 1->2->4, 1->3->4
출력: 1->1->2->3->4->4

## <풀이 1> 재귀구조로 연결

def mergeTwoLists(l1, l2):
  if (not l1) and (l2 and l1.val > l2.val):
    l1, l2 = l2, l1
  if l1:
l1.next = self.mergeTwoLists(l1.next, l2)
return l1

15. 역순 연결 리스트
연결 리스트를 뒤집어라
입력: 1->2->3->4->5->NULL

<풀이 1> 재귀 구조로 뒤집기
- 재귀 구조와 반복 구조 두가지 방식으로 풀이 할 수 있다.

def reverseList(head):
def reverse(node, prev=None):
if not node:
return prev
next, node.next = node.next, prev
return reverse(next, node)

return reverse(head)

<풀이 2> 반복 구조로 뒤집기

def reverseList(head):
node, prev = head, None

while node:
next, node.next = node.next, prev
prev, node = node, next

return prev

16. 두 수의 덧셈
역순으로 저장된 연결 리스트의 숫자를 더하라
입력: (2 -> 4 -> 3) + (5 -> 6- > 4)
출력: 7-> 0 -> 8
설명: 342 + 465 = 807

<풀이 1> 자료형 변환
- 연결 리스트를 문자열로 이어 붙인 다음에 숫자로 변환하고 이를 모두 계산한 후 다시 연결 리스트로 바꾼다.

<풀이 2> 전가산기 구현
- 논리 회로의 전가산기와 유사한 형태를 구현한다.

def addTwoNumbers(l1, l2):
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

# 몫과 나머지 계산
carry, val = divmod(sum + carry, 10)
head.next = ListNode(val)
head = head.next

return root.next

* 숫자형 리스트를 단일 값으로 병합하기
- a = [1, 2, 3, 4, 5]를 하나의 숫자로 합치는 코드
‘’’.join(str(e) for e in a) -> 가독성이 떨어지고 깔끔하지 않음
‘’.join(map(str, a)) -> 변수 e를 사용하지 않아 깔끔
functool.reduce(lambda x, y: 10 * x + y, a, 0) -> 문자열로 변환하지 않음

17. 페어의 노드 스왑 - 개어려움 모르겠음…
연결 리스트를 입력받아 페어 단위로 스왑하라
입력: 1 -> 2 -> 3 -> 4
출력: 2 -> 1 -> 4 -> 3

<풀이 1> 값만 교환
- 연결리스트의 노드를 변경하지 않고 값만 변경하는 방법

def swapPairs(head):
cur = head

while cur and cur.next:
# 값만 교환
cur.val, cur.next.val = cur.next.val, cur.val
cur = cur.next.next

return head

<풀이 2> 반복 구조로 스왑

def swapPairs(head):
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

<풀이 3> 재귀 구조로 스왑

def swapPairs(head):
if head and head.next:
p = head.next
# 스왑된 값 리턴 받음
head.next = self.swapPairs(p.next)
p.next = head
return p
return head

18. 홀짝 연결 리스트 - 이것도 모르겠음…
연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간복잡도 o(1), O(n)에 풀이하라.
입력: 1->2->3->4->5->NULL
출력: 1->3->5->2->4->NULL

<풀이 1> 반복 구조로 홀짝 노드 처리

def oddEvenList(head):
if head is None:
return None

odd = head
even = head.next
even_head = head.next

# 반복하면서 홀짝 노드 처리
while even and even.next:
odd.next, even.next = odd.next.next, even.next.next
odd, even = odd.next, even.next

# 홀수 노드의 마지막을 짝수 헤드로 연결
odd.next = even_head
return head

19. 역순 연결 리스트2
인덱스 m에서 n까지를 역순으로 만들어라 인덱스 m은 1부터 시작한다.
입력 : 1->2->3->4-> 5->NULL, m = 2, n = 4
출력: 1->4->3->2->5->NULL

<풀이 1> 반복 구조로 노드 뒤집기

def reverseBetween(head, m, n):
if not head or m == n:
return head

root = start = ListNode(None)
root.next = head
# start, end 지정
for _ in range(m -1):
start = start.next
end = start.next

# 반복하면서 노드 차례대로 뒤집기
for _ in range(n -m):
tmp, start.next, end.next = start.next, end.next, end.next.next
start.next.next = tmp
return root.next
