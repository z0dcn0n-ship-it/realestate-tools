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


# テスト（3パターン）
cases = [
    (20000000, 80000, 5000),
    (18000000, 120000, 10000),
    (25000000, 70000, 5000),
]

for price, rent, fee in cases:
    monthly_net, annual_net, rate, decision = evaluate_property(price, rent, fee)
    print("----")
    print(f"価格: {price:,.0f} 円")
    print(f"家賃: {rent:,.0f} 円 / 管理費: {fee:,.0f} 円")
    print(f"月手残り: {monthly_net:,.0f} 円")
    print(f"年手残り: {annual_net:,.0f} 円")
    print(f"利回り: {rate:.2f} %")
    print("判断:", decision)
