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

- 