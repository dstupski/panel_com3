# Example using panel_com
from panel_com.panel_com import PanelCom
import time
#import panel_com as pc
print("i go this far")
sleep_t = 15.0
com_port_num = 0
pattern_id = 3
gain_x, offset_x = 0, 0
gain_y, offset_y = 0, 0

print('testing PanelCom')
ctlr = PanelCom(userport='/dev/ttyUSB0')

ctlr.SetPatternID(pattern_id)
ctlr.SetGainOffset(gain_x, offset_x, gain_y, offset_y)
for i in range(96):
    ctlr.SetPositions(i, 0)
    time.sleep(.1)



#ctlr.Stop()
#ctlr.AllOff()

print('done')
