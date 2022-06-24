###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "PQFP128L")
newPart.addTag("oompName", "eagle-default/ref-packages/PQFP128L")

newPart.addTag("description", """&lt;b&gt;PQFP-128L&lt;/b&gt;&lt;p&gt;&#xD;
ADVANCED DEMICONDUCTOR ENGENEERING. INC&lt;br&gt;&#xD;
Package Outline 14x20x2.72 mm / 3.9mm Footprint&lt;br&gt;&#xD;
Source PQFP-128.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-PQFP128L",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='PQFP128L')

OOMP.parts.append(newPart)