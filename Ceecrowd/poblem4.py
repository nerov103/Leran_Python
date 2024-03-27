scent = int(input()) # this is my main scent

minets = scent // 60 #convrt to minet
# minets = minets % 60
scent = scent%60 #exta secent
hour = minets // 60 # this ismy hour
minets = minets % 60

# print("Hour:",hour)
# print("Minet:",minets)
# print("Scent:",scent)
print(f"{hour}:{minets}:{scent}") 

# x = "nerov"
# x = "python"
# print(x)
# print(x)
# print(x)
# print(x)