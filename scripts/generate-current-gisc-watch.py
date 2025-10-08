import csv
from datetime import datetime

input_file = 'gisc-watch-roster.csv'
output_file = 'current-gisc-watch.txt'
today = datetime.utcnow().date()

with open(input_file, newline='', encoding='utf-8') as csvfile:
		reader = csv.DictReader(csvfile)
		names = [row['gisc_name'] for row in reader
						 if row.get('start_date') and row.get('end_date')
						 and datetime.strptime(row['start_date'], '%Y-%m-%d').date() <= today <= datetime.strptime(row['end_date'], '%Y-%m-%d').date()]

with open(output_file, 'w', encoding='utf-8') as f:
		for name in names:
				f.write(f"{name}\n")