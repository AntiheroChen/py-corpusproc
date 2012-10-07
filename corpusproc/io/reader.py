from corpusproc.core import Instance

class Reader(object):
    """ construct the reader with file handle. """
    def __init__(self, fp):
        self.fp = fp;

    """ to be overwrited. """
    def get(self):
        pass

    def seek(self, position):
        self.fp.seek(0, 0)

class SegmentReader(Reader):
    """ """
    def get(self):
        line = self.fp.readline()

        if line == "":
            return None

        line = line.strip()

        inst = Instance()
        inst.raw   = line
        inst.forms = line.split()

        return inst

class PostagReader(Reader):
    """ """
    def get(self):
        line = self.fp.readline()

        if line == "":
            return None

        line = line.strip()

        inst = Instance()
        inst.raw     = line
        inst.forms   = [word.rsplit("_")[0] for word in line.split()]
        inst.postags = [word.rsplit("_")[1] for word in line.split()]

        return inst

class ConllReader(Reader):
    """ """
    def get(self):
        return None

if __name__=="__main__":
    reader = SegmentReader(open("./data/segment.sample", "r"))

    while True:
        inst = reader.get()

        if inst is None:
            break

        print inst