#level3
#1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    skills = person['skills']
    
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

if 'Python' in skills:
    print("Python skill found")

if skills == ['JavaScript', 'React']:
    print("He is a front end developer")
elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
    print("He is a backend developer")
elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
    print("He is a fullstack developer")
else:
    print("Unknown title")


if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")