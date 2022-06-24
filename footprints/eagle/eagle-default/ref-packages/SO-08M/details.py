###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SO-08M")
newPart.addTag("oompName", "eagle-default/ref-packages/SO-08M")

newPart.addTag("description", """&lt;B&gt;Small Outline Medium Plastic Gull Wing&lt;/B&gt;&lt;p&gt;&#xD;
207-mil body, package type SM""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SO-08M",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SO-08M')

OOMP.parts.append(newPart)