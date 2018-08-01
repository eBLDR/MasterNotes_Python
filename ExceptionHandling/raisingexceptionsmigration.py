import raisingexceptions as sharks

school = sharks.School()

for i in range(4):
    if i == 3:
        school.add_shark(sharks.Intruder())
        school.add_shark(sharks.Shark())
    else:
        school.add_shark(sharks.Shark())

school.migrate()
