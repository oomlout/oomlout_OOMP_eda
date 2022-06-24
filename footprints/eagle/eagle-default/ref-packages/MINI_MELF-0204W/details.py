###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MINI_MELF-0204W")
newPart.addTag("oompName", "eagle-default/ref-packages/MINI_MELF-0204W")

newPart.addTag("description", """&lt;b&gt;CECC Size RC3715&lt;/b&gt; Wave Soldering&lt;p&gt;&#xD;
source Beyschlag""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MINI_MELF-0204W",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MINI_MELF-0204W')

OOMP.parts.append(newPart)