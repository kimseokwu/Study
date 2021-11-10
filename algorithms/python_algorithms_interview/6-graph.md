# 그래프

- 그래프란 객체의 일부 쌍들이 연관되어 있는 객체 집합 구조를 말한다.



__해밀턴 경로__

- 해밀턴 경로는 각 정점을 한 번 씩 방문하는 무향 또는 유향 그래프 경로를 말한다.
- 오일러 경로의 차이점을 들자면 경로는 간선을 기준으로 하고 해밀턴 경로는 정점을 기준으로 한다는 점이다. 그러나 해밀턴 경로를 찾는 문제는 최적 알고리즘이 없는 np-완전 문제다.
- 원래의 출발점으로 돌아오는 경로는 해밀턴 순환이라고 부르는데 이 중에서도 특히 최단거리를 찾는 문제는 알고리즘 분야에서는 외판원 문제로 유명하다. 외판원 문제는 각 도시를 방문하고 돌아오는 가장 짧은 경로를 찾는 문제, 즉 최단 거리인 해밀턴 순환을 찾는 문제이며, np-난해 문제이다.



__그래프 순회__

- 그래프 순회란 그래프 탐색이라고도 불리우며 그래프의 각 정점을 방문하는 과정을 말한다.
- 그래프 순회에는 크게 깊이 우선 탐색(DFS)와 너비 우선 탐색(BFS)의 2가지 알고리즘이 있다. 
- DFS는 주로 스택으로 구현하거나 재귀로 구현하며, 이후에 살펴볼 백트래킹을 통해 뛰어난 효용을 보인다. 반면  BFS는 큐로 구현하며, 그래프의 최단 경로를 구하는 문제 등에 사용된다.
- 그래프를 표현하는 방법에는 크게 인접행렬과 인접리스트 2가지 방법이 있는데 여기서는 인접 리스트로 표현한다. 인접 리스트는 출발 노드를 키로, 도착 노드를 값으로 표현할 수 있다.

```python
graph = {
    1:[2, 3, 4],
    2:[5],
    3:[5],
    4:[],
    5:[6, 7],
    6:[],
    7:[3]
}
```



__깊이 우선 탐색(DFS)__

- 재귀를 통해 DFS를 구현해보면 다음과 같다.

```python
def DFS(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = DFS(w, discovered)
    return discovered
```



- 스택을 이용한 반복 결과로 DFS를 구현하면 다음과 같다. 코드가 빈틈없어 보이는 재귀 구현에 비해 우아함은 떨어지지만 좀 더 직관적이라 이해하기는 훨씬 더 쉽다. 실행 속도 또한 더 빠른 편이다.

```python
def DFS(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered
```



__너비 우선 탐색(BFS)__

- 스택을 사용하는 DFS와 달리 BFS를 반복 구조로 구현할 때는 큐를 이용한다. 최적화를 위해 데크 같은 자료형을 사용해 보는 것을 고민해볼 수 있다.

```python
def BFS(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[w]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
```

- BFS는 재귀로 동작하지 않는다. 큐를 이용한 반복 구현만 가능하다.



__백트래킹__

- 백트래킹은 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기해 정답을 찾아가는 범용적인 알고리즘으로 제약 충족 문제에 특히 유용하다.
- 백트래킹은 DFS와 같은 방식으로 탐색하는 모든 방법을 뜻하며 DFS는 백트래킹의 골격을 이루는 알고리즘이다. 백트래킹은 주로 재귀로 구현하며 알고리즘 마다 DFS 변형이 조금씩 일어나지만 기본적으로 모두 DFS의 범주에 속한다.
- 브루트 포스와 유사하지만 한번 방문 후 가능성이 없는 경우엔 후보를 포기한다는 점에서 더 우아한 방식이다.



__제약 충족 문제__

- 제약 충족 문제란 수많은 제약 조건을 충족하는 상태를 찾아내는 수학문제를 일컫는다.

- 백트래킹은 제약 충족 문제를 풀이하는 데 필수적인 알고리즘이다.



### 섬의 개수

- 1을 육지로 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라.

> __예제__
>
> - 입력: 
>
> 11110
>
> 11010
>
> 11000
>
> 00000
>
> - 출력: 3



__풀이 1. DFS로 그래프 탐색__

- 입력값이 정확히 그래프는 아니지만 사실상 동서남북이 모두 연결된 그래프로 가정하고 동일한 형태로 처리할 수 있다.
- 육지인 곳을 찾아 진행하다가 육지를 발견하면 그때부터 DFS()를 호출해 탐색을 시작한다.
- DFS()는 동서남북을 모두 탐색하면서 재귀 호출한다. 함수 상단에 육지가 아닌 곳은 return으로 종료 조건을 설정해둔다. 이미 방문한 곳은 0으로 마킹한다.
- dfs 함수를 빠져나온 후에는  해당 위치에서 탐색할 수 있는 모든 육지를 탐색한 것이므로 카운트를 1 증가시킨다.

```python
def solution(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or \
           j < 0 or j >= len(grid[0]) or \
           grid[i][j] != '1':
            return
        
        grid[i][j] = 0
        
        #동서남북 탐색
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                # 모든 육지 탐색 후 카운트 1 증가
                count += 1
    return count
```



### 전화번호 문자 조합

- 2에서 9까지 숫자가 주어졌을 때 전화번호로 조합 가능한 모든 문자를 출력하라

> __예제__
>
> - 입력: '23'
> - 출력: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']



__풀이 1. 모든 조합 탐색__

