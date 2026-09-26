# -*- coding: utf-8 -*-
"""Bai tap 1: Loc ra nhom can ho lon.

Doc bo du lieu, dem so can co dien tich lon hon 100 met vuong,
roi tinh gia trung binh cua rieng nhom can do.
"""

import pandas as pd

df = pd.read_csv("data/gia_nha.csv")

# Loc bang dieu kien dung sai (boolean mask): giu lai nhung dong
# co dien_tich lon hon 100.
nhom_lon = df[df["dien_tich"] > 100]

so_can_lon = len(nhom_lon)
gia_trung_binh_nhom_lon = nhom_lon["gia"].mean()

print(f"So can co dien tich lon hon 100 m2: {so_can_lon}")
print(f"Gia trung binh cua nhom can do : {gia_trung_binh_nhom_lon:.4f} ty dong")
