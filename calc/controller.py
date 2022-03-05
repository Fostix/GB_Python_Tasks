# связующее звено.
import model_mult as model
import view

def button_click():
    # model.init(1, 5)
    # model.init(get_value())
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b) # инициализация входных данных модели.
    result = model.do_it() # вычисляет сумму.
    view.view_data(result, 'result') # вернуть значение view.