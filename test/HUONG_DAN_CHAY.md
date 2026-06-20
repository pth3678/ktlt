# Mã nguồn Chương 8 — Kiểm thử và Đo đạc hiệu năng

## 1. Chạy lại Test case (testcase.py)

File `testcase.py` .
Để chạy, copy file này vào thư mục gốc của project (ngang hàng với main.py),
rồi chạy:

```
python3 testcase.py
```

Yêu cầu: máy có sẵn màn hình đồ hoạ (Tkinter cần hiển thị, dù đã ẩn cửa sổ
bằng root.withdraw()). Nếu chạy trên server/máy ảo không có màn hình,
cần cài thêm Xvfb (Linux) rồi chạy:

```
xvfb-run -a python3 testcase.py
```

Kết quả sẽ in ra console và đồng thời ghi vào file `test_report_log.txt`.

## 2. Đo hiệu năng trước/sau tối ưu (benchmark_chuong8.py)

File này KHÔNG cần import project gốc — nó tự định nghĩa lại 2 phiên bản
bubble_sort (trước và sau khi thêm cờ swapped) ngay bên trong, nên có thể
chạy độc lập ở bất kỳ đâu có Python 3, không cần cấu trúc thư mục project:

```
python3 benchmark_chuong8.py
```

Kết quả in ra console và xuất file `benchmark_chuong8_results.csv`
chứa toàn bộ số liệu thô (đã có sẵn 1 bản mẫu trong thư mục này,
chạy lại sẽ ghi đè bằng số liệu đo trên máy của bạn).

Thời gian chạy: khoảng 1-2 phút (do N=10.000 ở kịch bản ngẫu nhiên
mất vài chục giây cho mỗi phiên bản thuật toán).

## 3. Vẽ biểu đồ (plot_chuong8.py)

Yêu cầu cài matplotlib trước:

```
pip install matplotlib
```

Sau đó chạy (PHẢI chạy benchmark_chuong8.py trước để có file CSV):

```
python3 plot_chuong8.py
```

Sẽ xuất ra 4 file ảnh PNG trong cùng thư mục:
- chart_scenario_random.png   — Hình 8.4 trong báo cáo
- chart_scenario_sorted.png   — Hình 8.5 trong báo cáo
- chart_tonghop_4duong.png    — Hình 8.2 trong báo cáo
- chart_he_so_cai_thien.png   — Hình 8.3 trong báo cáo

## Lưu ý

Số liệu trong file benchmark_chuong8_results.csv đính kèm là số liệu
nhóm đã đo thực tế (dùng trong báo cáo). Nếu bạn chạy lại trên máy
cá nhân, số liệu tuyệt đối (ms) sẽ khác đôi chút tuỳ cấu hình máy,
nhưng XU HƯỚNG và TỈ LỆ cải thiện sẽ tương đồng.
