


class GPIO_Handler:

    def match(msg):
        import RPi.GPIO as GPIO
        import time

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        #GPIO.setup(SWITCH1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        GPIO.setup(2,GPIO.OUT)
        GPIO.output(2,False)
        Joined_msg = ''
        splitmsg = msg.split()
        Joined_msg = Joined_msg.join(splitmsg[:-1])
        print(Joined_msg)
        if(Joined_msg.lower() == 'turnonled'):
            LED_NO = int(splitmsg[-1])
            print(LED_NO)
            GPIO.output(LED_NO,True)
            print('->',msg)
            s = 'LED no '+str(LED_NO)+' turned on'
            return s
        else:
            print('Wrong Command')
            return 'Wrong Command'
