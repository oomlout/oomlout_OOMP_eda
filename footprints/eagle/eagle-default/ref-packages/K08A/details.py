###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "K08A")
newPart.addTag("oompName", "eagle-default/ref-packages/K08A")

newPart.addTag("description", """&lt;b&gt;TO-3&lt;/b&gt;&lt;p&gt;&#xD;
National Semiconductor K08A""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-K08A",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='K08A')

OOMP.parts.append(newPart)