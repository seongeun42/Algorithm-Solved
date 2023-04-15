def solution(prices):
    leng = len(prices)
    answer = [i for i in range(leng - 1, -1, -1)]
    st = [0]
    for i in range(1, leng):
        while st and prices[st[-1]] > prices[i]:
            j = st.pop()
            answer[j] = i - j
        st.append(i)
    return answer