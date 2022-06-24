###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TOP3S-2")
newPart.addTag("oompName", "eagle-default/ref-packages/TOP3S-2")

newPart.addTag("description", """&lt;b&gt;TOP 3&lt;/b&gt; vertical (Cathode; Anode; Gate)""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TOP3S-2",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TOP3S-2')

OOMP.parts.append(newPart)