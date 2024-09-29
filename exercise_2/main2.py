from lxml import etree  # Import the etree module from the lxml library for XML parsing.
from pathlib import Path  # Import Path from pathlib to handle file paths.

# Define the directory containing the XML file by getting the current working directory and appending 'data' to it.
data_dir = Path.cwd() / 'data'

# Define the path to the XML file by appending the file name to the data directory.
sample_xml_file = data_dir / 'sample_3.xml'

# Parse the XML file and create an ElementTree object representing the XML structure.
tree = etree.parse(sample_xml_file)

# Get the root element of the XML tree (the top-level element).
root = tree.getroot()

# Print the tag (name) of the root element.
print(f"Root Element: {root.tag}")

# Print the entire XML structure
for element in root.iter():
    print(f"Tag: {element.tag}, Text: {element.text}")
