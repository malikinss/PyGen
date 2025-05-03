'''
TODO:
    Implement a Selfie class whose instances remember their previous states
    and can restore themselves to the states they were in before.

    An object's state is a certain set of attributes and corresponding values.

    During its lifetime, a Selfie instance can change its state in various
    ways, for example, by acquiring new attributes or changing the values
    of existing ones:
        obj = Selfie()
        obj.x = 1
        obj.y = 2

    To capture the current state of a Selfie instance, the save_state() method
    should be used:
        obj.save_state() # capture the state: x=1, y=2
        obj.x = 0 # change the state
        obj.y = 0 # change the state

    The captured states of a Selfie instance should be indexed:
        the first captured state should have index 0,
        the second — 1,
        the third — 2,
        and so on.

    It should be possible to return to the required states using the same
    indices:
        print(obj.x) # 0
        print(obj.y) # 0
        obj = obj.recover_state(0) # return to the first state
        print(obj.x) # 1
        print(obj.y) # 2

    Please note that when returning to one of the previous states using
    the recover_state() method, a new instance of the Selfie class should be
    returned that has the required state.

    If the recover_state() method is passed an index at which the Selfie
    instance has no state, the current instance should be returned:
        obj = obj.recover_state(7)
        print(obj.x) # 1
        print(obj.y) # 2

    Each Selfie instance should know how many states it has captured:
        obj = Selfie()
        print(obj.n_states()) # 0
        obj.x = 0
        obj.save_state()
        obj.x = 1
        obj.save_state()
        obj.x = 2
        obj.save_state()
        print(obj.n_states()) # 3
'''
