import urllib.request

url = input("Enter the full url you would like to scrape: ")

req = urllib.request.Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
file = urllib.request.urlopen(req)
read_data = file.read()
data = read_data.decode('utf-8')

file.close()

with open('C:\\Users\\The Gibbon\\Desktop\\Projects\\Python\\Webscraper\\output.txt', 'w', encoding='utf-8') as f:
    f.write(data)
    
    f.close()
    