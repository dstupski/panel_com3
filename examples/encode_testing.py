class PanelCom:
    def __init__( self, userport='/dev/ttyS0' ):
        self.ser = serial.Serial(
            port=userport,               #number of device, numbering starts at
                                         #zero. if everything fails, the user
                                         #can specify _a device string, note
                                         #that this isn't portable anymore
                                         #if no port is specified an unconfigured
                                         #an closed serial port object is created
            baudrate=921600,             #baudrate
            bytesize=serial.EIGHTBITS,   #number of databits
            parity=serial.PARITY_NONE,   #enable parity checking
            stopbits=serial.STOPBITS_ONE,#number of stopbits
            timeout=None,                #set a timeout value, None for waiting forever
            xonxoff=0,                   #enable software flow control
            rtscts=0,                    #enable RTS/CTS flow control
        )

    #################################################################################
    def SetPatternID(self,patternid):
        if type(patternid) != int: raise TypeError
        if patternid < 0: raise ValueError
        self.send(chr(0x02) + chr(0x03) + chr(patternid))
