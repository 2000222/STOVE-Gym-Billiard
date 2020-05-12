from gym.envs.registration import register

register(
    id='billard-v0',
    entry_point='gym_billard.envs:BillardEnv',
)