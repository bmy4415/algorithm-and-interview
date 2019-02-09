### 자구
- 스택, 큐, 해쉬테이블
- binary tree
- heap, tree 만드는 방법 및 시간복잡도

### 알고리즘
- 시간복잡도 분석
- 각종 정렬 다시 공부(시간복잡도 및 수도코드)
- binary search
- k번째 원소 선택

### 컴구
- page fault 해결 방법
- page table 크기가 매우 큰데 어떻게 할 것인지?
- page와 page table이란 무엇인가

### OS
- process, thread 차이
- lock, race condition, dead lock, live lock
- 파일시스템

#### hash table
- search를 위한 자료구조
- key -> value mapping
- 구현
	- array와 hash function을 이용한 구현
		- close addressing(channing) => index값이 같은 경우 해당 index에서 이어나감(한개의 bucket에 들어갈 수 있는 key 수가 제한되어 있지 않음)
			- linked list + hash function
				- 해당 index에 linked list의 시작 포인터를 저장
				- 이후 같은 index에 대하여 insert, delete 시 linked list에서 insert, delete 수행
			- tree + hash function
				- linked list 대신 tree를 이용
				- linked list의 경우 search, insert, delete에 O(N)의 시간이 걸리는 반면에 tree에서는 O	(logN)의 시간이 걸림(JDK1.8의 경우 해당 index에 node가 8개 이상일 경우 tree 사용한다고함), 	collision이 많은 경우 linked list보다 tree가 효율적일 수 있음
		- open addressing => index값이 같은 경우 새로운 index를 찾아서 값을 넣음(한개으 bucket에 하나의 key만 들어감)
			- close addressing에 비하여 공간 효율적이지 않음(고정size array 를 초기에 할당)
			- linear probing
				- collision이 일어나는 경우 다음 index을 linear하게 변화시켜 구함
				- 특정 index 주변에 hash값이 몰려있는 경우 비효율적임(primary clustering)
			- quadratic probing
				- collision이 일어나는 경우 다음 index를 제곱 폭으로 변화시켜 구함
				- 최초 hash값이 몰리는 경우 비효율적임(secondary clustering)
			- double hashing
				- 다음 index를 구하는 폭도 hash를 이용하여 다양하게 해줌, 즉 첫 hash값을 위한 함수 h1과 probe 폭을 구하기 위한 함수 h2 총 2개의 hash 함수를 이용


	- tree를 이용한 구현
		- key를 이용하여 tree를 만듬(skewed가 아니라 balanced한 것으로, 그래야 search속도가 보장되므로)
		- tree에서의 search, insert, delete 시간은 O(logN)
		- 평균 탐색 시간은 array와 hash function을 이용한 구현에 비하여 느릴 수 있으나 space측면에서 더 적게 사용 할 수 있고(미리 많은 공간은 잡지 않아도 됨) key에 대하여 순차적 접근이 가능함


#### balanced binary search tree (full bst, complete bst)
	- TODO) search, insert, delete 시간복잡도 및 구현
		- abc



#### linked list
- array에 비하여 갖는 장점
	- 동적 size 사용 가능
	- 새로운 element insert, delete시 array의 경우에는 shift해야하는데 linked list는 pointer만 바꾸면 됨
- array에 비하여 갖는 단점
	- random access 불가능 => n번째 node의 값을 가져오는데에 O(n)시간 걸림
	- 모든 node가 다음 node에 대한 pointer를 갖으므로 memory낭비가 조금 있다
- doubly linked list
	- 연결 방향이 단방향이 아니라 양방향임
	- 양방향 포인터를 가지고 있으므로 단방향 linked list에 비하여 메모리를 조금 더 사용
- circular linked list
	- head의 prev가 tail이고 tail의 next가 head인 양방향 linked list


#### stack
- LIFO(Last In First Out)을 구현한 자료구조
- pop, peek, push, isEmpty를 구현해야함
- push, pop 상수시간에 수행
- 재귀알고리즘에 사용할 수 있음

#### queue
- FIFO(Last In Last Out)을 구현한 자료
- enqueue(뒤에 추가), dequeue(앞에서 꺼냄), isEmpty
- enqueue, dequeue 상수시간에 수행
- bfs에 사용 가능

#### tree
- tree: cycle이 없는 그래프인 동시에 임의의 두 node에 대하여 경로가 1개만 존재하는 그래프
- binary tree: 모든 node에 대하여 children의 수가 2개 이하인 tree
- binary search tree: 모든 노드에 대하여 노드 왼쪽의 값 < 노드의 값 < 노드 오른쪽의 값인 binary tree(중복값 처리는 상황마다 다를 수 있음)
- complete binary tree: 모든 높이에서 node가 꽉차있는 binary tree, leaf level은 꽉차지 않아도 되지만 대신 왼쪽부터 비어있는 곳이 없도록 차있어야함
- full binary tree: 모든 node의 children이 0개 또는 2개인 binary tree
- travelsal
	- TODO

