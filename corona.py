import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv, requests

def get_file(url):
    return csv.DictReader(requests.get(url).iter_lines(decode_unicode=True))

def get_data(x, y, file, state, county, title):
    for row in file:
        if row['Province_State'] == state and row['Admin2'] == county:
            i = 0
            title = row['Admin2'] + ' Coronavirus Stats'
            for _ , value in row.items():
                i += 1
                if i >= 12:
                    x.append(i - 11)
                    y.append(value)
            break


def print_counties(state, file):
    for row in file:
        if row['Province_State'] == state:
            print(row['Admin2'])


def check_county(state, county, file):
    for row in file:
        if row['Admin2'] == county:
            return True
        #print(row['Admin2'], county)
    return False


def main():
    file = get_file('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')

    state = str(input("Please Choose a State: "))
    print_counties(state, file)
    found_county = False
    file = get_file('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
    while not found_county:
        county = input("Please Choose a County/Region from above: ")
        found_county = check_county(state, county, file)
    x = []
    y = []
    title = ''

    file = get_file('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
    get_data(x, y, file, state, county, title)
    fig = plt.figure(figsize=(10,9.5))
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.scatter(x, y)
    axes.plot(x,y)
    plt.show()

if __name__ == '__main__':
    main()