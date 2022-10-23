from flask import Flask, render_template, request
import pandas as pd
import pickle






app = Flask(__name__)
df = pd.read_csv("Cleaned.csv")
model = pickle.load(open("RePrediction.pkl",'rb'))


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/index')
def index():
    UNDER_CONSTRUCTION = sorted(df['UNDER_CONSTRUCTION'].unique())
    RERA = sorted(df['RERA'].unique())
    BHK_NO = sorted(df['BHK_NO'].unique())
    SQUARE_FT	 = sorted(df['SQUARE_FT'].unique())
    READY_TO_MOVE = sorted(df['READY_TO_MOVE'].unique())
    LONGITUDE = sorted(df['LONGITUDE'].unique())
    LATITUDE	 = sorted(df['LATITUDE'].unique())
    BHK_OR_RK = sorted(df['BHK_OR_RK'].unique())
    return render_template('index.html', UNDER_CONSTRUCTION = UNDER_CONSTRUCTION, RERA=RERA, BHK_NO=BHK_NO,SQUARE_FT=SQUARE_FT,READY_TO_MOVE=READY_TO_MOVE,LONGITUDE=LONGITUDE,LATITUDE=LATITUDE,BHK_OR_RK=BHK_OR_RK)



@app.route('/predict', methods = ['POST'])
def predict():
    UC = int(request.form.get('Under_Construction'))
    Rera = int(request.form.get('Rera_Approved'))
    B_N = int(request.form.get('BHK_NO.'))
    S_F = float(request.form.get('Square_ft'))
    R_T_M = int(request.form.get('Ready_to_move'))
    Long = float(request.form.get('Longitude'))
    Lat = float(request.form.get('Latitude'))
    B_O_R = int(request.form.get('Bhk_Or_Rk'))
    print(UC,Rera,B_N,S_F,R_T_M,Long,Lat,B_O_R)

    prediction = model.predict(pd.DataFrame([[UC, Rera, B_N, S_F, R_T_M, Long, Lat, B_O_R]],
                                            columns=['UNDER_CONSTRUCTION', 'RERA', 'BHK_NO', 'SQUARE_FT',
                                                     'READY_TO_MOVE', 'LONGITUDE', 'LATITUDE', 'BHK_OR_RK']))
    print(prediction)
    return str(prediction[0])


if __name__ == "__main__":
    app.run(debug=True)


