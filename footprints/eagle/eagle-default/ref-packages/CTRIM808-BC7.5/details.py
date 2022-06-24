###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "CTRIM808-BC7.5")
newPart.addTag("oompName", "eagle-default/ref-packages/CTRIM808-BC7.5")

newPart.addTag("description", """&lt;b&gt;Trimm capacitor &lt;/b&gt; BC-Components""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-CTRIM808-BC7.5",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='CTRIM808-BC7.5')

OOMP.parts.append(newPart)