###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SO-18W")
newPart.addTag("oompName", "eagle-default/ref-packages/SO-18W")

newPart.addTag("description", """&lt;B&gt;Small Outline Wide Plastic Gull Wing&lt;/B&gt;&lt;p&gt;&#xD;
300-mil body, package type SO""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SO-18W",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SO-18W')

OOMP.parts.append(newPart)