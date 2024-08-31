import scipy.stats as stats

# data
file_path = "./SN2_data.txt"

with open(file_path, 'r') as file:
    next(file) # skip first line

    for line in file:
        value_list = line.strip().split('\t')
        mu1, sigma1, n1 = float(value_list[0]), float(value_list[1]), float(value_list[2])
        mu2, sigma2, n2 = float(value_list[3]), float(value_list[4]), float(value_list[5])

        # pooled standard deviation
        sp = (((n1-1)*sigma1**2 + (n2-1)*sigma2**2) / (n1+n2-2))**0.5

        # t statistic
        if mu1 >= mu2:
            t_statistic = (mu1 - mu2) / (sp * ((1/n1 + 1/n2)**0.5))
        else:
            t_statistic = (mu2 - mu1) / (sp * ((1/n1 + 1/n2)**0.5))

        # degrees of freedom
        df = n1 + n2 - 2

        # p-value
        p_value_1tail = stats.t.sf(abs(t_statistic), df)
        p_value_2tail = 2 * p_value_1tail

        print(f"p-value 1 tail: {p_value_1tail} , p-value 2 tail: {p_value_2tail}")