import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def extract_external_files(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    external_files = []

    # Find all script tags with external sources
    script_tags = soup.find_all('script', src=True)
    for script_tag in script_tags:
        external_files.append(script_tag['src'])

    # Find all link tags with external stylesheets
    link_tags = soup.find_all('link', rel='stylesheet', href=True)
    for link_tag in link_tags:
        external_files.append(link_tag['href'])

    # Find all img tags with external sources
    img_tags = soup.find_all('img', src=True)
    for img_tag in img_tags:    
        external_files.append(img_tag['src'])

    # Create XML file
    root = ET.Element("root")
    url_element = ET.SubElement(root, "url")
    url_element.text = url

    for file in external_files:
        file_element = ET.SubElement(root, "file")
        file_element.text = file

    tree = ET.ElementTree(root)
    tree.write(filename)

    return external_files

url = input("Enter a website to extract the URL's from: ")
filename = input("Enter the name for the output XML file: ")

if not filename.endswith('.xml'):
    filename += '.xml'

external_files = extract_external_files(url)