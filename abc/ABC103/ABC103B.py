# String Rotation
s = list(input())
t = list(input())
s_ = s
for i in s:
    if s_ != t:
        s_ += s[0]
        del s_[0]
    else:
        print('Yes')
        exit()
print('No')
