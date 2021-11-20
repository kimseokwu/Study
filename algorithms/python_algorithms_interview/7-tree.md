# 트리

- 트리는 계층형 트리 구조를 시뮬레이션 하는 추상 자료형으로 루트 값과 부모 자식 관계의 서브트리로 구성되며, 서로 연결된 노드의 집합이다.
- 트리의 중요한 속성 중 하나는 재귀로 정의된 자기 참조 자료구조라는 점이다. 트리는 자식도 트리고 그 자식도 트리다.,



__트리의 각 명칭__

- 트리는 항상 __루트(root)__에서부터 시작된다, 루트는 __자식(child)__ 노드를 가지며 __간선(edge)__으로 연결되어 있다. 자식 노드의 개수는 __차수(degree)__라고 하며, __크기(size)__는 자신을 포함한 모든 자식 노드의 개수다. __높이(height)__는 현재 위치부터 __리프(leaf)__까지의 거리, __깊이(depth)__는 루트에서부터 현재 노드까지의 거리다. __레벨(level)__은 0부터 시작한다. 트리는 항상 단방향이기 때문에 간선의 화살표는 생략 가능하다.



__그래프 vs 트리__

- 트리는 __순환구조를 갖지 않는__ 그래프이다.

- 또한 트리는 부모노드에서 자식노드를 가리키는 단 방향 노드 뿐이다.
- 트리는 하나의 부모 노드를 갖는다는 차이점이 있고 루트도 하나여야 한다.



__이진 트리__

- 트리 중에서도 가장 널리 사용되는 트리 자료구조는 이진 트리와 이진 탐색트리(binary search tree)다. 모든 노드의 차수가 2 이하일 경우를 이진 트리라고 부른다.

- 이진트리의 유형
  - full binary tree: 모든 노드가 0개 또는 2개의 자식 노드를 갖는다
  - complete binary tree: 마지막 레벨을 제외하고 모든 레벨이 완전히 채워져 있으며 마지막 레벨의 모든 노드는 가장 왼쪽부터 채워져 있다.
  - perfect binary tree: 모든 노드가 2개의 자식 노드를 갖고 있으며 모든 리프 노드가 동일한 깊이 또는 레벨을 갖는다.



### 이진트리의 최대 깊이

- 이진트리의 최대 깊이를 구하라. [3, 9, 20, null, null, 15, 7]가 주어졌을 때, 깊이는 3이다.



__풀이 1. 반복 구조로 BFS 풀이__

- 길이 depth는 while 구문의 반복 횟수이므로 BFS에서 반복 횟수는 곧 높이가 된다. 이제 반복 횟수를 리턴하면 최종 결과를 구할 수 있다.

```python
solution(root):
    if root is None:
        return 0
    queue = collections.deque([root])
    depth = 0
    
    while queue:
        depth += 1
        # 큐 연산 추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
   
	# BFS 반복 횟수 = 깊이
    return depth
```





### 이진 트리의 직경

- 이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라.



__풀이 1. 상태값 누적 트리 DFS__

- 가장 긴 경로를 찾는 방법은 먼저 가장 말단, 즉 리프 노드까지 탐색한 다음 부모로 거슬러 올라가면서 각각의 거리를 계산해 상태값을 업데이트 하면서 누적하여 찾아간다.
- 최종적으로 가장 긴 경로의 길이는 왼쪽 자식 노드의 상태값과 오른쪽 자식 노드의 상태값의 합에 2를 더한 값이다.

```python
class solution():
    longest = 0
    
    def diameterOfBinaryTree(root):
        def dfs(node):
            if not node:
                return -1
            
            # 왼쪽, 오른쪽 각 리프노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            
            # 상대값
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
```

- 리스트나 딕셔너리와 같은 자료형은 append()등의 메소드를 이용해 재할당 없이 조작이 가능하지만 숫자나 문자는 불변 객체이기 때문에 중첩함수 내에서는 값을 변경할 수 없다.



