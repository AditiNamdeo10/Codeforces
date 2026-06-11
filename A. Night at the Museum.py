s=input()

curr='a'
ans=0

for ch in s:
    diff=abs(ord(ch)-ord(curr))
    ans+=min(diff,26-diff)
    curr=ch
print(ans)