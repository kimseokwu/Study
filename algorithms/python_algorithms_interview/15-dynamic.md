# 다이나믹 프로그래밍

- 다이나믹 프로그래밍 알고리즘은 문제를 각각의 작은 문제로 나누어 해결한 결과를 저장해뒀다가 나중에 큰 문제의 결과와 합하여 풀이하는 알고리즘이다.
- 다이나믹 프로그래밍은 중복된 하위 문제들의 결과를 저장해뒀다가 풀이한다. 따라서 중복되지 않은 문제들은 다이나믹 프로그래밍으로 풀지 않는다.

- 다익스트라 알고리즘은 다이나믹 프로그래밍과 그리디 알고리즘 둘 다 해당하는 경우인데, BFS시 항상 최단 경로를 찾고 탐욕 선택 속성을 갖는 그리디 알고리즘이면서, 이미 계산한 경로는 저장해두었다가 활용하며 중복된 하위 문제들을 푸는 다이나믹 알고리즘이기도 하다.



__최적 부분 구조__

- 서울에서 부산까지 가는 최단 경로를 찾는다고 할때, 서울에서 대구까지 가는 최단 경로와 대구에서 부산까지 가는 최단 경로를 선택하면 풀 수 있다. 
- 이처럼 문제의 해결 방법이 부분 문제에 대한 최적 해결 방법으로 구성되는 구조를 최적 부분 구조라고 한다.



__다이나믹 프로그래밍 방법론__

- 방법론은 크게 상향식과 하향식으로 나뉜다. 일반적으로 상향식을 타뷸레이션, 하향식을 메모이제이션이라고 구분해 부르기도 한다.
- 상향식: 더 작은 하위 문제부터 살펴본 다음, 작은 문제의 정답을 이용해 큰 문제의 정답을 풀어나간다. 타뷸레이션이라고 부르며 일반적으로 이 방식만을 다이나믹 프로그래밍으로 지칭하기도 한다.
- 하향식: 하위 문제에 대한 정답을 계산했는지 확인하며 문제를 자연스러운 방식으로 풀이한다. 이 방식을 메모이제이션이라고 한다.



__피보나치 수열의 상향식과 하향식__

- 상향식

```python
def fib(n):
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```



- 하향식

```python
def fib(n):
    if n <= 1:
        return n
    if dp[n]:
        return dp[n]
    dp[n] = fib(n -1) + fib(n - 2)
    return dp[n]
```



### 피보나치 수열

- 피보나치 수를 구하라.
- 피보나치 수열을  구하는 가장 기본적인 풀이 알고리즘의 수도코드는 다음과 같다.

```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
```



__풀이 1. 메모이제이션__

- 앞서 설명에서 다이나믹 프로그래밍의 하향식 풀이로 정리한 것이 메모이제이션 풀이이다. 한번 계산한 수는 더이상 계산하지 않으므로 n이 5일 때, fib(2)와 fib(3)은 한번만 계산하게 되어 매우 효율적이다.

```python
class solution:
    dp = collections.defaultdict(int)
    
    def fib(n):
        if n <= 1:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]
```



__풀이 2. 타뷸레이션__

```python
class solution():
    dp = collections.defaultdict(int)
    
    def fib(n):
        self.dp[1] = 1
        
        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]
```



__풀이 3. 두 변수만 사용해서 풀이__

- 공간 복잡도를 O(n)에서 O(1)로 줄일 수 있고 시간 복잡도는 동일한 O(n)이다.

```python
def fib(n):
    x, y = 0, 1
    for i in range(0, n):
        x, y = y, x + y
    return x
```



### 0 -1 배낭문제

- 그리디 알고리즘으로 풀었던 배낭문제를 짐을 쪼갤 수 없는 0 - 1 배낭문제로 변경하면 그리디 알고리즘으로 풀 수 없어진다. 이 경우 모든 경우의 수를 계산해야 하며, 이렇게 모든 경우의 수를 계산하는 문제에서 다이나믹 프로그래밍은 위력을 발휘한다.

```python
def zero_one_knapsack(cargo):
    capacity = 15
    pack = []
    
    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] == c:
                pack[i].append(
                	max(
                		cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]], pack[i - 1][c]
                	))
            else:
                pakc[i].append(pack[i - 1][c])
```



### 최대 서브배열

- 합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라

> __예제__
>
> - 입력: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
> - 출력: 6



__풀이 1. 메모이제이션__

- 앞에서부터 계속 값을 계산하면서 누적 합을 계산한다. 이전 값을 계속 더해나가되 0이 이하가 되면 버린다. 어차피 최댓값을 찾는데 0 이하인 값은 굳이 서브 배열에 포함할 이유가 없기 때문이다.

```python
def solution(nums):
    for i in range(1, len(nums)):
        nums[i] += num[i - 1] if nums[i - 1] > 0 else 0
    return max(nums)
```



__풀이 2. 카데인 알고리즘__

- 이전 풀이에서는 매번 계산해서 넣기만 하고 마지막에 max()를 전체 계산해서 가져오게 했지만 카데인 알고리즘은 매번 best_sum을 계산한다.

```python
def solution(nums):
    best_sum = -sys.maxsize
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    
    return best_sum
```



### 계단 오르기

- 당신은 계단을 오르고 있다. 정상에 도달하기 위해 n계단을 올라야 한다. 매번 각각 1계단 또는 2계단씩 오를 수 있다면 정상에 도달하기 위한 방법은 몇 가지 경로가 되는지 계산하라.

> __예제__
>
> - 입력: 3
> - 출력: 3



__풀이 1. 재귀 구조 브루트 포스__

- n개의 계단을 오르는 방법의 수는 (n - 1)계단을 오르고 1 계단을 오르는 방법의 수와 (n - 2)계단을 오르고 2 계단을 오르는 방법의 수를 더한 것과 같으므로 피보나치 수와 비슷한 방법으로 풀이할 수 있다.
- 그러나 이 방법은 타임아웃으로 풀리지 않는다.

```python
def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return solution(n - 1) + solution(n - 2)
```



__풀이 2. 메모이제이션__

```python
class solution:
    dp = collections.defaultdict(int)
    
    def climbStairs(n):
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]
```



### 집도둑

- 당신은 전문 털이범이다. 어느 집에서든 돈을 훔쳐올 수 있지만 경보 시스템 때문에 바로 옆집은 훔칠 수 없고 한 칸 이상 떨어진 집만 가능하다. 각 집에는 훔칠 수 있는 돈의 액수가 입력값으로 표기되어 있다. 훔칠 수 있는 가장 큰 금액을 출력하라.

> __예제__
>
> - 입력: [1, 2, 3, 1]
> - 출력: 4



__풀이 1. 재귀구조 브루트포스__

- 바로 옆집은 훔칠 수 없으니 현재 집과 옆집 숫자 중의 최댓값을 구하고, 한 집 건넛집까지의 최댓값과 현재 집의 숫자값과의 합을 구해서 두 수 중 더 높은 값이 정답이 된다.

```python
def rob(nums):
    def _rob(int):
        if i < 0:
            return 0
        return max(_rob(i - 1), _rob(i - 2) + nums[i])
    return _rob(len(nums) - 1)
```



__풀이 2. 타뷸레이션__

- 알고리즘은 동일하지만 이미 계산한 값은 dp에 저장하고 두번 이상 계산하지 않는다.

```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    
    dp = collections.OrderedDict()
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i -1], dp[i - 2] + nums[i])
    
    return dp.popitem()[1]
```

