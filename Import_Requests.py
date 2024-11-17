url = 'https://screener.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data from the webpage
data = soup.find('div', class_='content')
print(data.text)