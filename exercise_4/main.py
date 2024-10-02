from lxml import etree
from pathlib import Path

# Define the paths to the XML and DTD files
data_dir = Path.cwd() / 'data'
xml_file = data_dir / 'library_2.xml'
dtd_file = data_dir / 'hospital.dtd'

# Parse the DTD file
with open(dtd_file, 'rb') as dtd_file_obj:
    dtd = etree.DTD(dtd_file_obj)

# Parse the XML file
tree = etree.parse(str(xml_file))

# Validate the XML against the DTD
if dtd.validate(tree):
    print("The XML is valid according to the DTD.")
else:
    print("The XML is invalid according to the DTD.")
    # Print detailed errors
    print(dtd.error_log.filter_from_errors())