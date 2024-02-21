# -*- coding: utf-8 -*-
"""Hands-on Activity 4.1_GALAPIA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RnQtCuLsHXtheiwER29VhsCeACOQvlb3

**Hands-on Activity 4.1: The Tower of Hanoi Problem**

Xander Sam E. Galapia
"""

def TOH(n,  Sour, Aux , Des):

  if n==1:
      print("Move Disk" , n," from ", Sour ," to ",Des)
  else:
      TOH(n-1,Sour,Des,Aux);
      print("Move Disk", n ," from ", Sour ," to ",Des)
      TOH(n-1,Aux,Sour,Des);

n = (int(input("How many Disk:")))
TOH(n, '1st' , '2nd' , '3rd' )

"""![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAL7CAYAAAAh7vucAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAB3MSURBVHhe7d1PjlNnvsfhqruEtG5E1AQYdLbAACyxBKQMWoqQGCMyyIxcWAC5YRIxAGWMhHqGhJQNIJkMUO8gPQBCC5Srzhbq8przVk5M/bGrvvb59zzSUb3lqnK5DAd/6neOze7eezsAAMT8V/MWAIAQgQUAECawAADCBBYAQJjAAgAIE1gAAGECCwAgzOtgAb0wn8+b1WbNZrNmBeNlf+qewDqGv6SwHfY1yLE/dc8hQgCAMIEFABAmsAAAwgQWAECYwAIACBNYAABhAgsAIExgAQCECSwAgDCBBQAQJrAAAMIEFgBAmMACAAgTWAAAYQILACBMYAEAhAksAIAwgQUAECawAADCBBYAQJjAAgAIE1gAAGECCwAgTGABAIQJLACAMIEFABAmsAAAwgQWAECYwAIACBNYAABhAgsAIExgAQCECSwAgDCBBQAQJrAAAMIEFgBAmMACAAgTWAAAYQILACBMYAEAhAksAIAwgQUAECawAADCBBYAQJjAAgAIE1gAAGECCwAgTGABAIQJLACAMIEFABAmsAAAwgQWAECYwAIACBNYAABhAgsAIExgAQCECSwAgDCBBQAQJrAAAMIEFgBAmMACAAgTWAAAYQILACBMYAEAhAksAIAwgQUAECawAADCBBYAQJjAAgAIE1gAAGECCwAgTGABAIQJLACAMIEFABAmsAAAwgQWAECYwAIACBNYAABhAgsAIExgAQCECSwAgDCBBQAQJrAAAMIEFgBAmMACAAgTWAAAYQILACBMYAEAhAksAIAwgQUAECawAADCBBYAQJjAAgAIE1gAAGECCwAgTGABAIQJLACAMIEFABAmsAAAwgQWAECYwAIACBNYAABhAgsAIExgAQCECSwAgDCBBQAQJrAAAMIEFgBAmMACAAgTWAAAYQILACBMYAEAhAksAIAwgQU99eLFi52zZ8827wEwJAKL3qlhce3atcW2qjt37uxvR3n69OnO5cuXm/dOp1xXua3trVwGwLQJLACAMIFFr5SJ1f3794+dQvXF119/vfPmzZv97cGDB4vLXr9+3XwGAFMksOiVx48fL7bDlHA56JBc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HhQgw77UPYcIAQDCBBYAQJjAAgAIE1gAAGECCwAgTGABAIQJLACAMIEFABAmsAAAwgQWAECYwAIACBNYAABhAgsAIExgAQCECSwAgDCBBQAQJrAAAMIEFgBAmMACAAgTWAAAYQILACBMYAEAhAksAIAwgQUAECawAADCBBYAQJjAAgAIE1gAAGECCwAgTGABAIQJLACAMIEFABAmsAAAwgQWAECYwAIACBNYAABhAgsAIExgAQCECSwAgDCBBQAQJrAAAMIEFgBAmMACAAgTWAAAYQILACBMYAEAhAksAIAwgQUAECawAADCBBYAQJjAAgAIE1gAAGECCwAgTGABAIQJLACAMIEFABAmsAAAwgQWAECYwAIACBNYAABhAgsAIExgAQCECSwAgDCBBQAQJrAAAMIEFgBAmMACAAgTWAAAYQILACBMYAEAhAksAIAwgQUAECawAADCBBYAQJjAAgAIE1gAAGECCwAgTGABAIQJLACAMIEFABAmsAAAwgQWAECYwAIACBNYAABhAgsAIExgAQCECSwAgDCBBQAQJrAAAMIEFgBAmMACAAgTWAAAYQILACBMYAEAhAksAIAwgQUAECawAADCBBYAQJjAAgAIE1gAAGECCwAgTGABAIQJLACAMIEFABAmsAAAwgQWAECYwAIACBNYAABhAgsAIExgAQCECSwAgDCBBQAQJrAAAMIEFgBAmMACAAgTWAAAYQILACBMYAEAhAksAIAwgQUAECawAADCBBYAQJjAAgAIE1gAAGECCwAgTGABAIQJLACAMIEFABAmsAAAwgQWAECYwAIACBNYAABhAgsAIExgAQCECSwAgDCBBQAQJrAAAMIEFgBAmMACAAgTWAAAYQILACBMYAEAhAksAIAwgQUAECawAADCBBYAQJjAAgAI2917r1n30ve7nzYrNuXbvd+aFXRrPp83q82azWbNCsbJvtQ9EywAgLDeTLBMqvrHZItt81s3ZNiXutf5BKuElbjqp/pn488IANbTWWB50B4ef14AsJrODhF6sB4uhw45yO+ff9Gsxu+TX39pVtBPDhF2b+uBJayGT2AxpZhaleiiTwRW9zyLEAAgzASLtZlgTZvp1dFMsqg83m1X3x6bBBZrE1jTJa5WI7KmxeNav3X1mCWwWJvAmiZxtTqBNW4ex4ZtW49hAivkf3b+r1l97H93/rtZ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)

Rules:
1. One Disk at a time
2. The disk can't be move if there is an upper disk
3. Larger/Higher disk can't be put above smaller disk

As there is only 2 disk here we only need to move the disk 1 to 2nd, disk 2 to 3rd, then the disk 1 to 3rd.
"""

