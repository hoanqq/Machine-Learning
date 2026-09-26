# Bài 1: Hồi quy tuyến tính — Học máy ứng dụng

Bài tập thực hành môn *Học máy ứng dụng* (Trường Đại học Văn Lang, Khoa Công
nghệ Thông tin), Bài 1: Hồi quy tuyến tính. Repo này chứa phần bài tập
(`baitap01/`), dùng bộ dữ liệu 60 căn hộ đi kèm tài liệu (`data/gia_nha.csv`).

## Cấu trúc thư mục

```
bai01_hoi_quy/
├── data/
│   └── gia_nha.csv          # 60 căn hộ: dien_tich, so_phong, tuoi_nha, gia
├── baitap01/
│   ├── bai1.py               # Lọc nhóm căn hộ > 100 m2, tính giá trung bình
│   ├── bai2.py                # Biểu đồ phân tán so_phong vs gia
│   ├── bai3.py                # Hồi quy 1 biến với tuoi_nha thay vì dien_tich
│   ├── bai4.py                # Hồi quy 2 biến (dien_tich + so_phong), so sánh R2
│   ├── bai5.py                # Gradient descent với các tốc độ học khác nhau
│   ├── bai6.py                # Hàm dự đoán giá có cảnh báo ngoại suy
│   └── figures/
│       └── bai2.png           # Hình do bai2.py vẽ ra
└── README.md
```

## Yêu cầu môi trường

- Python >= 3.11
- Thư viện: `numpy`, `pandas`, `matplotlib`, `scikit-learn`

Cài đặt:

```bash
python -m venv hocmay
hocmay\Scripts\activate        # Windows
# source hocmay/bin/activate   # macOS/Linux
pip install numpy pandas matplotlib scikit-learn
```

## Cách chạy

**Quan trọng:** luôn chạy lệnh từ thư mục gốc `bai01_hoi_quy/`, không `cd`
vào `baitap01/`, vì đường dẫn dữ liệu trong mã được viết là
`data/gia_nha.csv` (tương đối theo thư mục đang đứng, không phải theo vị
trí tệp mã).

```bash
cd bai01_hoi_quy
python baitap01/bai1.py
python baitap01/bai2.py
python baitap01/bai3.py
python baitap01/bai4.py
python baitap01/bai5.py
python baitap01/bai6.py
```

## Tóm tắt từng bài

| Bài | Nội dung | Kết quả chính |
|---|---|---|
| 1 | Lọc căn hộ có `dien_tich > 100 m2` | 10 căn, giá trung bình 8.9620 tỷ |
| 2 | Biểu đồ phân tán `so_phong` vs `gia` | Xu hướng đi lên nhưng không thẳng hàng như biểu đồ theo diện tích |
| 3 | Hồi quy 1 biến với `tuoi_nha` | w = -0.037858, b = 6.983593 (hệ số góc âm: nhà càng cũ giá càng giảm) |
| 4 | Hồi quy 2 biến `dien_tich + so_phong` | R² = 0.9698 trên tập kiểm tra (so với 0.9622 của mô hình 1 biến) |
| 5 | Gradient descent với tốc độ học 0.001 và 1.02 | 0.001 quá chậm (MSE ≈ 20.2 sau 200 vòng), 1.02 phân kỳ (MSE ≈ 2.9×10⁸) |
| 6 | Hàm `du_doan_gia(dien_tich)` có cảnh báo ngoại suy | Cảnh báo khi diện tích ngoài khoảng [35.5, 117.5] m2 |

## Ghi chú

- Toàn bộ bài tập dùng chung một cách chia dữ liệu
  (`test_size=0.2, random_state=42`) như tài liệu gốc, để việc so sánh giữa
  các mô hình là công bằng.
- Bộ dữ liệu `gia_nha.csv` là dữ liệu mô phỏng cho mục đích học tập, không
  phải số liệu giao dịch thật của thị trường bất động sản.
- Phần chú thích mã nguồn viết tiếng Việt có dấu; phần in ra màn hình cố
  ý viết không dấu để tránh lỗi mã hóa trên cửa sổ lệnh Windows.

## Tác giả

Bài thực hành biên soạn bởi ThS. Nguyễn Thái Anh — Trường Đại học Văn Lang.
Phần lời giải bài tập trong repo này được thực hiện dựa trên đề bài của
tài liệu gốc.
