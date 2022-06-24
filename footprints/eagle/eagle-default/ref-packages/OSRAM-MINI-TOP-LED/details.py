###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "OSRAM-MINI-TOP-LED")
newPart.addTag("oompName", "eagle-default/ref-packages/OSRAM-MINI-TOP-LED")

newPart.addTag("description", """&lt;b&gt;BLUE LINETM Hyper Mini TOPLED Hyper-Bright LED&lt;/b&gt;&lt;p&gt;&#xD;
Source: http://www.osram.convergy.de/ ... LB M676.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-OSRAM-MINI-TOP-LED",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='OSRAM-MINI-TOP-LED')

OOMP.parts.append(newPart)