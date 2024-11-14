
# Zcash Inflation Chart with ZIP 234 Integration

## Overview
This project visualizes the inflation of Zcash over time, including the impact of the ZIP 234 proposal. The chart highlights Zcash inflation trends, halvings, and the projected inflation curve as per ZIP 234.

## Features
- **Baseline Zcash Inflation Curve**: Plots the current inflation curve.
- **ZIP 234 Inflation Curve**: Shows the inflation adjustment after ZIP 234.
- **Halving Indicators**: Highlights key halving dates with vertical dashed lines.
- **Annotations**: Includes percentage annotations at significant points.

## Prerequisites
- **Python 3.7 or higher**
- Required libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `openpyxl` (for Excel support)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ruzcash/zcash-inflation-visualizer.git
   cd zcash-inflation-visualizer
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure the `zcash_inflation_data.xlsx` file is in the project directory.
2. Run the script:
   ```bash
   python zcash_inflation_plot_english.py
   ```
3. The script will generate and display the Zcash inflation chart.

## Files
- **zcash_inflation_plot_english.py**: Python script for generating the inflation chart.
- **zcash_inflation_data.xlsx**: Excel file containing the inflation data.
- **requirements.txt**: List of dependencies.

## Project Structure
```
zcash-inflation-visualizer/
│
├── zcash_inflation_plot_english.py  # Main Python script
├── zcash_inflation_data.xlsx        # Data source file
├── requirements.txt                 # Dependencies
└── README.md                        # Project documentation
```

## License
This project is licensed under the MIT License.

## Acknowledgments
- **Matplotlib and Pandas Libraries**: For enabling data visualization and analysis.

## Contact
For questions or feedback, please contact [ruzcash@proton.me].
