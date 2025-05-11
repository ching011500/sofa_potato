"""
Your job is, given a positive number N, determine if it is a multiple of eleven.

Input  
The input is a file such that each line contains a positive number. A line containing the number ‘0’ is the end of the input.  
The given numbers can contain up to 1000 digits.

Output  
The output of the program shall indicate, for each input number, if it is a multiple of eleven or not.

Sample Input  
112233  
30800  
2937  
323455693  
5038297  
112234  
0

Sample Output  
112233 is a multiple of 11.  
30800 is a multiple of 11.  
2937 is a multiple of 11.  
323455693 is a multiple of 11.  
5038297 is a multiple of 11.  
112234 is not a multiple of 11.
"""

# x = int(input())

# if x % 11 == 0:
#     print(f"{x} is a multiple of 11.")
# else:
#     print(f"{x} is not a multiple of 11.")

while True:
    s = input().strip()  # 讀入一行，移除換行與空白
    if s == '0':         # 題目規定：0 是結束的訊號
        break

    total = 0            # 初始化加總值
    for i, digit in enumerate(s):  # 一位一位走過字串中的數字
        if i % 2 == 0:             # 偶數位置（第1,3,5,...位）
            total += int(digit)
        else:                      # 奇數位置（第2,4,6,...位）
            total -= int(digit)
            
    # 判斷差值是否能被 11 整除
    if total % 11 == 0:
        print(f"{s} is a multiple of 11.")
    else:
        print(f"{s} is not a multiple of 11.")
