CORRECT_ANSWER = 1.04
NOT_REALLY_CORRECT_ANSWER = 41.04
VERY_CLOSE_ANSWER = 133.04

class Feedback:
    SYNTAX_ERROR = 'Ошибка при вводе ответа'
    CORRECT = 'Верно'
    INCORRECT = 'Сначала ищется несмещенная оценка данного дискретного ряда. Далее вычисляется несмещенная оценка параметра s. В итоге по формуле вычисляется значение стандартной ошибки.'
    NOT_REALLY_CORRECT = 'Найдена несмещённая оценка ряда. Далее следует вычислить несмещенную оценку параметра s.'
    VERY_CLOSE = 'Найдена несмещенная оценка параметра s. После этого стоит по формуле вычислить значение стандартной ошибки.'
    
##############################

def solve():
    return str(CORRECT_ANSWER)

def parse(reply):
    try:
        answer = float(reply)
    except ValueError:
        answer = None
    return answer


def check(reply):
    answer = parse(reply)
    if answer is None:
        return 0, Feedback.SYNTAX_ERROR

    if answer == NOT_REALLY_CORRECT_ANSWER:
        return 0, Feedback.NOT_REALLY_CORRECT
    elif answer == VERY_CLOSE_ANSWER:
        return 0, Feedback.VERY_CLOSE
    elif answer == CORRECT_ANSWER:
        return 1, Feedback.CORRECT
        return 1, Feedback.CORRECT
    return 0, Feedback.INCORRECT