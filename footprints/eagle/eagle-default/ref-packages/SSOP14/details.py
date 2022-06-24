###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SSOP14")
newPart.addTag("oompName", "eagle-default/ref-packages/SSOP14")

newPart.addTag("description", """&lt;b&gt;Shrink Small Outline Package&lt;/b&gt;&lt;p&gt;&#xD;
package type SS""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SSOP14",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SSOP14')

OOMP.parts.append(newPart)