###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MSOP8")
newPart.addTag("oompName", "eagle-default/ref-packages/MSOP8")

newPart.addTag("description", """&lt;b&gt;Micro Small Outline Package&lt;/b&gt; Grid .65mm&lt;p&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MSOP8",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MSOP8')

OOMP.parts.append(newPart)