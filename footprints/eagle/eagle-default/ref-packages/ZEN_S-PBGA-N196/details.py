###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "ZEN_S-PBGA-N196")
newPart.addTag("oompName", "eagle-default/ref-packages/ZEN_S-PBGA-N196")

newPart.addTag("description", """&lt;b&gt;ZEN (S-PBGA-N196)&lt;/b&gt;&lt;p&gt;&#xD;
Source: http://focus.ti.com/lit/ml/mpbg838/mpbg838.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-ZEN_S-PBGA-N196",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='ZEN_S-PBGA-N196')

OOMP.parts.append(newPart)