from flask import Flask,request,jsonify
app=Flask(__name__)
symptoms_list=[
              {
                        "id":0,
                        "sym1":"Headache",
                        "sym2":"Bodypain",
                        "sym3":"Chill",

              },
              {
                        "id":1,
                        "sym1":"Depression",
                        "sym2":"Phobia",
                        "sym3":"Stress and anxiety",

              },
              {

                       "id":2,
                       "sym1":"Hives",
                       "sym2":"Itching",
                       "sym3":"Rashes",
              },
              {

                       "id":3,
                       "sym1":"Throatpain",
                       "sym2":"Nasalcongesion",
                       "sym3":"Wheezing",
              },
              {
                       "id":4,
                       "sym1":"Swelling of legs",
                       "sym2":"Numbness",
                       "sym3":"Joint Pain",
              }
           ]
doctors_list=['GeneralPractitioner','Psychiatrist','Dermatologist','ENTspecialist','Orthopaedic']


@app.route('/symptoms',methods=['GET','POST'])
def symptoms():
    if request.method=='GET':
        if len(symptoms_list)>0:
            return jsonify(symptoms_list)
        else:
            'Nothing Found',404
    if request.method=='POST':
            new_sym1=request.form['sym1']
            new_sym2=request.form['sym2']
            new_sym3=request.form['sym3']
            for sy in symptoms_list:
                  if sy['sym1']==new_sym1 and sy['sym2']==new_sym2 and sy['sym3']==new_sym3:
                       num=int(sy['id'])
                       return "Please consult a "+doctors_list[num]
            return "Could not diagnose your symptoms"

@app.route('/symptoms/<int:id>',methods=['GET','PUT','DELETE'])
def one(id):
        if request.method=='GET':
             for sy in symptoms_list:
                if ['id']==id:
                    return jsonify(sy)
                pass
        if request.method=='PUT':
             for sy in symptoms_list:
                if int(sy['id'])==id:
                    sy['sym1']=request.form['sym1']
                    sy['sym2']=request.form['sym2']
                    sy['sym3']=request.form['sym3']
                    updated_symptom={
                        'id':id,
                        'sym1':sy['sym1'],
                        'sym2':sy['sym2'],
                        'sym3':sy['sym3'],

                    }
                    return jsonify(updated_symptom)
        if request.method=='DELETE':
             for index,sy in enumerate(symptoms_list):
                if sy['id']==id:
                   symptoms_list.pop(index)
                   return jsonify(symptoms_list)
if __name__=='__main__':
    app.run()
                   
                 
