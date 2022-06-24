###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "OSRAM-MINI-TOP-LED")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/OSRAM-MINI-TOP-LED")

newPart.addTag("description", """&lt;b&gt;BLUE LINETM Hyper Mini TOPLED Hyper-Bright LED&lt;/b&gt;&lt;p&gt;
Source: http://www.osram.convergy.de/ ... LB M676.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-OSRAM-MINI-TOP-LED",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='OSRAM-MINI-TOP-LED')

OOMP.parts.append(newPart)