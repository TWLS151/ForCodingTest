# 병사 번호와 버전 그리고 다음 노드(병사) 참조값
class Member():
    def __init__(self, id, version):
        self.id = id
        self.version = version
        self.next = None


class Team():
    def __init__(self):
        # 링크드 리스트
        self.groupByScore = [GroupByScore() for _ in range(6)]
        pass

    # 점수 갱신 함수
    # 팀 내 모든 점수 리스트를 score 만큼 옮긴다. 최대 5, 최소 1
    def update(self, score):
        newGroup = [GroupByScore() for _ in range(6)]
        for i in range(1, 6):
            idx = i + score
            if idx > 5:
                idx = 5
            elif idx < 1:
                idx = 1
            
            newGroup[idx].extend(self.groupByScore[i])
            
        self.groupByScore = newGroup

    # 최고점 리스트 내 최고 id 값 병사 탐색 함수
    def get_best(self):
        for i in range(5, 0, -1):
            if self.groupByScore[i].first == None:
                continue
        
            best = 0
            cur = self.groupByScore[i].first
            while cur:
                # 해고되지 않았고 더미데이터가 아니라면 값 갱신
                if not firedMemberList[cur.id] and version[cur.id] == cur.version:
                    best = max(best, cur.id)
                cur = cur.next

            # version 으로 인한 더미는 계산이 안됨.
            if best:
                return best
        # 모든 병사가 비활성화(해고) 되어 있으면 0 반환
        return 0

# 링크드 리스트
class GroupByScore():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, member):
        if self.first == None:
            self.first = member
            self.last = member
        else:
            self.last.next = member
            self.last = member
        self.size += 1
        pass

    def extend(self, other):
        if other.first == None:
            return
        if self.first == None:
            self.first = other.first
            self.last = other.last
            self.size = other.size
        else:
            self.last.next = other.first
            self.last = other.last
            self.size += other.size

        other.first = None
        other.last = None
        other.size = 0


"""
L = 제약
memberList = 전체 병사 명부
memberTeam = 각 병사의 팀
firedMemberList = 해고된 병사 id 명부
teams = 전체 팀 [ 내부는 점수 별 LinkedList 하나씩 총 5개 ]
    - teams[Team[LinkedList]]
version = 병사의 정보 갱신 횟수
"""

L = 100_001
memberList = [None] * L
memberTeam = [None] * L
firedMemberList = [False] * L
teams = [Team() for _ in range(6)]
version = [0] * L

# 초기화
def init():
    global memberList, memberTeam, firedMemberList, teams, version
    memberList = [None] * L
    memberTeam = [None] * L
    firedMemberList = [False] * L
    teams = [Team() for _ in range(6)]
    version = [0] * L
    pass

# 병사 고용
# 추후 노드를 삭제하는 비용이 너무 커서 version 리스트를 만들고 version 이 다르면 더미데이터, 말소 취급
# 둘이 같아야만 살아있는 데이터로 판단
def hire(mID, mTeam, mScore):
    version[mID] += 1
    member = Member(mID, version[mID])
    memberList[mID] = member
    memberTeam[mID] = mTeam
    teams[mTeam].groupByScore[mScore].add(member)
    pass

# 병사 해고
def fire(mID):
    firedMemberList[mID] = True
    pass

# 병사 개인 평판 업데이트
# 변동이 생겼으니 version 올리고 변동 적용, 팀 내 새 점수 리스트에 add
# 기존 데이터는 더미 취급
def updateSoldier(mID, mScore):
    version[mID] += 1
    member = Member(mID, version[mID])
    memberList[mID] = member
    teams[memberTeam[mID]].groupByScore[mScore].add(member)
    pass

# 팀 내 전체 점수 업데이트
def updateTeam(mTeam, mChangeScore):
    teams[mTeam].update(mChangeScore)
    pass

# 팀 내 최고점 그룹 내 최고 id 번호 반환
def bestSoldier(mTeam):
    return teams[mTeam].get_best()

# 소스코드와 같은 디렉토리에 input.txt 파일을 생성해서 거기에 입력을 넣은 뒤 아래 주석을 지우면 편하게 실행 가능합니다 :)
fs = open("input.txt", "r")
input = fs.readline

CMD_INIT = 1
CMD_HIRE = 2
CMD_FIRE = 3
CMD_UPDATE_SOLDIER = 4
CMD_UPDATE_TEAM = 5
CMD_BEST_SOLDIER = 6

def run():
    isCorrect = False
    numQuery = int(input())

    for i in range(numQuery):
        line = list(map(int, input().split()))
        cmd = line[0]

        if cmd == CMD_INIT:
            init()
            isCorrect = True
        elif cmd == CMD_HIRE:
            mID, mTeam, mScore = line[1], line[2], line[3]
            hire(mID, mTeam, mScore)
        elif cmd == CMD_FIRE:
            mID = line[1]
            fire(mID)
        elif cmd == CMD_UPDATE_SOLDIER:
            mID, mScore = line[1], line[2]
            updateSoldier(mID, mScore)
        elif cmd == CMD_UPDATE_TEAM:
            mTeam, mChangeScore = line[1], line[2]
            updateTeam(mTeam, mChangeScore)
        elif cmd == CMD_BEST_SOLDIER:
            mTeam = line[1]
            userAns = bestSoldier(mTeam)
            ans = line[2]

            # print(userAns, ans)

            if userAns != ans:
                isCorrect = False
        else:
            isCorrect = False

    return isCorrect

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print(f'#{tc} {score}')
