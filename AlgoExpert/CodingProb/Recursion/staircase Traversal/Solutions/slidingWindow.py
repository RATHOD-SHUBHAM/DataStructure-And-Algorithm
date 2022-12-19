def staircaseTraversal(height, maxSteps):
    count = 0
    window = [1]
    

    for idx in range(1, height + 1):
        start_window = idx - maxSteps
        end_window = idx - 1
        # get the end of prev window slide
        prev_window_end = start_window - 1

        if prev_window_end >= 0:
            # remove the existing count
            count -= window[prev_window_end]

        # add the prev count
        count += window[end_window]
        window.append(count)

    return count
        
        
