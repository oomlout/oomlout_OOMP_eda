###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "H08C")
newPart.addTag("oompName", "eagle-default/ref-packages/H08C")

newPart.addTag("description", """&lt;b&gt;TO-99&lt;/b&gt;&lt;p&gt;&#xD;
National Semiconductor H08C&lt;br&gt;&#xD;
Mototola 601-04""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-H08C",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='H08C')

OOMP.parts.append(newPart)