###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MAPBGA160")
newPart.addTag("oompName", "eagle-default/ref-packages/MAPBGA160")

newPart.addTag("description", """&lt;b&gt;Mold Array Process Ball Grid Array&lt;/b&gt; MAPBGA 160&lt;p&gt;&#xD;
CASE 1268-01""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MAPBGA160",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MAPBGA160')

OOMP.parts.append(newPart)