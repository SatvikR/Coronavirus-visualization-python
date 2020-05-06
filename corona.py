import matplotlib.pyplot as plt
import csv
import requests

def get_file(url):
    return csv.DictReader(requests.get(url).iter_lines(decode_unicode=True))

def get_data(x, y, file, state, county):
    for row in file:
        if row['Province_State'] == state and row['Admin2'] == county:
            i = 0
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
    return False


def main():
    file = get_file('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')

    state = str(input("Please Choose a State: "))
    print_counties(state, file)
    found_county = False
    
    while not found_county:
        file = get_file('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
        county = input("Please Choose a County/Region from above: ")
        found_county = check_county(state, county, file)
    x = []
    y = []

    file = get_file('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
    get_data(x, y, file, state, county)

    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 9
    fig_size[1] = 9
    plt.rcParams["figure.figsize"] = fig_size

    plt.scatter(x, y)
    plt.plot(x,y)

    plt.ylabel("Infected Citizens")
    plt.xlabel("Days")
    title = "Confirmed Cases in " + county + ", " + state + " For The Past 100 Days"
    
    plt.title(title)
    plt.show()

if __name__ == '__main__':
    main()
