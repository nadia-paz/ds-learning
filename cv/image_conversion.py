def f_rgb_to_hsv(r, g, b,scaleFactor=100): 
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)    # maximum of r, g, b 
    cmin = min(r, g, b)    # minimum of r, g, b 
    diff = cmax-cmin       # diff of cmax and cmin. 
    if cmax == cmin:  
        h = 0
    elif cmax == r:  
        h = (60 * ((g - b) / diff) + 0) % 360
    elif cmax == g: 
        h = (60 * ((b - r) / diff) + 120) % 360
    elif cmax == b: 
        h = (60 * ((r - g) / diff) + 240) % 360
   
    if h < 0:
        h = h + 360
    if cmax == 0: 
        s = 0
    else: 
        s = (diff / cmax) * scaleFactor
    v = cmax * scaleFactor
    return h, s, v 
    