# 힙

- 힙은 힙의 특성(최소 힙에서는 부모가 항상 자식보다 작거나 같다)을 만족하는 거의 완전한 트리인 특수한 트리 기반의 자료 구조다.

- 최소 힙은 부모가 항상 자식보다 작기 때문에 루트가 결국 가장 작은 값을 갖게 되며, 우선순위 큐에서 가장 작은 값을 추출하는 것은 매번 힙의 루트를 가져오는 형태로 구현된다.
- 힙은 부모노드가 항상 작다는 조건만 만족할 뿐, 왼쪽 노드와 오른쪽 노드에 대한 관계는 정의하지 않는다.
- 자식이 둘인 힙은 특별히 이진 힙이라고 하며, 대부분은 이진 힙이 널리 사용된다.



# 힙 연산

__삽입__

1. 요소를 가장 하위 레벨의 최대한 왼쪽으로 삽입한다.(배열로 표현할 경우 가장 마지막에 삽입)
2. 부모 값과 비교해 값이 더 작은 경우 위치를 변경한다.
3. 계속해서 부모 값과 비교해 위치를 변경한다.

- 시간복잡도는 O(log n)이다.

__추출__

- 추출은 루트를 추출하면 된다. 하지만 추출 후 힙의 특성을 유지해야 하기 때문에 시간 복잡도는 O(log n)이다.
- 추출 이후 비어 있는 노드엔 가장 마지막 요소가 올라가게 되고 자식 노드와 값을 비교해서 자식보다 크다면 내려가는 다운 힙 연산이 수행된다.



```python
class BinaryHeap():
    def __init__(self):
        self.items = [None]
    
    def __len__(self):
        return len(self.items) - 1
    
    # 삽입 시 실행, 반복 구조 구현
    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent
            parent = i // 2
    
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()
        
    # 추출시 실행, 재귀 구조 구현
    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx
        
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
        
        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self._percolate_down(smallest)
        
    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted
```





### 배열의 k번째 큰 요소

- 정렬되지 않은 배열에서 k번째 큰 요소를 추출하라.

> __예제__
>
> - 입력: [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
> - 출력: 4



__풀이 1. heapq 모듈 사용__

```python
def solution(nums, k):
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)
    
    for _ in range(1, k):
        heapq.heappop(heap)
    
    return -heapq.heappop(heap)
```



__풀이 2. heapq 모듈의 nlargest 이용__

```python
def solution(nums, k):
    return heapq.nlargest(k, nums)[-1]
```

- k번째만큼 큰 값이 가장 큰 값부터 순서대로 리스트로 리턴된다. 여기서 마지막 인덱스 -1이 k번째 값이 된다. nsmallest()를 사용하면 동일한 방식으로 n번째 작은 값도 추출할 수 있다.



__풀이 3. 정렬을 이용한 풀이__

- __추가, 삭제가 빈번할 때__는 heapq를 이용한 힙정렬이 유용하지만 입력값이 고정되어 있을 때는 한번 정렬하는 것만으로 충분하다.

```python
def solution(nums, k):
    return sorted(nums, reverse=True)[k - 1]
```



# 트라이

- 트라이(trie)는 검색 트리의 일종으로 일반적으로 키가 문자열인, 동적 배열 또는 연관 배열을 저장하는 데 사용되는 정렬된 트리 자료구조다.
- 검색을 뜻하는 retrieval의 중간음절에서 따왔다.
- 이진 트리가 아니라 다진 트리의 형태를 띈다.

- 트라이는 문자 단위로 색인을 구축한 것과 유사하다. 문자열의 길이만큼 탐색하면 원하는 결과를 찾을 수 있다.



### 트라이 구현

- 트라이의 insert, search, startswith 메소드를 구현하라.



__풀이 1. 딕셔너리를 이용해 간결한 트라이 구현__

```python
# 트라이의 노드
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # 단어 삽입
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True
    
    # 단어 존재 여부 판별
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.childeren:
                return False
            node = node.childeren[char]
        return node.word
    
    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True  
```



### 팰린드롬 페어

- 단어 리스트에서 word[i] + word[j]가 팰린드롬이 되는 모든 인덱스 조합(i, j)를 구하라.

> __예제__
>
> - 입력: ['abcd', 'dcba', 'lls', 's', 'sssll']
> - 출력: [[0, 1], [1, 0], [3, 2], [2, 4]]



__풀이 1. 팰린드롬을 브루트 포스로 계산__

- n^2번 반복하면서 모든 조합을 구성하고 매번 팰린드롬 여부인지 체크한다. 하지만 효율적이지 않아 타임아웃이 발생한다.

```python
def solution(words):
    def is_palindrome(word):
        return word == word[::-1]
    
    output = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                output.append([i, j])
    
    return output
```



__풀이 2 . 트라이 구현__

- 이 문제를 O(n)으로 풀기 위해선 모든 단어를 트라이로 만들어 두고 한 번씩만 탐색하는 문제로 변형할 것이다.
- 팰린드롬을 판별해야 하기 때문에, 뒤집어서 트라이로 구성하면 해법을 찾을 수 있다.
- 문자를 뒤집은 다음, 문자 단위로 계속 내려가며 트라이를 구현하고 단어가 끝나는 지점에는 단어 인덱스를 word_id로 부여한다.
- 판별 로직은 삽입 중에 남아 있는 단어가 팰린드롬이라면 미리 팰린드롬 여부를 세팅해 두는 방법이다.
- 예를 들어 'cbbc'는 단어 자체가 팰린드롬이므로 루트에 바로 입력값의 인덱스인 p = 4를 셋팅하고, word[0:len(word) - i] 형태로 단어에서 문자수를 계속 줄여 나가며 팰린드롬 여부를 체크한다.
- 문자가 하나만 남게 될 때는 항상 팰린드롬이므로 마찬가지고 p = 4를 마지막에 셋팅한다. 당연히 이 마지막 값은 항상 w의 앞 노드가 된다.

```python
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    @staticmethod
    def is_palindrome(word):
        return word[::] == word[::-1]
    
    # 단어 삽입
    def insert(self, index, word):
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0: len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index
        
    def search(self, index, word):
        result = []
        node = self.root
        
        while word:
            # 판별 로직
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
        
        # 판별 로직
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
        
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        
        return result
    
class Solution:
    def palindromePairs(words):
        trie = Trie()
        
        for i, word in enumerate(words):
            trie.insert(i, word)
        
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
        return result
        
```

