# b = breadth , h = height
# Tc: O(b^2 * h)
# Sc: O(w)

def waterfallStreams(array, source):
    # make a copy of the source row
    sourceRow = array[0][:] # O(W) = width of current row

    # change the source value for identification
    sourceRow[source] = -1

    # start going through the rest to make the water fall
    for i in range(1, len(array)):
        # make a copy of the row
        fall_to_Row = array[i][:] # the next row in which water will fall

        # go through each column to make the water fall
        for idx in range(len(sourceRow)):
            value_at_sourcerow = sourceRow[idx]

            # check if the current column has water in in
            hasWater = value_at_sourcerow < 0

            # check if the fallRow has a block, which would prevent the water fall
            hasBlock = fall_to_Row[idx] == 1

            if not hasWater:
                # if the current column doesnot have any water, simply continue
                continue

            if not hasBlock:
                # if there is no blockage. the water will simply flow down
                fall_to_Row[idx] += value_at_sourcerow
                continue # continue to check for other source

            # if the soure has water -- but there is a blockage at fall then 
            # split water
            splitWater = value_at_sourcerow / 2

            # once the water is split - move the water left and right 
            # moving left -- check if the water can move left -- and make it fall down
            leftIdx = idx
            # check for boundary
            while leftIdx - 1 >= 0:
                leftIdx -= 1

                # check if the water can move left
                # if there is a block then it cannot move. so water is tapped and lost
                if sourceRow[leftIdx] == 1:
                    break

                # in order to flow down, 
                # check the fall, if there are no blocks
                # if blockage keep moving left
                if fall_to_Row[leftIdx] != 1:
                    fall_to_Row[leftIdx] += splitWater
                    break

            # moving right -- check if the water can move right -- and make it fall down
            rightIdx = idx
            # check for boundary
            while rightIdx + 1 < len(sourceRow):
                rightIdx += 1

                # check if the water can move left
                # if there is a block then it cannot move. so water is tapped and lost
                if sourceRow[rightIdx] == 1:
                    break

                # in order to flow down, 
                # check the fall, if there are no blocks
                # if blockage keep moving left
                if fall_to_Row[rightIdx] != 1:
                    fall_to_Row[rightIdx] += splitWater
                    break

        # once i have move left and right for every value in my source row
        # go to the next row and make it further flow down -- till we reach the bucket
        sourceRow = fall_to_Row

    # once i reach the end row. calcuate the value
	# we keep our source negative. To change it to positve - multiply it by 1
	# return whole number . so insted of 1 use 100
    bucketRow = list(map(lambda x : x * -100, sourceRow) )

    return bucketRow