#### heap
- complete binary tree이며 부모node의 값이 항상 자식node의 값보다 큰(max-heap)/작은(min-heap) tree
- 두 자식node의 크기는 중요하지 않음(부모node와 자식node 사이의 관계만 중요)
- root는 가장 큰(max-heap)/작은(min-heap) 값임
- 주요 operation
	- 삽입
		- complete binary tree의 조건을 맞추기 위해 가장 밑 height의 가장 오른쪽 원소의 오른쪽에 추가
		- 추가한 원소에 대하여 값이 부모node의 값보다 크거나/작으면 부모node와 자리를 변경
		- root까지 해당 변경을 시도
	- 삭제(root 삭제)
		- root와 맨 마지막 node를 바꿈(한개를 제거하려면 맨 마지막 원소가 사라져야하고, root는 사라질 것이므로)
		- root부터 자식 node와 대소관계를 확인하면 자식node가 크거나/작으면 부모node와 변경
		- 위의 작업을 leaf까지 계속함
- 시간복잡도
	- 삽입 => O(logN) (최악의 경우 높이만큼 swap 일어남)
	- 삭제 => O(logN) (최악의 경우 root부터 leaf까지 swap 일어남)


#### dfs
- Depth First Search(깊이 우선 탐색)
- 모든 node를 방문하고자 할 때 종종 사용됨
- recursive하게 구현 가능
- 방문 node는 check를 해야함

#### bfs
- Breadth First Search(너비 우선 탐색)
- 두 node의 최단경로 또는 경로는 찾을 때 종종 사용됨
- queue로 구현

#### 양방향 탐색(biriectional search)
- TODO


#### graph
- bfs, dfs


#### overloading vs overriding
- TODO

#### dynamic programming
- 큰 문제를 해결하기위해 작은 문제를 해결하고 그 결과를 다시이용하는 방법, 즉 이미 해결했던 문제를 반복해서 해결하는 것을 줄여서 시간복잡도에서 이득을 봄
- 주로 이전에 해결했던 문제를 table 등에 값을 저장해 놓아서 재사용
	- **table에 저장되는 값이 무엇인지를 생각하면 table과 알고리즘을 생각할 수 있음**
- ex) 피보나치, 행렬 곱 순서문제, LCS(longest common substring), LCS(longest common subsequence)
- TODO: 피보나치
- TODO: 행렬곱 순서 문제
- LCS
	- longest common substring
		- table[i][j] = length of suffix between X[:i] and Y[:j]
		- table의 가장 큰 값이 lcs의 길이이며 lcs string은 lcs의 길이값을 같는 table의 위치에서 대각선 방향으로 값이 0이될 때 까지 따라가면 됨
	- longest common subsequence
		- table[i][j] = length of subsequence between X[:i] and Y[:j]
		- table의 가장 마지막값인 table[len(X)][len(Y)]가 lcs의 length 값임
		- lcs string은 여러개가 있을 수 있는데, table의 맨 마지막 값 부터 시작해서
			- X[i] == Y[j]이면 X[i]에 해당하는 character를 string의 마지막에 포함
			- X[i] != Y[j]이면 left(table[i-1][j])와 right(table[i][j-1])의 값을 비교하여
				- 같으면 양쪽 길을 모두 따라가고
				- 다르면 큰쪽을 따라가면됨
		- lcs string은 길이 나뉘어도 결국에 중복된 string이 나올 수 있으므로, set으로 처리

#### race condition
- https://medium.com/@ahaljh/%EB%8F%99%EC%8B%9C%EC%84%B1-%EA%B4%80%EB%A0%A8-%EA%B0%9C%EB%85%90-d2f3e6a62b99 참고
- 여러 thread가 공유자원(ex) 메모리)에 동시에 접근하는 상황
- 발생할 수 있는 문제(counter 예시)
	- thread1과 thread2가 num이라는 변수에 접근하여 num++를 하고 싶음
	- thread1과 thread2가 각각 num++ 작업을 한번 씩 하면 num이 2 증가해야함
	- num++ 라는 operation을 사실은 3가지 operation으로 이루어져있음
		1. num의 값을 가져옴(read)
		2. 가져온 num의 값에 1을 더함
		3. 2의 결과를 num에 다시 저장함(write)
	- num=0으로 초기화 되어있을 때 다음과 같은 scenario가 발생할 경우 num이 1만 증가함
		1. thread1이 num의 값을 가져옴
		2. thread1이 num에 1을 더함
		3. context switch(thread1 -> thread2), thread1 write를 하지 않았으므로 아직 num의 값은 바뀌지 않음
		4. thread2가 num의 값을 가져옴(아직 num의 값은 바뀌지 않았으므로 num=0)
		5. thread2가 num의 값에 1을 더함
		6. thread2가 5의 결과를 num에 저장(num = 1)
		7. context switch(thread2 -> thread1)
		8. thread1이 2의 결과를 num에 저장(num = 1)
		9. thread1과 thread2가 각각 num++을 수행하였으나 num의 값은 1만 증가하였음
