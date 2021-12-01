# DFS & BFS



## 타겟 넘버

- root가 0이고 그 아래로 + number와 - number 해준 것들이 가지로 달려있는 트리 형태의 그래프로 생각한다.
- dfs를 이용해 모든 경우의 수를 탐색하고 그 갯수를 센다.

```python
def solution(numbers, target):
    n_numbers = len(numbers)
    
    # dfs 구현
    def dfs(index, csum):
        cnt = 0
        
        if index == n_numbers:
            # target이면 1, target 아니면 0
            return int(csum == target)
        
        # cnt에 모두 더해주기
        cnt += dfs(index + 1, csum + numbers[index])
        cnt += dfs(index + 1, csum - numbers[index])
        
        return cnt
    
    return dfs(0, 0)
```



## 네트워크

- input을 이용해서 그래프 맵을 그리고 그래프 맵을 DFS로 순회하며 방문하는 노드들을 visited에 append한다. 그 후 DFS가 끝날 때 카운트를 하여 네트워크의 갯수를 센다.

```python
from collections import defaultdict
def solution(n, computers):
    graph, stack = defaultdict(list), []
    visited = []
    
    # 그래프 맵 만들기
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
    
    # dfs 구현
    def dfs(a):
        stack.append(a)
        visited.append(a)
        while stack:
            for i in graph[stack.pop()]:
                if i not in visited:
                    stack.append(i)
                    visited.append(i)
    
    # 네트워크 순회가 끝나면 count + 1
    count = 0
    for i in list(graph):
        if i not in visited:
            dfs(i)
            count += 1

    return count
```



## 단어 변환

- 한 글자만 다른 단어 사이가 연결된 그래프라고 생각하고 BFS로 타겟 단어까지 가는 최단 경로를 찾는 문제로 치환하여 푼다.

```python
from collections import defaultdict, deque
import sys

def solution(begin, target, words):
    graph = defaultdict(list)
    queue = deque()
    answer = []
    words.append(begin)
    
    # 그래프 맵 만들기
    for i in words:
        for j in words:
            if i != j:
                for idx in range(len(i)):
                    if i[:idx] + i[idx + 1:] == j[:idx] + j[idx + 1:]:
                        graph[i].append(j)
    
    # BFS 구현
    def bfs(w):
        min_step = sys.maxsize
        traced = []
        queue.append((0, w))
        while queue:
            step, temp = queue.popleft()
            if temp == target:
                # step 수를 세어 최소 step인지 확인
                min_step = min(step, min_step)

            for word in graph[temp]:
                # 최단경로를 알아내야하므로 이미 방문한 노드는 방문 하지 않음
                if word not in traced:
                    traced.append(word)
                    queue.append((step + 1, word))

        return min_step

    answer = bfs(begin)
    
    # 최소 step이 나오지 않았으면 0 리턴
    if answer == sys.maxsize:
        return 0
    else:
        return answer
```



## 여행경로

- 사전 순서로 방문해야하므로 공항 이름을 정렬하여 그래프 맵으로 만들고, DFS로 그래프에서 해당 공항을 pop해가면서 모든 노드를 순회하는 루트를 찾는다.

```python
def solution(tickets):
    from collections import defaultdict
    graph = defaultdict(list)
    
    # 그래프 맵 만들기(알파벳 순서로 방문하기 위해 sorted)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
    
    route = []
    
    # dfs 구현
    def dfs(a):
        while graph[a]:
            # 알파벳 순서로 방문하기 위해 pop
            dfs(graph[a].pop())
        route.append(a)

    
    dfs('ICN')
    
    # 나중에 방문한 곳이 배열의 앞에 위치하게 되므로 뒤집기
    return route[::-1]
```

