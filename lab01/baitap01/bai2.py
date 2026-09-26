# -*- coding: utf-8 -*-
"""Bai tap 2: Ve bieu do phan tan theo so phong.

Truc hoanh la so_phong, truc tung la gia. Luu hinh ra tep bai2.png
roi in nhan xet ve xu huong nhin thay.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/gia_nha.csv")

so_phong = df["so_phong"]
gia = df["gia"]

plt.figure(figsize=(8, 6))
plt.scatter(so_phong, gia, color="tab:blue", label="60 can nha")
plt.xlabel("So phong ngu")
plt.ylabel("Gia (ty dong)")
plt.title("Gia nha theo so phong ngu")
plt.legend()

# Luu hinh truoc khi goi show, vi show se dong hinh lai.
plt.savefig("baitap01/figures/bai2.png", dpi=150)
plt.show()

print(
    "Nhan xet: cac cham nhin chung cung di len tu trai sang phai, "
    "nghia la can co nhieu phong ngu hon thi thuong co gia cao hon. "
    "Tuy nhien cac cham khong bam sat mot duong thang nhu bieu do "
    "theo dien tich, vi voi cung mot so phong van co nhieu muc gia "
    "khac nhau (do dien tich va tuoi nha cua tung can khac nhau)."
)
