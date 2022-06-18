###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Xilinx_CLG225")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Xilinx_CLG225")

newPart.addTag("kicadDesc", "Zynq-7000 BGA, 15x15 grid, 13x13mm package, 0.8mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug865-Zynq-7000-Pkg-Pinout.pdf#page=77, NSMD pad definition Appendix A")
newPart.addTag("kicadTags", "BGA 225 0.8 CLG225")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_CLG225.wrl")

OOMP.parts.append(newPart)