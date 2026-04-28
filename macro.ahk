; Script Quick Change PB by Mr.Rm19
; Gunakan tombol Q untuk mengaktifkan/matikan script

#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

Enabled := false

~Q:: ; Tekan Q untuk On/Off
Enabled := !Enabled
if (Enabled)
    SoundBeep, 750, 200 ; Bunyi beep tinggi saat ON
else
    SoundBeep, 500, 200 ; Bunyi beep rendah saat OFF
return

~LButton:: ; Klik Kiri Mouse
if (Enabled) {
    Sleep, 20 ; Jeda sebelum ganti
    Send, 3   ; Pindah ke pisau
    Sleep, 20 ; Jeda milidetik
    Send, 1   ; Pindah ke senjata utama
}
return