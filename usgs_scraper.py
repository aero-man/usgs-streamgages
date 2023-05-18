'''
Get extra data about a USGS Water Services monitoring location
by scraping it from the monitoring location's inventory webpage.

Input:
    - Monitoring location ID number (Example: 09504500)
Output:
    - latitude
    - longitude
    - lat/long type
    - county
    - hydrologic unit
    - drainage area (square miles)
    - datum of gage (AKA elevation)

Inventory page URLs look like:
    https://waterdata.usgs.gov/nwis/inventory?site_no=00000000&agency_cd=USGS

    where "00000000" is the monitoring location ID
'''

import re
import requests
from bs4 import BeautifulSoup

# URL for latitude/longitude web scraping
usgs_inventory_url = 'https://waterdata.usgs.gov/nwis/inventory?site_no=00000000&agency_cd=USGS'

def extra_data_scraper(monitoring_location_id):
    '''
    Takes in a USGS Water Services monitoring location ID, scrapes the USGS website 
    for that monitoring location's latitude and longitude, and returns the lat/long.

    Args:
        monitoring location ID. Example: '09504500'
    Returns:
        dictionary of monitoring location data
            - latitude
            - longitude
            - lat/long type
            - county
            - hydrologic unit
            - drainage area (square miles)
            - datum of gage (AKA elevation)
    '''

    # Print monitoring location we're scraping data for
    print(f'Scraping data from USGS site for monitoring location: {monitoring_location_id}')

    # Get the HTML from the USGS inventory page
    full_url = usgs_inventory_url.replace('00000000', monitoring_location_id)
    response = requests.get(full_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the chunk of data we want to parse (which has the lat/long, etc.)
    try:
        data_table = soup.find(id="stationTable")
        raw_data_points = data_table.find_all('dd')
    except Exception as e:
        print('ERROR:', 'could not find stationTable div on USGS inventory page.', e)
        raw_data_points = []

    # Fix character encoding to help regex. (Gets rid of u'\xa0' chars)
    raw_data_points = [x.text for x in raw_data_points]
    raw_data_points = [x.replace(u'\xa0', u' ') for x in raw_data_points]

    # Pick out the lines we want to parse. If they don't exist, assign `None`.
    try:
        lat_long_row = [x for x in raw_data_points if 'Latitude' in x][0]
    except Exception as e:
        print('ERROR: could not parse lat/long:', e)
        lat_long_row = None
    try:
        county_and_hydro_row = [x for x in raw_data_points if 'Hydrologic Unit' in x][0]
    except Exception as e:
        print('ERROR: could not parse county and hydrologic unit:', e)
        county_and_hydro_row = None
    try:
        drainage_row = [x for x in raw_data_points if 'Drainage area' in x][0]
    except Exception as e:
        print('ERROR: could not parse drainage area:', e)
        drainage_row = None
    try:
        datum_row = [x for x in raw_data_points if 'Datum of gage' in x][0]
    except Exception as e:
        print('ERROR: could not parse datum of gage:', e)
        datum_row = None

    # Create dict with empty values to prevent unassigned variable errors
    scraped_data = {
        'latitude': None,
        'longitude': None,
        'lat_long_type': None,
        'county': None,
        'hydrologic_unit': None,
        'drainage_area': None,
        'datum_of_gage': None,
        'datum_type': None
    }

    # Parse latitude and longitude
    try:
        lat_long_regex = r'Latitude\s{1,2}([0-9]{1,3}°[0-9]{1,3}\'[0-9.]{1,5}\"),\s{1,3}Longitude\s{1,2}([0-9]{1,3}°[0-9]{1,3}\'[0-9.]{1,5}\")\s{1,3}([a-zA-Z0-9]+)'
        extraction1 = re.search(lat_long_regex, lat_long_row)
        scraped_data['latitude'] = extraction1.group(1)
        scraped_data['longitude'] = extraction1.group(2)
        scraped_data['lat_long_type'] = extraction1.group(3)
    except Exception as e:
        print("ERROR:", lat_long_row, e)

    # Parse county
    try:
        county_regex = r'([a-zA-Z\-\s]+),.+Hydrologic Unit [0-9]+'
        extraction2 = re.search(county_regex, county_and_hydro_row)
        scraped_data['county'] = extraction2.group(1)
    except Exception as e:
        print("ERROR:", county_and_hydro_row, e)

    # Parse hydrologic unit (separate from county in case of regex error)
    try:
        huc_regex = r'[a-zA-Z\-\s]+,.+Hydrologic Unit ([0-9]+)'
        extraction3 = re.search(huc_regex, county_and_hydro_row)
        scraped_data['hydrologic_unit'] = extraction3.group(1)
    except Exception as e:
        print("ERROR:", county_and_hydro_row, e)

    # Parse drainage area
    try:
        drainage_regex = r'Drainage area:\s+([0-9.,]+)\s+square miles'
        extraction4 = re.search(drainage_regex, drainage_row)
        scraped_data['drainage_area'] = extraction4.group(1).replace(',', '')
    except Exception as e:
        print("ERROR:", drainage_row, e)

    # Parse datum of gage (elevation) and datum type
    try:
        datum_regex = r'Datum of gage:\s+([0-9.,]+)\s+feet above\s+([a-zA-Z0-9]+).*'
        extraction5 = re.search(datum_regex, datum_row)
        scraped_data['datum_of_gage'] = extraction5.group(1).replace(',', '')
        scraped_data['datum_type'] = extraction5.group(2)
    except Exception as e:
        print("ERROR:", datum_row, e)

    try:
        print(f'Scraped data: {scraped_data}')
    except Exception as e:
        print("ERROR: could not print all parsed data:", e)

    return scraped_data

