snow_num = int(input())
best_sb_quality = 0
best_sb_data = ""
for i in range(snow_num):
    weight = int(input())
    time = int(input())
    quality = int(input())
    result = (weight / time) ** quality
    if result > best_sb_quality:
        best_sb_quality = result
        best_sb_data = f"{weight} : {time} = {int(result)} ({quality})"
print(best_sb_data)