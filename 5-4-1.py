#배열을 오름차순으로 정렬
def solution(arr):
    arr.sort()
    return arr 

#배열을 내림차순으로 정렬
def solution_rev(arr):
    arr.sort(reverse=True)
    return arr


arr = [1,2,10,4,6,3]
print(solution(arr))
print(solution_rev(arr))


#sort()메서드를 사용하지 않고 o(n**2)정렬 알고리즘을 사용하면?
import time
def bubble_sort(arr):#버블 정렬
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr

def do_sort(arr):#sort()함수
    arr.sort()
    return arr

def measure_time(func,arr): #시간을 측정하고 뒤집힌 배열 반환 
    start_time= time.time()
    result = func(arr)
    end_time = time.time()
    return end_time - start_time, result

arr = list(range(10000))

#첫 번째 코드 시간 측정
#첫 번째 코드 실행 시간 : 3.9616279602
bubble_time, bubble_result = measure_time(bubble_sort, arr)
print("첫 번째 코드 실행 시간: ", format(bubble_time, ".10f"))

#두 번째 코드 실행 시간: 0.0000560284
arr = list(range(10000))
reverse_time, reverse_result = measure_time(do_sort,arr)
print("두 번째 코드 실행 시간:", format(reverse_time,".10f"))

