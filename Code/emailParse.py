import email
from email import message_from_file as mf
import os
import pandas as pd

dataPath = "D:\\python\\Choice\\Data"


def file_exists (f,projPath):
    """Checks if eml file exists"""
    return os.path.exists(os.path.join(projPath, f))

def fileJoin(f,projPath):
    return os.path.join(projPath, f)

def main(dataPath):
    table=[]
    row=[]
    files = os.listdir(dataPath)
    for file in files:
        if file_exists(file,dataPath):
            try:
                message=mf(open(fileJoin(file,dataPath)))
                stIndex=message['subject'].index("(")
                endIndex=message['subject'].index(")")
                
                row.append(message['subject'][0:stIndex])
                row.append(message['subject'][stIndex+1:endIndex])
            except:
                row=["Null","Null"]
            finally:
                #print(row)
                table.append(row)
                row=[]
    finalFrame = pd.DataFrame(table)
    finalFrame =finalFrame.rename(columns={0: "Trip", 1: "CONFIRMATION NUMBER"})
    finalFrame.to_csv("D:\\python\\choice\\output\\conf.csv",index=False)

    
        

    
    return True

if __name__ == "__main__":
    main(dataPath)

