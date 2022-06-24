###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "MICROMELF-R")
newPart.addTag("oompName", "eagle-default/ref-packages/MICROMELF-R")

newPart.addTag("description", """&lt;b&gt;Micro Melf Diode Reflow soldering&lt;/b&gt; VISHAY mcl4148.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-MICROMELF-R",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='MICROMELF-R')

OOMP.parts.append(newPart)