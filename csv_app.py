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
    for i, row in enumerate(reader, start=1):
        try:
            price = float(row["price"])
            rent = float(row["rent"])
            fee = float(row["fee"])
        except (ValueError, KeyError) as e:
            print(f"[警告] {i}行目スキップ: {e} / {row}")
            continue

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

# ===== CSV書き出し =====
import csv

# 全結果を書き出し
with open("results_all.csv", "w", newline="") as f:
    fieldnames = ["price", "rent", "fee", "monthly_net", "annual_net", "yield_rate", "decision"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for r in results:
        writer.writerow(r)

# 検討のみを書き出し
with open("results_kento.csv", "w", newline="") as f:
    fieldnames = ["price", "yield_rate", "decision"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for r in results:
        if r["decision"] == "検討":
            writer.writerow({
                "price": r["price"],
                "yield_rate": r["yield_rate"],
                "decision": r["decision"]
            })
