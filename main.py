import retro
import time
env = retro.make('MortalKombatII-Genesis')

def closeenv():
    env.close()
def observation_space():
    print(env.observation_space)
def render():
    obs = env.reset()
    done = False
    for game in range(2):
        while not done:
            if done:
                obs = env.reset()
            env.render()
            obs, reward, done, info = env.step(env.action_space.sample())
            print('health ' , info['health'])
            print("enemy health ",info["enemy_health"])
            if reward>0:
                print('reward ' , reward)
            time.sleep(0.01)



def action_space():
    print(env.action_space.sample())

def test():
    print(env.action_space)

def reward():
    env.reset()
    print(env.step(env.action_space.sample()))

test()
# observation_space()
render()
# closeenv()

# reward()