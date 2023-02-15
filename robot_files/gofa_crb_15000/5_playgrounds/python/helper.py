from compas.utilities import DataEncoder
from compas.utilities import DataDecoder


class ProductionData(object):
    def __init__(self, actions=[]):
        self.actions = {action.id: action for action in actions}

    @property
    def data(self):
        return dict(
            actions=[p.to_data() for p in self.actions.values()]
        )
    
    @classmethod
    def from_data(cls, data):
        return cls([Action.from_data(d) for d in data['actions']])
    
    def to_data(self):
        return self.data


class Action(object):
    def __init__(self, name, parameters={}, action_id= None, namespace= "/", dependency_ids=[]):
        self.name = name
        self.parameters = parameters
        self.id = action_id
        self.namespace = namespace
        self.dependency_ids = dependency_ids

    def __str__(self):
        return 'Action<name={}>'.format(self.id, self.namespace, self.name)

    @property
    def data(self):
        return dict(
            id = self.id,
            namespace = self.namespace,
            name=self.name,
            parameters={param_key: DataEncoder().default(p) if hasattr(p, 'to_data') else p for param_key, p in self.parameters.items()},
            dependency_ids=self.dependency_ids
        )
    
    @classmethod
    def from_data(cls, data):
        return cls( data['name'], {param_key: DataDecoder().object_hook(p) if hasattr(p, '__iter__') else p for param_key, p in data['parameters'].items()}, data['id'], data['namespace'],data['dependency_ids'])
    
    def to_data(self):
        return self.data