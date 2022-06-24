###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MELF-MLL41")
newPart.addTag("oompName", "eagle-default/ref-packages/MELF-MLL41")

newPart.addTag("description", """&lt;b&gt;DIODE&lt;/b&gt;&lt;p&gt;&#xD;
metal electrode face (MELF)""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MELF-MLL41",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MELF-MLL41')

OOMP.parts.append(newPart)