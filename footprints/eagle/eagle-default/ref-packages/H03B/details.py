###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "H03B")
newPart.addTag("oompName", "eagle-default/ref-packages/H03B")

newPart.addTag("description", """&lt;b&gt;Metal Can Package&lt;/b&gt;&lt;p&gt;&#xD;
National Semiconductor H03B""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-H03B",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='H03B')

OOMP.parts.append(newPart)