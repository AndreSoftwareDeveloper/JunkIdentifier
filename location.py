from googlemaps import Client


def get_my_location(api_key):
    gmaps = Client(api_key)

    try:
        result = gmaps.geolocate()
        latitude = result['location']['lat']
        longitude = result['location']['lng']
        return {"latitude": latitude, "longitude": longitude}
    except Exception as e:
        print("Błąd podczas pobierania lokalizacji:", str(e))


def get_disposal_point_location(api_key, disposal_point_category):
    coordinates = get_my_location(api_key)
    latitude = coordinates["latitude"]
    longitude = coordinates["longitude"]
    return f"https://www.google.com/maps/search/{disposal_point_category}/@{latitude},{longitude}" \
           f",11z/data=!3m1!4b1?entry=ttu"  # TODO change magic string to something smarter
