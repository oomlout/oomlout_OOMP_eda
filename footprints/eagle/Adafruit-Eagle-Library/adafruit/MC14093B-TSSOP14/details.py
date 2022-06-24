###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "MC14093B-TSSOP14")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/MC14093B-TSSOP14")

newPart.addTag("description", """&lt;b&gt;plastic thin shrink small outline package; 14 leads; body width 4.4 mm &lt;/b&gt;&lt;p&gt;
SOT402-1&lt;br&gt;
Source: http://www.onsemi.com/pub_link/Collateral/MC14093B-D.PDF""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-MC14093B-TSSOP14",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='MC14093B-TSSOP14')

OOMP.parts.append(newPart)