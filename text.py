import os
libs=["AutomaticTrajectoryDrawing.py","BaseNumberCompute.py","BMI.py","GovermentWordcloud.py",
      "hollandRadarDraw.py","KochSnow.py","MonteCarloMethod.py","PythonDraw.py","RoseDraw.py",
      "SevenDightDraw.py","SPGanalyse.py","TempStr.py","ThePowerOfDayup.py","ThirdPartyLibrariesInstsll.py",
      "Txtprocess.py","WordTimeCollect.py"]
try:
    for lib in libs:
        os.system("pyinstaller "+lib)
        print("successful")
except:
    print("failed somehow")