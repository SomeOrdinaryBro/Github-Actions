import yaml
import xml.etree.ElementTree as xml_tree

# Load the YAML file
with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Create the root RSS element with namespaces
rss_element = xml_tree.Element('rss', {
    'version': '2.0',
    'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
})

# Create the channel element
channel_element = xml_tree.SubElement(rss_element, 'channel')

# Add basic channel elements
xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'author').text = yaml_data['author']
xml_tree.SubElement(
    channel_element, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_element, 'category').text = yaml_data['category']
# Add a link element as RSS requires a link
xml_tree.SubElement(channel_element, 'link').text = "http://example.com"

# Add image element
image_element = xml_tree.SubElement(channel_element, 'image')
xml_tree.SubElement(image_element, 'url').text = yaml_data['image']
xml_tree.SubElement(image_element, 'title').text = yaml_data['title']
# Same link as the channel
xml_tree.SubElement(image_element, 'link').text = "http://example.com"

# Add items
for item in yaml_data['item']:
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title').text = item['title']
    xml_tree.SubElement(item_element, 'description').text = item['description']
    xml_tree.SubElement(item_element, 'pubDate').text = item['published']
    enclosure_element = xml_tree.SubElement(item_element, 'enclosure', {
        'url': item['file'],
        'length': str(item['length']),
        'type': 'audio/mpeg'
    })
    xml_tree.SubElement(
        item_element, 'itunes:duration').text = item['duration']

# Write the XML to a file
output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
