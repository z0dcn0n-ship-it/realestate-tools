price = 18000000.    #物件価格（円）
rent = 120000.         #月家賃（円）
management_fee = 0 #管理費(円)

monthly_ent = rent - management_fee
annual_ent = monthly_ent * 12
yield_rate = annual_ent / price * 100

print("月手残り(円):", monthly_ent)
print("年手残り(円):", annual_ent)
print("手残り利回り(%):", yield_rate)

#判定ロジック
if yield_rate >= 5:
    decision = "検討"
elif yield_rate >= 3:
    decision = "条件次第"
else:
    decision = "見送り"

print("判断:", decision)