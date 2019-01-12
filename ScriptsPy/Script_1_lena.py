#modified by Lena. This script extracts the number of strategies for every language: Pronominal (including non canonical strategies), Nominal  (including  non canonical strategies)
import xml.etree.ElementTree as ET
tree = ET.parse('Database_merged_2017_07.xml')
root = tree.getroot()
print('LangID, PronominalPossession, StrategyNotFound, StrategyPronomNonCanonical, NominalPossession, StrategyNotFound, StrategyNomNotCanonical')
nodes=list(['Possession/PronominalPossession/*','Possession/PronominalPossession/StrategyNotFound','Possession/PronominalPossession/StrategyPronomNonCanonical'])
nodes=nodes+['Possession/NominalPossession/*','Possession/NominalPossession/StrategyNotFound','Possession/NominalPossession/StrategyNomNonCanonical']
for lang in root:
    print(lang.find('GeneralInfo/LangID').text, end=' ')
    for node in nodes:
        tempFound=lang.findall(node)
        print(',',len(tempFound) if tempFound else 0, end=' ')    
    print('')
    
