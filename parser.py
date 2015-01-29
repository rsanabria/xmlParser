
import xml.etree.ElementTree as ET

from sys import argv

script, filepath = argv

tree = ET.parse(filepath)

root = tree.getroot()

blogs = []

def escaparBlog(blog):
	blog_escapado = ""
	salta = False
	for letter in blog:
		if(salta == False):
			if(letter == "<"):
				salta = True
			else:
				blog_escapado +=letter
		else:
			if(letter ==">"):
				salta = False

	return blog_escapado
			
for document in root.iter('document'):
	print document.attrib
	blogs.append(document.text)


for indice in range(len(blogs)):
	blogs[indice] = escaparBlog(blogs[indice])


x=raw_input("Elige un blog: ")
print blogs[int(x)]


			




