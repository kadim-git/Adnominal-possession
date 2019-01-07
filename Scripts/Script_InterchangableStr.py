#For each language, this script extracts element InterchangableStr and shows its attributes: Word_changing, Factors affecting, Strategies
import xml.etree.ElementTree as ET
tree = ET.parse('Database_merged_2017_07.xml')
root = tree.getroot()
print('Lang N, LangID, Interchangable Str N, Word_changing,  Factors affecting, Strategies')
for langIter in range(len(root)):
    exampleStrats=root[langIter].findall('./GeneralInfo/InterchangeaStrategies/ExampleStr')
    if exampleStrats:
        for exampleIter in range(len(exampleStrats)):
            print(langIter, end=', ')
            print(root[langIter].find('./GeneralInfo/LangID').text, end=', ')
            print(exampleIter+1, end=',')
  
            print(exampleStrats[exampleIter].get('WordChanging'),',', exampleStrats[exampleIter].get('FactorsAffecting'),',', exampleStrats[exampleIter].get('Strategies'))
    else :
        print(langIter, end=', ')
        print(root[langIter].find('./GeneralInfo/LangID').text, end=', ')

        print(', , , ')
    
   # print(root[langIter].find('./GeneralInfo/LangID/InterchangeaStrategies/ExampleStr')[0].attrib)
    
#exit()
