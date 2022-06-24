###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MINI_MELF-0102W")
newPart.addTag("oompName", "eagle-default/ref-packages/MINI_MELF-0102W")

newPart.addTag("description", """&lt;b&gt;CECC Size RC2211&lt;/b&gt; Wave Soldering&lt;p&gt;&#xD;
source Beyschlag""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MINI_MELF-0102W",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MINI_MELF-0102W')

OOMP.parts.append(newPart)