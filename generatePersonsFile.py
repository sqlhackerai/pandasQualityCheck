import random
import pandas as pd

def random_year():
    prob = random.random()
    if prob < 0.05:
        return random.choice([1700, 1800])  # historical year
    elif prob < 0.10:
        return random.randint(1900, 1920)  # old year
    else:
        return random.randint(1921, 2021)  # realistic year

def random_blood_type():
    prob = random.random()
    if prob < 0.95:
        return random.choice(['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'])
    else:
        return random.choice(['C+', 'XYZ'])  # random inconsistency

def random_ssn():
    prob = random.random()
    if prob < 0.95:
        return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"
    else:
        return f"{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}"  # missing hyphens and too long

def random_postal_code():
    prob = random.random()
    if prob < 0.95:
        return f"{random.randint(10000, 99999)}"
    else:
        return f"{random.randint(100000, 999999)}"  # too long postal code

data = {
    'id': range(1, 101),
    'firstname': [random.choice(['John', 'Jane', 'Mark', 'Emily', 'Alex', 'Sarah', 'David', 'Lisa', 'James', 'Michael', 'William', None]) for _ in range(100)],
    'lastname': [random.choice(['Doe', 'Smith', 'Brown', 'White', 'Jones', 'Davis', 'Wilson', 'Taylor', 'Harris', 'Lewis', 'Clark', None]) for _ in range(100)],
    'year_of_birth': [random_year() for _ in range(100)],
    'gender': [random.choice(['M', 'F']) for _ in range(100)],
    'postal_code': [random_postal_code() for _ in range(100)],
    'blood_type': [random_blood_type() for _ in range(100)],
    'social_security': [random_ssn() for _ in range(100)]
}

df = pd.DataFrame(data)
print(df)
df.to_csv('persons_updated.csv', index=False)