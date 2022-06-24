###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "DPAK")
newPart.addTag("oompName", "eagle-default/ref-packages/DPAK")

newPart.addTag("description", """&lt;b&gt;DPAK&lt;/b&gt; CASE 369-07&lt;br&gt;&#xD;
Source MOTOROLA / ON Semiconductor mjd32-d.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-DPAK",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='DPAK')

OOMP.parts.append(newPart)