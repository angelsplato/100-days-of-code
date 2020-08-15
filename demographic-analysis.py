import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count =  df.groupby('race').age.count().sort_values(ascending = False).values

    # What is the average age of men?
    average_age_men = df[df['sex']=='Male']['age'].mean()


    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df.groupby(['education']).count().age.Bachelors /df.groupby(['education']).count().sum().age * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df["education-num"]>12) & (df["salary"]==">50K")].count().age / df[df["education-num"]>=13].count().age * 100
    lower_education = (df[df['education']=="Bachelors"].count().salary / df[df['education']=="Bachelors"].count().sum() ) * 100

    # percentage with salary >50K
    higher_education_rich = df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df["salary"]==">50K")].count().age / df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count().age * 100
    lower_education_rich = df[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df["salary"]==">50K")].count().age / df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count().age * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"]==df['hours-per-week'].min()].count().age 

    rich_percentage = df[(df["hours-per-week"]==df['hours-per-week'].min()) & (df["salary"]==">50K")].count().age  / num_min_workers * 100
    # What country has the highest percentage of people that earn >50K?
    all = df[['native-country','salary']]
    entire = all.groupby(['native-country']).count()
    plus50k = all[df['salary']=='>50K']
    plus50k = plus50k.groupby(['native-country']).count()
    plus50k = (plus50k*100)/entire
    plus50k.sort_values(by= ['salary'] , inplace = True , ascending = False )
    final = pd.Series(plus50k['salary'])
    highest_earning_country = final.index[0]
    highest_earning_country_percentage = round(final.values[0] ,1)

    # Identify the most popular occupation for those who earn >50K in India.
    all = df[['salary','native-country','occupation']]
    india50K = all[(all['salary']=='>50K')&(all['native-country']=='India')]
    data = india50K.groupby(['occupation']).count().sort_values(by=['salary'] , ascending =False)
    top_IN_occupation = data.index[0]
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
