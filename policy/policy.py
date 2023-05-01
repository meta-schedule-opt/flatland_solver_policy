from environment.environment import Environment


class Policy:

    def __init__(self):
        print('>> ' + self.get_name())

    def get_name(self):
        raise NotImplementedError

    def save(self, filename):
        raise NotImplementedError

    def load(self, filename):
        raise NotImplementedError

    def start_episode(self, train: bool):
        pass

    def start_step(self, train: bool):
        pass

    def start_act(self, handle: int, train: bool):
        pass

    def act(self, handle: int, state, eps=0.):
        raise NotImplementedError

    def end_act(self, handle: int, train: bool):
        pass

    def step(self, handle: int, state, action, reward, next_state, done):
        raise NotImplementedError

    def end_step(self, train: bool):
        pass

    def end_episode(self, train: bool):
        pass

    def load_replay_buffer(self, filename):
        pass

    def test(self):
        pass

    def reset(self, env: Environment):
        pass

    def clone(self):
        return self