### 가장 긴 동일 값의 경로

- 동일한 값을 지닌 가장 긴 경로를 찾아라.

__풀이 1. 상태값 거리 계산 DFS__

- 트리의 말단 리프노드까지 DFS로 탐색해 내려간 다음, 값이 일치할 경우 거리를 쌓아 올라가며 백트래킹한다.

```python
class longestUnivaluePath():
    result = 0

    def solution(node):
        def dfs(node):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)

        dfs(root)
        return self.return
```

 

### 이진 트리 반전

- 중앙을 기준으로 이진트리를 반전하라.



__풀이 1. 파이썬다운 방식__

```python
def solution(root):
    if root:
        root.left, root.right = self.solution(root.right), self.solution(root.left)
        return root
    return None
```

- 재귀가 마지막 노드까지 갔을 때부터, None을 return하고 스왑이 일어난다.



__풀이 2. 반복 구조로 BFS__

```python
def solution(root):
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left
            
            queue.append(node.left)
            queue.append(node.right)
    
    return root
```

- 재귀 풀이가 가장 말단 노드까지 내려가서 백트래킹하며 스왑하는 방식이라면 이 풀이는 부모 노드부터 스왑하면서 계속 내려가는 하향 방식 풀이다.



__풀이 3. 반복 구조로 DFS__

```python
def solution(root):
    stack = collections.deque([root])
    
    while queue:
        node = stack.pop()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left
            
            stack.append(node.left)
            stack.append(node.right)
    
    return root
```



### 두 이진트리 병합

- 두 이진 트리를 병합하라. 중복되는 노드는 값을 합산한다.

  

__풀이 1. 재귀탐색__

```python
def solution(t1, t2):
    if t1 and t2:
        node = Treenode(t1.val + t2.val)
        node.left = solution(t1.left, t2.left)
        node.right = solution(t1.right, t2.right)
        return node
    else:
        return t1 or t2
```

- 각 이진 트리의 루트부터 시작해 합쳐 나가면서 좌, 우 자식 노드 또한 병합될 수 있도록 각 트리 자식 노드를 재귀호출 한다. 만약 어느 한쪽 노드가 없다면 존재하는 노드만 리턴하고 재귀호출을 진행하지 않는다.



### 이진 트리 직렬화 & 역직렬화

- 이진 트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라.



__풀이 1. 직렬화 & 역직렬화 구현__

- 이진 트리 데이터 구조는 논리적인 구조이다. 이를 파일이나 디스크에 저장하기 위해서는 물리적인 형태로 바꿔줘야 하는데, 이를 직렬화라고 한다.
- 파이썬에는 pickle이라는 직렬화 모듈을 기본으로 제공한다. 이 모듈의 이름으로 인해 파이썬 객체의 계층 구조를 바이트 스트림으로 변경하는 작업을 피클링이라고도 한다.



__직렬화__

- BFS를 이용해 직관적으로 구현한다.

```python
def serialize(root):
    queue = collections.deque([root])
    result = ['#']
    # 트리 BFS 직렬화
    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)
            
            result.append(str(node.val))
        else:
            result.append('#')
    
    return ' '.join(result)
```



__역직렬화__

- 왼족 자식과 오른쪽 자식에 각각 별도의 인덱스르 부여하여 nodes를 탐색한다.

```python
def deserialize(data):
    # 예외 처리
    if data == '# #':
        return None
    
    nodes = data.split()
    
    root = TreeNode(int(nodes[1]))
    queue = collections.deque([root])
    index = 2
    # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
    while queue:
        node = queue.popleft()
        if nodes[index] is not '#':
            node.left = TreeNode(int(nodes[index]))
            queue.append(node.left)
        index += 1
        
        if nodes[index] is not '#':
            node.right = TreeNode(int(nodes[index]))
            queue.append(node.right)
        index += 1
        
    return root
```



