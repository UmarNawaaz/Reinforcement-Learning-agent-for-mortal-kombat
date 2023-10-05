import retro
import joblib
import numpy as np
from PIL import Image
def practise():
    reg = joblib.load("modelWithTenImages")
    env = retro.make(game="MortalKombatII-Genesis", use_restricted_actions = retro.Actions.FILTERED)
    print(reg.intercept_)

    # obs=env.reset()
    # img=np.array(Image.fromarray(obs).convert('L')).flatten()
    # print(img.ndim)
    # img=img.reshape(1,len(img))
    # print(img.ndim)
    # action=np.array(list(np.binary_repr(int(reg.predict(img)))), dtype=int)
    # print(type(action))

    env.reset()
    done = False
    obs = env.reset()
    for i in range(1):
        while not done:
            if done:
                obs = env.reset()
            env.render()
            img=np.array(Image.fromarray(obs).convert('L')).flatten()
            img=img.reshape(1,len(img))
            action=np.array(list(np.binary_repr(int(reg.predict(img)))), dtype=int)
            print(env.unwrapped.get_action_meaning(action))
            obs, reward, done, info = env.step(action)



practise()
