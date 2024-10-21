#!/usr/bin/env python
# coding: utf-8

# # Q1 ~ Q3 Evaluating Points on Elliptic Curve

# In[129]:


import time, random, hashlib


# In[124]:


# Define the elliptic curve for secp256k1
E = EllipticCurve(GF(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F), [0, 7])
G = E.gen(0)  # Base point


# In[2]:


# Calculate 4G
result_4G = 4*G
result_4G


# In[3]:


# Calculate 5G
result_5G = 5*G
result_5G


# In[58]:


# Calculate Q=dG
start_1 = time.time()
d = 1142 # my ID is b09901142
Q = d*G
end_1 = time.time()
print((end_1 - start_1))
Q


# In[115]:


Q


# # Q4 Standard Double and Add

# In[36]:


print(binary[2:])


# In[130]:


# 1 on bit 10,6,5,4,2,1


# In[66]:


current_point = G
double = 0
add = 0
start_2 = time.time()
# Apply the decomposition
for power in range(9,-1,-1):
    current_point = 2*current_point
    double += 1
    if power in [6, 5, 4, 2, 1]:  # Add G at these powers
        current_point = current_point + G
        add += 1
end_2 = time.time()
print(end_2 - start_2)

(current_point, double, add)


# In[70]:


binary = bin(d)
binary = binary[2:]

double = 0
add = 0

for bit in binary[1:]:
    double += 1
    if bit == '1':
        add += 1

print(double, add)
        


# In[133]:


# test time from P to -P
current_point2 = current_point
start = time.time()
current_point2 = -current_point2
end = time.time()
print((end-start))


# # Q5 Fastest Computing

# In[143]:


# 1142 = 2^10 + 2^7 - 2^3 - 2^1
current_point2 = G
double = 0
add = 0
start_3 = time.time()

# Apply the decomposition
for power in range(9,-1,-1):
    current_point2 = 2*current_point2
    double += 1
    if power in [3,1]:  # subtract G at these powers
        current_point2 = current_point2 - G
        add += 1
    elif power == 7:
        current_point2 = current_point2 + G
        add += 1
end_3 = time.time()
print(end_3 - start_3)

(current_point2, double, add)


# In[144]:


current_point2 = G
double = 0
add = 0

pos = list()
neg = list()
start_3 = time.time()
# Apply the decomposition
for power in range(1,11):
    current_point2 = 2*current_point2
    if power in [3,1]:  # subtract G at these powers
        neg.append(current_point2)
    elif power in [7,10]:
        pos.append(current_point2)
ans = pos[0] + pos[1] - neg[0] - neg[1] 
end_3 = time.time()
print(end_3 - start_3)

ans


# # Q6 Bitcoin Transaction Signature

# In[145]:


# Step 0
d_a = d
n = E.order()
m = "Sample Bitcoin Transaction Signing"

# Step 1
e = int(hashlib.sha256(m.encode()).hexdigest(), 16)

# Step 2
Ln = len(bin(n)[2:])
z = int(str(e)[:Ln])
random.seed(int(40))
k = random.randint(1,n-1)

# Step 3
(x1,y1) = (k*G).xy()
r = lift(x1) % n

# Step 4
s = ((z + r*d) * inverse_mod(k, n)) % n

# print("My Bitcoin Transaction Signature is")
(r,s)


# # Q7 Bitcoin Transaction Verification

# In[138]:


# Step 1
assert((1 <= r and r <= n-1) and (1 <= s and s <= n-1))

e_ver = int(hashlib.sha256(m.encode()).hexdigest(), 16)
# Step 2
Ln = len(bin(n)[2:])
z = int(str(e_ver)[:Ln])

w = inverse_mod(s, n) % n
u1 = (z*w) % n
u2 = (r*w) % n


# Step 3
(x2,y2) = (u1*G + u2 * Q).xy()
r2 = lift(x2) % n

# Step 4
assert(r2 == x1)

print("Verified")


# # Q8 Quadratic Polynomial

# In[123]:


R = PolynomialRing(Zmod(10007), 'x')
x = R.gen()
p = R.lagrange_polynomial([(1, 10), (2, 20), (3, 1142)])
p

