import re

string = "jQuery .Net Cloud-computing"
el = re.findall('[a-z]?[A-Z\.][a-z0-9A-Z#+\.-]*', string)

print(el)