def build_person(first_name, last_nameage=0):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	return person

	if age:
		person['age'] = age

musician = build_person('jimi', 'hendrix', age=27)
print(musician)