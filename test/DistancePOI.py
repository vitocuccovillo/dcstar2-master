# Distance è una classe che nel suo costruttore prende in input uno stato
# espone poi una funzione che accetta in input un altro stato di interesse
# e ne restituisce la distanza fra il primo stato ed il nuovo stato

class DistancePOI():

    def __init__(self, _state, _distance_function):
        self.state = _state
        self.distance_function = _distance_function

    def getDistance(self, new_state): #misura la distanza fra self.state e new_state
        return self.distance_function(self.state, new_state)
