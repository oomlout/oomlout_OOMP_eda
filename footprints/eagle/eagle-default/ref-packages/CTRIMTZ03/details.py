###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "CTRIMTZ03")
newPart.addTag("oompName", "eagle-default/ref-packages/CTRIMTZ03")

newPart.addTag("description", """&lt;b&gt;Trimm capacitor&lt;/b&gt; muRata""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-CTRIMTZ03",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='CTRIMTZ03')

OOMP.parts.append(newPart)