### 균형 이진트리

- 이진트리가 높이 균형인지 판단하라. 높이 균형은 모든 노드의 서브 트리 간의 높이 차이가 1 이하인 것을 말한다.

__풀이 1. 재귀 구조로 높이차이 계산__

- 재귀로 노드의 높이를 출력하면서 왼쪽과 오른쪽의 높이 차이가 1 이상나면 false를 리턴한다.

```python
def solution(root):
    def check(root):
        if not root:
            return 0
        
        left = check(root.left)
        right = check(root.right)
        # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    
    return check(root) != -1
```



### 최소높이 트리

- 노드의 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록을 리턴하라.

> __예시__
>
> - 입력: n = 4, edge = [[1, 0], [1, 2], [1, 3]]
> - 출력: [1]



__풀이 1. 단계별 리프노드 제거__

- 최소 높이를 구성하려면 가장 가운데에 있는 값이 루트여야 한다. 이 말은 리프 노드를 하나씩 제거해 나가면서 남아 있는 값을 찾으면 이 값이 가장 가운데에 있는 값이 될 수 있다는 것이다.
- 리프노드는 그래프에서 해당 키의 값이 1개뿐인 것을 말한다.

```python
def solution(n, edge):
    if n <= 1:
        return [0]
    
    # 양방향 그래프 구성
    graph = collections.defaultdict(list)
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    
    # 첫번째 리프 노드 추가
    leaves = []
    for i in range(n + 1):
        if len(graph[i]) == 1:
            leaves.append(i)
    
    # 루트 노드만 남을 때까지 반복 제거
    while n < 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves
        
    return leaves
```





# 이진 탐색 트리(BST)

- 노드의 왼쪽 서브트리에는 그 노드의 값보다 작은 값들을 지닌 노드들로 이뤄져 있는 반면, 노드의 오른쪽 서브트리에는 그 노드의 값과 같거나 큰 값들을 지닌 노드로 이루어져 있는 트리
- 탐색 시 시간복잡도가 O(log n)이다.



__자가 균형 이진 탐색 트리__

- 자가 균형 이진 탐색 트리는 삽입, 삭제시 자동으로 높이를 작게 유지하는 노드 기반의 이진 탐색 트리다.
- 자가 균형 이진 탐색트리는 최악의 경우에도 이진 트리의 균형이 잘 맞도록 유지한다. 높이를 최대한 낮게 유지하는 것이 중요하다는 것이다.



### 정렬된 배열의 이진 탐색 트리 변환

- 오름차순으로 정렬된 배열을 높이 균형 이진 탐색 트리로 변환하라.
- 이 문제에서 높이 균형이란 모든 노드의 두 서브 트리 간 깊이 차이가 1 이하인 것을 말한다.



__풀이 1. 이진 검색 결과로 트리 구성__

```python
def solution(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    
    # 분할 정복으로 이진 검색 결과 트리 구성
    node = TreeNode(nums[mid])
    node.left = solution(nums[:mid])
    node.right = solution(nums[mid + 1:])
    
    return node
```



### 이진 탐색 트리를 더 큰 수 합계 트리로

- BST의 각 노드를 현재값보다 더 큰 값을 가진 모든 노드의 합으로 만들어라.



__풀이 1. 중위 순회로 노드 값 누적__

- 자신보다 같거나 큰 값을 구하려면 자기 자신을 포함한 우측 자식 노드의 합을 구하면 된다.
- 루트를 입력받았을 때 먼저 맨 오른쪽까지 내려가고 그 다음 부모 노드, 다시 왼쪽 노드 순으로 이동하ㅕㄴ서 자신의 값을 포함해 누적한다.

```python
class solution:
    val = 0
    
    def bstToGst(root):
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        
        return root
```



### 이진 탐색 트리 합의 범위

- 이진 탐색 트리가 주어졌을 때 L 이상 R 이하의 값을 지닌 노드의 합을 구하라.

