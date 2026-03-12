"""
DATASET 2: E-Commerce Indonesia (Simulasi Data)
Visualisasi insight dari data penjualan e-commerce
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches

np.random.seed(2024)

# =========================================================
# GENERATE DATASET E-COMMERCE INDONESIA
# =========================================================
n = 500
categories = ['Elektronik', 'Fashion', 'Makanan', 'Kecantikan', 'Olahraga', 'Buku']
cities = ['Jakarta', 'Bandung', 'Surabaya', 'Medan', 'Yogyakarta', 'Makassar']
methods = ['Transfer Bank', 'QRIS', 'COD', 'Dompet Digital', 'Kartu Kredit']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun',
          'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']

cat_weights = [0.25, 0.22, 0.18, 0.15, 0.12, 0.08]
city_weights = [0.35, 0.20, 0.18, 0.12, 0.09, 0.06]
method_weights = [0.20, 0.30, 0.20, 0.22, 0.08]

cat_prices = {
    'Elektronik': (500000, 5000000),
    'Fashion': (50000, 800000),
    'Makanan': (20000, 300000),
    'Kecantikan': (30000, 600000),
    'Olahraga': (80000, 1500000),
    'Buku': (30000, 250000)
}

data_ecom = []
for i in range(n):
    cat = np.random.choice(categories, p=cat_weights)
    city = np.random.choice(cities, p=city_weights)
    method = np.random.choice(methods, p=method_weights)
    month_idx = np.random.randint(0, 12)
    month = months[month_idx]
    lo, hi = cat_prices[cat]
    price = np.random.randint(lo, hi)
    qty = np.random.randint(1, 5)
    revenue = price * qty
    rating = round(np.random.uniform(3.0, 5.0), 1)
    data_ecom.append({
        'id': i+1, 'kategori': cat, 'kota': city,
        'metode_bayar': method, 'bulan': month,
        'bulan_idx': month_idx + 1, 'harga': price,
        'qty': qty, 'revenue': revenue, 'rating': rating
    })

df = pd.DataFrame(data_ecom)
print("Dataset E-Commerce:")
print(df.head())
print(f"\nShape: {df.shape}")
print(f"\nTotal Revenue: Rp {df['revenue'].sum():,.0f}")
print(f"Rata-rata Rating: {df['rating'].mean():.2f}")

# =========================================================
# VISUALISASI KOMPREHENSIF
# =========================================================
fig = plt.figure(figsize=(18, 14))
fig.patch.set_facecolor('#0F0F23')

gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.38)

DARK_BG = '#1A1A2E'
ACCENT1 = '#E94560'
ACCENT2 = '#0F3460'
COLORS = ['#E94560', '#16213E', '#0F3460', '#533483', '#2B9348', '#E9C46A']
TEXT_COLOR = 'white'

def style_ax(ax, title):
    ax.set_facecolor(DARK_BG)
    ax.tick_params(colors=TEXT_COLOR, labelsize=9)
    ax.title.set_color(TEXT_COLOR)
    ax.title.set_fontsize(11)
    ax.title.set_fontweight('bold')
    ax.set_title(title, pad=10)
    for spine in ax.spines.values():
        spine.set_edgecolor('#333355')
    if ax.get_xlabel():
        ax.xaxis.label.set_color(TEXT_COLOR)
    if ax.get_ylabel():
        ax.yaxis.label.set_color(TEXT_COLOR)

# Judul utama
fig.text(0.5, 0.97, 'Dashboard Analisis E-Commerce Indonesia 2024',
         ha='center', va='top', fontsize=20, fontweight='bold',
         color='white', family='monospace')
fig.text(0.5, 0.945, 'Eksplorasi & Visualisasi Data — Dataset Simulasi',
         ha='center', va='top', fontsize=11, color='#8888AA')

# --- 1. Bar Chart: Revenue per Kategori ---
ax1 = fig.add_subplot(gs[0, 0])
rev_cat = df.groupby('kategori')['revenue'].sum().sort_values(ascending=True)
rev_millions = rev_cat / 1_000_000
bar_colors = ['#E94560','#E9C46A','#2B9348','#4895EF','#533483','#F77F00']
bars = ax1.barh(rev_millions.index, rev_millions.values, color=bar_colors[::-1],
                edgecolor='none', height=0.6)
for bar, val in zip(bars, rev_millions.values):
    ax1.text(val + rev_millions.max()*0.01, bar.get_y() + bar.get_height()/2,
             f'{val:.0f}M', va='center', color='white', fontsize=8, fontweight='bold')
ax1.set_xlabel('Revenue (Juta Rp)', color=TEXT_COLOR, fontsize=9)
ax1.grid(axis='x', linestyle='--', alpha=0.2, color='white')
style_ax(ax1, 'Revenue per Kategori')

# --- 2. Pie Chart: Metode Pembayaran ---
ax2 = fig.add_subplot(gs[0, 1])
method_counts = df['metode_bayar'].value_counts()
pie_colors = ['#E94560', '#4895EF', '#2B9348', '#E9C46A', '#533483']
wedges, texts, autotexts = ax2.pie(
    method_counts.values, labels=method_counts.index,
    autopct='%1.1f%%', colors=pie_colors,
    startangle=90, pctdistance=0.75,
    wedgeprops=dict(edgecolor='#0F0F23', linewidth=2)
)
for text in texts:
    text.set_color('white')
    text.set_fontsize(8)
for at in autotexts:
    at.set_color('white')
    at.set_fontweight('bold')
    at.set_fontsize(8)
ax2.set_facecolor(DARK_BG)
ax2.set_title('Metode Pembayaran', color='white', fontsize=11,
              fontweight='bold', pad=10)

# --- 3. Bar Chart: Transaksi per Kota ---
ax3 = fig.add_subplot(gs[0, 2])
kota_rev = df.groupby('kota')['revenue'].sum().sort_values(ascending=False) / 1_000_000
city_colors = ['#E94560', '#4895EF', '#2B9348', '#E9C46A', '#533483', '#F77F00']
bars3 = ax3.bar(kota_rev.index, kota_rev.values, color=city_colors,
                edgecolor='none', width=0.6)
for bar, val in zip(bars3, kota_rev.values):
    ax3.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
             f'{val:.0f}M', ha='center', color='white', fontsize=8, fontweight='bold')
ax3.set_xticklabels(kota_rev.index, rotation=30, ha='right', color='white', fontsize=8)
ax3.set_ylabel('Revenue (Juta Rp)', color=TEXT_COLOR, fontsize=9)
ax3.grid(axis='y', linestyle='--', alpha=0.2, color='white')
style_ax(ax3, 'Revenue per Kota')

# --- 4. Line Chart: Tren Revenue Bulanan ---
ax4 = fig.add_subplot(gs[1, :2])
monthly_rev = df.groupby('bulan_idx')['revenue'].sum() / 1_000_000
ax4.fill_between(monthly_rev.index, monthly_rev.values, alpha=0.3, color=ACCENT1)
ax4.plot(monthly_rev.index, monthly_rev.values, color=ACCENT1,
         linewidth=2.5, marker='o', markersize=6, markerfacecolor='white',
         markeredgecolor=ACCENT1, markeredgewidth=2)
for x, y in zip(monthly_rev.index, monthly_rev.values):
    ax4.annotate(f'{y:.0f}M', (x, y), textcoords="offset points",
                 xytext=(0, 10), ha='center', color='white', fontsize=8)
ax4.set_xticks(range(1, 13))
ax4.set_xticklabels(months, color='white', fontsize=9)
ax4.set_ylabel('Revenue (Juta Rp)', color=TEXT_COLOR, fontsize=9)
ax4.grid(linestyle='--', alpha=0.15, color='white')
style_ax(ax4, 'Tren Revenue Bulanan')

# --- 5. Donut Chart: Distribusi Quantity ---
ax5 = fig.add_subplot(gs[1, 2])
qty_dist = df['qty'].value_counts().sort_index()
donut_colors = ['#E94560', '#4895EF', '#2B9348', '#E9C46A']
wedges5, texts5, autotexts5 = ax5.pie(
    qty_dist.values,
    labels=[f'Qty {q}' for q in qty_dist.index],
    autopct='%1.0f%%', colors=donut_colors,
    startangle=90, pctdistance=0.75,
    wedgeprops=dict(edgecolor='#0F0F23', linewidth=2, width=0.5)
)
for t in texts5:
    t.set_color('white')
    t.set_fontsize(9)
for at in autotexts5:
    at.set_color('white')
    at.set_fontweight('bold')
ax5.set_facecolor(DARK_BG)
ax5.set_title('Distribusi Qty Pembelian', color='white', fontsize=11,
              fontweight='bold', pad=10)

# --- 6. Grouped Bar: Rating per Kategori ---
ax6 = fig.add_subplot(gs[2, 0])
rating_cat = df.groupby('kategori')['rating'].mean().sort_values(ascending=False)
bar_colors6 = ['#2B9348' if v >= 4.0 else '#E9C46A' if v >= 3.7 else '#E94560'
               for v in rating_cat.values]
bars6 = ax6.barh(rating_cat.index, rating_cat.values, color=bar_colors6,
                 edgecolor='none', height=0.5)
for bar, val in zip(bars6, rating_cat.values):
    ax6.text(val - 0.08, bar.get_y() + bar.get_height()/2,
             f'{val:.2f}⭐', va='center', color='white', fontsize=8.5, fontweight='bold')
ax6.set_xlim(3.0, 5.2)
ax6.set_xlabel('Rating Rata-rata', color=TEXT_COLOR, fontsize=9)
ax6.grid(axis='x', linestyle='--', alpha=0.2, color='white')
style_ax(ax6, 'Rating per Kategori')

# --- 7. Scatter: Harga vs Revenue per Kategori ---
ax7 = fig.add_subplot(gs[2, 1])
cat_colors_map = dict(zip(categories, ['#E94560','#4895EF','#2B9348','#E9C46A','#533483','#F77F00']))
for cat in categories:
    subset = df[df['kategori'] == cat]
    ax7.scatter(subset['harga']/1000, subset['revenue']/1_000_000,
                c=cat_colors_map[cat], label=cat, alpha=0.5, s=25, edgecolors='none')
ax7.set_xlabel('Harga (Ribu Rp)', color=TEXT_COLOR, fontsize=9)
ax7.set_ylabel('Revenue (Juta Rp)', color=TEXT_COLOR, fontsize=9)
legend = ax7.legend(fontsize=7, loc='upper left',
                    facecolor='#1A1A2E', edgecolor='#333355', labelcolor='white',
                    title='Kategori', title_fontsize=8)
legend.get_title().set_color('white')
ax7.grid(linestyle='--', alpha=0.15, color='white')
style_ax(ax7, 'Harga vs Revenue')

# --- 8. Stacked Bar: Metode Bayar per Kota ---
ax8 = fig.add_subplot(gs[2, 2])
city_method = df.groupby(['kota', 'metode_bayar']).size().unstack(fill_value=0)
city_method_pct = city_method.div(city_method.sum(axis=1), axis=0) * 100
bottom = np.zeros(len(city_method_pct))
method_colors = ['#E94560', '#4895EF', '#2B9348', '#E9C46A', '#533483']
for i, method in enumerate(city_method_pct.columns):
    ax8.bar(city_method_pct.index, city_method_pct[method],
            bottom=bottom, label=method, color=method_colors[i], edgecolor='none')
    bottom += city_method_pct[method].values
ax8.set_xticklabels(city_method_pct.index, rotation=35, ha='right', color='white', fontsize=7.5)
ax8.set_ylabel('Persentase (%)', color=TEXT_COLOR, fontsize=9)
legend2 = ax8.legend(fontsize=6.5, loc='upper right', bbox_to_anchor=(1.0, 1.0),
                     facecolor='#1A1A2E', edgecolor='#333355', labelcolor='white')
ax8.grid(axis='y', linestyle='--', alpha=0.15, color='white')
style_ax(ax8, 'Metode Bayar per Kota')

plt.savefig('/home/claude/latihan_modul/visualisasi_ecommerce.png', dpi=150,
            bbox_inches='tight', facecolor='#0F0F23')
print("✅ Dashboard E-Commerce tersimpan!")

# Ringkasan insight
print("\n=== INSIGHT UTAMA ===")
print(f"• Kategori terlaris: {rev_cat.idxmax()} (Rp {rev_cat.max()/1e6:.0f} juta)")
print(f"• Metode bayar terpopuler: {method_counts.index[0]} ({method_counts.iloc[0]/n*100:.1f}%)")
print(f"• Kota revenue tertinggi: {kota_rev.idxmax()} (Rp {kota_rev.max():.0f} juta)")
print(f"• Kategori rating tertinggi: {rating_cat.idxmax()} ({rating_cat.max():.2f}⭐)")
