import json

with open("distances.json") as f:
	distances = json.load(f)

for artiste, distances_artiste in distances.items():
	for autre_artiste, distances_autre_artiste in distances.items():
		if artiste == autre_artiste:
			continue

		if autre_artiste not in distances_artiste and artiste not in distances_autre_artiste:
			dist = input(f'Quelle est la distance entre {artiste} et {autre_artiste} ? [0=pareil..1=opposés]')
			distances_artiste[autre_artiste] = float(dist)

			with open("distances.json", 'w') as f:
				f.write(json.dumps(distances, indent=2))