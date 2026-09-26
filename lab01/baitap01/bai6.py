# -*- coding: utf-8 -*-
"""Bai tap 6: Viet ham du doan co canh bao.

Ham nhan vao dien tich va tra ve gia du doan theo mo hinh mot bien
da hoc o muc 5 cua tai lieu (w = 0.078367, b = 0.401752). Neu dien
tich nam ngoai khoang du lieu da thay (35.5 toi 117.5 m2) thi in
them mot dong canh bao truoc khi tra ve ket qua.
"""

W = 0.078367
B = 0.401752

DIEN_TICH_NHO_NHAT = 35.5
DIEN_TICH_LON_NHAT = 117.5


def du_doan_gia(dien_tich):
    """Du doan gia nha (ty dong) tu dien tich (met vuong)."""
    if dien_tich < DIEN_TICH_NHO_NHAT or dien_tich > DIEN_TICH_LON_NHAT:
        print(
            f" Canh bao: {dien_tich} m2 nam ngoai khoang du lieu da hoc "
            f"({DIEN_TICH_NHO_NHAT} toi {DIEN_TICH_LON_NHAT} m2), "
            "ket qua chi la ngoai suy, khong chac day du dang tin."
        )
    return W * dien_tich + B


for dien_tich in (60, 80, 200):
    gia_du_doan = du_doan_gia(dien_tich)
    print(f"Can {dien_tich} m2 -> du doan {gia_du_doan:.3f} ty dong")
    print()