> __예제__
>
> - 입력: root = [10, 5, 15, 3, 7, null, 18], L = 7, R = 15
> - 출력: 32



__풀이 1. 재귀 구조 DFS로 브루트 포스 탐색__

- DFS로 전체를 탐색한 다음 노드의 값이 L과 R 사이일 때만 값을 부여하고 아닐 경우에는 0을 취해 계속 더해 나가면 쉽게 구할 수 있다.

```python
def solution(root, L, R):
    if not root:
        return 0
    
    return (root.val if L <= root.val <= R else 0) + solution(root.left, L, R) + solution(root.right, L, R)
```



__풀이 2. DFS 가지치기로 필요한 노드 탐색__

- DFS로 탐색하되 L, R의 조건에 해당되지 않은 가지를 쳐내는 형태로 탐색에서 배제하도록한다.
- 현재 root가 L보다 작을 경우 더 이상 왼쪽 가지는 탐색할 필요가 없기 때문에 오른족만 탐색하도록 재귀 호출을 리턴한다.

```python
def solution(root, L, R):
    def dfs(node):
        if not node:
            return 0
        
        if node.val < L:
            return dfs(node.right)
        elif node.val > R:
            return dfs(node.left)
        return node.val + dfs(node.left) + dfs(node.right)
    
    return dfs(root)
```



### 이진 탐색 트리 노드간 최소 거리

- 두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라.

> __예제__
>
> - 입력: root = [4, 2, 6, 1, 3, null, null]
> - 출력: 1



__풀이 1. 재귀 구조로 중위 순회__

- 중위 순회를 하면서 이전 탐색 값과 현재 값을 비교한다.

```python
class solution:
    prev = -sys.maxsize
    result = sys.maxsize
    
    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(root):
        if root.left:
            self.minDiffInBST(root.left)
        
        self.result = min(self.result, root.val - self.prev)
        self.prev = result.val
        
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.result
```



# 트리 순회

- 트리 순회란 그래프 순회의 한 형태로 트리 자료구조에서 각 노드를 정확히 한 번 방문하는 과정을 말한다.
- 이진 트리에서 DFS는 노드의 방문 순서에 따라 다음과 같이 크게 3가지 방식으로 구분된다.
  - 전위 순회(pre - order): 현재 노드를 먼저 순회한 다음 왼쪽, 오른쪽 서브트리 순회
  - 중위 순회(in - order): 왼쪽 서브트리를 순회한 후 현재 노드, 오른쪽 서브트리 순회
  - 후위 순회(post - order): 왼쪽과 오른쪽 서브트리를 순회한 다음 현재 노드 순회



__전위 순회__

```python
def preorder(node):
	if node is None:
    	return
    print(node.val)
    preorder(node.left)
    preorder(node.right)
```



__중위 순회__

```python
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)
```



__후위 순회__

```python
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)
```



### 전위, 중위 순회 결과로 이진트리 구축

- 전위, 중위 순회 결과를 입력값으로 받아 이진 트리를 구축하라.



__풀이 1. 전위 순회 결과로 중위 순회 분할 정복__

- 전위 순회의 첫번째 결과는 중위 순회 결과를 왼쪽과 오른쪽으로 분할 시키는 역할을 한다. 이를 이용해 중위 순회의 분할 정복 문제로 바꾼다.
- 전위 순회의 두번째 노드는 중위 순회의 왼쪽 결과를 정확히 반으로 가른다.
- 이후 남아 있는 노드들을 계속 분할을 시도한다.

```python
def solution(preorder, inorder):
    if inorder:
        # 전위 순회 결과는 중위 순회 분할 인덱스
        index = inorder.index(preorder.pop(0))
        
        # 중위 순회 결과 분할 정복
        node = TreeNode(inorder[index])
        node.left = solution(preorder, inorder[0:index])
        node.right = solution(preorder, inorder[indes + 1:])
        
        return node
```

