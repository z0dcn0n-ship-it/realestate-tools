def evaluate_preoperty(price, rent, management_fee):
    monthly_net = rent - management_fee
    annual_net = monthly_net * 12
    yield_rate = annual_net / price * 100

    if yield_rate >= 5:
        decision = "検討"
    elif yield_rate >= 3:
        decision = "条件次第"
    else:
        decision = "見送り"

    return {
        "price": price,
        "rent": rent,
        "fee": management_fee,
        "monthly_net": monthly_net,
        "annual_net": annual_net,
        "yield_rate": yield_rate,
        "decision": decision
    }

properties = [
    {"price": 20000000, "rent": 80000, "fee": 5000},
    {"price": 18000000, "rent": 120000, "fee": 10000},
    {"price": 25000000, "rent": 70000, "fee": 5000},
    {"price": 16000000, "rent": 90000, "fee": 5000},
]

results = []
for p in properties:
    result = evaluate_preoperty(p["price"], p["rent"], p["fee"])
    results.append(result)

#利回りが高い順に並び替え
results = sorted(results, key=lambda x: x["yield_rate"], reverse=True)

for r in results:
    print("----")
    print (f"価格: {r['price']:,.0f} 円")
    print(f"利回り: {r['yield_rate']:.2f} %")
    print("判断:", r["decision"])