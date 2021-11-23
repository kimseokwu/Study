# 이진검색

- 이진 검색이란 정렬된 배열에서 타겟을 찾는 검색 알고리즘이다.
- 이진 검색은 시간복잡도가 O(log n)이라는 점에서 대표적인 로그 알고리즘이며 이진 탐색트리와도 유사한 점이 많다.



### 이진 검색

- 정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾아라

> __예제__
>
> - 입력: nums = [-1, 0, 3, 5, 9, 12], target = 9
> - 출력: 4



__풀이 1. 재귀 풀이__

- 절반씩 범위를 줄여나가며 맞출 때까지 계속 재귀 호출한다.

```python
def solution(nums, target):
    def binary_search(left, right):
        if left <= right:
            mid = (left + right) // 2
            
            if nums[mid] > target:
                binary_search(mid + 1, right)
            elif nums[mid] < target:
                binary_search(left, mid - 1)
            else:
                return mid
        else:
            return -1
    return binary_search(0, len(nums) - 1)
```



__재귀 제한__

- 파이썬에는 재귀 호출에 대한 호출 횟수 제한이 있으며 기본 값은 1000으로 설정되어 있다.



__풀이 2. 반복 풀이__

```python
def solution(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] > target:
            left = mid + 1
        elif nums[mid] < target:
            right = mid - 1
        else:
            return mid
     return -1
```



__풀이 3. 이진 검색 모듈__

- 파이썬은 이진 검색 알고리즘을 지원하는 bisect 모듈을 기본으로 제공한다. 여러가지 예외 처리를 포함한 이진 검색 알고리즘을 지원한다. 

```python
def solution(nums, target):
    index = bisect.bisect_left(nums, target)
    
    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1
```





### 회전 정렬된 배열 검색

- 특정 피벗을 기준으로 회전하여 정렬된 배열에서 target값의 인덱스를 출력하라.

> __예제__
>
> - 입력: nums = [4, 5, 6, 7, 0, 1, 2], target = 1
> - 출력: 5



__풀이 1. 피벗을 기준으로 한 이진 검색__

- 정렬이 되어 있긴 한데 피벗을 기준으로 입력값이 돌아간 상황이다. 먼저 피벗을 찾아야 이진 검색을 할 수 있다. 예제 입력값의 경우 피벗은 4다.
- 가장 작은 값을 찾는다면 해당 위치의 인덱스가 피벗이 될 수 있다.
- 최솟값 인덱스 left를 찾아내 pivot에 할당하고 이를 기준으로 mid를 피벗만큼 틀어 mid_pivot을 구성한다.
- mid_pivot = (mid + pivot) % len(nums)



```python
def solution(nums, target):
    # 예외 처리
    if not nums:
        return -1
    
    # 최솟값을 찾아 피벗 설정
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    pivot = left
    
    # 피벗 기준 이진 검색
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_pivot = (mid + pivot) % len(nums)
        
        if nums[mid_pivot] < target:
            left = mid + 1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot
    
    return -1
```



### 두 배열의 교집합

- 두 배열의 교집합을 구하라

> __예제__
>
> - 입력: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
> - 출력: [2]



__풀이 1. 이진 검색으로 일치 여부 판별__

- 한쪽은 순서대로 탐색하고 다른 쪽은 정렬해서 이진 검색으로 값을 찾는다.

```python
def solution(nums1, nums2):
    result = set()
    nums2.sort()
    for n1 in nums1:
        # 이진 검색으로 일치 여부 판별
        i2 = bisect.bisect_left(nums2, n1)
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)
            
        return result
```



__풀이 2. 투 포인터로 일치 여부 판별__

- 양쪽 다 정렬하여 투 포인터로 풀이할 수도 있다.

```python
def solution(nums1, nums2):
    result = set()
    
    # 양쪽 모두 정렬
    nums1.sort()
    nums2.sort()
    
    i = j = 0
    
    # 투 포인터 우측으로 이동하며 일치 여부 판별
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1
    
    return result
```





