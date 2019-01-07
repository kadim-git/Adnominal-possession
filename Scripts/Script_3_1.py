#ТThis scrip gives the content of GramDefLabel only for pronominal possession
import xml.etree.ElementTree as ET
#tree = ET.parse('Database_merged_2017_07.xml')
tree = ET.parse('Database_merged.xml')
root = tree.getroot()
print('N, LangID, StrategyID/Type, GramDefLabel')
foundCounter=0
#nodes=list(['Possession/PronominalPossession/*','Possession/PronominalPossession/StrategyPronom/StrategyNotFound','Possession/PronominalPossession/StrategyPronomNonCanonical'])
for lang in root[:]:
    #tempFound=lang.findall('./Possession/PronominalPossession/StrategyPronom')
    #tempFound=lang.findall('./Possession/PronominalPossession/*')
    tempFound=lang.findall('./Possession/*/*')
 #   print(len(tempFound))
    for strat in tempFound:
        tempMorphemePron=strat.findall('./Morphology/*/[@GramDefLabel]')
        #if tempMorphemePron:
        for tempMorpeme in strat.findall('./Morphology/*/[@GramDefLabel]'):
            foundCounter+=1
            print(foundCounter,lang.find('GeneralInfo/LangID').text, end=' ')
     #       print(',',strat.attrib,end=' ')
            print(',','ID='+strat.get('StrategyID')+' '+strat.tag,end=' ')
     #       print(',',tempMorphemePron.attrib)
            print(',',tempMorpeme.get('GramDefLabel'))
print('')
    
