def good_years(papers):
    max = 0
    for i in papers:
        if i[1]>max:
            max = i[1]
    years = []
    for i in papers:
        if i[1] == max:
            years.append(i[0])
    return years

print(good_years([["2010", 10], ["2011", 20], ["2012", 11], ["2016", 20]]))