# sqlalchemy-challenge
Module 10 Assignment

# Hawaii Climate Analysis and API

## Overview
I'm planning a vacation to Honolulu, Hawaii, and I've conducted a climate analysis to help with trip planning. This project uses Python, SQLAlchemy, Pandas, and Matplotlib to explore climate data and provides a Flask API to access the data.

## Instructions

### Part 1: Analyze and Explore the Climate Data
1. **Database Connection**:
    - Connect to the SQLite database using `create_engine()`.
    - Reflect the tables into classes using `automap_base()`.
    - Save references to the `station` and `measurement` classes.
    - Create a SQLAlchemy session to link Python to the database.

2. **Precipitation Analysis**:
    - Find the most recent date in the dataset.
    - Query the last 12 months of precipitation data.
    - Load the results into a Pandas DataFrame and plot the data.
    - Print summary statistics for the precipitation data.

3. **Station Analysis**:
    - Calculate the total number of stations.
    - Find and list the most-active stations.
    - Query min, max, and avg temperatures for the most-active station.
    - Query the last 12 months of temperature observations for the most-active station and plot a histogram.
  
4. **Link**
    - - [Jupyter Notebook (Surfs_Up/climate_starter.ipynb)](Surfs_Up/climate_starter.ipynb)

### Part 2: Design the Climate App
I created a Flask API based on the queries developed in Part 1.

- `/` : Landing page with all available routes.
- [`/api/v1.0/precipitation`](http://127.0.0.1:5000/api/v1.0/precipitation) : JSON representation of the last 12 months of precipitation data.
- [`/api/v1.0/stations`](http://127.0.0.1:5000/api/v1.0/stations) : JSON list of stations.
- [`/api/v1.0/tobs`](http://127.0.0.1:5000/api/v1.0/tobs) : JSON list of temperature observations for the previous year for the most-active station.
- [`/api/v1.0/<start>`](http://127.0.0.1:5000/api/v1.0/2016-04-01) : JSON list of min, avg, and max temperatures for all dates greater than or equal to the start date.
- [`/api/v1.0/<start>/<end>`](http://127.0.0.1:5000/api/v1.0/2016-04-01/2016-10-31) : JSON list of min, avg, and max temperatures for dates between the start and end date inclusive.

### Best Dates to Visit Hawaii
Based on the analysis, the best time to visit Hawaii would be during the months with the least precipitation and moderate temperatures, typically from April to October.

## Files
- [App Code (Surfs_Up/app.py)](Surfs_Up/app.py)
- [Jupyter Notebook (Surfs_Up/climate_starter.ipynb)](Surfs_Up/climate_starter.ipynb)
- [Precipitation Plot (Images/Precipitation_Plot.png)](Images/Precipitation_Plot.png)
- [Temperature Histogram (Images/Temp_Histogram.png)](Images/Temp_Histogram.png)

## Resources
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [ChatGPT](https://chat.openai.com/)



