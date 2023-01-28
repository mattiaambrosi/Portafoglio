import requests
import csv

def getFile(url):
    header = {'Connection': 'keep-alive',
            'Expires': '-1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
            }
    website = requests.get(url, headers=header)
    return website.text

def parseCsv(content):
    csvReader = csv.DictReader(content.splitlines())
    data = [row for row in csvReader]
    return data

def main():
    csvContent = getFile("https://query1.finance.yahoo.com/v7/finance/download/PIRC.MI?period1=1642923403&period2=1674459403&interval=1d&events=history&includeAdjustedClose=true")
    data = parseCsv(csvContent)
    print(data)

if __name__ == "__main__":
    main()
