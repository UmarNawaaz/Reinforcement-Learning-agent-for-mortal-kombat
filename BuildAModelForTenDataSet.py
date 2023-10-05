import retro
import numpy as np
from PIL import Image
import random
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
def practiseImages():
    env = retro.make(game="MortalKombatII-Genesis", use_restricted_actions = retro.Actions.FILTERED)
    env.reset()
    d=False

    num_actions = env.action_space.n
    all_actions = [np.binary_repr(i, width=num_actions) for i in range(
        2 ** num_actions)]  # np.binary_reprconvert an integer into its binary representation as a string and width is output binary length,this line takes all action from 000000000000 to 111111111111

    actions = []  # for all actions of player
    bin_action = []  # for all binary actions of player
    total_act_num = 0  # number  of actions of player

    for index, binary_action in enumerate(
            all_actions):  # enumerate keeping track of both the elements and their corresponding indices  000000000001  000000000010
        if (env.unwrapped.get_action_meaning(binary_action) != [] and env.unwrapped.get_action_meaning(
                binary_action) not in actions
                and not (env.unwrapped.get_action_meaning(binary_action).__contains__(
                    'Z') or env.unwrapped.get_action_meaning(
                    binary_action).__contains__('Y') or env.unwrapped.get_action_meaning(binary_action).__contains__(
                    'X'))):  # if there is no meaning of an binary action then reject them
            print(f"Action ", index, binary_action, env.unwrapped.get_action_meaning(binary_action))
            actions.append(env.unwrapped.get_action_meaning(
                binary_action))  # append the meaning of action in actions list to check if the same action come again then if statement reject them
            bin_action.append(binary_action)
            total_act_num = total_act_num + 1

    print("Total actions is ", total_act_num)

    image_stack=[]
    dataimg=[]
    dataaction=[]
    dx=[]
    dy=[]
    t=0
    done = False
    for i in range(1000000):

        while not done:
            if done:
                obs = env.reset()
            env.render()
            act=random.choice(bin_action)
            obs, reward, d, info = env.step(act)
            image_stack.append(obs)
            if reward>0:
                if t>10:
                    done = True
                dataimg.append(np.array(Image.fromarray(image_stack[-12]).convert('L')).flatten())
                dataaction.append(int(str(''.join(map(str, act))),2))
                t+=1
    dataimg=np.array(dataimg)
    dataaction=np.array(dataaction)

    # print(np.array(dataimg).ndim)
    # print(type(np.array(dataimg)))
    #
    # print(np.array(dataaction).ndim)
    # print(type(np.array(dataaction)))
    # plt.imshow(pandaData['image'][0])
    # plt.show()
    # x_train, x_test, y_train, y_test = train_test_split(dataimg,dataaction, test_size=0.2)
    reg = LogisticRegression()
    reg.fit(dataimg,dataaction)


    joblib.dump(reg,'modelWithTenImages')

practiseImages()

