#Paket som gör det enkare att skicka HTTP-förfrågningar som att hämta data från en webbsida
import requests 
import pandas as pd

#Länken till den offentliga Google-filen (detta fall excell-dokument)
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSOdy-HETIa5d5u9_OSTGeAZ_mTwwn9C8cy5zZrGYG8lOWJlrvx7MDamB4i2xzP0SXbbqCMkj5pdMmF/pub?output=csv" 

#Namnet för filen när man laddar ner den
output_file = "Test_form.csv"


#"Try"-kommandot andvänds för att fånga eventuella fel som kan uppstå när koden körs. Ifall koden inte kan gå igenom så kommer koden direkt hoppa till "except"-delen
try:
    
    #Med "Get"-funktionen hämtar koden data från den offentliga datan i Excell-dokumentet. När förfrågan är klar sparar servern att svara med innehållet och lagras i variabeln "response"
    response = requests.get(url)
    
    #Denna funktion kollar om HTTP-förfrågan lycakdes. Om den misslyckas hoppar koden direkt till except. Annars kör den vidare.
    response.raise_for_status()
    
    #Den första raden öppnar den fil där vi vill spara den nedladdade CSV-filen. "open(output_file, "wb") öppnar filen in binart skrivläge (viktigs för att hantera icke-textdata)
    with open(output_file, "wb") as file:
        
        #Här skriver man det faktiska innehålle från response till den öppnade filen. "response.content" innehåller den råa binära datan från Googel Excell.
        file.write(response.content)
        
    #Meddelar användaren att filen är nerladdad
    print(f"CSV downloaded successfully and save as '{output_file}'")
    
#Visas upp ifall filen inte lyckades ladda ner
except requests.exceptions.RequestException as e:
    print(f"Error fetching the CSV: {e}")
    exit()
    
# Steg 2: Läs och visa grundläggande information om CSV-filen
try:
    # Läs CSV-filen med pandas
    df = pd.read_csv(output_file)

    # Visa de första raderna för att förstå strukturen
    print("\nAllt data:")
    print(df.to_string())


except Exception as e:
    print(f"Fel vid läsning eller bearbetning av CSV-filen: {e}")
    exit()  # Avsluta programmet om CSV inte kunde läsas


try:
    
    if 'Car' in df.columns:
        total_cars = df['Car'].count()
        different_cars = df['Car'].value_counts()
        print(f"\nNumber of cars: {total_cars}")
        print(f"\nTotal number for each brand: {different_cars}")
        
    if 'Color' in df.columns:
        color_counts = df['Color'].value_counts()
        print(f"\nTotal number for each color : {color_counts}")
              
except Exception as e:
    print(f"Fel vid analys av data: {e}")
    exit()
      

'''


    # Visa information om kolumner och datatyper
    print("\nKolumninformation:")
    print(df.info())

    # Statistisk sammanfattning av numeriska kolumner
    print("\nStatistisk sammanfattning:")
    print(df.describe())
'''