A viewer (file  viewer_2.html) was created to give access to the most important information from database Adnominal Possession (later DB) in convenient and simple way. This viewer is  standard HTML5 file. It uses JavaScript and XSLT ver.1 to transform information from DB written in XML into HTML. 

For the viewer to function the following files should be present in the same directory: LangDB2HTML.xsl, LangList.xsl, lang_XMLasText.html and the viewer itself viewer_2.html. File with DB should have name Database_merged.xml and be in subdirectory with name DB.
The file structure is the following:
	viewer_2.html
	lang_XMLasText.html
	LangDB2HTML.xsl
	LangList.xsl
	DB/Database_merged.xml

If this files are stored on web-server, then most of the modern Web browsers can be used to open viewer_2.html. It was tested with Google Chrome, Mozilla Firefox, and Microsoft Edge.
To open viewer_2.html from local file storage system (without using web-server) use  Mozilla Firefox.
At present Google Chrome (Version 71) does not work. Cross-Origin XMLHttp Requests are blocked for the files from local storage by Chrome because of Google’s the same origin policy.
