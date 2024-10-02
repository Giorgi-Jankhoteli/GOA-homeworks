P = True 
Q = False

P_and_not_Q = P and not Q
not_P_and_Q = P or not Q
P_xor_Q = (P and not Q) or (not P and Q)

print(P_and_not_Q)
print(not_P_and_Q)
print(P_xor_Q)