def evaluate_property(price, rent, management_fee):
    monthly_net = rent - management_fee
    annual_net = monthly_net * 12
    yield_rate = annual_net / price * 100

    if yield_rate >= 5:
        decision = "検討"
    elif yield_rate >= 3:
        decision = "条件次第"
    else:
        decision = "見送り"

    return monthly_net, annual_net, yield_rate, decision


print("=== 不動産評価ツール ===")

price = float(input("物件価格(円): "))
rent = float(input("月家賃(円): "))
fee = float(input("管理費(円): "))

monthly_net, annual_net, rate, decision = evaluate_property(price, rent, fee)

print("\n--- 結果 ---")
print(f"月手残り: {monthly_net:,.0f} 円")
print(f"年手残り: {annual_net:,.0f} 円")
print(f"利回り: {rate:.2f} %")
print("判断:", decision)
