def slices(series, length):
    result = []
    seriesLength = len(series)
    
    if seriesLength == 0:
        raise ValueError("Can't use an empty series !!")
    if length <= 0:
        raise ValueError("Can't use zero or negative length !!")
    if length > seriesLength:
        raise ValueError("Length too large for this series !!")

    for i in range(seriesLength-length+1):
        result.append(series[i:i+length])
    return result
