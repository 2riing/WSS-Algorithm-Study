import sys
sys.stdin = open('input.txt')

def dfs(target, nodes):
    # -2 => 삭제한다는 뜻
    nodes[target] = -2
    for i in range(len(nodes)):
        # 삭제할 타겟을 부모로 가지고 있으면 삭제하는 dfs 실행
        if target == nodes[i]:
            dfs(i, nodes)

N = int(input())
nodes = list(map(int, input().split(' ')))
target_node = int(input())

dfs(target_node, nodes)
cnt = 0
for i in range(N):
    # 삭제된 노드가 아니면서, 누구의 부모도 아닌 리프노드의 개수 세기
    if nodes[i] != -2 and i not in nodes:
        cnt += 1

print(cnt)


