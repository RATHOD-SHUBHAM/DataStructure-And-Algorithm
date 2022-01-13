# Time = O(n) , n = number of employees
# Space = O(d) , d = depth of tree

def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    return getManager(topManager,reportOne, reportTwo).lowestCommonManager


def getManager(manager,empOne, empTwo):
	
	emp_Count = 0 # this name has to match with class name
	
	for emp in manager.directReports:
		print("manager direct emp are: ",manager.name)
		print("employees are: ",emp.name)
		print("\n")
		emp_Info = getManager(emp, empOne, empTwo)
		print("here")
		# if we found a manager
		if emp_Info.lowestCommonManager is not None:
			return emp_Info
		
		emp_Count += emp_Info.emp_Count
	
	print("jump here")
	print("manager.name : ",manager.name)
	# if the cur emp is a employee we are looking for
	if manager == empOne or manager == empTwo:
		emp_Count += 1
	
	print("emp count: ",emp_Count)
	lowestCommonManager = manager if emp_Count == 2 else None
	
	return OrgInfo(lowestCommonManager, emp_Count)
# after adding to my orgInfo . control automatically return to emp_info


class OrgInfo:
	def __init__(self,lowestCommonManager, emp_Count):
		self.lowestCommonManager = lowestCommonManager
		print("lowestCommonManger: ",self.lowestCommonManager)
		self.emp_Count = emp_Count
		print("emp count : ",self.emp_Count)
		
		
# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
