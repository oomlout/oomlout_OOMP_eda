###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SC79_INFINEON")
newPart.addTag("oompName", "eagle-default/ref-packages/SC79_INFINEON")

newPart.addTag("description", """&lt;b&gt;Diode Package&lt;/b&gt; Reflow soldering&lt;p&gt;&#xD;
INFINEON, www.infineon.com/cmc_upload/0/000/010/257/eh_db_5b.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SC79_INFINEON",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SC79_INFINEON')

OOMP.parts.append(newPart)