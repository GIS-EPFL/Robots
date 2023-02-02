from compas.utilities import DataEncoder
from compas.utilities import DataDecoder

class Action(object):
    def __init__(self, name, parameters={}):
        self.name = name
        self.parameters = parameters

    def __str__(self):
        return 'Action<name={}>'.format(self.name)

    @property
    def data(self):
        return dict(
            name=self.name,
            parameters={param_key: DataEncoder().default(p) if hasattr(p, 'to_data') else p for param_key, p in self.parameters.items()},
        )
    
    @classmethod
    def from_data(cls, data):
        return cls(data['name'], {param_key: DataDecoder().object_hook(p) if hasattr(p, '__iter__') else p for param_key, p in data['parameters'].items()})
    
    def to_data(self):
        return self.data

class ProductionData(object):
    def __init__(self, actions=[]):
        self.actions = actions

    @property
    def data(self):
        return dict(
            actions=[p.to_data() for p in self.actions]
        )
    
    @classmethod
    def from_data(cls, data):
        return cls([Action.from_data(d) for d in data['actions']])
    
    def to_data(self):
        return self.data