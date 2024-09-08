import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
joint_prob = np.array([[0.125, 0, 0,0],     # P(X=-3, Y={0,1,2,3})
                       [0, 0.375, 0,0],     # P(X=-1, Y={0,1,2,3})
                       [0, 0.125, 0.25,0],  # P(X=1, Y={0,1,2,3})
                       [0, 0,0, 0.125]])    # P(X=3, Y={0,1,2,3})
X_values=[-3,-1,1,3]
marginal_X = np.sum(joint_prob, axis=1)
marginal_Y = np.sum(joint_prob, axis=0)
print("Marginal Probability of X:", marginal_X)
print("Marginal Probability of Y:", marginal_Y)
joint_prob_df = pd.DataFrame(joint_prob, columns=['Y=0', 'Y=1', 'Y=2','Y=3'], index=['X=-3', 'X=-1', 'X=1','X=3'])
plt.figure(figsize=(8, 6))
sns.heatmap(joint_prob_df, annot=True, cmap="YlGnBu", cbar=True, linewidths=0.5)
plt.title("Joint Probability Distribution P(X, Y)")
plt.xlabel("Y")
plt.ylabel("X")
plt.show()
fig, ax = plt.subplots(1, 2, figsize=(14, 6))
ax[0].bar(X_values, marginal_X, color='red')
ax[0].set_title('Marginal Probability of X')
ax[0].set_xlabel('X')
ax[0].set_ylabel('P(X)')
ax[0].set_xticks(X_values)

ax[1].bar(range(len(marginal_Y)), marginal_Y, color='green')
ax[1].set_title('Marginal Probability of Y')
ax[1].set_xlabel('Y')
ax[1].set_ylabel('P(Y)')
ax[1].set_xticks(range(len(marginal_Y)))

plt.tight_layout()
plt.show()
