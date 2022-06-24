###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "eagle-default")
newPart.addTag("oompDesc", "ref-packages")
newPart.addTag("oompIndex", "PANASONIC_B")
newPart.addTag("oompName", "eagle-default/ref-packages/PANASONIC_B")

newPart.addTag("description", """&lt;b&gt;Panasonic Aluminium Electrolytic Capacitor VS-Serie Package B&lt;/b&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-eagle-default-ref-packages-PANASONIC_B",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='eagle-default',oompDesc='ref-packages',oompIndex='PANASONIC_B')

OOMP.parts.append(newPart)