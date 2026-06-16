devir = 9500
motor_sicakligi = 95
if motor_sicakligi >= 110:
    print("Motoru durdur.")
if motor_sicakligi <=110 and devir >= 12000:
    print("REv limiti, vites yukselt")
if motor_sicakligi <=110 and devir <= 12000:
    print("hersey normal")
