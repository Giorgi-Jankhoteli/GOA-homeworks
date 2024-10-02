Grade = int(input("ნუგზარის ნიშანი: "))
is_A = Grade >= 9
is_B = Grade >= 8 and Grade < 9
is_C = Grade >= 7 and Grade < 8
is_D = Grade >= 6 and Grade < 7
is_F = Grade < 6
print(is_A)
print(is_B)
print(is_C)
print(is_D)
print(is_F)