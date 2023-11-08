# MJVS - Majority Judgment Voting System

## Overview

The Majority Judgment voting system, conceived by French researchers Michel Balinski and Rida Laraki, is a single-winner voting system proposed in 2010 by Michel Balinski and Rida Laraki. It was introduced through a mathematical theory published in 2007 and later expanded upon in a comprehensive book published by MIT Press in 2011. The Majority Judgment system stands as a significant advancement in electoral theory, addressing the constraints identified in Arrow's Impossibility Theorem (1951) within the field of social choice theory.

The essence of the Majority Judgment system lies in its ability to offer voters the freedom to express their opinions through qualitative ratings, referred to as "mentions", rather than using traditional numerical or categorical ballots. This innovative approach to voting aims to provide a more intuitive and universally understood method for gauging voter sentiment.

## Advantages of Majority Judgment

The adoption of the Majority Judgment system comes with several distinct benefits:

1. **Mitigates the Spoiler Effect**: By allowing voters to evaluate candidates independently, the need for strategic or tactical voting is effectively eliminated.

2. **Robust Against Tactical Manipulation**: The election outcome remains stable even if a candidate is added or removed from the race, reducing strategic advantage in the voting process.

3. **Facilitates Nuanced Expression**: Voters can utilize a comprehensive set of mentions, including options like "to be rejected" or "insufficient", enabling highly nuanced expression of preferences.

4. **Fine-Grained Evaluation**: The utilization of detailed value scales empowers voters to convey their preferences with exceptional granularity.

5. **Transparent Candidate Support**: Each candidate's "merit profile" is determined by the proportions of different mentions assigned by voters, offering invaluable insights into the types of support each elected candidate enjoys.

## How to Use this software

This Python script provides a user-friendly graphical interface for conducting elections using the Majority Judgment voting system. It facilitates the input of candidate details, collection of votes, and visualization of the results through stacked horizontal bar charts.

### Getting Started

1. **Setting up the Environment**: Ensure you have Python installed on your system.

2. **Running the Script**: Execute the Python script provided in this repository.

3. **GUI Interface**: The GUI will prompt you to enter the number of voters and candidates.

4. **Entering Votes**: For each voter, assign mentions to each candidate using the drop-down menu.

5. **Calculating Results**: Click the "Calculate Results" button to compute the election outcome.

6. **Viewing Results**: The script will generate horizontal bar charts representing the results for each candidate.
   
The candidate with the highest median score is the winner. If several candidates have the same highest median score, the winner of the majority judgment is discovered by deleting (one by one) all the scores equal in value to the shared median score in the column of each tied candidate. This operation is repeated until only one of the previously tied candidates has the highest median score. 

### Understanding the Color Legend

- Red: "To be rejected"
- Orange: "Insufficient"
- Yellow: "Passable"
- Light Green: "Satisfactory"
- Green: "Good"
- Dark Green: "Very Good"

### Important Considerations

Please note that this script serves as a simulation tool and does not possess the full legal and procedural framework of an official election. It is intended for educational and illustrative purposes.

For a more in-depth understanding of the Majority Judgment voting system, it is highly recommended to refer to the research publications authored by Michel Balinski and Rida Laraki.

## Acknowledgements

Special appreciation goes to Michel Balinski and Rida Laraki for their groundbreaking contributions to the development of the Majority Judgment voting system.

## License

please note that the code for this software (and ONLY the code, nothing else is licensed) is, unless otherwise stated, licensed under [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

---

*Disclaimer: This script is a simulation tool and should not be considered a substitute for official election procedures. Use it for educational and illustrative purposes ONLY.*
