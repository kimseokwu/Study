# 백준 단계별로 풀기 - 스택

### 10828번 

- https://www.acmicpc.net/problem/10828

- 스택을 구현하는 문제다. 파이썬의 경우 리스트가 스택의 모든 기능을 제공하므로 리스트를 이용ㅎ면 쉽게 구현할 수 있다.
- 자꾸 시간 초과가 나서 코드가 잘못 되었나 했더니 백준에서는 input()대신 sys.stdin.readline()를 사용해야 시간초과를 막을 수 있다고 한다.

```python
import sys

# 스택 개체 구현
class stack():
    def __init__(self):
        self.stk = []
        self.count = 0
    
    def empty(self):
        return int(self.count == 0)
    
    def size(self):
        return self.count
    
    def push(self, n):
        self.stk.append(n)
        self.count += 1
    
    def pop(self):
        if self.empty() == 0:
            self.count -= 1
            return self.stk.pop()
        else:
            return -1
    
    def top(self):
        if self.empty() == 0:
            return self.stk[-1]
        else:
            return -1
        
n = int(input())

stack = stack()

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'empty':
        print(stack.empty())
    elif command[0] == 'top':
        print(stack.top())
    elif command[0] == 'size':
        print(stack.size())
```

 



### 10773번 

- https://www.acmicpc.net/problem/10773
- 입력값이 들어오면 stack에 push하고 0이 입력될 때 마다 stack에서 pop한 뒤, stack 값들의 합계를 출력하면 되는 문제다.

```python
import sys
k = int(input())

stack = []
for i in range(k):
    n = int(sys.stdin.readline())
    
    # 0이 입력될 경우
    if n == 0:
        stack.pop()
    # 다른 입력값이 들어왔을 경우
    else:
        stack.append(n)

print(sum(stack))
```



## 9012번

- https://www.acmicpc.net/problem/9012
- 괄호 입력값을 차례대로 스택에 쌓다가 ')'이 들어오면 stack의 마지막 값을 확인 한 뒤 '('이면 stack에서 pop을 한다. 그 후 모든 문자열을 확인하고 스택이 비어있으면 올바른 괄호 문자열, 비어있지 않으면 올바르지 않은 괄호 문자열이다.

```python
t = int(input())
map_ = {'(':')'}

for i in range(t):
    s = list(input())
    stack = []
    for letter in s:
        if stack and stack[-1] in map_ and map_[stack[-1]] == letter:
            stack.pop()
        else:
            stack.append(letter)
    
    if stack:
        print('NO')
    else:
        print('YES')
```



## 4949번

- https://www.acmicpc.net/problem/4949
- 9012번과 비슷하나, 문자열에 괄호가 아닌 문자가 섞여있고, 소괄호와 대괄호가 섞여있다. 나는 문자열을 스캔하면서 대괄호 혹은 소괄호 일때는 스택에 push하고, )나 ]가 들어왔을 때, 스택의 마지막값을 확인해서 (나 [이면 스택에서 pop하는 것으로 구현했다.
- 처음엔 대괄호와 소괄호를 각각 다른 스택에 담는 것으로 구현했는데 이 경우 '([)]'와 같은 경우를 걸러낼 수가 없어서 다시 한 개의 스택으로 바꿨다. 괄호 내부의 문자열도 균형잡힌 문자열이어야 한다는 조건을 잊어버리는 실수를 했다.

```python
string = input()
map_ = {'(':')', '[':']'}

while string != '.':
    stack = []
    for s in string:
        if s in ['[', ']', '(', ')']:
            if stack and stack[-1] in map_ and map_[stack[-1]] == s:
                stack.pop()
            else:
                stack.append(s)
        
    
    if stack:
        print('no')
    else:
        print('yes')
    
    string = input()
```



## 1874번

- https://www.acmicpc.net/problem/1874
- 숫자를 입력받아 입력받은 값이 push되지 않은 값보다 크면, 해당 입력값이 나올때까지 stack에 push하고 입력값을 pop한다. push와 pop을 할때마다 answer 리스트에 '+'와 '-'를 삽입한다. 그러나 입력받은 값이 push되지 않은 값보다 작을 경우 push를 통해서는 해당 값을 찾을 수 없으므로 is_false 변수를 1로 바꿈으로써 불가능한 경우라는 것을 표시한다. 마지막단에서 answer을 출력할 때는 is_false가 1일 경우 'NO'를 출력하고 0일 경우 한줄마다 '+'와 '-'를 하나씩 출력한다.
- 최소 한번의 push는 해야하므로 answer엔 '+'를 넣어놓았고 stack에는 1을 넣어놓았다. push되지 않은 수를 뜻하는 p는 2부터 시작하는 것으로 했다.

```python
n = int(input())
answer = ['+']
stack = [1]
is_false = 0
p = 2

for i in range(n):
        
    k = int(input())
    
    if not stack:
        stack.append(p)
        answer.append('+')
        p += 1
    
    while stack[-1] != k:
        if stack[-1] < k:
            stack.append(p)
            answer.append('+')
            p += 1
        elif stack[-1] > k:
            is_false = 1
            break
    
    stack.pop()
    answer.append('-')

if is_false == 1:
    answer = ['NO']

for i in answer:
    print(i)
```



## 17298번

- https://www.acmicpc.net/problem/17298
- 파이썬 알고리즘 인터뷰에서 나온 '일일 온도'(https://littledatascientist.tistory.com/17?category=981837) 문제와 비슷하다고 느꼈다. 값 대신 인덱스를 스택에 쌓으면서 전보다 큰 값이 나올 경우 stack의 마지막 인덱스의 해당 값이 현재 값보다 클때까지 pop한다. 그 후 answer 리스트에는 pop된 인덱스마다 현재의 값을 저장한다.
- 스택에 인덱스를 push한다는 아이디어가 중요한 것 같다.

```python
n = int(input())
A = list(map(int, input().split()))
answer = ['-1'] * n
stack = []

for i, cur in enumerate(A):
    while stack and cur > A[stack[-1]]:
        last = stack.pop()
        answer[last] = str(cur)
    stack.append(i)
print(' '.join(answer))
```

