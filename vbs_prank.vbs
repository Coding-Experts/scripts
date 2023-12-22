Msgbox "Your computer has been infected by a malware",16,"Warning!"
dim x,yes,no
x=Msgbox("Virus has infected hard drive (C:). Deletion of the virus will require complete formatting of hard drive (C:). Would you like to format hard drive (C:) ?",52,"Warning!")
if x=6 then
dim box
box=Msgbox("Hard drive (C:) formatting complete. In order to function correctly your computer must restart, would you like to restart now ?",36,"Formatting has been completed")
if box=6 then
Msgbox "Fatal error, code 08x48631643.B-7",16,"ERROR"
Msgbox "Just kidding, this was all a joke. Follow coding.experts_",64,"Made by coding.experts_"
end if
if box=7 then
Msgbox "Fatal error, code 08x48631643.B-7",16,"ERROR"
Msgbox "Just kidding, this was all a joke. Follow coding.experts_",64,"Made by coding.experts_"
end if
end if
if x=7 then
Msgbox "Fatal error, code 08x48631643.B-7",16,"ERROR"
Msgbox "Just kidding, this was all a joke. Follow coding.experts_",64,"Made by coding.experts_"
end if
