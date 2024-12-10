# import pandas lib as pd
import pandas as pd
import requests

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSZq2ReCkXH3NVFAnGRmCz7gTAGZk5zM35bngJDb27Ni0HO9U89Pm5g_orGtcQKcQ/pub?gid=400371444&single=true&output=csv"

output_file = "Fakturor.csv"

try: 
    
    response = requests.get(url)
    response.raise_for_status()
    
    with open(output_file, "wb") as file:
        file.write(response.content)
        
    print(f"SCV downloaded successfully and save as '{output_file}")
    
except requests.exceptions.RequestsException as e:
    print(f"Error fetching the CSV: {e}")
    exit()
    
try:
    dataframe = pd.read_csv(output_file)
    

    

    
except Exception as e:
    print(f"\nFel vid läsning eller bearbetnign av CSV-filen: {e}")



try:
    
    
    dataframe['Summa (exkl. moms)'] = dataframe['Antal'] * dataframe['Enhetspris (kr/antal)']
    dataframe['Total momskostnad'] = dataframe['Summa (exkl. moms)'] * (dataframe['Moms (%)']/100)
    dataframe['Summa (inkl. moms)'] = dataframe['Summa (exkl. moms)'] + dataframe['Total momskostnad']
    print(dataframe)
    
    

    
except Exception as e:
    print(f"Fel vid analys av data: {e}")
    exit()






'''
    antal = dataframe['Antal']
    enhetpris = dataframe['Enhetspris (kr/antal)']
    moms = dataframe['Moms (%)']
    total = antal * enhetpris


    print("\nAllt data:")
    print(dataframe.to_string())


    print("\nKolumninformation")
    print(dataframe.info())
    
    print("\nSatistisk sammanfattning:")
    print(dataframe.describe)
'''