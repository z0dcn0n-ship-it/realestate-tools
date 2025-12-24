# realestate-tools

不動産物件の利回り計算・投資判断を自動化する Python ツール群です。  
CSV（Excel不要）を入力として、複数物件を一括評価し、  
「検討すべき物件」を自動で抽出・CSV出力できます。

---

## できること

- 物件価格・家賃・管理費から
  - 月手残り
  - 年手残り
  - 利回り（%）
- 利回り基準による自動判定
  - 検討（>= 5%）
  - 条件次第（>= 3%）
  - 見送り
- CSVから複数物件を一括評価
- 不正データ（欠損・文字混入）を自動スキップ
- 評価結果をCSVとして書き出し

---

## 使用技術

- Python 3.x
- 標準ライブラリ（csv）
- VS Code / macOS

※ Excel 不要

---

## ファイル構成

realestate-tools/
├─ yield_calc.py # Day1: Hello World
├─ basic_calc.py # 基本的な利回り計算
├─ evaluate.py # 関数化した評価ロジック
├─ bulk_evaluate.py # 複数物件の一括評価
├─ app.py # 入力式ミニアプリ
├─ csv_app.py # CSV読み込み・評価・書き出し
├─ properties.csv # サンプル物件データ
├─ results_all.csv # 全件評価結果（生成）
├─ results_kento.csv # 検討物件のみ（生成）

---

## 使い方（CSV一括評価）

1. `properties.csv` を用意

```csv
price,rent,fee
20000000,80000,5000
18000000,120000,10000
