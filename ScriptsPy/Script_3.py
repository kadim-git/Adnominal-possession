#ТThis scrip gives the content of GramDefLabel only for pronominal possession
import xml.etree.ElementTree as ET
#tree = ET.parse('Database_merged_2017_07.xml')
tree = ET.parse('Database_merged.xml')
root = tree.getroot()
print('LangID, StrategyID, SharedWithNominal')
nodes=list(['Possession/PronominalPossession/*','Possession/PronominalPossession/StrategyPronom/StrategyNotFound','Possession/PronominalPossession/StrategyPronomNonCanonical'])
for lang in root:
    #tempFound=lang.findall('./Possession/PronominalPossession/StrategyPronom')
    tempFound=lang.findall('./Possession/PronominalPossession/*')
 #   print(len(tempFound))
    for strat in tempFound:
        tempMorphemePron=strat.find('./Morphology/MorphemePron/[@GramDefLabel]')
        if tempMorphemePron:
            print(lang.find('GeneralInfo/LangID').text, end=' ')
     #       print(',',strat.attrib,end=' ')
            print(',',strat.get('StrategyID'),end=' ')
     #       print(',',tempMorphemePron.attrib)
            print(',',tempMorphemePron.get('GramDefLabel'))
print('')
    
