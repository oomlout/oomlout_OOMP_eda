###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SMARTLED-TTW")
newPart.addTag("oompName", "eagle-default/ref-packages/SMARTLED-TTW")

newPart.addTag("description", """&lt;b&gt;SmartLED TTW&lt;/b&gt;&lt;p&gt;&#xD;
Recommended Solder Pad useable for SmartLEDTM and Chipled - Package 0603&lt;br&gt;&#xD;
Package able to withstand TTW-soldering heat&lt;br&gt;&#xD;
Package suitable for TTW-soldering&lt;br&gt;&#xD;
Source: http://www.osram.convergy.de/ ... LO_LS_LY L89K.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SMARTLED-TTW",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SMARTLED-TTW')

OOMP.parts.append(newPart)