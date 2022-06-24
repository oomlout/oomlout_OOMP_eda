###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "TQFP64-10X10")
newPart.addTag("oompName", "eagle-default/ref-packages/TQFP64-10X10")

newPart.addTag("description", """&lt;b&gt;Thin Quad Flat Pack&lt;/b&gt;&lt;p&gt;&#xD;
package type TQ""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-TQFP64-10X10",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='TQFP64-10X10')

OOMP.parts.append(newPart)