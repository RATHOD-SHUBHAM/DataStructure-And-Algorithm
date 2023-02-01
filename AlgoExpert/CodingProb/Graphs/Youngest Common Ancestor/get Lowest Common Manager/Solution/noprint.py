def getLowestCommonManager(topManager, reportOne, reportTwo):
    commonManager, empCount = getCommonManager(topManager, reportOne, reportTwo)
    return commonManager

# dfs
def getCommonManager(manager, empOne, empTwo):
    emp_count = 0

    # check if this manager is common for both employee by going through his list of employee
    for emp in manager.directReports:
        new_manager = emp
        emp_name , emp_cnt = getCommonManager(new_manager, empOne, empTwo)

        # if there is emp_name, then he is the common manager
        if emp_name is not None:
            # return both since function call  expect 2 value
            return (emp_name , emp_cnt)

        # if he is not the manager with 2 emplyee but has one of the employee
        # then increse emp count of current manager as well
        emp_count += emp_cnt

    # once we are done with all the employee
    # check if manager is one of the employee we are looking for
    if manager == empOne or manager == empTwo:
        emp_count += 1

    # return manager name, if both the employee is found
    # else return None
    commonManager = manager if emp_count == 2 else None

    return (commonManager, emp_count)

        

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
