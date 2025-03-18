import wmi

donne = wmi.WMI()
for nom_os in donne.Win32_OperatingSystem():
    print(nom_os.Caption)