from gpiozero import LED
import time 

red_led = LED(3)
yellow_led = LED(4)
green_led = LED(17)
x=0

def stop_light(traffic_status):
    red,yellow,green = traffic_status
    if (traffic_status[red]):
         red_led.on()
    else :
         red_led.off()
         
    if (traffic_status[yellow]):
         yellow_led.on()
    else :
         yellow_led.off()
        
    if (traffic_status[green]):
         green_led.on()
    else :
         green_led.off() 


def main():
    print("Welcome To The STEAM Clown Makey Bot")
    traffic_status = {'red_LED' : 0, 'yellow_LED' : 0, 'green_LED' : 0}
    
    while True:
        x=(input("color >>> "))
        if x=="green":
            traffic_light_status = {'red_LED' : 0, 'yellow_LED' : 0, 'green_LED' : 1}
            #green_led.on()
            print(traffic_light_status)
        if x=="red":
            traffic_light_status = {'red_LED' : 1, 'yellow_LED' : 0, 'green_LED' : 0}
            #red_led.on()
            print(traffic_light_status)
        if x=="yellow":
            traffic_light_status = {'red_LED' : 0, 'yellow_LED' : 1, 'green_LED' : 0}
            #yellow_led.on()
            print(traffic_light_status)
        if x=="q":
            traffic_light_status = {'red_LED' : 0, 'yellow_LED' : 0, 'green_LED' : 0}
            break
        stop_light(traffic_light_status)
main()

