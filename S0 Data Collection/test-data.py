from pybaseball import *
import pandas as pd

#Dylan Cease
pitchingdata = statcast_pitcher('2026-05-01', '2026-06-01', player_id=656302)
release_speed_column = pitchingdata['release_speed']

print(release_speed_column)
ff_data = pitchingdata[pitchingdata['pitch_type'] == 'FF']

print(ff_data['strikes'].value_counts())

print(ff_data['strikes'].value_counts() / pitchingdata['strikes'].value_counts())

#Spindata = statcast_pitcher_arsenal_stats(2026, minPA=100)
#print(Spindata)


#Justin Verlander
v_id = playerid_lookup('verlander','justin')['key_mlbam'].iloc[0]
v_pd = statcast_pitcher('2026-03-01','2026-10-25', player_id = v_id)

v_pd['is_strike'] = v_pd['type'].isin(['S','X'])

strike_type_sum = (v_pd.groupby('pitch_type').agg(
    total_pitches = ('pitch_type', 'size'),
    strikes = ('is_strike', 'sum'),
    avg_speed = ('release_speed', 'mean'),
    max_speed = ('release_speed', 'max'))
    .reset_index()
)

strike_type_sum['avg_speed'] = strike_type_sum['avg_speed'].round(2)
strike_type_sum['strike%'] = (strike_type_sum['strikes'] / strike_type_sum['total_pitches'] * 100).round(2)
strike_type_sum = strike_type_sum.sort_values('total_pitches', ascending=False)

print(strike_type_sum)