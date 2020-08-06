#*******************************************************************************
#Name : Prakash GM
#Function : Isolating Face Area
#Organisation : Individual
#********************************************************************************

import ansa
from ansa import*
deck=constants.OPENFOAM
from ansa import guitk
from ansa import constants
 
def Isolate_face_area():
	TopWindow = guitk.BCWindowCreate("Display faces Less than", guitk.constants.BCOnExitDestroy)
	BCGridLayout_1 = guitk.BCGridLayoutCreate(TopWindow, 1, 2)
	BCLabel_1 = guitk.BCLabelCreate(TopWindow, "Input")
	BCLineEdit_1 = guitk.BCLineEditCreate(TopWindow, "1")
	bclist=[BCLineEdit_1]
	BCDialogButtonBox_1 = guitk.BCDialogButtonBoxCreate(TopWindow)
    guitk.BCGridLayoutAddWidget(BCGridLayout_1,BCLabel_1,0,0,guitk.constants.BCAlignVCenter)
    guitk.BCGridLayoutAddWidget(BCGridLayout_1,BCLineEdit_1,0,0,guitk.constants.BCAlignVCenter)
    guitk.BCWindowSetAcceptFunction(TopWindow,main,bclist)
    guitk.BCWindowSetRejectFunction(TopWindow,sub,0)
    guitk.BCShow(TopWindow)




def main(w,bclist):
	area_text=guitk.BCButtonLineEditGetText(bclist[0])
	area_fl=float(area_text)
	faces=base.CollectEntities(deck,None,"FACE",False)
	print(faces)
	print(type(faces))
	print(len(faces))
	for e_f in faces:
		area=base.GetFaceArea(e_f)
		hidden_list=[]
		if area>area_fl:
			hidden_list.append(e_f)
			base.Not(hidden_list)

def sub():
	print("The Process Canceled")


Isolate_face_area()