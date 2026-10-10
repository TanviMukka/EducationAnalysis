# India Female Education Analysis
A data analysis project exploring how education in India changed over time and how rural and urban areas differ in access to technology.

### Research Question
What factors cause the difference in education received by rural and urban females in India?

### Dataset
`livwell135.csv` covers India from 1993 to 2006.

### How to Run
1. Make sure `main.py` and `livwell135.csv` are in the same folder.
2. Install the required libraries by typing this in the terminal: `pip install pandas matplotlib`
3. Run the program by typing this in the terminal: `python main.py`
4. Follow the prompts in the terminal and press Enter whenever it says "Press enter to see...".

### Viewing the Graphs
The graphs don't pop up in a new window. Instead, they are saved as image files in the project folder. After the program has run, open the file explorer on the left side of your screen and click each file. (If you don't see them, try refreshing the file explorer.)
* `schooling_over_time.png` shows mean years of schooling in India from 1993 to 2006.
* `electricity_urban_vs_rural.png` compares the percentage of urban and rural households with electricity.

### Findings
Schooling in India rose from about 3.1 to 5.9 years between 1993 and 2006, and rural households had less electricity access than urban ones. However, this data doesn't split education by rural and urban areas, so it can't show what causes the gap.

### Limitations
* The data ends in 2006, so it does not describe India today.
* The dataset does not break education down by rural vs. urban, so this project can't directly show what causes the rural/urban education gap. Electricity access is used as one example of a rural/urban difference in technology.
* The values change in very small, even steps from year to year, so they may be estimates rather than exact survey results.

### Built With
* Python
* pandas
* matplotlib

### P.S.
*This project is built as part of Girls Who Code's Data Science for Good Course*