def convert(base_list):
    final_list = list()
    for n in base_list:
        final_n = round(float(n))
        final_list.append(final_n)
    print(final_list)
num_list = input().split(' ')
convert(num_list)