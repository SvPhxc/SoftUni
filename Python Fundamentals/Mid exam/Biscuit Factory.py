bsc_per_worker = int(input())
workers = int(input())
comp_bsc = int(input())
normal_day = 20 * bsc_per_worker * workers
third_day = 10 * (bsc_per_worker * 0.75) * workers
total_sum = normal_day + third_day
difference = total_sum - comp_bsc
percentage = difference / comp_bsc * 100
print(f"You have produced {int(total_sum)} biscuits for the past month.")
if percentage > 0:
    print(f"You produce {percentage :.2f} percent more biscuits.")
else:
    percentage_v2 = abs(percentage)
    print(f"You produce {percentage_v2:.2f} percent less biscuits.")
