A = 30
B = 20
C = 10

is_a_greatest = A > B and A > C
is_b_middle = (B < A and B > C)
is_c_least = (C < A and C < B)

print("is_a_greatest:", is_a_greatest)
print("is_b_middle:", is_b_middle)
print("is_c_least:", is_c_least)