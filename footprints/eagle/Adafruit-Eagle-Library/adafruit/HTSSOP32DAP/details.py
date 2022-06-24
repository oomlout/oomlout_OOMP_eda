###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "HTSSOP32DAP")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/HTSSOP32DAP")

newPart.addTag("description", """&lt;b&gt;PowerPAD(TM) PLASTIC SMALL-OUTLINE PACKAGE&lt;/b&gt; DAP (R-PDSO-G**)&lt;p&gt;
Source: http://focus.ti.com/lit/ml/mpds029b/mpds029b.pdf / slma002.pdf""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-HTSSOP32DAP",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='HTSSOP32DAP')

OOMP.parts.append(newPart)