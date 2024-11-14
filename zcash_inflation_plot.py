
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
df_updated = pd.read_excel('zcash_inflation_data.xlsx', sheet_name='Sheet1')
df_updated['Date'] = pd.to_datetime(df_updated['Date'])

# Define halving dates and labels
halving_dates_corrected = [pd.to_datetime('2020-11-17'), pd.to_datetime('2024-11-23'), pd.to_datetime('2028-11-28')]
halving_labels_corrected = ['1-й Халвинг', '2-й Халвинг', '3-й Халвинг']

# Define specific values for annotation
nov_17_value = df_updated.loc[df_updated['Date'] == pd.to_datetime('2020-11-17'), 'Current Inflation (%)'].values[0]
nov_18_value = df_updated.loc[df_updated['Date'] == pd.to_datetime('2020-11-18'), 'Current Inflation (%)'].values[0]
nov_23_2024_value = df_updated.loc[df_updated['Date'] == pd.to_datetime('2024-11-23'), 'Current Inflation (%)'].values[0]
nov_24_2024_value = df_updated.loc[df_updated['Date'] == pd.to_datetime('2024-11-24'), 'Current Inflation (%)'].values[0]
nov_28_2028_value = df_updated.loc[df_updated['Date'] == pd.to_datetime('2028-11-28'), 'Current Inflation (%)'].values[0]
nov_29_2028_value = df_updated.loc[df_updated['Date'] == pd.to_datetime('2028-11-29'), 'Current Inflation (%)'].values[0]

zip_234_start_date_corrected = pd.to_datetime('2026-12-01')
zip_234_activation_value = df_updated.loc[df_updated['Date'] == zip_234_start_date_corrected, 'Current Inflation (%)'].values[0]

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(df_updated['Date'], df_updated['Current Inflation (%)'], label='Эталонная инфляция Zcash', linewidth=2, color='orange')
plt.plot(df_updated['Date'], df_updated['ZIP 234'], label='Инфляция по ZIP 234', linewidth=2, color='green')

for date, label in zip(halving_dates_corrected, halving_labels_corrected):
    plt.axvline(x=date, color='blue', linestyle='--', linewidth=1)
    plt.text(date, df_updated['Current Inflation (%)'].max() * 0.95, label, rotation=90, verticalalignment='center', color='blue')

plt.text(pd.to_datetime('2020-11-17') - pd.DateOffset(days=50), nov_17_value + 1, f'{nov_17_value:.1f}%', color='black', fontsize=10, ha='right')
plt.text(pd.to_datetime('2020-11-18') + pd.DateOffset(days=50), nov_18_value + 1, f'{nov_18_value:.1f}%', color='black', fontsize=10, ha='left')

plt.text(pd.to_datetime('2024-11-23') - pd.DateOffset(days=50), nov_23_2024_value + 1, f'{nov_23_2024_value:.1f}%', color='black', fontsize=10, ha='right')
plt.text(pd.to_datetime('2024-11-24') + pd.DateOffset(days=50), nov_24_2024_value - 2, f'{nov_24_2024_value:.1f}%', color='black', fontsize=10, ha='left')

plt.text(pd.to_datetime('2028-11-28') - pd.DateOffset(days=50), nov_28_2028_value + 1, f'{nov_28_2028_value:.1f}%', color='black', fontsize=10, ha='right')
plt.text(pd.to_datetime('2028-11-29') + pd.DateOffset(days=50), nov_29_2028_value - 1.5, f'{nov_29_2028_value:.1f}%', color='black', fontsize=10, ha='left')

plt.axvline(x=zip_234_start_date_corrected, color='red', linestyle='--', linewidth=1)
plt.text(zip_234_start_date_corrected, 43, 'Блок активации ZIP 234', rotation=90, verticalalignment='center', color='red')

intersection_date = pd.to_datetime('2028-11-28')
intersection_value = df_updated.loc[df_updated['Date'] == intersection_date, 'ZIP 234'].values[0]
plt.annotate(f'{intersection_value:.1f}%',
             xy=(intersection_date, intersection_value),
             xytext=(intersection_date + pd.DateOffset(months=6), intersection_value + 2),
             arrowprops=dict(arrowstyle='->', color='green'),
             color='green', fontsize=10)

plt.annotate(f'{zip_234_activation_value:.1f}%',
             xy=(zip_234_start_date_corrected, zip_234_activation_value),
             xytext=(zip_234_start_date_corrected + pd.DateOffset(months=6), zip_234_activation_value + 2),
             arrowprops=dict(arrowstyle='->', color='red'),
             color='red', fontsize=10)

plt.text((halving_dates_corrected[0] + (halving_dates_corrected[1] - halving_dates_corrected[0]) / 2),
         df_updated['Current Inflation (%)'].min() * 1.5, 'Источник: pro.zcash.ru', fontsize=12, style='italic', fontweight='bold', ha='center')

plt.ylim([0, df_updated['Current Inflation (%)'].max() + 5])
plt.yticks(np.arange(0, df_updated['Current Inflation (%)'].max() + 6, 2))

plt.title('График инфляции Zcash с добавлением ZIP 234', fontsize=16, pad=20)
plt.xlabel('')
plt.ylabel('Инфляция (%)', fontsize=14)
plt.xlim([pd.to_datetime('2019-01-01'), pd.to_datetime('2031-01-01')])
plt.grid(True)
plt.legend()
plt.show()
