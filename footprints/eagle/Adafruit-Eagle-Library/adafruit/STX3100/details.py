###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "STX3100")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/STX3100")

newPart.addTag("description", """&lt;b&gt;MIC/HEADPHONE JACK&lt;/b&gt;&lt;p&gt;
KS-S stereo microphone/headphone jack&lt;p&gt;
 PG203JN (Schukat)""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-STX3100",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='STX3100')

OOMP.parts.append(newPart)