### 두 수의 합

- 정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라. 이 문제에서 배열은 0이 아닌 1부터 시작하는 것으로 한다.

> __예제__
>
> - 입력: numbers = [2, 7, 11, 15], target = 9
> - 출력: [1, 2]



__풀이 1. 투 포인터__

- 단순히 두 수의 합은 투 포인터로 풀 수 없지만 이 문제는 입력 배열이 정렬되어 있으므로 투 포인터로도 풀 수 있다.
- 투 포인터 풀이의 경우 O(n)에 풀이할 수 있다.

```python
def solution(numbers, target):
    left, right = 0, len(numbers) - 1
    while not left == right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numsbers[left] + numbers[right] > target:
            right -= 1
        else:
            return left + 1, right + 1
```



__풀이 2. 이진 검색__

- 현재 값을 기준으로 나머지 값이 맞는지 확인하는 형태의 이진 검색 풀이를 한다.

```python
def solution(number, target):
    for k, v in enumerate(numbers):
        left, right = k + 1, len(numbers) - 1
        expected = target - v
        # 이진 검색으로 나머지 값 판별
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] < expected:
                left = mid + 1
            elif numbers[mid] > expected:
                right = mid - 1
            else:
                return k + 1, mid + 1
```



__풀이 3. bisect 모듈__

- bisect_left()는 lo와 hi를 통해 좌우 범위를 제한할 수 있다.

```python
def solution(numbers, target):
    for k, v in enumerate(numbers):
        expected = target - v
        i = bisect.bisect_left(numbers, expected, k + 1)
        if i < len(numbers) and numbers[i] == expected:
            return k + 1, i + 1
```



__슬라이싱 성능__

- 슬라이싱은 매번 새롭게 객체를 생성해서 할당하고 엄청나게 큰 배열의 경우 슬라이싱으로 새로운 객체를 생성하는 데 상당한 시간이 든다.
- 마찬가지로 배열의 길이를 계산하는 데도 매번 길이를 계산하는 비용이 들어서 상당한 시간이 소요된다.
- 슬라이싱을 하게 되면 전체 객체를 복사하게 되고 이 과정에서 시간이 들게 된다.



### 2D 행렬 검색

- m * n 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라. 행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순으로 정렬되어 있다.

> __예제__
>
> - 입력:
>
> [
>
> ​	[1, 4, 7, 11, 15],
>
> ​	[2, 5, 8, 12, 19],
>
> ​	[3, 6, 9, 16, 22],
>
> ​	[10, 13, 14, 17, 24],
>
> ​	[18, 21, 23, 26, 30]
>
> ]



__풀이 1. 첫 행의 맨 뒤에서 탐색__

- 이 문제는 열을 기준으로 이진 검색을 수행한 다음 찾아낸 값을 기준으로 해당 위치의 각 행을 기준으로 다시 이진검색을 수행하면 해결할 수 있다.

- 첫 행의 맨 뒤 요소를 택한 다음 타겟이 이보다 작으면 왼쪽으로, 크면 아래로 이동하게 한다.

```python
def solution(matrix, target):
    # 예외처리
    if not matrix:
        return False
    
    # 첫 행의 맨 뒤
    row = 0
    col = len(matrix[0]) - 1
    
    while row <= len(matrix) - 1 and col >= 0:
        if target == matrix[row][col]:
            return True
        # 타겟이 작으면 왼쪽으로 이동
        elif target < matrix[row][col]:
            col -= 1
        # 타겟이 크면 아래로 이동
        elif target > matrix[row][col]:
            row += 1
    
    return False
```



__풀이 2. 파이썬다운 방식__

```python
def solution(matrix, target):
    return any(target in row for row in matrix)
```

- 내부적으로 행렬에 값이 존재하는지 여부를 위에서부터 차례대로 한 줄씩 탐색하게 될 것이다.
- any()는 하나라도 True라면 True를 출력하고, all()는 모든 값이 참이어야 True를 출력한다.