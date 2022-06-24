###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "HA04E")
newPart.addTag("oompName", "eagle-default/ref-packages/HA04E")

newPart.addTag("description", """&lt;b&gt;Metal Can Package&lt;/b&gt;&lt;p&gt;&#xD;
National Semiconductor HA04E""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-HA04E",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='HA04E')

OOMP.parts.append(newPart)