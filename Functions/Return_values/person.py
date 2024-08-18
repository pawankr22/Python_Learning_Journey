# returning a dictionary
def build_person(first_name ,last_name, age=None, occupation=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    if occupation:
        person['occupation'] = occupation
    return person
musician = build_person('pawan', 'kumar',age=24, occupation = 'software engineer')
print(musician)