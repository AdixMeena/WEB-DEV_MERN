arr = [1,2,3,4]
min = arr[0]*100+arr[1]*10+arr[2]
max = arr[len(arr)-1]*100+arr[len(arr)-2]*10+arr[len(arr)-3]
count = 0
for i in range(min , max , 1):
    if i % 2 == 0:
        count+=1

print(count)

print(max-min)