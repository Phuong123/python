import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()

print(root.tag, root.attrib)

for child in root:
    print(child.tag, child.attrib)

print(root[0][0].text)
print(root[0][1].text)
print(root[0][2].text)

for country in root.iter('country'):
    print(country.attrib)

print("consider neighbor:")

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

# Find interesting elements
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

# Remove elements
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')

# parsing XML with namespaces

tree = ET.parse('xml_test.xml')
root = tree.getroot()

for actor in root.findall('{http://people.example.com}actor'):
    name = actor.find('{http://people.example.com}name')
    print(name.text)
    for char in actor.findall('{http://characters.example.com}character'):
        print(' |-->', char.text)


