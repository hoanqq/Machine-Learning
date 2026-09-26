# -*- coding: utf-8 -*-
"""Bai tap 3: Doi bien dau vao sang tuoi_nha.

Dung lai cong thuc binh phuong toi thieu o muc 5 cua tai lieu,
nhung doi bien dau vao tu dien_tich sang tuoi_nha. Bien can du
doan van la gia.
"""

import numpy as np
import pandas as pd

df = pd.read_csv("data/gia_nha.csv")
x = df["tuoi_nha"].to_numpy()
y = df["gia"].to_numpy()

x_tb = x.mean()
y_tb = y.mean()

# Cong thuc binh phuong toi thieu cho duong thang mot bien
tu_so = ((x - x_tb) * (y - y_tb)).sum()
mau_so = ((x - x_tb) ** 2).sum()

w = tu_so / mau_so
b = y_tb - w * x_tb

print(f"Trung binh tuoi nha : {x_tb:.4f}")
print(f"Trung binh gia : {y_tb:.4f}")
print()
print(f"He so goc w = {w:.6f}")
print(f"He so chan b = {b:.6f}")
print()
print(f"Mo hinh: gia = {w:.6f} * tuoi_nha + {b:.6f}")

print()
print(
    "Nhan xet: he so goc w mang dau am, nghia la nha cang gia (tuoi_nha "
    "cang lon) thi gia du doan cang thap. Dieu nay khop voi hieu biet "
    "thong thuong, vi nha moi bang giao thuong duoc dinh gia cao hon "
    "nha da xay lau nam do hao mon va khau hao theo thoi gian."
)
