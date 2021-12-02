# 힙(Heap)



## 더 맵게

- 배열을 heapq로 만든 뒤, 문제 조건에 따라 두번 heappop을 하고 새 값을 만들어 배열에 다시 heappush하는 것을 반복한다.
- 다만 계속 반복해도 모든 음식의 스코빌 지수가 K 이상으로 올라가지 않을 경우 -1을 리턴해야 하므로 heap에 마지막 남은 원소하나가 K보다 큰지 작은지 판별하는 예외처리를 추가한다.

```python
def solution(scoville, K):
    import heapq
    # 힙 만들기
    heapq.heapify(scoville)
    
    # 예외 처리(배열이 비어있을 경우)
    if sum(scoville) == 0 and K > 0:
        return -1
    
    cnt = 0
    # 과정 반복(배열에 원소가 하나만 남을때까지)
    while len(scoville) > 1:
        p = heapq.heappop(scoville)
        # 최솟값이 K보다 작을 경우(모든 음식이 K 이상이 아님)
        if p < K:
            q = heapq.heappop(scoville)
            heapq.heappush(scoville, p+2*q)
            cnt += 1
        # 모든 음식이 K 이상임 -> break
        else:
            break
    
    # 모든 과정을 거쳤음에도 K 이상이 되지 않으면 -1 리턴
    if scoville[0] < K:
        return -1
    
    return cnt
```



## 디스크 컨트롤러

- 이 문제의 목적은 작업 요청부터 종료까지 걸린 시간의 평균을 최소화해야 하므로, 작업 요청부터 종료까지의 시간을 계산하여 heap에 넣은뒤, heappop으로 처리한 작업을 없애는 식으로 구현한다.

```python
import heapq
def solution(jobs):
    # 먼저 요청한 작업이 맨 뒤로 가게 정렬
    jobs.sort(reverse=True)
    result = 0
    length = len(jobs)
    
    # 요청받은 작업을 담아두는 heap
    on_request = []
    # 걸린 시간을 저장하는 변수
    time = 0
    
    # 모든 작업을 처리할때까지 반복문
    while jobs or on_request:
        # on_request에 해당 시간에 요청받은 작업 heappush
        while (not on_request) or (jobs and time >= jobs[-1][0]):
            job = jobs.pop()
            # 걸리는 시간을 기준으로 heappush
            heapq.heappush(on_request, [job[1], job[0]])
        
        # 처리할 작업을 heappop
        work = heapq.heappop(on_request)
        
        # 만약 요청받은 시간이 현재 시간보다 뒷 시간일 경우, time을 요청받은 시간으로 변경해주기
        if time < work[1]:
            time = work[1]
        
        # 걸린 시간을 time에 더해주고, 평균 시간을 구하기 위해 result에 요청부터 종료까지의 시간을 더해주기
        time += work[0]
        result += time - work[1]
    
    return int(result / length)
```



## 이중 우선순위 큐

- 최솟값을 pop할때는 heapify, heappop을 이용하고, 최댓값을 pop할때는 sort와 pop을 사용한다.
- heapify + heappop의 시간복잡도는 O(n) + O(1) = O(n), sort + pop의 시간복잡도는 O(n log n) + O(1) = O(n log n) 이므로, 전체 알고리즘의 시간복잡도는 평균적으로 추출 명령의 수가 K일때, O(K * n log n)일 것이다.
- 두개의 배열을 사용하는 방법도 생각해봤지만 두 배열에서 동일한 값을 지우는 과정에서 더 많은 시간이 소요될 것 같아 이 방식으로 변경했다.

```python
import heapq
def solution(operations):
    q = []
    
    for op in operations:
        op = op.split()
        if op[0] == 'I':
            q.append(int(op[1]))
        elif op[0] == 'D':
            if q:
                if op[1] == '1':
                    q.sort()
                    q.pop()
                else:
                    heapq.heapify(q)
                    heapq.heappop(q)

    if not q:
        return [0, 0]
    
    return [max(q), min(q)]
```

