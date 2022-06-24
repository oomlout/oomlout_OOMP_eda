###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "eagle")
newPart.addTag("oompColor", "Adafruit-Eagle-Library")
newPart.addTag("oompDesc", "adafruit")
newPart.addTag("oompIndex", "INDUCTOR_5X5MM_TDK_VLC5045")
newPart.addTag("oompName", "Adafruit-Eagle-Library/adafruit/INDUCTOR_5X5MM_TDK_VLC5045")

newPart.addTag("description", """&lt;b&gt;Source: http://www.tdk.co.jp/tefe02/e531_vlc5045.pdf&lt;/b&gt;""")

newPart = OOMPtags.addTags(newPart,"FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-INDUCTOR_5X5MM_TDK_VLC5045",hexID='',oompType='FOOTPRINT',oompSize='eagle',oompColor='Adafruit-Eagle-Library',oompDesc='adafruit',oompIndex='INDUCTOR_5X5MM_TDK_VLC5045')

OOMP.parts.append(newPart)