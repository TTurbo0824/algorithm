# 프로그래머스 2019 KAKAO BLIND RECRUITMENT: 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    answer = [len(stages)] * N
    num = N + 1
    # 게임에 참여한 전체 인원
    total = len(stages)
    # 스테이지를 클리어한 누적 인원의 수
    acc = 0

    for i in range(num):
        # 1단계부터 시작하기 때문에 i + 1
        people = stages.count(i + 1)
        # (i + 1)이 stages의 최소값보다 작다면 (i + 1)단계를 클리어하지 못한 사람이 없다는 뜻 => 실패율 0
        if i + 1 < min(stages):
            answer[i] = 0
        elif i < N:
            # 도전한 사람이 있다면 실패율 계산
            if total - acc != 0:
                answer[i] = people / (total - acc)
            # 도전한 사람이 없다면 실패율 0
            else:
                answer[i] = 0
        acc += people

    answer = sorted(list(enumerate(answer)), key=lambda x: -x[1])
    answer = [x[0] + 1 for x in answer]

    return answer
