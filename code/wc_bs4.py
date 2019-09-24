from bs4 import BeautifulSoup

html = """

<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p class="item">This is a paragraph.</p>
<p class="item">This is a content.</p>

</body>
</html>

"""

soup = BeautifulSoup(html, 'html.parser')

# Direct
# print(soup.body)
# print(soup.head)
# print(soup.head.title)

# find()
el = soup.find('div')

# find_all() or findAll()
# el = soup.find_all('div')
# el = soup.find_all('div')[1]

# el = soup.find(id='section-1')
# el = soup.find(class_='items')
# el = soup.find(attrs={"data-hello": "hi"})

# Select 
# el = soup.select('#section-1')
# el = soup.select('#section-1')[0]
# el = soup.select('.item')[0]

# get_text()
# el = soup.find(class_='item').get_text()

el = soup.select('.item')
for item in el:
    print(item.get_text())

# Navigation
# el = soup.body.contents[1].contents[1].find_next_sibling()
# el = soup.find(class_='item').find_parent()
# el = soup.find('h3').find_next_sibling('p')

print(el)