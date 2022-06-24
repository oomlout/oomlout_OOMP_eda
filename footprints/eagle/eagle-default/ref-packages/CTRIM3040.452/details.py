###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "CTRIM3040.452")
newPart.addTag("oompName", "eagle-default/ref-packages/CTRIM3040.452")

newPart.addTag("description", """&lt;b&gt;Trimm capacitor&lt;/b&gt; STELCO GmbH&lt;p&gt;&#xD;
 7 S-Triko 160 V DC for PCB mounting &lt;p&gt;&#xD;
 Adjustable from one side for automatic adjustment, vertical to PCB""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-CTRIM3040.452",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='CTRIM3040.452')

OOMP.parts.append(newPart)