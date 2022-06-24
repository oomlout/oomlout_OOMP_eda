###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "CTRIMTZBX4")
newPart.addTag("oompName", "eagle-default/ref-packages/CTRIMTZBX4")

newPart.addTag("description", """&lt;b&gt;Trimm capacitor&lt;/b&gt; muRata""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-CTRIMTZBX4",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='CTRIMTZBX4')

OOMP.parts.append(newPart)