def TOH(n,  Sour, Aux , Des):

  if n==1:
      print("Move Disk" , n," from ", Sour ," to ",Des)
  else:
      TOH(n-1,Sour,Des,Aux);
      print("Move Disk", n ," from ", Sour ," to ",Des)
      TOH(n-1,Aux,Sour,Des);

n = (int(input("How many Disk:")))
TOH(n, '1st' , '2nd' , '3rd' )

"""![image.png](data:image/png;base64,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BgAAgCRCNwAAACQRugEAACCJ0A0AAABJhG4AAABIInQDAABAEqEbAAAAkgjdAAAAkEToBgAAgCRCNwAAACQRugEAACCJ0A0AAABJhG4AAABIInQDAABAEqEbAAAAkgjdAAAAkEToBgAAgCRCNwAAACQRugEAACCJ0A0AAABJhG4AAABIInQDAABAEqEbAAAAkgjdAAAAkEToBgAAgCRCNwAAACQRugEAACCJ0A0AAABJhG4AAABIInQDAABAEqEbAAAAkgjdAAAAkEToBgAAgCRCNwAAACQRugEAACCJ0A0AAABJhG4AAABIInQDAABAEqEbAAAAkgjdAAAAkEToBgAAgCRCNwAAACQRugEAACCJ0A0AAABJhG4AAABIInQDAABAEqEbAAAAkgjdAAAAkEToBgAAgCRCNwAAACQRugEAACCJ0A0AAABJhG4AAABIInQDAABAEqEbAAAAkgjdAAAAkEToBgAAgCRCNwAAACQRugEAACCJ0A0AAABJhiv71WUmGA6HdakZVvfyaXIf2LdvX+P7FPPZsmVLY/+Pe/fureYHsBGa/B1xXLJ8HJu2w6k7L6tL3ffBjufrEvMSutfhiw2hu5uEbmBZCd395th0c/UpbI8SvBfjKBEAAIBVxcmGvp5waILQDQAAsA6hk3kJ3QAAAGsQuA+wHuYjdAMAAEASoRsAAACSCN0AAACQROgGAACAJEI3AAAAJBG6AQAAIInQDQAAAEmEbgAAAEgidAMAAEASoRsAAACSCN0AAACQROgGAACAJEI3AAAAJBG6AQAAIInQDQAAAEmEbgAAAEgidAMAAEASoRsA2DQnnHDC4Oabb64fAbTTBzuer0v9Zj3MR+gGAObyxRdfDJ544okqOJfhmmuuGbz88sv1FNP56quv6tJ8YjkefPDBwSWXXFItwznnnDO45557Bm+++WY9BcDi+h44Be75Cd0AbKoIbWo6l8+77747uPbaawd33XXX4Iwzzhicf/751fjVV18d/Pu//3s91QHbtm2rwnCGWI5zzz138PDDDw/efvvtajk++uijweOPPz644YYb6qkOiP0sliP2OQCmJ3AvRugGYGYlvEwaImDN4uuvv1bTuWRifd90001VyI2g/cILLwyefPLJavzOO+8M7r333nrKAxbdvmv5+c9/Xs0/liPeO5Yjxg888MDgmGOOqac6oCxH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)

**1. Explain the programming paradigms/techniques (like recursion or dynamic programming) that you used to solve the given problem.**



**2. Provide screenshots of the techniques and provide a quick analysis.**

The recursion that happened here is that the disk 1 and 2 is moved to 3rd as 3-1 = 2 so we have to move the disk to 2nd and the n==1 will move the largest disk/disk 3 to the 3rd. And move the disk 1 to 1st then move the 2nd disk to 3rd. Then the If statemenet will occur to the disk 1 moving it to the destination/3rd
"""