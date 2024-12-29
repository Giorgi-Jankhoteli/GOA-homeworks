def converter(mpg):
    mtk = 1.609344
    gtl = 4.54609188
    kpl = (mpg * mtk) / gtl
    return round(kpl, 2)