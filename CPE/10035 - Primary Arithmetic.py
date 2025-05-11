"""
Children are taught to add multi-digit numbers from right-to-left one digit at a time. Many find the
"carry" operation - in which a 1 is carried from one digit position to be added to the next - to be a
significant challenge. Your job is to count the number of carry operations for each of a set of addition
problems so that educators may assess their difficulty.

Input
Each line of input contains two unsigned integers less than 10 digits. The last line of input contains '0 0'.

Output
For each line of input except the last you should compute and print the number of carry operations
that would result from adding the two numbers, in the format shown below.

Sample Input
123 456
555 555
123 594
0 0

Sample Output
No carry operation.
3 carry operations.
1 carry operation.
"""

from itertools import zip_longest

while True:
    a, b = input().split()
    if a == '0' and b == '0':
        break

    # 將 a, b 反轉
    a = a[::-1]
    b = b[::-1]

    # 初始化
    carry = 0         # 統計有幾次 carry
    carry_next = 0    # 前一位是否有進位

    for digit_a, digit_b in zip_longest(a, b, fillvalue='0'):
        # 轉成整數
        d1 = int(digit_a)
        d2 = int(digit_b)

        # 加上上次的進位
        total = d1 + d2 + carry_next

        # 檢查是否進位
        if total >= 10:
            carry += 1
            carry_next = 1  # 下一位要加上這次的進位
        else:
            carry_next = 0

    # 輸出結果
    if carry == 0:
        print("No carry operation.")
    elif carry == 1:
        print("1 carry operation.")
    else:
        print(f"{carry} carry operations.")
