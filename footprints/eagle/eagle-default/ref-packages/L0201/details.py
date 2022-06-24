###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "L0201")
newPart.addTag("oompName", "eagle-default/ref-packages/L0201")

newPart.addTag("description", """&lt;b&gt;NIS02 Chip Inductor&lt;/b&gt;&lt;p&gt;&#xD;
Source: http://www.niccomp.com/Catalog/nis.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-L0201",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='L0201')

OOMP.parts.append(newPart)