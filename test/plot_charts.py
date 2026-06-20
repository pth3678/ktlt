"""Vẽ 3 biểu đồ minh họa hiệu năng cho báo cáo:
1. So sánh thời gian shuffle vs bubble_sort theo N (trục y dạng log để nhìn rõ cả 2 đường)
2. Biểu đồ riêng bubble_sort (trục thường) thể hiện rõ độ cong bậc 2
3. Biểu đồ riêng shuffle (trục thường) thể hiện độ tuyến tính
"""
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rows = list(csv.DictReader(open("/home/claude/ktlt-new/ktlt-main/benchmark_results.csv")))
n_vals = [int(r["n"]) for r in rows]
shuffle_ms = [float(r["shuffle_mean_ms"]) for r in rows]
shuffle_std = [float(r["shuffle_std_ms"]) for r in rows]
bubble_ms = [float(r["bubble_sort_mean_ms"]) for r in rows]
bubble_std = [float(r["bubble_sort_std_ms"]) for r in rows]

plt.rcParams.update({
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
})

# ===== Biểu đồ 1: So sánh tổng quan (log scale) =====
fig, ax = plt.subplots(figsize=(8, 5.5))
ax.errorbar(n_vals, shuffle_ms, yerr=shuffle_std, marker='o', label='shuffle() — O(n)', color='#2563eb', linewidth=2, capsize=4)
ax.errorbar(n_vals, bubble_ms, yerr=bubble_std, marker='s', label='bubble_sort() — O(n²)', color='#dc2626', linewidth=2, capsize=4)
ax.set_xlabel("Số lượng câu hỏi (N)")
ax.set_ylabel("Thời gian thực thi (ms) — thang log")
ax.set_yscale("log")
ax.set_title("So sánh thời gian thực thi: shuffle() vs bubble_sort()")
ax.legend()
for x, y in zip(n_vals, shuffle_ms):
    ax.annotate(f"{y:.2f}", (x, y), textcoords="offset points", xytext=(0, 8), fontsize=8, color='#2563eb')
for x, y in zip(n_vals, bubble_ms):
    ax.annotate(f"{y:.0f}", (x, y), textcoords="offset points", xytext=(0, 8), fontsize=8, color='#dc2626')
plt.tight_layout()
plt.savefig("/home/claude/ktlt-new/ktlt-main/chart_comparison.png", dpi=150)
plt.close()

# ===== Biểu đồ 2: bubble_sort riêng - dùng trục N dạng rời rạc (categorical)
fig, ax = plt.subplots(figsize=(8, 5.5))
x_pos = range(len(n_vals))
ax.errorbar(x_pos, bubble_ms, yerr=bubble_std, marker='s', color='#dc2626', linewidth=2, capsize=4, label='Thực đo (đo lặp lại, lấy trung bình)')
ax.fill_between(x_pos, [b - s for b, s in zip(bubble_ms, bubble_std)],
                 [b + s for b, s in zip(bubble_ms, bubble_std)], color='#dc2626', alpha=0.1)
ax.set_xticks(list(x_pos))
ax.set_xticklabels([f"{n:,}" for n in n_vals])
ax.set_xlabel("Số lượng câu hỏi (N)")
ax.set_ylabel("Thời gian thực thi (ms)")
ax.set_title("Thời gian thực thi bubble_sort() theo kích thước dữ liệu\n(đường cong thể hiện rõ độ phức tạp O(n²))")
for x, y in zip(x_pos, bubble_ms):
    ax.annotate(f"{y:,.1f} ms", (x, y), textcoords="offset points", xytext=(0, 10), fontsize=9, ha='center')
ax.legend()
plt.tight_layout()
plt.savefig("/home/claude/ktlt-new/ktlt-main/chart_bubble_sort.png", dpi=150)
plt.close()

# ===== Biểu đồ 3: shuffle riêng - trục N dạng rời rạc =====
fig, ax = plt.subplots(figsize=(8, 5.5))
x_pos = range(len(n_vals))
ax.errorbar(x_pos, shuffle_ms, yerr=shuffle_std, marker='o', color='#2563eb', linewidth=2, capsize=4, label='Thực đo (đo lặp lại, lấy trung bình)')
ax.fill_between(x_pos, [b - s for b, s in zip(shuffle_ms, shuffle_std)],
                 [b + s for b, s in zip(shuffle_ms, shuffle_std)], color='#2563eb', alpha=0.1)
ax.set_xticks(list(x_pos))
ax.set_xticklabels([f"{n:,}" for n in n_vals])
ax.set_xlabel("Số lượng câu hỏi (N)")
ax.set_ylabel("Thời gian thực thi (ms)")
ax.set_title("Thời gian thực thi shuffle() theo kích thước dữ liệu\n(quan hệ gần tuyến tính O(n))")
for x, y in zip(x_pos, shuffle_ms):
    ax.annotate(f"{y:.3f} ms", (x, y), textcoords="offset points", xytext=(0, 10), fontsize=9, ha='center')
ax.legend()
plt.tight_layout()
plt.savefig("/home/claude/ktlt-new/ktlt-main/chart_shuffle.png", dpi=150)
plt.close()

print("Đã tạo xong 3 biểu đồ.")
