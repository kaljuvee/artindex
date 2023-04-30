# Kanvas.AI Art Index Dashboard

This repository contains the source code for the Kanvas.AI Art Index Dashboard, an interactive web-based data visualization tool built using Streamlit, Plotly Express, and Pandas. The dashboard helps users analyze and explore the art market, specifically focusing on Allee Galerii art auction data from 2020 to 2022.

## Features

The dashboard has three main sections, each with a different visualization:

1. A treemap displaying the best-selling artists based on total art auction sales and overbidding percentages, organized hierarchically by category, technique, and author.
2. A scatter plot examining the relationship between the age of an artwork and its end price at the auction, with data points colored based on their category and sized by the decade in which the artwork was created.
3. A scatter plot investigating the relationship between the dimensions of an artwork and its end price at the auction, with data points colored based on their category and sized by the artwork's dimensions.

## Installation

1. Clone this repository:

```
git clone https://github.com/yourusername/kanvas-ai-art-index.git
```

2. Navigate to the project directory:

```
cd kanvas-ai-art-index
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit server:

```
streamlit run app.py
```

2. Open the provided URL in your web browser to view the dashboard.

## Data

The data used in this dashboard is sourced from Allee Galerii auctions held between 2020 and 2022. Please note that the data may be subject to change or updates, and the dashboard should be updated accordingly.

## Contributing

We welcome contributions to improve the dashboard or add new features. Please feel free to submit pull requests or create issues for any bugs you encounter or enhancements you'd like to see.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Author: Julian Kaljuvee
- Source: Allee Galerii auctions (2020-2022)
- Built with Streamlit, Plotly Express, and Pandas
