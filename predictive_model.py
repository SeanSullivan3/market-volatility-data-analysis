
def predict(data, trend, range, time_delta = 'day') -> list:

    predict_values = []
    if time_delta == 'day':
        for i, change in enumerate(data):
            if i > len(trend) and i < len(data) - 1:
                if change < trend[0] + range and change > trend[0] - range:
                    predict_values.append(data[i + 1])
    elif time_delta == 'week':
        pass
    elif time_delta == 'month':
        pass
    elif time_delta == 'year':
        pass
    else: 
        raise ValueError('time_delta incorrect value')
    
    return predict_values