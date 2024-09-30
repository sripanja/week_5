from lxml import etree  # Importing the lxml library's etree module for XML handling
from pathlib import Path  # Importing Path from pathlib to manage file paths

# Define the directory where the XML file will be saved
data_dir = Path.cwd() / 'data'

# Define the file path for the output XML file
sample_xml_output_file = data_dir / 'sample_5.xml'

# Create the root element of the XML tree, <patients>
root = etree.Element("patients")

# Create the first patient element with attributes and sub-elements
patient1 = etree.SubElement(root, "patient", attrib={"id": "001"})
first_name1 = etree.SubElement(patient1, "first_name")
first_name1.text = "John"
last_name1 = etree.SubElement(patient1, "last_name")
last_name1.text = "Doe"
age1 = etree.SubElement(patient1, "age")
age1.text = "45"
gender1 = etree.SubElement(patient1, "gender")
gender1.text = "Male"
diagnosis1 = etree.SubElement(patient1, "diagnosis")
diagnosis1.text = "Hypertension"

# Create medications sub-element for patient1
medications1 = etree.SubElement(patient1, "medications")
medication1_1 = etree.SubElement(medications1, "medication")
medication1_1.text = "Lisinopril"
medication1_2 = etree.SubElement(medications1, "medication")
medication1_2.text = "Amlodipine"

# Create the second patient element with attributes and sub-elements
patient2 = etree.SubElement(root, "patient", attrib={"id": "002"})
first_name2 = etree.SubElement(patient2, "first_name")
first_name2.text = "Jane"
last_name2 = etree.SubElement(patient2, "last_name")
last_name2.text = "Smith"
age2 = etree.SubElement(patient2, "age")
age2.text = "37"
gender2 = etree.SubElement(patient2, "gender")
gender2.text = "Female"
diagnosis2 = etree.SubElement(patient2, "diagnosis")
diagnosis2.text = "Diabetes"

# Create medications sub-element for patient2
medications2 = etree.SubElement(patient2, "medications")
medication2_1 = etree.SubElement(medications2, "medication")
medication2_1.text = "Metformin"
medication2_2 = etree.SubElement(medications2, "medication")
medication2_2.text = "Insulin"

# Create an ElementTree object from the root element
tree = etree.ElementTree(root)

# Open the file for writing in binary mode and write the XML content to it
# The 'pretty_print=True' option formats the output nicely with indentation
# 'xml_declaration=True' adds the XML declaration (e.g., <?xml version='1.0'?>)
# 'encoding="UTF-8"' ensures the file is encoded in UTF-8
with open(sample_xml_output_file, "wb") as file:
    file.write(etree.tostring(tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))
