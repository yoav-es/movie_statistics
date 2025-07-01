# Movie Statistics Analysis

This project analyzes Netflix Originals data to answer questions about language, genre, IMDb scores, and runtime statistics.  
It uses Python, pandas, and matplotlib for data analysis and visualization.

## Features

- Calculates proportions of English-language and multi-language films
- Identifies genres most common among multi-language films
- Analyzes IMDb score distribution, top/bottom films, and runtime statistics
- Visualizes distributions and relationships (including correlation analysis)
- Demonstrates how correlation can be misleading with synthetic data

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/movie_statistics.git
    cd movie_statistics
    ```

2. Install requirements (if needed):
    ```sh
    pip install pandas matplotlib
    ```

3. Place `NetflixOriginals.csv` in the project directory.

4. Run the analysis:
    ```sh
    python main.py
    ```

## Files

- `main.py` — Main analysis script
- `NetflixOriginals.csv` — Data file (not included; obtain from your source)

## Data Source

This project uses the [Netflix Original Films IMDb Scores dataset from Kaggle](https://www.kaggle.com/datasets/luiscorter/netflix-original-films-imdb-scores).

## License

MIT License

---

*This project was inspired by a Codecademy exercise. All analysis and code are original, and the dataset is from Kaggle.*