- race condition에서 발생하는 inconsistency 문제를 해결하기 위해 lock을 사용할 수 있음
	- 공유 자원(여기서는 num의 memory 값)에 lock을 걸어서 lock을 소유한 thread만이 값을 write할 수 있음


#### page fault
- 가상메모리란?
	- 실제 메모리보다 더 큰 메모리를 사용하는듯한 illusion을 주기위한 방법
		- disk(느린 장치)의 도움을 받아서 결과적으로 더 많은 메모리를 사용하는듯한 illusion을 줌
	- 각 프로세스는 각자의 가상메모리 공간을 가짐
		- A 프로세스의 0x123 주소와 B 프로세스의 0x123 주소는 실제메모리에서 전혀 다른 주소임
	- software level에서는 (충분히 큰) 가상메모리만 이용하면 됨
	- 가상메모리와 실제메모리의 mapping은 page table이 해줌
	- 즉 프로세스 마다 가상메모리 공간과 page table을 가짐
	- 가상메모리의 단위를 page라고함, 주로 4kb크기 page를 이용
	- 이것이 가능한 이유는 하나의 process를 실행할 때, 모든 영역이 다 메모리에 올라와있지 않고 필요한 부분만 올라와도 실행에 문제가 없기 때문
	- 실제메모리에는 page들이 올라와있고 내가 필요한 page가 메모리에 없을때(= disk에 있을때)는 disk의 page와 실제메모리의 page를 교체함(page replacement)
	- 참조의 spatial/temporal locality 때문에 실제로 페이지 교체는 자주 일어나지 않음
	- high level programming을 하면서 보는 모든 주소는 다 virtual address(가상메모리 주소)임
- page
	- 가상메모리를 구성하는 단위
	- page의 크기가 너무 작으면 I/O빈도가 늘어나고 page의 크기가 너무 크면 fraction이 커짐
	- 주로 4kb크기 page를 이용
- page table
	- 가상메모리 주소와 실제메모리 주소의 mapping정보를 가진 table
	- 메모리에 위치
	- page table의 cache 역할을 하는 것이 TLB(table lookaside buffer)
	- TLB는 MMU에 위치함
- page fault handling scenario
	- cpu가 특정 memory address(가상메모리 주소)에 접근을 요구함
	- MMU(memory management unit)이 TLB를 확인
		- TLB에 있을 경우 실제메모리로 접근
		- TLB에 없을 경우 page table을 확인
			- page table에 등록조차 되어있지 않은 주소면 잘못된 주소이므로 process 종료
			- page table에 등록되어 있는 주소인데 해당 page가 메모리에 없으면(즉 disk에 있다면) disk에서 메모리로 해당 page를 upload함, 이때 메모리에 여유공간이 있으면 바로 upload가 가능하지만 여유공간이 없다면 disk로 옮겨야할 page를 정해야함 => page replacement algorithm
		- page table에 등록되어있는 가상메모리 주소인 경우 TLB에 update하고 실제메모리로 접근
- demand paging
	- 프로세스를 실행하기위한 모든 주소영역을 메모리에 다 올리는 것이 아니라 필요할 때 마다 메모리에 올리는 것
- page replacement algorithm
	- page fault에 의해 실제메모리에 올라온 page를 교체할 때 필요한 algorithm
	- 주로 LRU(least recently used) 이용
		- 사용하지 않은지 가장 오래된 것을 버림
- copy on write
	- 부모 프로세스에서 자식 프로세스를 clone 할 때, 자식 프로세스에서 write하기 전에는 부모 프로세스와 같은 실제메모리의 page를 이용하고, 자식 프로세스에서 write가 생겼을 때, 새로운 page를 할당해서 자식 프로세스에게 제공함으로써 메모리 공간을 절약할 수 있음
- multi-level page table
	- page table의 크기를 줄이기위해 page table을 다시 paging하는 방법
	- 32bit, 4kb page 크기인 시스템의 경우
		- 전체 page의 갯수 => 2^32(전체 주소 공간) / 2^12(page 1개의 크기) = 2^20개의 page
		- page table entry의 크기 => 페이지 번호(20bit) + 페이지 내부 offset(12bit == page의 크기) = 32bit = 4byte
		- 프로세스별 page table의 크기 = PTE 크기 * PTE 갯수 = 4byte * 2^20 = 4MB
	- PTE의 페이지 번호(20bit) = level1 page번호(10bit) + level2 page번호(10bit)
		- level1 page는 2^10개
		- 각 level1 page마다 2^10개의 PTE를 갖음
		- level1 page는 모두 사용중인 것이 아니므로 level1 page가 사용중이지 않은 page들에 해당하는 level2 page공간은 아직 필요가 없음 => page table이 너무 커지는 문제에 어느정도 기여
