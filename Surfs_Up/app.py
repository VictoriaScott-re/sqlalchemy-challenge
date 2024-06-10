# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Helper Functions
#################################################
def get_last_date():
    return session.query(func.max(Measurement.date)).first()[0]

def get_query_date(last_date):
    return dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=365)

def query_precipitation_data(query_date):
    return session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= query_date).all()

def query_station_list():
    return session.query(Station.station).all()

def query_temperature_data(most_active_station, query_date):
    return session.query(Measurement.date, Measurement.tobs).filter(
        Measurement.station == most_active_station,
        Measurement.date >= query_date
    ).all()

def query_temperature_stats(start, end=None):
    query = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start)
    
    if end:
        query = query.filter(Measurement.date <= end)
        
    return query.all()[0]

def format_temperature_stats(results):
    return {
        "TMIN": results[0],
        "TAVG": results[1],
        "TMAX": results[2]
    }

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
        f"<br/>"
        f"Note: Replace &lt;start&gt; and &lt;end&gt; with dates in the format YYYY-MM-DD.<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the last 12 months of precipitation data."""
    last_date = get_last_date()
    query_date = get_query_date(last_date)
    results = query_precipitation_data(query_date)
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    results = query_station_list()
    stations = [station[0] for station in results]
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the last 12 months of temperature observations for the most active station."""
    most_active_station = 'USC00519281'
    last_date = get_last_date()
    query_date = get_query_date(last_date)
    results = query_temperature_data(most_active_station, query_date)
    temperature_data = [{date: tobs} for date, tobs in results]
    return jsonify(temperature_data)

@app.route("/api/v1.0/<start>")
def start_date(start):
    """Return TMIN, TAVG, TMAX for all dates greater than or equal to the start date."""
    results = query_temperature_stats(start)
    temperature_stats = format_temperature_stats(results)
    return jsonify(temperature_stats)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    """Return TMIN, TAVG, TMAX for dates between the start and end date inclusive."""
    results = query_temperature_stats(start, end)
    temperature_stats = format_temperature_stats(results)
    return jsonify(temperature_stats)

if __name__ == '__main__':
    app.run(debug=True)
