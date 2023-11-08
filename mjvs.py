import tkinter as tk
from tkinter import ttk, simpledialog
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

# Function to retrieve votes and calculate the median
def calculate_results():
    global_results = defaultdict(list)
    global_mentions_count = {'Rejected': 0, 'Insufficient': 0, 'Passable': 0, 'Fair': 0, 'Good': 0, 'Very Good': 0}

    for voter in range(num_voters):
        results = defaultdict(list)
        mentions_count = {'Rejected': 0, 'Insufficient': 0, 'Passable': 0, 'Fair': 0, 'Good': 0, 'Very Good': 0}

        for candidate in range(num_candidates):
            mention = candidates[candidate][voter].get()
            results[mention].append(candidate)
            mentions_count[mention] += 1

        global_mentions_count = {k: global_mentions_count[k] + mentions_count[k] for k in global_mentions_count.keys()}

        mentions = list(results.keys())
        mentions.sort()
        if len(mentions) % 2 == 0:
            median1 = mentions[len(mentions) // 2 - 1]
            median2 = mentions[len(mentions) // 2]
            winners = results[median1] + results[median2]
        else:
            median = mentions[len(mentions) // 2]
            winners = results[median]

        for winner in winners:
            global_results[winner].append(voter + 1)  # +1 for display starting from 1

    # Copy mention data for each candidate before calculating percentages
    candidates_mentions = []
    for candidate in range(num_candidates):
        mentions = {'Rejected': 0, 'Insufficient': 0, 'Passable': 0, 'Fair': 0, 'Good': 0, 'Very Good': 0}
        for voter in range(num_voters):
            mention = candidates[candidate][voter].get()
            mentions[mention] += 1
        candidates_mentions.append(mentions)

    display_results(global_results, global_mentions_count, candidates_mentions)

# Function to display the results
def display_results(global_results, global_mentions_count, candidates_mentions):
    fig, ax = plt.subplots(figsize=(8, 4))
    labels = ['Rejected', 'Insufficient', 'Passable', 'Fair', 'Good', 'Very Good']
    colors = ['red', 'orange', 'yellow', 'lightgreen', 'green', 'darkgreen']

    candidates_labels = [f'Candidate {i+1}' for i in range(num_candidates)]
    y_pos = np.arange(len(candidates_labels))

    for candidate, voters in global_results.items():
        mentions_count = candidates_mentions[candidate]  # Use copied mentions for this candidate

        total_votes = len(voters)
        percentages = [mentions_count[label] / total_votes * 100 for label in labels]

        left = 0
        for i in range(len(labels)):
            ax.barh([candidate], [percentages[i]], color=colors[i], left=left)
            left += percentages[i]

    ax.set_yticks(y_pos)
    ax.set_yticklabels(candidates_labels)
    ax.set_xlabel('Percentage of Votes (%)')
    ax.set_title('Results by Candidate')

    # Set up a legend for the colors
    color_patches = [plt.Rectangle((0,0),1,1,fc=color, edgecolor = 'none') for color in colors]
    ax.legend(color_patches, labels)

    plt.tight_layout()

    # Save the image
    img_path = 'results.png'
    plt.savefig(img_path)
    plt.close(fig)

    # Display the image
    img = tk.PhotoImage(file=img_path)
    img_label = ttk.Label(root, image=img)
    img_label.grid(row=num_voters+2, column=0, columnspan=num_candidates*2, pady=10)
    img_label.image = img

# Create the main window
root = tk.Tk()
root.title('Majority Judgment Voting System')

# Ask for the number of voters
num_voters = simpledialog.askinteger("Number of Voters", "Enter the number of voters:")

# Ask for the number of candidates
num_candidates = simpledialog.askinteger("Number of Candidates", "Enter the number of candidates:")

# Add candidates
candidates = []
for i in range(num_candidates):
    candidate_votes = []
    for j in range(num_voters):
        label = ttk.Label(root, text=f'C{i+1} - V{j+1}')
        label.grid(row=j, column=i*2, padx=2, pady=2)
        mention = ttk.Combobox(root, values=['Rejected', 'Insufficient', 'Passable', 'Fair', 'Good', 'Very Good'], width=10)
        mention.grid(row=j, column=i*2+1, padx=2, pady=2)
        mention.current(0)  # Default to "Rejected"
        candidate_votes.append(mention)
    candidates.append(candidate_votes)

# Button to calculate the results
calculate_button = ttk.Button(root, text='Calculate Results', command=calculate_results)
calculate_button.grid(row=num_voters, columnspan=num_candidates*2, pady=10)

root.mainloop()
