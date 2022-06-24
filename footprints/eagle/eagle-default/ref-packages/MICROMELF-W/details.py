###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MICROMELF-W")
newPart.addTag("oompName", "eagle-default/ref-packages/MICROMELF-W")

newPart.addTag("description", """&lt;b&gt;Micro Melf Diode Wave soldering&lt;/b&gt; VISHAY mcl4148.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MICROMELF-W",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MICROMELF-W')

OOMP.parts.append(newPart)