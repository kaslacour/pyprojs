
from docx2pdf import convert
import os

def main():
    thisDir = os.path.dirname(__file__)
    os.chdir(thisDir)
    for name in os.listdir(thisDir):
        name_no_extension, extension = os.path.splitext(name)
        if extension == ".docx":
            inputFile = name
            outputFile = name_no_extension + ".pdf"
            if outputFile in os.listdir(thisDir):
                continue
            with open(outputFile, "w") as file:
                file.close
            convert(inputFile, outputFile)
    pass


if __name__ == "__main__":
    main()
