from pybaseball import *

#data = standings(1992)[0]
#print(data)

#Testing

#data = playerid_lookup('cease', 'dylan')
#print(data)


pitchingdata = statcast_pitcher('2026-05-01', '2026-06-01', player_id=656302)
#print(pitchingdata)

release_speed_column = pitchingdata['release_speed']

print(release_speed_column)

ff_data = pitchingdata[pitchingdata['pitch_type'] == 'FF']
#print(ff_data)

print(ff_data['strikes'].value_counts())

print(ff_data['strikes'].value_counts() / pitchingdata['strikes'].value_counts())

#Spindata = statcast_pitcher_arsenal_stats(2026, minPA=100)
#print(Spindata)

