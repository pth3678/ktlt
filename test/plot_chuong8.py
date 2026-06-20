"""
Script vẽ biểu đồ minh họa kết quả benchmark trước/sau tối ưu Bubble Sort.
Đọc dữ liệu từ benchmark_chuong8_results.csv (phải chạy benchmark_chuong8.py trước).

Yêu cầu: pip install matplotlib

Xuất ra 3 biểu đồ:
  1. chart_scenario_random.png  - So sánh trước/sau ở kịch bản Ngẫu nhiên
  2. chart_scenario_sorted.png  - So sánh trước/sau ở kịch bản Đã sắp sẵn
  3. chart_tonghop_4duong.png   - Biểu đồ tổng hợp cả 4 đường trên 1 hình (log scale)
"""
import csv
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "benchmark_chuong8_results.csv")
rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))

random_rows = [r for r in rows if r["scenario"] == "random"]
sorted_rows = [r for r in rows if r["scenario"] == "sorted"]

n_vals = [int(r["n"]) for r in random_rows]  # giống nhau cho cả 2 kịch bản

plt.rcParams.update({
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
})

OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def plot_scenario(scenario_rows, title, filename, color_before="#dc2626", color_after="#16a34a"):
    before = [float(r["before_mean_ms"]) for r in scenario_rows]
    before_std = [float(r["before_std_ms"]) for r in scenario_rows]
    after = [float(r["after_mean_ms"]) for r in scenario_rows]
    after_std = [float(r["after_std_ms"]) for r in scenario_rows]

    x_pos = range(len(n_vals))
    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.errorbar(x_pos, before, yerr=before_std, marker='s', label='Trước tối ưu (không có swapped)',
                color=color_before, linewidth=2, capsize=4)
    ax.errorbar(x_pos, after, yerr=after_std, marker='o', label='Sau tối ưu (có swapped)',
                color=color_after, linewidth=2, capsize=4)
    ax.set_xticks(list(x_pos))
    ax.set_xticklabels([f"{n:,}" for n in n_vals])
    ax.set_xlabel("Số lượng bản ghi (N)")
    ax.set_ylabel("Thời gian thực thi (ms)")
    ax.set_yscale("log")
    ax.set_title(title)
    ax.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, filename), dpi=150)
    plt.close()
    print(f"Đã lưu: {filename}")


# Biểu đồ 1: Kịch bản ngẫu nhiên
plot_scenario(
    random_rows,
    "Kịch bản NGẪU NHIÊN — So sánh Trước/Sau tối ưu\n(gần với trường hợp trung bình/xấu nhất)",
    "chart_scenario_random.png"
)

# Biểu đồ 2: Kịch bản đã sắp sẵn
plot_scenario(
    sorted_rows,
    "Kịch bản ĐÃ SẮP SẴN — So sánh Trước/Sau tối ưu\n(trường hợp tốt nhất - best case)",
    "chart_scenario_sorted.png"
)

# Biểu đồ 3: Tổng hợp 4 đường trên 1 hình
fig, ax = plt.subplots(figsize=(9, 6))
x_pos = range(len(n_vals))

before_r = [float(r["before_mean_ms"]) for r in random_rows]
after_r = [float(r["after_mean_ms"]) for r in random_rows]
before_s = [float(r["before_mean_ms"]) for r in sorted_rows]
after_s = [float(r["after_mean_ms"]) for r in sorted_rows]

ax.plot(x_pos, before_r, marker='s', label='Trước tối ưu — Ngẫu nhiên', color='#dc2626', linewidth=2, linestyle='-')
ax.plot(x_pos, after_r, marker='s', label='Sau tối ưu — Ngẫu nhiên', color='#16a34a', linewidth=2, linestyle='-')
ax.plot(x_pos, before_s, marker='o', label='Trước tối ưu — Đã sắp sẵn', color='#dc2626', linewidth=2, linestyle='--')
ax.plot(x_pos, after_s, marker='o', label='Sau tối ưu — Đã sắp sẵn', color='#16a34a', linewidth=2, linestyle='--')

ax.set_xticks(list(x_pos))
ax.set_xticklabels([f"{n:,}" for n in n_vals])
ax.set_xlabel("Số lượng bản ghi (N)")
ax.set_ylabel("Thời gian thực thi (ms) — thang log")
ax.set_yscale("log")
ax.set_title("Biểu đồ tổng hợp: Bubble Sort Trước/Sau tối ưu × 2 kịch bản dữ liệu")
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "chart_tonghop_4duong.png"), dpi=150)
plt.close()
print("Đã lưu: chart_tonghop_4duong.png")

# Biểu đồ 4: Hệ số cải thiện (improvement factor) theo N - chỉ kịch bản đã sắp sẵn vì đây là nơi có cải thiện rõ
fig, ax = plt.subplots(figsize=(8, 5.5))
improvement_s = [float(r["improvement_factor"]) for r in sorted_rows]
improvement_r = [float(r["improvement_factor"]) for r in random_rows]
ax.plot(x_pos, improvement_s, marker='o', label='Kịch bản Đã sắp sẵn', color='#16a34a', linewidth=2)
ax.plot(x_pos, improvement_r, marker='s', label='Kịch bản Ngẫu nhiên', color='#dc2626', linewidth=2)
ax.axhline(y=1, color='gray', linestyle=':', linewidth=1)
ax.set_xticks(list(x_pos))
ax.set_xticklabels([f"{n:,}" for n in n_vals])
ax.set_xlabel("Số lượng bản ghi (N)")
ax.set_ylabel("Hệ số cải thiện (lần nhanh hơn)")
ax.set_yscale("log")
ax.set_title("Hệ số cải thiện tốc độ sau khi thêm cờ swapped")
ax.legend()
for x, y in zip(x_pos, improvement_s):
    ax.annotate(f"x{y:,.0f}", (x, y), textcoords="offset points", xytext=(0, 8), fontsize=8, ha='center', color='#16a34a')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "chart_he_so_cai_thien.png"), dpi=150)
plt.close()
print("Đã lưu: chart_he_so_cai_thien.png")

print("\nHoàn tất vẽ biểu đồ.")
