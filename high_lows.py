import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates, low, and high temperatures for Death Valley from file.
dv_file = 'data/death_valley_2014.csv'
with open(dv_file) as dv_f:
    dv_reader = csv.reader(dv_f)
    dv_header_row = next(dv_reader)

    dv_highs, dv_dates, dv_lows =[], [], []
    for row in dv_reader:
        try:
            dv_current_date = datetime.strptime(row[0], "%Y-%m-%d")
            dv_high = int(row[1])
            dv_low = int(row[3])
        except ValueError:
            print(dv_current_date, 'missing data')
        else:
            dv_dates.append(dv_current_date)
            dv_highs.append(dv_high)
            dv_lows.append((dv_low))

# Get dates, low, and high temperatures for Sitka from file
sitka_file = 'data/sitka_weather_2014.csv'
with open(sitka_file) as sitka_f:
    sitka_reader = csv.reader(sitka_f)
    sitka_header_row = next(sitka_reader)

    sitka_lows, sitka_highs, sitka_dates = [], [], []
    for row in sitka_reader:
        try:
            sitka_high = int(row[1])
            sitka_low = int(row[3])
            sitka_current_date = datetime.strptime(row[0], "%Y-%m-%d")
        except ValueError:
            print("missing data")
        else:
            sitka_lows.append(sitka_low)
            sitka_highs.append(sitka_high)
            sitka_dates.append(sitka_current_date)

print("Death valley's max temp: " + str(max(dv_highs)))
print("Sitka's max temp: " + str(max(sitka_highs)))
print(len(dv_dates)) # 359
print(len(dv_highs)) # 359
print(len(sitka_dates)) # 356
print(len(sitka_highs)) # 356

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))

# Death Valley
plt.plot(dv_dates, dv_highs, c='red', alpha=0.1)
plt.plot(dv_dates, dv_lows, c='blue', alpha=0.1)

# Sitka
plt.plot(sitka_dates, sitka_highs, c='orange', alpha=0.1)
plt.plot(sitka_dates, sitka_lows, c='green', alpha=0.1)

dv_temp_range = plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor='blue', alpha=0.3,
                                 label='Death Valley temp. range')
sitka_temp_range = plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='red', alpha=0.3,
                                    label='Sitka temp. range')

# Format plot
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA vs Sitka", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.axis([dv_dates[0], dv_dates[-1], 0, 120])

plt.legend()

plt.show()