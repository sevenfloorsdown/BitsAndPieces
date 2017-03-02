#!/usr/bin/python

import random
import commands

email_addy = 'name@domain.com'
email_pswd = '\'password_here\''

male_codenames   = ['Patrick Garcia',
                    'Paolo Contis',
                    'Janus del Prado',
                    'Carlo Aquino',
                    'Gio Alvarez',
                    'Victor Neri',
                    'Christopher Roxas',
                    'Carlo Pascual',
                    'Tony Lambino',
                    'John Prats',
                    'Geoff Eigenmann',
                    'Vandolph Quizon',
                    'Kristoffer Peralta',
                    'Igi Boy Muhlach']

female_codenames = ['Cheska Garcia',
                    'Anna Larrucea',
                    'Kaye Abad',
                    'Camille Prats',
                    'Angelica Panganiban',
                    'Angelu de Leon',
                    'Jolina Magdangal',
                    'Guila Alvarez',
                    'Jan Marini Alano',
                    'Claudine Barretto',
                    'Roselle Nava',
                    'Kristine Hermosa',
                    'Rica Peralejo',
                    'Maxene Magalona',
                    'Maybelyn dela Cruz',
                    'Katya Santos']



# make sure Y < X
the_guys = [('Terence',   'mail@email'),
            ('Mackoy',    'mail@email'),
            ('Tennessy',  'mail@email'),
            ('Marvin',    'mail@email'),
            ('Louie',     'mail@email'),
            ('Edrick',    'mail@email'),
            ('Patrick',   'mail@email'),
            ('JB',        'mail@email'),
            ('Christian', 'mail@email')
            ]

# make sure Z < X
the_girls = [('Jayne', 'mail@email'),
            ('Thessa', 'mail@email'),
            ('Ella',   'mail@email'),
            ('Julie',  'mail@email'),
            ('Em',     'mail@email')
            ]
person = {'Name': 'Test',
          'Email': 'test@test.com',
          'Alias': 'test',
          'Baby':  'test_baby'}

participants = []

# shuffle
for i in range(3):
    random.shuffle(the_guys)
    random.shuffle(the_girls)

for i in range(len(the_guys)):
    person['Name']  = the_guys[i][0]
    person['Email'] = the_guys[i][1]
    person['Alias'] = male_codenames[i]
    participants.append(person.copy())

for i in range(len(the_girls)):
    person['Name']  = the_girls[i][0]
    person['Email'] = the_girls[i][1]
    person['Alias'] = female_codenames[i]
    participants.append(person.copy())

# shuffle again before assigning
for i in range(3):
    random.shuffle(participants)

# given that the list is shuffled several times already,
# just assign the next entry as the baby to make it easier
# to ensure that no duplicate and everyone is assigned

num_peeps = len(participants)

for i in range(num_peeps):
    if i >= num_peeps-1:
        x = 0
    else:
        x = i+1
    participants[i]['Baby'] = participants[x]['Alias']

# Debugging print lines
for x in participants:
    print x['Name'] +  " is " + x['Alias'] + " whose baby is " + x['Baby']

# now send the individual emails
emailer = ""
carbon = ""

#for x in participants:
#    carbon = carbon + x['Email'] + ", "
#print carbon

for x in participants:
    emailer = "sendemail -f " + email_addy + " -t " + x['Email'] + " -bcc " 
    emailer = emailer + email_addy + " -u [KRIS KRINGLE 2012 TOTOHANAN NA TO FOR REAL]"
    emailer = emailer + " -s smtp.gmail.com -o tls=yes -xu sevenfloorsdown -xp "
    emailer = emailer + email_pswd  + " -m \"Hello, " + x['Name'] + ","
    emailer = emailer + "\n\n" + "Ikaw si " + x['Alias'] + " "
    emailer = emailer + "at baby mo si " + x['Baby'] + "." + '\n\n'
    print emailer
    commands.getoutput(emailer) 
