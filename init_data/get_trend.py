def trend(row):
	if row['short_avg'] > row['med_avg'] and row['med_avg'] > row['long_avg']:
		return 'up'
	elif row['short_avg'] < row['med_avg'] and row['med_avg'] < row['long_avg']:
		return 'down'
	else:
		return 'none'
