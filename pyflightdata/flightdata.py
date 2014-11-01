from .common import REG_BASE, FLT_BASE, AIRPORT_BASE, get_data, get_countries_data, get_airports_data

#most of these are resundant from common.py
#doing it this way so that we can tweak for different sites later

def get_by_flight_number(flight_number):
	url = FLT_BASE+flight_number
	return get_data(url)
	
def get_by_tail_number(tail_number):
	url = REG_BASE+tail_number
	return get_data(url)

def get_countries():
	return get_countries_data()
	
def get_airports(country):
	url = AIRPORT_BASE+country
	return get_airports_data(url)