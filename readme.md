# Netflix Movie Statistics Analysis Report

This report analyzes Netflix Originals data to answer questions about language, genre, IMDb scores, and runtime statistics. It uses Python, pandas, matplotlib, and Jupyter notebooks for interactive analysis and visualization. All analysis and code are original, and the dataset is from Kaggle.

## Report Highlights

- Calculates proportions of English-language and multi-language films  
- Identifies genres most common among multi-language films  
- Analyzes IMDb score distribution, top/bottom films, and runtime statistics  
- Visualizes distributions and relationships (including correlation analysis)  
- Demonstrates how correlation can be misleading with synthetic data  

## Viewing the Report

1. Clone the repository:  
   ```sh
   git clone https://github.com/yourusername/movie_statistics.git  
   cd movie_statistics
   ```  
2. Install dependencies:  
   ```sh
   pip install pandas matplotlib jupyter
   ```  
3. Launch the interactive notebook:  
   ```sh
   jupyter notebook notebooks/Movie_Statistics_Analysis.ipynb
   ```  
4. Or open the static HTML report:  
   ```sh
   open reports/Movie_Statistics_Analysis_Report.html
   ```  

## Files

- `notebooks/Movie_Statistics_Analysis.ipynb` — Interactive analysis notebook  
- `reports/Movie_Statistics_Analysis_Report.html` — Static HTML version of the report  
- `data/NetflixOriginals.csv` — Data file (not included; obtain from [Kaggle](https://www.kaggle.com/datasets/luiscorter/netflix-original-films-imdb-scores))  
- `requirements.txt` — Python dependencies  
- `README.md` — This file  

## Data Source

This report uses the Netflix Original Films IMDb Scores dataset from Kaggle: https://www.kaggle.com/datasets/luiscorter/netflix-original-films-imdb-scores

## 📝 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
