
import os
import glob


class TestData(object):

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))

    def __init__(self, sensor):
        """ Initialize testdata for a sensor """
        self.sensor = sensor
        # load bandmap

    @classmethod
    def list_sensors(cls):
        """ List all sensors available """
        return [f for f in os.listdir(cls.path) if os.path.isdir(f)]

    def spath(self):
        return os.path.join(self.path, self.sensor)

    def list_scenes(self):
        """ List scenes for this sensor """
        return [f for f in os.listdir(self.spath()) if os.path.isdir(f)]

    def get_filenames(self, scene):
        """ Get dictionary of {filename: [bandnames]} for this sensor and scene """
        spath = os.path.join(self.spath(), scene)
        fnames = glob.glob(os.path.join(spath), '*')
        # make dictionary
