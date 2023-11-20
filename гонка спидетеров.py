Zoom_Speed = int(input()) # корость зума
Flash_Speed = int(input()) # скорость флеша
if Zoom_Speed > Flash_Speed: # если зум быстрее флеша - флеш проиграет
    print("no")
elif Flash_Speed > Zoom_Speed: # если флеш быстрее зума - флеш выиграет
    print("yes")
else:  # если скорость флеша и зума одинакова то выиграет тот на чьей стороне будет удача
    print("don t know")
