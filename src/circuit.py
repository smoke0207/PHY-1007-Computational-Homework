from typing import List

from src.wire import Wire


class Circuit:

    def __init__(self, wires: List[Wire]):
        self._wires = wires

    @property
    def wires(self):
        WIRES_A = [
        Wire(start=(54, 35), stop=(29, 35), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(29, 35), stop=(29, 86), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(29, 86), stop=(54, 86), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(54, 86), stop=(80, 86), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(80, 86), stop=(80, 35), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(80, 35), stop=(54, 35), current=Current(x=-1, y=0), voltage=-4.5),
    ]
#                                 Circuit B
    WIRES_B =[
        Wire(start=(45, 50), stop=(44, 50), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(44, 50), stop=(44, 101), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(44, 101), stop=(94, 101), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(94, 101), stop=(95, 101), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(95, 101), stop=(95, 50), current=Current(x=0, y=1), voltage=-4.5),
        Wire(start=(95, 50), stop=(94, 50), current=Current(x=-1, y=0), voltage=-4.5),    
    ]
#                                 Circuit c
    WIRES_C = [
        Wire(start=(120, 20), stop=(20, 20), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(20, 20), stop=(20, 71), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(20, 71), stop=(120, 71), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(120, 71), stop=(121, 71), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(121, 71), stop=(121, 20), current=Current(x=0, y=1), voltage=-4.5),
        Wire(start=(121, 20), stop=(120, 20), current=Current(x=-1, y=0), voltage=-4.5),
    ]

        return self._wires
