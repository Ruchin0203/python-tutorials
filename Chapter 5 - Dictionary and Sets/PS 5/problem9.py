# 9. Can you change the values inside a list which is contained in set S? s = {8, 7, 12, "Harry", [1,2]}
   
s = {8, 7, 12, "Harry", [1,2]}

s[4][0] = 8

# It can't change. Because itrequire all their element to be immutable and hashable.
