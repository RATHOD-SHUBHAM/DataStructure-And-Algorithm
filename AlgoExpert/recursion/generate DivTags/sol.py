# TIme = Space = very very large
#( (2n)! / ((n!((n+1)!) ))))))

def generateTags(openingTag, closingTag,curTag,res):
	if openingTag > 0:
		print("opening Tag: ",openingTag)
		newCurTag = curTag + "<div>"
		print("curTag is : ",newCurTag)
		generateTags(openingTag-1, closingTag,newCurTag,res)
		
	if openingTag < closingTag:
		print("opening Tag: ",openingTag)
		print("closing Tag: ",closingTag )
		newCurTag = curTag + "</div>"
		print("cur Claosing Tag: ",newCurTag)
		generateTags(openingTag, closingTag-1,newCurTag,res)
		
	if closingTag == 0:
		res.append(curTag)
		print("res: ", res)
		print("\n")
