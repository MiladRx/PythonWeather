import requests  # ? Importerer requests modulet, som tillader os at sende forespørgsler

def få_vejr(by_navn, api_nøgle):
    
    # ? Funktion til at hente vejrdata for en given by ved hjælp af OpenWeatherMap API'en
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={by_navn}&appid={api_nøgle}&units=metric"
    # ? URL'en til API'en med den specificerede by og API-nøgle, samt enheden sat til metric for Celsius
    
    respons = requests.get(url)  # ? Sender en GET-forespørgsel til API'en og gemmer svaret
    
    data = respons.json()  # ? Konverterer svaret til JSON-format og gemmer dataen
    
    return data  # ? Returnerer vejrdataen til funktionens kalderskope

def hoved():
    api_nøgle = "adedf584a288b61edece573a8f4527d1"  # ? Erstat "DIN_API_NØGLE" med din faktiske API-nøgle fra OpenWeatherMap
    
    by = input("Indtast bynavn: ")  # ? Modtager brugerens input af bynavn

    vejrdata = få_vejr(by, api_nøgle)  # ? Kalder funktionen få_vejr() for at hente vejrdataen for den angivne by

    if vejrdata["cod"] == 200:  # ? Hvis statuskoden er 200, hvilket betyder succes
        
        print("\nVejrrapport for", by)  # ? Udskriver vejrrapportens overskrift med den angivne by
        
        print("Temperatur:", vejrdata["main"]["temp"], "°C")  # ? Udskriver temperaturdataen i Celsius
        
        print("Vejr:", vejrdata["weather"][0]["description"])  # ? Udskriver vejrbeskrivelsen
        
        print("Luftfugtighed:", vejrdata["main"]["humidity"], "%")  # ? Udskriver luftfugtigheden i procent
        
        print("Vindhastighed:", vejrdata["wind"]["speed"], "m/s")  # ? Udskriver vindhastigheden i meter per sekund
    else:
        print("By ikke fundet eller der opstod en fejl. Prøv igen.")  # ? Hvis statuskoden ikke er 200, udskrives en fejlmeddelelse

if __name__ == "__main__":
    hoved()  # ? Kald til hovedfunktionen for at køre applikationen
