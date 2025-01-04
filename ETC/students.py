import json


students = [{"name":"Ahmed","College":"IT","City":"Dongola"},
            {"name":"Mohamed","College":"IT","City":"Jeddah"},
            {"name":"Wali","College":"IT","City":"Jeddah"},
            {"name":"Mohammed","College":"IT","City":"Khartoum"},
            {"name":"Sara","College":"IT","City":"Riyadh"},
            {"name":"Ladan","College":"IT","City":"Al-Taif"}]
print(json.dumps(students,indent=2))

cities = set()

for city in students:
    cities.add(city["City"])
print(cities)