###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "SSIP-32")
newPart.addTag("oompName", "eagle-default/ref-packages/SSIP-32")

newPart.addTag("description", """&lt;b&gt; 32-pin SSIP&lt;/b&gt;&lt;p&gt;&#xD;
Source: http://www.tripath.com/audio.htm""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-SSIP-32",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='SSIP-32')

OOMP.parts.append(newPart)