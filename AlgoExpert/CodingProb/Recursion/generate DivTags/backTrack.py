def generateDivTags(numberOfTags):
    validTags = []
    curTag = ""
    openTag_count = numberOfTags
    closeTag_count = numberOfTags
    generatedTag(curTag, openTag_count, closeTag_count, validTags)
    return validTags

def generatedTag(curTag, openTag_count, closeTag_count, validTags):
    # open the tag
    if openTag_count > 0:
        # append a open tag to current tag
        new_curTag = curTag + "<div>"
        # reduce the count of open tag as we just used one
        generatedTag(new_curTag, openTag_count - 1, closeTag_count, validTags)

    # there must be a tag open
    if openTag_count < closeTag_count:
        # append a open tag to current tag
        new_curTag = curTag + "</div>"
        # reduce the count of open tag as we just used one
        generatedTag(new_curTag, openTag_count, closeTag_count - 1, validTags)

    # once closed tag become 0, we have got a valid string
    if closeTag_count == 0:
        validTags.append(curTag)

    return