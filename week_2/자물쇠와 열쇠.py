'''
* 문제 유형 : 구현

* 체감 난이도 : *****

* 아이디어 1
  - 주어진 key의 크기만큼 확장한 배열(maps)에 key를 전부 대입해서 lock이 풀리는지 확인
  - key는 회전이 가능하기 때문에 4가지 방향에 대해서 전부 수행
  - 매번 maps에 새로운 key위치를 대입해야하기 때문에 check할때마다 maps를 deepcopy를 통해 복사
  - ex) lock = 1 1 1  key = 0 0 0
               1 1 0        1 0 0
               1 0 1        0 1 1
               
        maps = 0 0 0 0 0 0 0
               0 0 0 0 0 0 0
               0 0 1 1 1 0 0
               0 0 1 1 0 0 0
               0 0 1 0 1 0 0
               0 0 0 0 0 0 0
               0 0 0 0 0 0 0
        key를 (0,0)에서 (2,2)까지, (0,1)에서 (2,3)까지, ... , (5,5)에서 (7,7)까지 전부 대입하면서 확인
  
'''



import copy

def solution(key, lock):
    answer = True
    n, m = len(lock), len(key)
    length = n + ((m-1) * 2)
    
    # lock이 열리는지 확인하기 위한 함수
    def check(i, j):
        # 현재 key가 시작되는 위치부터 tmp_maps에 key값 추가
        for x, kx in zip(range(i, i+m), range(m)):
            for y, ky in zip(range(j, j+m), range(m)):
                tmp_maps[x][y] += key[kx][ky]
        
        # tmp_maps의 lock 부분의 값이 1이 아니라면 돌기부분끼리 중복되었거나 홈이라는 뜻이므로 return False
        for i in range(m-1, m+n-1):
            for j in range(m-1, m+n-1):
                if tmp_maps[i][j] != 1:
                    return False
        
        return True
    
    # key 배열을 회전시키기 위한 함수 - 오른쪽 90도 회전
    def rotation(key):
        tmp_key = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                tmp_key[j][(m-1)-i] = key[i][j]
        
        return tmp_key
    
    # 확장된 크기를 가지는 maps 생성
    maps = [[0] * length for _ in range(length)]
    
    # maps 의 가운데 부분 즉, lock이 들어갈 부분에 lock 대입
    for i, li in zip(range(m-1, m+n-1), range(n)):
        for j, lj in zip(range(m-1, m+n-1), range(n)):
            maps[i][j] = lock[li][lj]
    
    # key의 4가지 방향에 대해서 수행
    for _ in range(4):
        key = rotation(key)
        
        for i in range(length-m+1):
            for j in range(length-m+1):
                # 매번 key가 초기화 되어야 하기 때문에 deepcopy수행 -> 시간이 오래걸림
                tmp_maps = copy.deepcopy(maps)
                if check(i, j):
                    return True
    
    return False
