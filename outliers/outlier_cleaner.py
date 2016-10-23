 #!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """



    cleaned_data = [(e[1], e[2], (e[0] - e[2])**2)
        for e in zip(predictions, ages, net_worths)]

    print cleaned_data
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2], reverse=True)[9:]
    print cleaned_data

    return cleaned_data


if __name__ == '__main__':
    outlierCleaner()