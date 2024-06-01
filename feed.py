import yaml
import xml.etree.ElementTree as xml_tree

'''
We start by importing the necessary libraries. 
The yaml library helps us read YAML files, and xml.etree.ElementTree (abbreviated as xml_tree) 
is used to create and manipulate XML documents.
'''

# Open the YAML file and load its contents into a dictionary
with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Create the root RSS element with necessary namespaces for iTunes and content
rss_element = xml_tree.Element('rss', {
    'version': '2.0',
    'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
})

# Create the channel element which will hold the metadata for the podcast
channel_element = xml_tree.SubElement(rss_element, 'channel')

# Store the link prefix from the YAML data to be used for constructing full URLs
link_prefix = yaml_data['link']

# Add basic channel elements to the RSS feed using data from the YAML file
# Title of the podcast
xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']

# Subtitle of the podcast
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']

# Author of the podcast
xml_tree.SubElement(
    channel_element, 'itunes:author').text = yaml_data['author']

# Description of the podcast
xml_tree.SubElement(
    channel_element, 'description').text = yaml_data['description']

# Image associated with the podcast
xml_tree.SubElement(channel_element, 'itunes:image', {
    'href': link_prefix + yaml_data['image']
})

# Language of the podcast
xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']

# Link to the podcast website
xml_tree.SubElement(channel_element, 'link').text = link_prefix

# Category of the podcast
xml_tree.SubElement(channel_element, 'itunes:category', {
    'text': yaml_data['category']
})

# Loop through each item in the YAML data to add individual podcast episodes
for item in yaml_data['item']:
    # Create an item element for each episode
    item_element = xml_tree.SubElement(channel_element, 'item')

    # Title of the episode
    xml_tree.SubElement(item_element, 'title').text = item['title']

    # Author of the episode (same as the podcast author)
    xml_tree.SubElement(
        item_element, 'itunes:author').text = yaml_data['author']

    # Description of the episode
    xml_tree.SubElement(item_element, 'description').text = item['description']

    # Duration of the episode
    xml_tree.SubElement(
        item_element, 'itunes:duration').text = item['duration']

    # Publication date of the episode
    xml_tree.SubElement(item_element, 'pubDate').text = item['published']

    # Enclosure element containing the URL and metadata of the audio file
    enclosure = xml_tree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'],
        'type': 'audio/mpeg',
        # Convert length to string as it should be in string format
        'length': str(item['length'])
    })

# Write the constructed XML tree to a file named 'podcast.xml'
output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
