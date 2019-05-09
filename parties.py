import csv
import pprint


def get_bar_party_data():
    """this function reads from a csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific location and the number of complaint calls
     it received in 2016"""

    bar_list = []
    with open('bar_locations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            bar_dict = {'location_type': row[0],
                        'zip_code': row[1],
                        'city': row[2],
                        'borough': row[3],
                        'latitude': row[4],
                        'longitude': row[5],
                        'num_calls': row[6]}
            bar_list.append(bar_dict)
    return bar_list


def print_data(data):
    for entry in data:
        #print(entry)
        pprint.pprint(entry)


def get_most_noisy_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    
    borough_bronx_num_calls = []
    borough_brooklyn_num_calls = []
    borough_manhattan_num_calls = []
    borough_queens_num_calls = []
    borough_staten_island_num_calls = []

    city_dictionary = {'BRONX':[],
                       'BROOKLYN':[],
                       'NEW YORK':[],
                       'ASTORIA':[],
                       'BAYSIDE':[],
                       'BELLEROSE':[],
                       'CAMBRIA HEIGHTS':[],
                       'COLLEGE POINT':[],
                       'CORONA':[],
                       'EAST ELMHURST':[],
                       'ELMHURST':[],
                       'FAR ROCKAWAY':[],
                       'FLUSHING':[],
                       'FOREST HILLS':[],
                       'GLEN OAKS':[],
                       'HOLLIS':[],
                       'HOWARD BEACH':[],
                       'JACKSON HEIGHTS':[],
                       'JAMAICA':[],
                       'KEW GARDENS':[],
                       'LITTLE NECK':[],
                       'LONG ISLAND CITY':[],
                       'MASPETH':[],
                       'OZONE PARK':[],
                       'QUEENS VILLAGE':[],
                       'REGO PARK':[],
                       'RICHMOND HILL':[],
                       'RIDGEWOOD':[],
                       'ROCKAWAY PARK':[],
                       'ROSEDALE':[],
                       'SAINT ALBANS':[],
                       'SOUTH OZONE PARK':[],
                       'SOUTH RICHMOND HILL':[],
                       'SUNNYSIDE':[],
                       'WHITESTONE':[],
                       'WOODHAVEN':[],
                       'WOODSIDE':[],
                       'STATEN ISLAND':[]}


    for i in range(len(data)):
        for key,val in data[i].items():
            if key == 'borough' and val == 'BRONX':
                borough_bronx_num_calls.append(int(data[i]['num_calls']))
                for city,num_calls in city_dictionary.items():
                    if city == data[i]['city']:
                        city_dictionary[city].append(int(data[i]['num_calls']))
            if key == 'borough' and val == 'BROOKLYN':
                borough_brooklyn_num_calls.append(int(data[i]['num_calls']))
                for city,num_calls in city_dictionary.items():
                    if city == data[i]['city']:
                        city_dictionary[city].append(int(data[i]['num_calls']))
            if key == 'borough' and val == 'MANHATTAN':
                borough_manhattan_num_calls.append(int(data[i]['num_calls']))
                for city,num_calls in city_dictionary.items():
                    if city == data[i]['city']:
                        city_dictionary[city].append(int(data[i]['num_calls']))
            if key == 'borough' and val == 'QUEENS':
                borough_queens_num_calls.append(int(data[i]['num_calls']))
                for city,num_calls in city_dictionary.items():
                    if city == data[i]['city']:
                        city_dictionary[city].append(int(data[i]['num_calls']))
            if key == 'borough' and val == 'STATEN ISLAND':
                borough_staten_island_num_calls.append(int(data[i]['num_calls']))
                for city,num_calls in city_dictionary.items():
                    if city == data[i]['city']:
                        city_dictionary[city].append(int(data[i]['num_calls']))
            if key == 'borough' and val == 'Unspecified':
                for city,num_calls in city_dictionary.items():
                    if city == data[i]['city']:
                        city_dictionary[city].append(int(data[i]['num_calls']))

    dictionary = {}
    dictionary.setdefault('BRONX',sum(borough_bronx_num_calls))
    dictionary.setdefault('BROOKLYN',sum(borough_brooklyn_num_calls))
    dictionary.setdefault('MANHATTAN',sum(borough_manhattan_num_calls))
    dictionary.setdefault('QUEENS',sum(borough_queens_num_calls))
    dictionary.setdefault('STATEN_ISLAND',sum(borough_staten_island_num_calls))
    
    for city,num_calls in city_dictionary.items():
        city_dictionary[city].append(sum(city_dictionary[city]))

    num_borough_calls = float('-Inf')
    borough = ''
    for key,val in dictionary.items():
        if val > num_borough_calls:
            num_borough_calls = val
            borough = key

    num_city_calls = float('-Inf')
    city = ''
    for key in city_dictionary.keys():
        if city_dictionary[key][-1] > num_city_calls:
            num_city_calls = city_dictionary[key][-1]
            city = key

    noisiest_city_and_borough = {'city': city, 'borough': borough, 'num_city_calls': num_city_calls, 'num_borough_calls': num_borough_calls}

    # write code here to find the noisiest city and borough and their respective metrics

    return noisiest_city_and_borough


