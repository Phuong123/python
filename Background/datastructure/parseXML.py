from xml.etree import ElementTree

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)

print(tree)

# traversing the parsed tree
for node in tree.iter():
    print(node.tag)

# consider only nodes with tag 'outline'
for node in tree.iter('outline'):
    name = node.attrib.get('text')
    url = node.attrib.get('xmlUrl')
    if name and url:
        print('    %s' % name)
        print('    %s' % url)
    else:
        print(name)

# find nodes in a document
for node in tree.findall('.//outline'):
    url = node.attrib.get('xmlUrl')
    if url:
        print(url)

    html = node.attrib.get('htmlUrl')
    if html:
        print(html)

print('There are more information')
# find more
for node in tree.findall('.//outline/outline'):
    url = node.attrib.get('xmlUrl')
    print(url)

