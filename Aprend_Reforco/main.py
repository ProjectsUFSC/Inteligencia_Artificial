import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np

env = gym.make('Taxi-v3', render_mode='rgb_array')

env.reset()

env.render()
plt.imshow(env.render(mode='rgb_array'))
plt.axis('off')
plt.show()

episodios = 10
epocas = 1000

tabela_q = np.zeros([env.observation_space.n, env.action_space.n])

for i in range(1, epocas+1):
    recompensa = 0
    total_recompensa = 0

    env.reset()

    for j in range(1, episodios+1):
        while not done:
            estado, recompensa, done, _,_ = env.step(np.argmax(tabela_q[estado]))

            tabela_q[estado] = np,max(tabela_q[estado]) + 0.1 * (recompensa + 0.9 * np.max(tabela_q[estado]) - np.max(tabela_q[estado]))
