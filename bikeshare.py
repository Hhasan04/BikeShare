import pandas as pd
import numpy as np
import time

def get_city():
    
    valid_cities = ["chicago", "new york", "washington"]

    while True:
        try:
            city_name = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n').lower()
            if city_name in valid_cities:
                break 
            else:
                print("Invalid city. Please try again.\n")
        except:
            print('Ivalid input, Please try again')
    return city_name

def get_time_period():
    
    valid_choice = ["month", "day", "none"]
    while True:
        try:
            time_period = input('\nWould you like to filter the data by month, day, or not at'
                            ' all? Type "none" for no time filter.\n').lower()
            if time_period in valid_choice:
             break
            else:
                print('Invalid Choice. Please try again.\n')
        except:
            print('Ivalid input, Please try again')
    return time_period
        


def get_month(df):
    
    while True:
        try:
            month = int(input('\nWhich month? Please type your response as an integer (January = 1, February = 2, ..., June = 6).\n'))
            if 1 <= month <= 12:
                break
            else:
                print("The number is out of range. Please try again.")
        except ValueError:
            print("That's not a valid number. Please try again.")
    df = df[df['month'] == month]
    return df
    


def get_day(df):
    
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    while True:
        day = input('\nWhich day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n').lower()
        if day in days:
            break
        else:
            print('invalid day name Please enter a day name')
    df = df[df['day_of_week'] == day.title()]
    return df


def popular_month(df):
    months_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    return months_dict[df['month'].mode()[0]]

def popular_day(df):
    return df['day_of_week'].mode()[0]


def popular_hour(df):
    df['hour'] = df['Start Time'].dt.hour
    return df['hour'].mode()[0]

def sum_of_trip_durations(df):
    return df['Trip Duration'].sum()

def avg_of_trip_durations(df):
    return df['Trip Duration'].mean()

def popular_start_stations(df):
    return df['Start Station'].mode()[0]

def popular_end_stations(df):
    return df['End Station'].mode()[0]

def popular_trip(df):

    most_popular_trip = df[['Start Station', 'End Station']].mode().iloc[0]

    return (most_popular_trip['Start Station'], most_popular_trip['End Station'])


def users(df):
    user_count = df['User Type'].value_counts()
    return user_count

def gender(df):
    gender_count = df['Gender'].value_counts()
    return gender_count

def birth_years(df):
    return (df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode()[0])

def display_data(df, start, end):
    try:
        
        print(df[start:end])
    except StopIteration:
        print("No more data to display.")


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
    city = get_city()
    
    df = pd.read_csv(CITY_DATA[city])
    original_df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
  # Filter by time period (month, day, none)
    time_period = get_time_period()
    if time_period == 'month':
        df = get_month(df)
        print('\nCalculating the first statistic...')
        start_time = time.time()

        print('\nThe most popular day is:',popular_day(df))

        print("\nThat took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")

    elif time_period == 'day':
        df = get_day(df)
        print('\nCalculating the first statistic...')
        start_time = time.time()

        print('\nThe most popular month is:',popular_month(df))

        print("\nThat took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")

    else:
        print('\nCalculating the first statistic...')
        start_time = time.time()

        print('\nThe most popular month is:',popular_month(df))
        print('The most popular day is:',popular_day(df)) 

        print("\nThat took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")    

    start_time = time.time()

    print('\nThe most riding hour is:',popular_hour(df))

    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    print(f'\nThe total of trip durations is {sum_of_trip_durations(df)} seconds')
    print(f'The average of trip durations is {avg_of_trip_durations(df)} seconds')

    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    print('\nThe most popular start station is:', popular_start_stations(df))
    print('The most popular end station is:', popular_end_stations(df))

    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    most_popular_trip = popular_trip(df)
    print(f"\nMost Popular Trip: Start Station - {most_popular_trip[0]}, End Station - {most_popular_trip[1]}")

    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    user_types = users(df)
    print(f'\nThere is {user_types.iloc[0]} Subscribers and {user_types.iloc[1]} Customers')
    # TODO: call users function and print the results

    print("\nThat took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    if city != 'washington':

        modified_df = df.dropna(axis=0)
        
        genders = gender(modified_df)
        print(f'\nThere is {genders.iloc[0]} Male Trips and {genders.iloc[1]} Females Trips')


        print("\nThat took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
        start_time = time.time()

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
        # TODO: call birth_years function and print the results
        years = birth_years(modified_df)
        print(f'\nThe oldes subscriber was born in {years[0]} and the youngest was born in {years[1]}.\nthe most popular birth year is {years[2]}')

        print("\nThat took %s seconds." % (time.time() - start_time))
    else:
        print('\nSorry, There is no data available about the Gender and birth year for washington city')

    # Display five lines of data at a time if user specifies that they would like to
    start = 0
    end = 5
    while True:
        try:            
            display = input('\nWould you like to view individual trip data?'
                    '\nType \'yes\' to show or anything else for no.\n').lower()
            if display == 'yes':                
                display_data(df, start, end)
                start += 5
                end += 5
            else:
                break
        except:
            print('Ivalid input, Please try again')

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' to restart or anything else for no.\n').lower()
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
