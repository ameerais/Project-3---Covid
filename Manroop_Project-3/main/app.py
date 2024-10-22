#Flask API with a route that retrieves data based on user input
#Import dependencies 
from flask import Flask, jsonify, request, send_from_directory
import pandas as pd
import warnings
from flask import render_template


# Name of the current module
app = Flask(__name__)

# Reading the dataset
df = pd.read_csv('merged_df_2021_cleaned.csv')

#Default page setup and draw html file for visualization
@app.route('/')
def home():
    return render_template('index.html')

# Route to return data for a specific country for all the months
# We have data available for these countries 'Argentina', 'Austria', 'Belgium', 'Bulgaria', 'Chile', 'Croatia',
        #'Cyprus', 'Czechia', 'Denmark', 'Ecuador', 'Estonia', 'Finland',
       #'France', 'Germany', 'Hungary', 'Ireland', 'Italy', 'Latvia',
       #'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands',
       #'Norway', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia',
       #'Spain', 'Sweden', 'Switzerland', 'United States'

import warnings

@app.route('/country', methods=['GET'])
def get_country_data():
    # Ignore the DeprecationWarning for the groupby apply operation
    #Newer version of pandas will resolve this issue
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Get the country from the dataset for query parameters
    country = request.args.get('country')

    # Make sure taht the country parameter is provided
    if country:
        # Get the data for the specified country
        country_data = df[df['location'] == country]

        # Make sure if there is data for the country
        if not country_data.empty:
            # Groupping by 'month' and converted to dictionary
            #This function was giving warnings and these warnings were ignored
            monthly_data = country_data.groupby('month').apply(lambda x: x.to_dict(orient='records')).to_dict()

            # Dispaly the monthly data as JSON
            return jsonify(monthly_data)
        else:
            # Display an error if no data is found for the country
            return jsonify({'error': f'No data found for {country}'}), 404
    else:
        # Display an error if no country is specified
        return jsonify({'error': 'No country specified'}), 400


# Route to return summarized data for all vacciantions, deaths and cases of Covid-19
#This route is called summarized and we will sum the values for display
@app.route('/summarized', methods=['GET'])
def get_aggregated_data():
    result = df.groupby('location').agg({
        'total_vaccinations': 'sum',
        'total_deaths': 'sum',
        'total_cases': 'sum'
    }).reset_index().to_dict(orient='records')
    return jsonify(result)

# Flask app initialization
if __name__ == '__main__':
    app.run(debug=True)


