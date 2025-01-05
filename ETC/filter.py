

students = [{"Name":"Ahmed","College":"IT","City":"Dongola"},
            {"Name":"Mohamed","College":"IT","City":"Jeddah"},
            {"Name":"Ali","College":"CS","City":"Khartoum"},
            {"Name":"Omer","College":"CS","City":"Khartoum"},
            {"Name":"Khalid","College":"IT","City":"Khartoum"}]


def khartoum(c):
    return c["City"] == "Khartoum"

khartoums = filter(khartoum,students)

for kha in sorted(khartoums,key= lambda name: name["Name"]):
    print(kha["Name"])