# -*- coding: utf-8 -*-
"""Bai tap 5: Thu hai toc do hoc khac.

Chay lai gradient descent voi toc do hoc 0.001 va 1.02, giu nguyen
so_vong = 200 nhu tai lieu. Ghi lai MSE o vong 200 cua moi lan roi
giai thich vi sao chung khac nhau.

Phan lam them: thu them toc do hoc 0.5 va 0.9 de do ranh gioi giua
chay duoc va hong.
"""

import numpy as np
import pandas as pd

df = pd.read_csv("data/gia_nha.csv")
x_goc = df["dien_tich"].to_numpy()
y = df["gia"].to_numpy()

# Dua dien tich ve thang do nho quanh so 0, giong het muc 7 cua tai lieu.
x_tb = x_goc.mean()
x_do_lech = x_goc.std()
x = (x_goc - x_tb) / x_do_lech

n = len(x)
so_vong = 200


def chay_gradient_descent(toc_do_hoc):
    """Chay gradient descent voi mot toc do hoc cho truoc.

    Tra ve MSE tai vong lap cuoi cung (vong 200).
    """
    w, b = 0.0, 0.0
    for _ in range(so_vong):
        y_du_doan = w * x + b
        chenh_lech = y_du_doan - y

        grad_w = (2 / n) * (chenh_lech * x).sum()
        grad_b = (2 / n) * chenh_lech.sum()

        w -= toc_do_hoc * grad_w
        b -= toc_do_hoc * grad_b

    mse_cuoi = ((w * x + b - y) ** 2).mean()
    return mse_cuoi


print("Ket qua yeu cau cua bai (toc do hoc 0.001 va 1.02):")
for toc_do_hoc in (0.001, 1.02):
    mse_cuoi = chay_gradient_descent(toc_do_hoc)
    print(f" toc_do_hoc = {toc_do_hoc:<6} -> MSE tai vong 200 = {mse_cuoi:.6f}")

print()
print(
    "Giai thich: voi toc_do_hoc = 0.001, buoc di moi vong qua ngan nen "
    "sau 200 vong may van con o lung chung suon doi, MSE con lon hon "
    "nhieu so voi dap an 0.1790 vi chua toi duoc day. Voi toc_do_hoc = "
    "1.02, buoc di qua dai nen moi vong nhay vot qua day sang phia ben "
    "kia va con xa day hon vong truoc, khien MSE tang vot theo cap so "
    "nhan chu khong giam. Hai ket qua nay khac nhau vi tot do hoc "
    "quyet dinh do dai moi buoc chan tren duong cong sai so, buoc qua "
    "ngan thi cham toi dich, buoc qua dai thi nhay qua dich roi lac "
    "duong."
)

print()
print("Lam them, do ranh gioi voi cac toc do hoc khac:")
for toc_do_hoc in (0.1, 0.5, 0.9, 1.0, 1.01):
    mse_cuoi = chay_gradient_descent(toc_do_hoc)
    print(f" toc_do_hoc = {toc_do_hoc:<6} -> MSE tai vong 200 = {mse_cuoi:.6f}")

print()
print(
    "Nhan xet phan lam them: toc do hoc 0.5 va 0.9 van ve dung 0.1790 "
    "nhu toc do hoc 0.1, chi la hoi tu nhanh cham khac nhau. Ranh gioi "
    "giua chay duoc va hong nam dau do quanh muc toc do hoc bang 1, "
    "vi 1.0 va 1.01 da bat dau khong on dinh hoac phinh to, con 1.02 "
    "thi hong han."
)
