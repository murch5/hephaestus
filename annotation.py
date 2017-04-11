import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as collect
import pandas as pd

class annotation():


    def __init__(self, annotateList, target):
        self.targetAx = target
        self.annotationList = self.parseAnnotation(annotateList)
        self.annotationFileData = {}


        return

    def addAnnotation(self):

        return


    def addLineCollection(self,args):

        if self.annotationFileData.get(args["file"]) is None:
            print("booya")
            self.annotationFileData[args["file"]] = pd.read_table(args["file"])
            print(self.annotationFileData[args["file"]])

        lineCoord = list(zip(self.annotationFileData.get(args["file"])["x"],self.annotationFileData.get(args["file"])["y"]))
        print(lineCoord)
        lineCollection = collect.LineCollection(lineCoord, linewidths=args.get("lineWidths"), colors=args.get("colors"))
        self.targetAx.add_collection(lineCollection)

        return


    def addText(self,args):


        self.targetAx.annotate(s=args.get("text"),xy=args.get("xy"),xycoords=args.get("xycoords"),xytext=args.get("xytext"),textcoords=args.get("textcoords"),color=args.get("color"))

        return

    types = {"text": addText, "lineCollection": addLineCollection}

    def annotate(self):

        for x in self.annotationList:
           temp = annotation.types[x[0]](self,x[1])

        return
    def parseValue(self, valueStr):

        val = valueStr.split(".",1)
        valType = val[0]

        if valType=="i": #integer
            value = int(val[1])

        if valType == "ia": #integer array
            value = val[1].split("~")
            value = [int(i) for i in value]

        if valType == "f":  #float
            value = float(val[1])

        if valType == "fa": #float array
            value = val[1].split("~")
            value = [float(i) for i in value]

        if valType == "s": #string
            value = val[1]

        if valType == "p":  #file path
            value = val[1]



        return value

    def getValue(self,argName):

        return
    def parseAnnotation(self, annotateList):

        annotatePD = pd.Series(annotateList)
        annotate = []
        argName = []
        argVal = []

        if annotatePD.any():
            for i in annotatePD:

                if i != "0":
                    typeSplit = i.split("=", 1)
                    type = typeSplit[0]
                    args = typeSplit[1].split(":")
                    for y in args:
                        argParse = y.split("=")
                        argName.append(argParse[0])
                        argVal.append(self.parseValue(argParse[1]))

                    argSet = dict(zip(argName,argVal))
                    c = [type,argSet]

                    annotate.append(c)

        return annotate


