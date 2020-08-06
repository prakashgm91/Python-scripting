#*******************************************************************************
#Name : Prakash GM
#Function : Isolating Face Area
#Organisation : Individual
#********************************************************************************

import ansa
from ansa import*
deck=constants.OPENFOAM

def main():
	faces=base.CollectEntities(deck,None,"FACE",False)
	print(faces)
	print(type(faces))
	print(len(faces))
	for e_f in faces:
		area=base.GetFaceArea(e_f)
		hidden_list=[]
		if area>10:
			hidden_list.append(e_f)
			base.Not(hidden_list)

main()