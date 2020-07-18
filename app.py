from flask import Flask , render_template ,request,url_for
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/query',methods=['POST'])
def query():
	Name = request.form['Name']
	email = request.form['email']
	Mobile  = request.form['Mobile']
	return render_template('query.html',Name=Name,email=email,Mobile=Mobile)

@app.route('/predict',methods=['POST'])
def predict():
	Airline = request.form['Airline']
	if (Airline=='Jet Airways'):
		Airline = 0.2
	elif(Airline=='Indigo'):
		Airline=0.11
	elif(Airline=='Air India'):
		Airline = 0.12
	elif(Airline=='Multiple carriers'):
		Airline = 0.13
	elif(Airline=='Spicejet'):
		Airline=0.14
	elif(Airline=='Vistara'):
		Airline=0.15
	elif(Airline=='Air Asia'):
		Airline=0.16
	elif(Airline=='GoAir'):
		Airline=0.17
	elif(Airline=='Multiple Carriers Premier Economy'):
		Airline=0.19
	elif(Airline=='Jet Airways Business'):
		Airline=0.05
	elif(Airline=='Vistara Premium Economy'):
		Airline=0.02
	else:
		Airline=0.03

	Source = request.form['Source']
	if (Source=='Delhi'):
		Source=0.1
	elif(Source=='Kolkata'):
		Source=0.11
	elif(Source=='Banglore'):
		Source=0.12
	elif(Source=='Mumbai'):
		Source=0.13
	elif(Source=='Chennai'):
		Source=0.14

	Destination = request.form['Destination']
	if (Destination=='Cochin'):
		Destination=0.15
	elif (Destination=='Banglore'):
		Destination=0.12
	elif(Destination=='Delhi'):
		Destination=0.1
	elif(Destination=='New Delhi'):
		Destination=0.16
	elif(Destination=='Hyderabad'):
		Destination=0.17
	elif(Destination=='Kolkata'):
		Destination=0.11

	Total_Stops = int(request.form['Total_Stops'])

	Additional_info = request.form['Additional_info']
	if(Additional_info=='No info'):
		Additional_info=0.1
	elif(Additional_info=='In-flight meal not included'):
		Additional_info=0.11
	elif(Additional_info=='No check-in baggage included'):
		Additional_info=0.12
	elif(Additional_info=='1 Long layover'):
		Additional_info=0.13
	elif(Additional_info=='Change airports'):
		Additional_info=0.14
	elif(Additional_info=='Business class'):
		Additional_info=0.15
	elif(Additional_info=='No Info'):
		Additional_info=0.16
	elif(Additional_info=='Red-eye flight'):
		Additional_info=0.17
	elif(Additional_info=='1 Short layover'):
		Additional_info=0.18
	elif(Additional_info=='2 Long layover'):
		Additional_info=0.19

	Date = int(request.form['Date'])
	Month = int(request.form['Month'])
	Year = int(request.form['Year'])

	dep_hour = int(request.form['dep_hour'])
	dep_mint = int(request.form['dep_mint'])

	arr_hour = int(request.form['arr_hour'])
	arr_mint = int(request.form['arr_mint'])

	hour_duration = int(request.form['hour_duration'])
	mint_duration = int(request.form['mint_duration'])

	prediction = model.predict([[Airline, Source, Destination, Total_Stops,
       Additional_info, Date, Month, Year, dep_hour, dep_mint,
       arr_hour, arr_mint, hour_duration, mint_duration]])
	output=round(prediction[0],2)
	return render_template('result.html',output=output)

if __name__ == '__main__':
	app.run(debug=True)

 			









