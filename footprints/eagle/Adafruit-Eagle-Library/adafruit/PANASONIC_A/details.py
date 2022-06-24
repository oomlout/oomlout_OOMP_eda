###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "PANASONIC_A")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/PANASONIC_A")

newPart.addTag("description", """&lt;b&gt;Panasonic Aluminium Electrolytic Capacitor VS-Serie Package A&lt;/b&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-PANASONIC_A",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='PANASONIC_A')

OOMP.parts.append(newPart)