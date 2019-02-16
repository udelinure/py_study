s = "Let's take LeetCode contest"
s = s.split(" ")
for i in range(len(s)):
  s[i] = s[i][::-1]
print " ".join(s)
