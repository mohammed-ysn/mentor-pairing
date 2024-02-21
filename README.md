# Mentor Pairing

This program, developed for the Cambridge University Islamic Society, pairs students with mentors based on various criteria such as industry interest and types of support sought.

### Prerequisites

- Python 3.x
- CSV files containing participant data:
  - `students.csv`: Information about students.
  - `mentors.csv`: Information about mentors.

### Instructions

1. **Prepare Data Files**:
   - Ensure that you have the following CSV files in the `data/` directory:
     - `students.csv`: Includes fields such as Full name, Username, Desired industry, and Support types.
     - `mentors.csv`: Includes fields such as Full name, Email address, Industry, Support types, and Maximum number of students.

2. **Run the Script**:
   - Execute the script `main.py` in your Python environment.

3. **View Pairings**:
   - Upon successful execution, the script generates a CSV file named `pairings.csv` in the `data/` directory. This file contains the pairings of students with their respective mentors along with relevant details.

4. **Review Pairings**:
   - The script also prints the pairings to the console, providing insights into the matched student-mentor pairs, including their names and industries.

5. **Handle Unassigned Participants**:
   - If any students or mentors remain unassigned, the script displays their details separately.

### Running the Script

```bash
python main.py
```

### Output

- The script generates pairings.csv in the data/ directory.
- Pairing details are also displayed in the console.
- Information about unassigned students or mentors is provided if applicable.

### Note
- Ensure that the CSV files (students.csv and mentors.csv) are correctly formatted and accessible to the script.
- For additional assistance or inquiries, please contact the script author.
