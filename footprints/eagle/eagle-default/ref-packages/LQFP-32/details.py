###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "LQFP-32")
newPart.addTag("oompName", "eagle-default/ref-packages/LQFP-32")

newPart.addTag("description", """&lt;b&gt;Quad FLat Pack&lt;/b&gt;&lt;p&gt;&#xD;
RFMicro Device TQFP / LQFP-32 see IPC-SQR.LBR SQFP 5x5-32""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-LQFP-32",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='LQFP-32')

OOMP.parts.append(newPart)