def get_quietest_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    borough_bronx_num_calls = []
    borough_brooklyn_num_calls = []
    borough_manhattan_num_calls = []
    borough_queens_num_calls = []
    borough_staten_island_num_calls = []

    city_dictionary = {'BRONX':[],
                       'BROOKLYN':[],
                       'NEW YORK':[],
                       'ASTORIA':[],
                       'BAYSIDE':[],
                       'BELLEROSE':[],
                       'CAMBRIA HEIGHTS':[],
                       'COLLEGE POINT':[],
                       'CORONA':[],
                       'EAST ELMHURST':[],
                       'ELMHURST':[],
                       'FAR ROCKAWAY':[],
                       'FLUSHING':[],
                       'FOREST HILLS':[],
                       'GLEN OAKS':[],
                       'HOLLIS':[],
                       'HOWARD BEACH':[],
                       'JACKSON HEIGHTS':[],
                       'JAMAICA':[],
                       'KEW GARDENS':[],
                       'LITTLE NECK':[],
                       'LONG ISLAND CITY':[],
                       'MASPETH':[],
                       'OZONE PARK':[],
                       'QUEENS VILLAGE':[],
                       'REGO PARK':[],
                       'RICHMOND HILL':[],
                       'RIDGEWOOD':[],
                       'ROCKAWAY PARK':[],
                       'ROSEDALE':[],
                       'SAINT ALBANS':[],
                       'SOUTH OZONE PARK':[],
                       'SOUTH RICHMOND HILL':[],
                       'SUNNYSIDE':[],
                       'WHITESTONE':[],
                       'WOODHAVEN':[],
                       'WOODSIDE':[],
                       'STATEN ISLAND':[]}


    for i in range(len(data)):
        for key,val in data[i].items():
            if key == 'borough' and val == 'BRONX':
                borough_bronx_num_calls.append(int(data[i]['num_calls']))
                for city,num_calls in city_dictionary.items():
                    if city == data[i]['city']:
                        city_dictionary[city].append(int(data[i]['num_calls']))
            if key == 'borough' and val == 'BROOKLYN':
                borough_brooklyn_num_calls.append(int(data[i]['num_calls']))
                for city,num_calls in city_dictionary.items():
                    if city == data[i]['city']:
                        city_dictionary[city].append(int(data[i]['num_calls']))
            if key == 'borough' and val == 'MANHATTAN':
                borough_manhattan_num_calls.append(int(data[i]['num_calls']))
                for city,num_calls in city_dictionary.items():
                    if city == data[i]['city']:
                        city_dictionary[city].append(int(data[i]['num_calls']))
            if key == 'borough' and val == 'QUEENS':
                borough_queens_num_calls.append(int(data[i]['num_calls']))
                for city,num_calls in city_dictionary.items():
                    if city == data[i]['city']:
                        city_dictionary[city].append(int(data[i]['num_calls']))
            if key == 'borough' and val == 'STATEN ISLAND':
                borough_staten_island_num_calls.append(int(data[i]['num_calls']))
                for city,num_calls in city_dictionary.items():
                    if city == data[i]['city']:
                        city_dictionary[city].append(int(data[i]['num_calls']))
            if key == 'borough' and val == 'Unspecified':
                for city,num_calls in city_dictionary.items():
                    if city == data[i]['city']:
                        city_dictionary[city].append(int(data[i]['num_calls']))

    dictionary = {}
    dictionary.setdefault('BRONX',sum(borough_bronx_num_calls))
    dictionary.setdefault('BROOKLYN',sum(borough_brooklyn_num_calls))
    dictionary.setdefault('MANHATTAN',sum(borough_manhattan_num_calls))
    dictionary.setdefault('QUEENS',sum(borough_queens_num_calls))
    dictionary.setdefault('STATEN_ISLAND',sum(borough_staten_island_num_calls))
    
    for city,num_calls in city_dictionary.items():
        city_dictionary[city].append(sum(city_dictionary[city]))

    num_borough_calls = float('Inf')
    borough = ''
    for key,val in dictionary.items():
        if val < num_borough_calls:
            num_borough_calls = val
            borough = key

    num_city_calls = float('Inf')
    city = ''
    for key in city_dictionary.keys():
        if city_dictionary[key][-1] < num_city_calls:
            num_city_calls = city_dictionary[key][-1]
            city = key

    quietest_city_and_borough = {'city': city, 'borough': borough, 'num_city_calls': num_city_calls, 'num_borough_calls': num_borough_calls}

    # write code here to find the quietest city and borough and their respective metrics

    return quietest_city_and_borough


if __name__ == '__main__':
    bar_data = get_bar_party_data()

    # uncomment the line below to see what the data looks like
    # print_data(bar_data)

    noisy_metrics = get_most_noisy_city_and_borough(bar_data)

    quiet_metrics = get_quietest_city_and_borough(bar_data)

    print('Noisy Metrics: {}'.format(noisy_metrics))
    print('Quiet Metrics: {}'.format(quiet_metrics))
