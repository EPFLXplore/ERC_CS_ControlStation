import numpy as np

class Science:
    '''
        Monitoring Science Data
    '''

    def __init__(self):
        # humidity of the specific tube
        self.__tubeHum = -1
        
        # parameters (11 elements):
        #   - disc position
        #   - whether tubes 0 to 2 are closed
        #   - whether tubes 0 to 2 are empty
        #   - whether trap is closed
        #   - mass of each tube
        self.__params = []

        # smthg to do with the picture analysis of images from the science bay
        # unfortunately it wasn't implemented this year
        self.__volumes = [0,0,0]
        self.__colors = [0,0,0]
        self.__particleSizes = [0,0,0]
        self.__densities = [0,0,0]

        self.__images = []

        # array of infos coming from the SC (in the form of Strings)
        self.__info = []

        # variable to know what operation we'd like to execute on which tube: [op, tube]
        # operations: 10 = sampling, 20 = rotation to camera, 30 = mass measurement
        self.__op_tube = np.zeros(2)
        # command we'd like the science bay to execute (in the case of a tube-specific operation: op + tube)
        self.__cmd = -1

    #--------SC Mass--------

    def setSCMass(self, mass):
        self.__masses[self.__op_tube[1]] = mass
    
    def getSCMass(self, idx):
        if(idx < 0 or 2 < idx): raise ValueError("impossible tube number chosen (can be either 0, 1 or 2)")
        return self.__sc_mass[idx]

    def getMasses(self):
        return self.__masses

    #--------Tube Humidity--------

    def setTubeHum(self, val):
        self.__tubeHum = val

    def getTubeHum(self):
        return self.__tubeHum

    #--------SC Operation--------

    def setOperation(self, op):
        self.__op_tube[0] = op
        self.setTubeCmd()

    def getOperation(self):
        return self.__op_tube[0]

    #--------Tube--------

    def selectTube(self, t):
        self.__op_tube[1] = t
        self.setTubeCmd()

    def getSelectedTube(self):
        return self.__op_tube[1]

    #--------Specific Tube Command--------

    def setTubeCmd(self):
        arr = self.__op_tube
        self.setCmd(arr[0] + arr[1])
    
    #--------Command--------

    def setCmd(self, cmd):
        self.__cmd = cmd

    def getCmd(self):
        return self.__cmd

    #--------Opened tubes--------

    def setTubeState(self, idx, val):
        self.__tubes_closed[idx] = bool(val)

    def getTubesState(self):
        return self.__tubes_closed

    #--------Densities--------
    def setDensity(self, idx, val):
        self.__densities[idx] = val

    def getDensities(self):
        return self.__densities

    #--------Volumes--------

    def setVolume(self, idx, val):
        self.__volumes[idx] = val

    def getVolumes(self):
        return self.__volumes
        
    #--------Trap--------

    def setTrapState(self, val):
        self.__trap_closed= bool(val)

    def getTrapState(self):
        return self.__trap_closed

    #--------Particle Size--------

    def setParticleSize(self, idx, val):
        self.__particleSizes[idx] = val

    def getParticleSizes(self):
        return self.__particleSizes

    #--------Filled--------

    def setTubeEmpty(self, idx, val):
        self.__empty[idx] = val

    def areEmpty(self):
        return self.__empty

    #--------Colors--------

    def setColor(self, idx, val):
        self.__colors[idx] = val

    def getColors(self):
        return self.__colors

    #--------INFO--------

    def addInfo(self, txt):
        self.__info.append(txt)

    def getInfos(self):
        return self.__info

    #--------STATE--------
    def setState(self, txt):
        self.__state = txt

    def getState(self):
        return self.__state

    #--------PARAMS#--------

    def setParams(self, arr): 
        self.__params = arr
    def getParams(self): 
        return self.__params

    #--------DESERIALIZATION--------
    def deSerializeState(self, save_list):
        '''
        Undo the serialization of serializeState and save the variables.
        Input: save_list (list of int) list to be deserialized
        Output: None
        '''

        #cast to ints
        #save_list = map(int,save_list)

        #desrializing
        #self.disc_position = save_list[0]

        '''self.__tubes_closed = map(bool,save_list[1:4])
        self.__empty = map(bool,save_list[4:7])
        self.__trap_closed = bool(save_list[7])
        self.__masses = save_list[8:] ''' # TODO il me semble que ça renvoit 4 nombres et pas 3
        self.__tubes_closed = np.array(save_list[1:4]).astype(bool).tolist()
        self.__empty = np.array(save_list[4:7]).astype(bool).tolist()
        self.__trap_closed = np.array(save_list[7]).astype(bool).tolist()
        self.__masses = save_list[8:]


    #--------IMAGE--------
    def addImage(self, im):
        self.__images.append(im)

    def getImages(self):
        return self.__images