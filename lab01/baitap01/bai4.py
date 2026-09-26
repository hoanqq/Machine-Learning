# -*- coding: utf-8 -*-
"""Bai tap 4: Them so phong vao mo hinh.

Huan luyen mot mo hinh hoi quy tuyen tinh voi hai cot dau vao la
dien_tich va so_phong. Chia du lieu giong het muc 6 va muc 8 cua
tai lieu (test_size=0.2, random_state=42) roi so sanh R2 voi mo
hinh mot bien.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/gia_nha.csv")
y = df["gia"]

X_hai_bien = df[["dien_tich", "so_phong"]]

X_train, X_test, y_train, y_test = train_test_split(
    X_hai_bien, y, test_size=0.2, random_state=42
)

mo_hinh = LinearRegression()
mo_hinh.fit(X_train, y_train)

r2_hai_bien = r2_score(y_test, mo_hinh.predict(X_test))

print(f"R2 tren tap kiem tra (dien_tich + so_phong) = {r2_hai_bien:.4f}")
print("R2 cua mo hinh mot bien (chi dien_tich), theo muc 6 = 0.9622")
print()

if r2_hai_bien > 0.9622:
    print(
        "So sanh: R2 tang len so voi mo hinh mot bien, nghia la them "
        "cot so_phong giup mo hinh giai thich duoc them mot chut bien "
        "dong cua gia. Muc tang khong lon, vi dien_tich va so_phong di "
        "kem nhau kha chat trong bo du lieu nay nen dien_tich da ganh "
        "gan het cong viec roi."
    )
else:
    print(
        "So sanh: R2 khong tang len so voi mo hinh mot bien, nghia la "
        "them cot so_phong khong giup ich duoc gi cho mo hinh trong "
        "lan chia du lieu nay."
    )
