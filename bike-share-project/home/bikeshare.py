import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    while True:
          try:
            city: str = input("Please Choose from the following cities: Chicago, New York City, Washington\n").lower()
            if city in CITY_DATA:
                break
            else:
                print('\nSorry, Invaflid inputs\n')
                continue
          except:
              print('\nSorry, Invaflid inputs\n')

    #months=['all','january','feburary','march','april','may','june']
    while True:
          try:
            month = input("Please choose one of thease months : January, Feburary, March, April, May and June, or enter 'all'\n").lower()
            if month in ['all','january','feburary','march','april','may','june']:
                break
            else:
                print('\nSorry, Invaflid inputs\n')
                continue
          except:
              print('\nSorry, Invaflid inputs\n')

    #days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        try:
            day = input("Please choose one of the week days : Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday, or enter 'all'\n").lower()
            if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
                break
            else:
                print('\nSorry, Invaflid inputs\n')
                continue
        except:
            print('\nSorry, Invaflid inputs\n')



    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'feburary', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]

    print('Most Common Month is :', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    print('Most Common Day Of Week is :', common_day)

    # display the most common start hour    
    common_hour = df['hour'].mode()[0]

    print('Most Common Start Hour :', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('Most Common Start Station is :', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('Most Common End Station is :', common_end_station)

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to : ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print('Most Common Combination is :', common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('The Total Travel Time is :', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('The Mean Travel Time is :', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)

    else:
        print("Sorry, there is no gender information for this city.")

    # Display earliest, most recent, and most common year of birth
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)

    else:
        print("Sorry, there is no gender information for this city.")
   

    x='Birth Year' in df
    if x:
        earliest_value = df['Birth Year'].min()
        print('The Earliest Of Birth Years is :', earliest_value)
        recent_value = df['Birth Year'].max()
        print('The recent Of Birth Years is :', recent_value)
        common_birth = df['Birth Year'].mode()[0]
        print('The Most Common Year Of Birth is :', common_birth)
    else: 
        print("Sorry, there is no information about the year of birth for this city.")

        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def display_raw_data(df):
    i = 0
    while True:
     try:
        raw = input("Would you like to see the raw data\n").lower() 
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5])
            i += 5
        else:
             print('\nSorry, Invaflid inputs\n')
             continue
     except:
        print('\nSorry, Invaflid inputs\n')

def main():
 while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
