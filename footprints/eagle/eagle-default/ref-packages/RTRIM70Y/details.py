###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "RTRIM70Y")
newPart.addTag("oompName", "eagle-default/ref-packages/RTRIM70Y")

newPart.addTag("description", """&lt;b&gt;Trimm resistor&lt;/b&gt; Spectrol&lt;p&gt;&#xD;
waschfest MIL-R-22097""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-RTRIM70Y",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='RTRIM70Y')

OOMP.parts.append(newPart)