- 이 문제는 전체를 탐색하여 풀이할 수 있다. 항상 전체를 탐색해야하고 가지치기 등으로 최적화할 수 있는 문제는 아니기 때문에 어떻게 풀이하든 결과는 비슷하다. 모두 조합하는 형태로 전체를 탐색한 후 백트래킹하면서 결과를 조합한다.

```python
def solution(digits):
    def dfs(index, path):
        # 끝까지 탐색하면 백트래킹
        if len(path) == len(digits):
            result.append(path)
            return
        
        # 입력값 자릿수 단위 반복
        for i in range(index, len(digits[i])):
            dfs(i + 1, path + j)
    
    # 예외 처리
    if not digits:
        return []
    
    dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5'L 'jkl',
          '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = []
    dfs(0, "")
```



### 조합의 합

- 숫자 집합 cadidates를 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복으로 나열 가능하다.

> __예제__
>
> - 입력: candidates = [2, 3, 6, 7], target = 7
> - 출력: [[7], [2, 2, 3]]



__풀이 1. DFS로 중복 조합 그래프 탐색__

- target을 만들 수 있는 모든 번호 조합을 찾는 문제이다. DFS와 백트래킹으로 풀이할 수 있다.
- 모든 중복 조합에서 찾아야 하기 때문에, 이 그림과 같이 항상 부모의 값부터 시작하는 그래프로 구성할 수 있다.
- DFS의 종료조건은 2가지 경우다. csum < 0인 경우, csum == 0인 경우

```python
def solution(candidates, target):
    result = []
    
    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])
    
    dfs(target, 0, [])
    return result
```

- 입력값에 0이 포함되어 있다면 종료조건을 만족할 수 없기 때문에 무한히 깊이 탐색을 시도하게 된다. dfs(csum - candidates[i], 0, path + [candidates[i]])로 바꿔주면 항상 첫번째 값부터 탐색을 시도하기 때문에 순열로 풀이할 수 있다.



### 부분 집합

- 모든 부분 집합을 리턴하라.

> __예제__
>
> - 입력: nums = [1, 2, 3]
> - 출력: [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]



__풀이 1. 트리의 모든 DFS 결과__

- 경로 path를 만들어 나가면서 인덱스를 1씩 증가하는 형태로 깊이 탐색한다. 별도의 종료 조건 없이 탐색이 끝나면 저절로 함수가 종료되게 한다.
- 부분 집합은 모든 탐색의 경로가 결국 정답이 되므로 다음과 같이 탐색할 때마다 매번 결과를 추가하면 된다.

```python
def solution(nums):
    result = []
    
    def dfs(index, path):
        # 매번 결과 추가
        result.append(path)
        
        # 경로를 만들면서 DFS
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])
    
    dfs(0, [])
    return result
```



### 일정 재구성

- [from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행일정을 구성하라. 여러 일정이 있는 경우 사전 어휘 순으로 방문한다.

> __예제__
>
> - 입력: [['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]
> - 출력: ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']



__풀이 1. DFS로 일정 그래프 구성__

- 여행일정을 그래프로 구성하여 DFS로 문제를 풀이한다.
- 어휘 순으로 방문해야 하므로 일단 그래프를 구성한 후에 다시 꺼내 정렬한다.

```python
def solution(tickets):
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
        
    route = []
    def dfs(a):
        # 첫번째 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)
    
    dfs('JFK')
    # 다시 뒤집어 어휘 순 결과로
    return route[::-1]
```



__풀이 2. 일정 그래프 반복__

- 재귀가 아닌 스택을 이용한 반복으로 처리한다.

```python
def solution(tickets):
    graph = collections.defaultdict(list)
    
    for a, b in sorted(tickets):
        graph[a].append(b)
        
    route, stack = [], ['JFK']
    while stack:
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())
        
    return route[::-1]
```



### 코스 스케줄

- 0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0, 1] 쌍으로 표현하는 n개의 코스가 있다. 코스 개수 n과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료 가능한지 판별하라.

>  __예제__
>
> - 입력: 2, [[1, 0]]
> - 출력: true



__풀이 1. DFS로 순환 구조 판별__

- 이 문제는 graph가 순환 구조인지를 판별하는 문제로 풀이할 수 있다. 순환 구조라면 계속 뱅글뱅글 맴돌게 될 것이고 해당 코스는 처리할 수 없기 때문이다.
- 이미 방문했던 곳을 중복 방문한다면 순환 구조로 간주할 수 있고, 이 경우 False를 리턴하고 종료할 수 있다.
- 순환이 아닌데 순환으로 판단할 수 있으므로 한번 경로가 탐색이 끝난 후에는 traced.remove(i)로 노드가 모두 삭제되어야 한다.

```python
def solution(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)
    
    traced = set()
    
    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        
        return True
    
    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False
    
    return True
```



__풀이 2. 가지치기를 이용한 최적화__

- 앞서 풀이한 DFS 풀이는 순환이 발견될 때 까지 모든 자식 노드를 탐색하는 구조로 되어 있다. 따라서 한 번 방문했던 그래프는 두번 이상 방문하지 않도록 무조건 True로 리턴하는 구조로 개선한다면 탐색시간을 획기적으로 줄일 수 있을 것이다.

```python
def solution(numCouses, prerequsites):
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)
    
    traced = set()
    visited = set()
    
    def dfs(i):
        # 순환구조이면 False
        if i in traced:
            return False
        
        # 이미 방문했던 노드라면 True
        if i in visited:
            return True
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        
        traced.remove(i)
        visited.add(i)
        
        return True
    
    for x in list(graph):
        if not dfs(x):
            return False
        
    return True
```

