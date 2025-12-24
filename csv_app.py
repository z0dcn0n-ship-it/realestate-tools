import csv

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

    return {
        "price": price,
        "rent": rent,
        "fee": management_fee,
        "monthly_net": monthly_net,
        "annual_net": annual_net,
        "yield_rate": yield_rate,
        "decision": decision,
    }

results = []
with open("properties.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        rent = float(row["rent"])
        fee = float(row["fee"])
        results.append(evaluate_property(price, rent, fee))

# 利回りが高い順
results = sorted(results, key=lambda x: x["yield_rate"], reverse=True)

print("=== 全物件（利回り順） ===")
for r in results:
    print("----")
    print(f"価格: {r['price']:,.0f} 円")
    print(f"利回り: {r['yield_rate']:.2f} %")
    print("判断:", r["decision"])

print("\n=== 検討のみ ===")
for r in results:
    if r["decision"] == "検討":
        print(f"価格 {r['price']:,.0f} 円 / 利回り {r['yield_rate']:.2f} %")
