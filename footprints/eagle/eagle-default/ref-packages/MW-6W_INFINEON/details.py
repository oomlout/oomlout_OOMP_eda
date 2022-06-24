###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MW-6W_INFINEON")
newPart.addTag("oompName", "eagle-default/ref-packages/MW-6W_INFINEON")

newPart.addTag("description", """&lt;b&gt;MW; 6 leads&lt;/b&gt; Wafe soldering&lt;p&gt;&#xD;
INFINEON, www.infineon.com""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MW-6W_INFINEON",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MW-6W_INFINEON')

OOMP.parts.append(newPart)