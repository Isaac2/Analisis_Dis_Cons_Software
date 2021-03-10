import math

def runTest(value):
    try:
        result = math.ceil(value)
        print(result)
    except:
        print("An error has ocurred")

#Right B I C E P tests
runTest(15.000000000001)
runTest(15.999999999999)
runTest(15.05)
runTest(15 + .05)
runTest(15.05 + 1 - 1)
runTest("15.05")
runTest(-15.05)
runTest(-15.000000000001)
runTest(-15.999999999999)
runTest(False)