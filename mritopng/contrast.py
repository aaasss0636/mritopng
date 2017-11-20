
def histogram(image):

    hist = dict()

    # Initialize dict
    for shade in range(0, 256):
        hist[shade] = 0
    
    # Poppulate
    for row in image:
        for col in row:
            hist[col] += 1
    
    return hist


def shade_at_percentile(hist, percentile):

    n = sum(hist.values())
    cumulative_sum = 0.0
    for shade in range(0, 256):
        cumulative_sum += hist[shade]
        if cumulative_sum/n >= percentile:
            return shade
    
    return None
