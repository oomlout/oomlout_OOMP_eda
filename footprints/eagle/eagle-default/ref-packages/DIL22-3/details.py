###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "DIL22-3")
newPart.addTag("oompName", "eagle-default/ref-packages/DIL22-3")

newPart.addTag("description", """&lt;b&gt;Dual In Line Package&lt;/b&gt; 0.3 inch""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-DIL22-3",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='DIL22-3')

OOMP.parts.append(newPart)