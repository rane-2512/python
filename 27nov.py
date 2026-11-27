def clean_customer(raw):
    # Split customer details using semicolon
    fields = raw.split(';')
    # Check whether exactly 4 fields are available
    if len(fields) != 4:
        return None
    # Remove extra spaces and format the data
    name = fields[0].strip().title()
    email = fields[1].strip().lower()
    phone = fields[2].strip()
    city = fields[3].strip().title()
    # Validate name
    if name == "":
        return None
    for word in name.split():
        if not word.isalpha():
            return None
In [7]:
    # Validate city
    if city == "":
        return None
    # Validate email
    if email.count('@') != 1:
        return None
    username, domain = email.split('@')
    if username == "":
        return None
    if '.' not in domain:
        return None
    if domain.startswith('.') or domain.endswith('.'):
        return None
    # Validate phone number
    phone = phone.replace(' ', '').replace('-', '')
    if phone.startswith('+91'):
        phone = phone[3:]
    elif len(phone) == 12 and phone.startswith('91'):
        phone = phone[2:]
    if len(phone) != 10:
        return None
    if not phone.isdigit():
        return None
    if phone[0] not in '6789':
        return None
    # Return cleaned customer details
    return {
        'name': name,
        'email': email,
        'phone': phone,
        'city': city
    }
# List of customer records
lines = [
    ' asha VERMA ; ASHA.V@Example.COM ; +91 98765-43210 ;pune ',
    'ravi kumar;ravi@@corp.in;9123456780;Mumbai',
    'meera;meera@mail;9123456780;Delhi',
    'john doe; john@x.org ;12345; Goa',
    'Neha Rao;neha.rao@firm.co.in;919876501234;nashik',
    'amit;amit@site.com;9876543210'
]
# Count rejected customer records
rejected = 0
# Process each customer record
for line in lines:
result = clean_customer(line)
if result is not None:
print(result)
else:
rejected += 1
# Display total rejected records
print("Rejected:", rejected)
