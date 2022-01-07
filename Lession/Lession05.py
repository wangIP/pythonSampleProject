s1 = {3,4,5}
print(3 not in s1)
s2 = {4,5,6}
s3 = s1 & s2 #  兩個集合 相同資料
s3 = s1 | s2 #聯集 所有資料但不重複
s3 = s1 ^ s2 #反交集 不重複的資料輸出
s3 = set ("hello") 
print ("h" in s3) 
print(s3)
dic = {x:x*3 for x in [2,3,4]}
print(dic)