# USGS Streamgage Data Scraper

Download, scrape, and clean data about the US Geological Survey's (USGS)
streamgages around the United States.

USGS has over 10,000 streamgages, which collect data about the waterflow of rivers
and waterways. This script gets identifying info, like the monitoring location ID 
and name, from the Water Services API, then uses the monitoring location ID to scrape
USGS inventory webpages for the following additional info:
- the agency monitoring the streamgage (usually USGS)
- monitoring location ID number
- name of monitoring location
- latitude
- longitude
- lat/long type
- county
- hydrologic unit
- drainage area (square miles)
- datum of gage (AKA elevation)
- datum type

## Usage
```
python3 get_streamgages_for_state.py ny
```

where `ny` is a state's two-letter code (examples: `az`, `ca`, `or`)

## Data sources:
* [USGS National Water Dashboard](https://dashboard.waterdata.usgs.gov/app/nwd/en/?aoi=default)
* [USGS Water Services API](https://waterdata.usgs.gov/nwis/rt)
* [USGS Water Services API URL builder tool](https://waterservices.usgs.gov/rest/IV-Test-Tool.html)

## Data output on Kaggle
* [USGS Alabama Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-alabama-streamgages-may-2023)  
* [USGS Alaska Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-alaska-streamgages-may-2023)  
* [USGS Arizona Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-arizona-streamgages-may-2023)  
* [USGS Arkansas Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-arkansas-streamgages-may-2023)  
* [USGS California Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-california-streamgages-may-2023)  
* [USGS Colorado Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-colorado-streamgages-may-2023)  
* [USGS Connecticut Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-connecticut-streamgages-may-2023)  
* [USGS Delaware Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-delaware-streamgages-may-2023)  
* [USGS Florida Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-florida-streamgages-may-2023)  
* [USGS Georgia Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-georgia-streamgages-may-2023)  
* [USGS Hawaii Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-hawaii-streamgages-may-2023)  
* [USGS Idaho Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-idaho-streamgages-may-2023)  
* [USGS Indiana Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-indiana-streamgages-may-2023)  
* [USGS Iowa Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-iowa-streamgages-may-2023)  
* [USGS Kansas Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-kansas-streamgages-may-2023)  
* [USGS Kentucky Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-kentucky-streamgages-may-2023)  
* [USGS Louisiana Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-louisiana-streamgages-may-2023)  
* [USGS Maine Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-maine-streamgages-may-2023)  
* [USGS Maryland Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-maryland-streamgages-may-2023)  
* [USGS Massachusetts Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-massachusetts-streamgages-may-2023)  
* [USGS Michigan Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-michigan-streamgages-may-2023)  
* [USGS Minnesota Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-minnesota-streamgages-may-2023)  
* [USGS Mississippi Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-mississippi-streamgages-may-2023)  
* [USGS Missouri Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-missouri-streamgages-may-2023)  
* [USGS Montana Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-montana-streamgages-may-2023)  
* [USGS Nebraska Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-nebraska-streamgages-may-2023)  
* [USGS Nevada Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-nevada-streamgages-may-2023)  
* [USGS New Hampshire Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-new-hampshire-streamgages-may-2023)  
* [USGS New Jersey Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-new-jersey-streamgages-may-2023)  
* [USGS New Mexico Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-new-mexico-streamgages-may-2023)  
* [USGS New York Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-new-york-streamgages-may-2023)  
* [USGS North Carolina Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-north-carolina-streamgages-may-2023)  
* [USGS North Dakota Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-north-dakota-streamgages-may-2023)  
* [USGS Ohio Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-ohio-streamgages-may-2023)  
* [USGS Oklahoma Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-oklahoma-streamgages-may-2023)  
* [USGS Oregon Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-oregon-streamgages-may-2023)  
* [USGS Pennsylvania Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-pennsylvania-streamgages-may-2023)  
* [USGS Rhode Island Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-rhode-island-streamgages-may-2023)  
* [USGS South Carolina Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-south-carolina-streamgages-may-2023)  
* [USGS South Dakota Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-south-dakota-streamgages-may-2023)  
* [USGS Tennessee Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-tennessee-streamgages-may-2023)  
* [USGS Texas Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-texas-streamgages-may-2023)  
* [USGS Utah Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-utah-streamgages-may-2023)  
* [USGS Vermont Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-vermont-streamgages-may-2023)  
* [USGS Virginia Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-virginia-streamgages-may-2023)  
* [USGS Washington Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-washington-streamgages-may-2023)  
* [USGS Washington, D.C., Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-washington-dc-streamgages-may-2023)  
* [USGS West Virginia Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-west-virginia-streamgages-may-2023)  
* [USGS Wisconsin Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-wisconsin-streamgages-may-2023)  
* [USGS Wyoming Streamgages](https://www.kaggle.com/datasets/protobioengineering/usgs-wyoming-streamgages-may-2023)  
