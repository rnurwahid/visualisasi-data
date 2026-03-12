"""
LATIHAN MODUL 4 - VISUALISASI DATA
Tugas: Tampilkan visualisasi sebaran laki-laki dan perempuan 
(dengan persentase) yang memberikan tips pada restoran.

Dataset: tips.csv
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# =========================================================
# LOAD DATA
# =========================================================
data = pd.read_csv("tips.csv")
print("Data berhasil dibaca!")
print(data.head())
print(f"\nJumlah data: {data.shape[0]} baris, {data.shape[1]} kolom")

# =========================================================
# LATIHAN 1: Pie Chart - Sebaran Gender dengan Persentase
# =========================================================
gender_counts = data['sex'].value_counts()
gender_pct = data['sex'].value_counts(normalize=True) * 100

print("\n=== Sebaran Gender ===")
for gender, count in gender_counts.items():
    pct = gender_pct[gender]
    print(f"  {gender}: {count} orang ({pct:.1f}%)")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Analisis Tips Restoran - Visualisasi Gender', fontsize=16, fontweight='bold', y=1.02)

# -- Chart 1: Pie Chart Gender --
colors = ['#FF6B9D', '#4A90D9']
explode = (0.05, 0.05)

wedges, texts, autotexts = axes[0].pie(
    gender_counts,
    labels=gender_counts.index,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode,
    startangle=90,
    textprops={'fontsize': 12}
)
for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_fontsize(13)

axes[0].set_title('Sebaran Gender\nPemberi Tips', fontsize=13, fontweight='bold', pad=15)

# -- Chart 2: Bar Chart - Rata-rata Tip per Gender --
avg_tip = data.groupby('sex')['tip'].mean()
bar_colors = ['#FF6B9D', '#4A90D9']
bars = axes[1].bar(avg_tip.index, avg_tip.values, color=bar_colors, 
                   edgecolor='white', linewidth=2, width=0.5)

for bar, val in zip(bars, avg_tip.values):
    axes[1].text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.02,
                 f'Rp {val:.2f}', ha='center', va='bottom', 
                 fontweight='bold', fontsize=11)

axes[1].set_title('Rata-rata Tip\nper Gender', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Gender', fontsize=11)
axes[1].set_ylabel('Rata-rata Tip ($)', fontsize=11)
axes[1].set_ylim(0, avg_tip.max() * 1.2)
axes[1].grid(axis='y', linestyle='--', alpha=0.5)
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

# -- Chart 3: Stacked Bar - Gender per Hari --
day_gender = data.groupby(['day', 'sex']).size().unstack(fill_value=0)
day_order = ['Thur', 'Fri', 'Sat', 'Sun']
day_gender = day_gender.reindex(day_order)

day_gender.plot(kind='bar', ax=axes[2], color=colors, edgecolor='white', 
                linewidth=1.5, width=0.6)

axes[2].set_title('Jumlah Pemberi Tips\nper Hari & Gender', fontsize=13, fontweight='bold')
axes[2].set_xlabel('Hari', fontsize=11)
axes[2].set_ylabel('Jumlah Orang', fontsize=11)
axes[2].legend(title='Gender', fontsize=10)
axes[2].set_xticklabels(day_order, rotation=0, fontsize=10)
axes[2].grid(axis='y', linestyle='--', alpha=0.5)
axes[2].spines['top'].set_visible(False)
axes[2].spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('visualisasi_gender_tips.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("\n✅ Chart 1 tersimpan: visualisasi_gender_tips.png")
plt.close()

# =========================================================
# VISUALISASI TAMBAHAN: Insight Lebih Dalam
# =========================================================
fig2, axes2 = plt.subplots(2, 2, figsize=(14, 10))
fig2.suptitle('Eksplorasi Lengkap Dataset Tips Restoran', fontsize=16, 
               fontweight='bold', y=1.01)

# -- Chart 4: Scatter Plot Total Bill vs Tip (by Gender) --
for gender, color in zip(['Male', 'Female'], ['#4A90D9', '#FF6B9D']):
    subset = data[data['sex'] == gender]
    axes2[0,0].scatter(subset['total_bill'], subset['tip'], 
                       c=color, label=gender, alpha=0.7, s=60, edgecolors='white', linewidth=0.5)

axes2[0,0].set_title('Total Tagihan vs Tip\n(berdasarkan Gender)', fontsize=12, fontweight='bold')
axes2[0,0].set_xlabel('Total Tagihan ($)', fontsize=10)
axes2[0,0].set_ylabel('Tip ($)', fontsize=10)
axes2[0,0].legend(title='Gender', fontsize=9)
axes2[0,0].grid(linestyle='--', alpha=0.4)
axes2[0,0].spines['top'].set_visible(False)
axes2[0,0].spines['right'].set_visible(False)

# -- Chart 5: Box Plot Tip per Hari --
day_order = ['Thur', 'Fri', 'Sat', 'Sun']
data_by_day = [data[data['day'] == d]['tip'].values for d in day_order]
bp = axes2[0,1].boxplot(data_by_day, labels=day_order, patch_artist=True,
                         medianprops=dict(color='black', linewidth=2))

box_colors = ['#FFD93D', '#6BCB77', '#4D96FF', '#FF6B6B']
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

axes2[0,1].set_title('Distribusi Tip\nper Hari', fontsize=12, fontweight='bold')
axes2[0,1].set_xlabel('Hari', fontsize=10)
axes2[0,1].set_ylabel('Tip ($)', fontsize=10)
axes2[0,1].grid(axis='y', linestyle='--', alpha=0.4)
axes2[0,1].spines['top'].set_visible(False)
axes2[0,1].spines['right'].set_visible(False)

# -- Chart 6: Pie Chart Smoker vs Non-Smoker --
smoker_counts = data['smoker'].value_counts()
colors_smoke = ['#FF6B6B', '#6BCB77']
wedges2, texts2, autotexts2 = axes2[1,0].pie(
    smoker_counts, labels=['Non-Smoker', 'Smoker'],
    autopct='%1.1f%%', colors=colors_smoke,
    explode=(0.05, 0.05), startangle=90,
    textprops={'fontsize': 11}
)
for at in autotexts2:
    at.set_fontweight('bold')
axes2[1,0].set_title('Sebaran Perokok\nvs Non-Perokok', fontsize=12, fontweight='bold')

# -- Chart 7: Bar Chart - Total Tips per Waktu Makan --
time_tip = data.groupby('time')['tip'].sum()
colors_time = ['#FF9F43', '#5F27CD']
bars2 = axes2[1,1].bar(time_tip.index, time_tip.values, color=colors_time,
                        edgecolor='white', linewidth=2, width=0.4)

for bar, val in zip(bars2, time_tip.values):
    axes2[1,1].text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
                    f'${val:.1f}', ha='center', va='bottom',
                    fontweight='bold', fontsize=12)

axes2[1,1].set_title('Total Tips\nper Waktu Makan', fontsize=12, fontweight='bold')
axes2[1,1].set_xlabel('Waktu', fontsize=10)
axes2[1,1].set_ylabel('Total Tips ($)', fontsize=10)
axes2[1,1].set_ylim(0, time_tip.max() * 1.15)
axes2[1,1].grid(axis='y', linestyle='--', alpha=0.4)
axes2[1,1].spines['top'].set_visible(False)
axes2[1,1].spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('visualisasi_eksplorasi_tips.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("✅ Chart 2 tersimpan: visualisasi_eksplorasi_tips.png")
plt.close()

print("\n=== KESIMPULAN ANALISIS ===")
print(f"• {gender_pct['Male']:.1f}% pemberi tips adalah laki-laki, {gender_pct['Female']:.1f}% perempuan")
print(f"• Rata-rata tip laki-laki: ${data[data['sex']=='Male']['tip'].mean():.2f}")
print(f"• Rata-rata tip perempuan: ${data[data['sex']=='Female']['tip'].mean():.2f}")
print(f"• Hari tersibuk: {data['day'].value_counts().index[0]}")
print(f"• Waktu terbanyak tips: {data.groupby('time')['tip'].sum().idxmax()}")
