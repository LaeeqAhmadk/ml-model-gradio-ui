import gradio as gr
#['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
import joblib
loaded_model = joblib.load('trained_model.pkl')
def predict(preg, plas, pres, skin, test, mass, pedi, age):

    result = loaded_model.predict([[int(preg), int(plas), int(pres), int(skin), int(test), int(mass), int(pedi), int(age)]])
    if int(result[0]) == 1:
      return "The person is diabetic"
    else:
      return "The person is not diabetic"
    #return str(result)

demo = gr.Interface(
    fn=predict,
    inputs=["text", "text","text", "text","text", "text","text", "text"],
    outputs=["text"],
)

demo.launch()