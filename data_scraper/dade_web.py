import requests
import re
import time

folio_1 = "01"
folio_2 = ["4115","4116","4120","4121","4122","4128","4129","4140"]
url_prefix = r"https://www8.miamidade.gov/Apps/PA/PApublicServiceProxy/PaServicesProxy.ashx?Operation=GetPropertySearchByFolio&clientAppName=PropertySearch&folioNumber="
results = {}
for folio_sec in folio_2:
    found_valid = False
    consecutive_invalid = 0
    for i in range(1, 200):
        time.sleep(3)
        folio = f"{folio_1}-{folio_sec}-{i:03d}-0010"
        url = f"{url_prefix}{folio.replace('-', '')}"
        print(url)
        response = requests.get(url)
        # print(response.text)
        match = re.findall(r'"SubdivisionDescription":"(.+?)"', response.text)
        if match:
            print(match[0])
            results[folio] = match[0]
            found_valid = True
            consecutive_invalid = 0
        elif found_valid:
            consecutive_invalid += 1
        if consecutive_invalid >= 20:
            break

print("===== All results =====")
with open('miami.csv', 'w') as fh:
    for folio in results:
        print(f'{folio} - "{results[folio]}"')
        fh.write(f'{folio},{results[folio]}\n')
