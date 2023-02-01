def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    emp_Info, empCount = getManager(topManager,reportOne, reportTwo)
    return emp_Info


# DFS
def getManager(manager,empOne, empTwo):
	
	emp_Count = 0 # this name has to match with class name
	
	for emp in manager.directReports:
		# print("manager direct emp are: ",manager.name)
		# print("employees are: ",emp.name)
		# print("\n")
		emp_Info, empCount = getManager(emp, empOne, empTwo)
		# print("emp info is: ",emp_Info)
        # print("emp count is: ",empCount)
		# print("here")
		# if we found a manager
		if emp_Info is not None:
			return emp_Info, empCount
		
		emp_Count += empCount
    #     print("moving back to for")
    #     print("\n")
	
	# print("\n")
    # print("jump here out")
	# print("manager.name : ",manager.name)
	# if the cur emp is a employee we are looking for
	if manager == empOne or manager == empTwo:
		emp_Count += 1
	
	# print("emp count: ",emp_Count)
	emp_Info = manager if emp_Count == 2 else None
	# print("\n")
	return (emp_Info, emp_Count)

		
		
# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

