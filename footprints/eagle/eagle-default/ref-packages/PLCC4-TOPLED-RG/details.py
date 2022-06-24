###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "PLCC4-TOPLED-RG")
newPart.addTag("oompName", "eagle-default/ref-packages/PLCC4-TOPLED-RG")

newPart.addTag("description", """&lt;b&gt;Multi TOPLED RG&lt;/b&gt;&lt;p&gt;&#xD;
Source: http://www.osram.convergy.de ... LSG T770.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-PLCC4-TOPLED-RG",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='PLCC4-TOPLED-RG')

OOMP.parts.append(newPart)