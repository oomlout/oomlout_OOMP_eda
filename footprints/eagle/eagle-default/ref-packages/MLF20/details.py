###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MLF20")
newPart.addTag("oompName", "eagle-default/ref-packages/MLF20")

newPart.addTag("description", """&lt;b&gt;HP-VFQFP-N20&lt;/b&gt; Micro Lead Frame package (MLF)""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MLF20",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MLF20')

OOMP.parts.append(newPart)