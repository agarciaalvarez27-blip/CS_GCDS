musicians = ["Bad Bunny", "Carlos Santana", "Louis Armstrong", "Shakira"]
instruments = ["Plena", "Guitar", "Trumpet", "Vocals"]

print(musicians)

for instrument in instruments:
    print(instrument)

for i in range(4):
    print(f'musician: {musicians[i]}, instrument: {instruments[i]}')

for i in range(len(musicians)):
    print(f'Musician: {musicians[i]}, Instrument: {instruments[i]}')

for index, instrument in enumerate(instruments):
        print(f'Musician: {musicians[index]}, Instrument: {instruments[index]}')