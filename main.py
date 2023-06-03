from plyer import webbrowser

def open_address_in_browser(address):
    url = "https://www.google.com/maps/search/" + address
    webbrowser.open(url)

# Przykład użycia
address = "Warsaw, Poland"
open_address_in_browser(address)