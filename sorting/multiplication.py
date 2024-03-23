# traditional algorithm of multiplication
# takes n^2 multiply operations
# divide and conquer
# break x and y into first n/2 digits and last n/2 digits
# x = x1 * 10^(n/2) + x0
# y = y1 * 10^(n/2) + y0
# x * y = x1*y1*10^n + (x1*y0+x0*y1)*10^(n/2) + x0*y0
# T(n) = 4 * T(n/2) + cn, cn is cost of addition
# a = 4, b = 2, d = 1
# log(b,a) = log(2,4) = 2
# so T(n) = n^(log(b,a)) = n^2
# 