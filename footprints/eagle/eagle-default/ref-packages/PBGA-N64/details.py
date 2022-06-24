###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "PBGA-N64")
newPart.addTag("oompName", "eagle-default/ref-packages/PBGA-N64")

newPart.addTag("description", """&lt;b&gt;GXG (S-PBGA-N64&lt;/b&gt;&lt;p&gt;&#xD;
Source: http://focus.ti.com/lit/ds/symlink/ddc232.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-PBGA-N64",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='PBGA-N64')

OOMP.parts.append(newPart)