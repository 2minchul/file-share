class Entity:
    id: int

    def __eq__(self, other):
        if not isinstance(other, Entity):
            return False
        return self.id == other.id
