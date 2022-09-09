from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    reportList = { id: set() for id in id_list }
    user = defaultdict(int)
    
    # id 별 신고자 목록
    for i in range(len(report)):
        reporter, reported = report[i].split()
        reportList[reported].add(reporter)
    
    # 신고 메일 카운트
    for u, s in reportList.items():
        if len(s) >= k:
            for r in s:
                user[r] += 1
                
    # answer 배열 만들기
    for id in id_list:
        answer.append(user[id])
        
    return answer