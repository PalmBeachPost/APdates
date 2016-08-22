import os
import glob

class language(object):
	def __init__(self):
		self.filename = ""
		self.name = ""
		self.markdownname = ""
		self.contents = ""

masterlist = []
intro = "# AP date formatting in a bunch of languages\r\n\r\n"
intro = intro + "Find thee text file for the language you want, or scroll down.\r\n\r\n"
intro = intro + "Pull requests for fixes or especially new languages (we're looking at you, Rubyists and R-whatevers!) are most welcomed.\r\n\r\n"
intro = intro + "#### Contributors\r\n\r\n"
intro = intro + "Chris Alcantara (@chrisalcantara), Matthew Dudak (@mjdudak), Ted Han (@knowtheory), Mike Stucka (@stucka)\r\n\r\n"
intro = intro + "\r\n\r\n"

sourcefiles = glob.glob("APdate*.txt")
for sourcefile in sourcefiles:
    newone = language()
    newone.filename = sourcefile
    newone.name = sourcefile.replace("APdate", "").replace(".txt", "")
    newone.markdownname = newone.name.lower()
    with open(sourcefile, 'r') as handle:
        newone.contents = handle.read().replace("\r\n", "\r\n\r\n")
    masterlist.append(newone)
    
with open("README.md", "w") as destination:
    destination.write(intro)
    for language_object in masterlist:
        destination.write("\r\n\r\n##### " + language_object.name + "\r\n\r\n") 
        destination.write("```" + language_object.markdownname + "\r\n")
        destination.write(language_object.contents)
        destination.write("```\r\n\r\n")
    destination.write("\r\n")
    
      
        