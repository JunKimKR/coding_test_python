def solution(arr):
    arr = list(set(arr)) #set으로 중복제거 후 다시 리스트로(sort는 리스트만 됨. set에선 안됨.)
    arr.sort(reverse=True)
    return arr

print(solution([1,2,3,3,3,10,5,7,3,4,5,6,21]))