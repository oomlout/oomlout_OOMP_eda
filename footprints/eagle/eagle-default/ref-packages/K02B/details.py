###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "K02B")
newPart.addTag("oompName", "eagle-default/ref-packages/K02B")

newPart.addTag("description", """&lt;b&gt;TO-3&lt;/b&gt;&lt;p&gt;&#xD;
National Semiconductor K02B""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-K02B",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='K02B')

OOMP.parts.append(newPart)