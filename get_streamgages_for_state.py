'''
Get all the monitoring locations for a state from the USGS Water Services API.

Input:
    The state we want data from (Arizona, New York, etc.)
Output:
    A CSV of all monitoring locations, including:
        - the agency monitoring them (usually USGS)
        - monitoring location ID number
        - name of monitoring location
        - latitude
        - longitude
        - lat/long type
        - county
        - hydrologic unit
        - drainage area (square miles)
        - datum of gage (AKA elevation)
    Example CSV:
        agency

Data:
    USGS National Water Dashboard:
        https://dashboard.waterdata.usgs.gov/app/nwd/en/?aoi=default
    USGS Water Services API:
        https://waterdata.usgs.gov/nwis/rt
    USGS Water Services API URL builder tool:
        https://waterservices.usgs.gov/rest/IV-Test-Tool.html
'''

import csv
import numpy as np
import pandas as pd
import re
import requests
import sys

from datetime import datetime

from usgs_scraper import extra_data_scraper


def add_location_details(row):
    '''
    Scrapes the following from the USGS website and adds it to the dataframe for the current row:
        - latitude
        - longitude
        - lat/long type
        - county
        - hydrologic unit
        - drainage area (square miles)
        - datum of gage (AKA elevation)
    '''
    location_id = row['location_id']
    scraped_data = extra_data_scraper(location_id)
    row['latitude'] = scraped_data['latitude']
    row['longitude'] = scraped_data['longitude']
    row['lat_long_type'] = scraped_data['lat_long_type']
    row['county'] = scraped_data['county']
    row['hydrologic_unit'] = scraped_data['hydrologic_unit']
    row['drainage_area'] = scraped_data['drainage_area']
    row['datum_of_gage'] = scraped_data['datum_of_gage']
    row['datum_type'] = scraped_data['datum_type']

    return row

def main(arg):
    # Set the state (e.g. AZ, NY, CA) with user args
    state = arg
    print(f'Getting USGS streamgage data for state: {state}')

    # Define output CSV
    timestamp = datetime.now().strftime('%Y%m%d')
    outfile = f'data/usgs_streamgages_{state}_{timestamp}.csv'

    # Build the API URL with the state code
    data_type = 'rdb' # USGS RDB tab-delimited datatype
    water_api_url = f"https://nwis.waterservices.usgs.gov/nwis/iv/?format={data_type}&stateCd={state}&parameterCd=00060,00065&siteStatus=all"

    # Send the data request to the Water Services API
    response = requests.get(water_api_url)

    # Split the data into neat lines
    text = response.text
    lines = text.split('\n')

    # Remove information header
    for i in range(len(lines)):
        if lines[i][:24] == '# Data for the following':
            data_block_start = i + 1
            print(lines[i])
    lines = lines[data_block_start:]

    # Parse the data file for monitoring station data
    monitoring_locations = []
    for line in lines:
        if line[:5] == '# ---': # End of block that lists monitoring location IDs
            break
        else:
            try:
                regex = r'#    ([a-zA-Z]+) ([0-9]+) ([A-Za-z0-9\.\,\s\-\@\(\)]+)'
                extraction = re.search(regex, line)
                print(extraction.groups())
                agency = extraction.group(1)
                location_id = extraction.group(2)
                name = extraction.group(3)

                monitoring_locations.append({
                    'agency': agency,
                    'location_id': location_id,
                    'name': name
                    })
            except Exception as e:
                print('ERROR:', 'could not extract info from line:', line)
    
    # Convert parsed data to Pandas dataframe
    df = pd.DataFrame(monitoring_locations)

    # Get the extra data (lat/long, drainage area, etc.) for the monitoring location via web scraping
    df = df.apply(add_location_details, axis=1)

    # Print df with new rows
    print(df)

    # Save data to a CSV file
    df.to_csv(outfile)

if __name__ == '__main__':
    if sys.argv[1]:
        state = sys.argv[1] # Examples: az, ny, ca
        main(state)
    else:
       default_state = 'az'
       main(default_state)

