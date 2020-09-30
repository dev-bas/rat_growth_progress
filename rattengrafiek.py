import pandas as pd
import os
import datetime as dt

rats = ['Kiwi', 'Oscar', 'Moomin', 'Freddie', 'Daffy']

if os.path.isfile('rats.csv'):
    df_rats = pd.read_csv('rats.csv', index_col=0)
else:
    df_rats = pd.DataFrame(columns=['Date', 'Name', 'Weight', 'Birthday', 'Age'])

def add_entry(df_rats):
    while True:
        current_date = dt.date.today()
        print(f'Was the date of measurement today? {current_date}')
        print('yes/no')
        date_answer = input('> ')

        if date_answer == 'yes':
            measurement_date = current_date
        elif date_answer == 'no':
            print('What was the date of measurement?')
            print('Please use the following format: dd-mm-yyyy')
            measurement_date = input('> ')
            measurement_date = dt.datetime.strptime(measurement_date, '%d-%m-%Y').date()
        else:
            print(f'{date_answer} is not yes / no.')
            add_entry(df_rats)

        print(f"Insert name: {rats}")
        name = input('> ')

        if name not in rats:
            print(f'{name} is not in {rats}')
        else:
            pass

        print(F"Insert the weight of {name} in grams:")
        weight = int(input('> '))

        if name in ['Kiwi', 'Oscar']:
            birthday = dt.datetime.strptime('05-01-2020', '%d-%m-%Y').date()
        else:
            birthday = dt.datetime.strptime('27-05-2020', '%d-%m-%Y').date()

        age = measurement_date - birthday
        age = age.days

        print('Please check if the following values are correct:\n')
        print(f'Date: {measurement_date} \nName: {name} \nWeight: {weight} grams \nBirthday: {birthday}, \nAge: {age} days\n')
        print('yes / no')
        answer = input('> ')

        if answer == 'yes':
            df_rats = df_rats.append({'Date': measurement_date, 'Name': name, 'Weight': weight, 'Birthday': birthday, 'Age': age}, ignore_index=True)
            print('Input saved!')
            print('\nDo you want to register another rat?')
            print('yes/no')
            answer = input('> ')
            if answer == 'yes':
                pass
            else:
                return df_rats
        else:
            print('\nDo you want to try again?')
            print('yes/no')
            answer = input('> ')
            if answer == 'yes':
                pass
            else:
                return df_rats


df_rats = add_entry(df_rats)

print('saving to csv file...')
df_rats.to_csv('rats.csv')
print('saving done!')
