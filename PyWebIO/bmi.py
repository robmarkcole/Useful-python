from pywebio import start_server
from pywebio.input import input, FLOAT
from pywebio.output import put_text

def bmi():
    height = input("Your Height(cm)：", type=FLOAT)
    weight = input("Your Weight(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(14.9, 'Severely underweight'), (18.4, 'Underweight'),
                  (22.9, 'Normal'), (27.5, 'Overweight'),
                  (40.0, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_text('Your BMI: %.1f, category: %s' % (BMI, status))
            break

if __name__ == '__main__':
    # bmi() # basic, closes after form completion
    start_server(bmi, port=80) # run as server