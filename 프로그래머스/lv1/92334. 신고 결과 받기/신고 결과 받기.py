def solution(id_list, report, k):
    reportList = { id: [] for id in id_list }
    user = { id: 0 for id in id_list }
    
    # id 별 신고자 목록
    for s in set(report):
        reporter, reported = s.split()
        reportList[reported].append(reporter)
    
    # 신고 메일 카운트
    for u, l in reportList.items():
        if len(l) >= k:
            for r in l:
                user[r] += 1
        
    return list(user.values())