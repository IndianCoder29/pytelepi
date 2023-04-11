

class GPIO_Handler:
    def InitPI():
        PINS = [1,2,3,4,5,6,7,8,9,10]
        INIT_STATUS = ''
        for pin in PINS:
            print('-->Pin no:',pin,'set as output')
            INIT_STATUS = INIT_STATUS + 'Pin no: ' +str(pin) +' set as output\n'
        print('---->Pins are initialized')
        return INIT_STATUS


    def match(msg):
        Joined_msg = ''
        splitmsg = msg.split()
        Joined_msg = Joined_msg.join(splitmsg[:-1])
        print(Joined_msg)
        if(Joined_msg.lower() == 'turnonled'):
            LED_NO = int(splitmsg[-1])
            print(LED_NO)
            print('->',msg)
            s = 'LED no '+str(LED_NO)+' turned on'
            return s
        else:
            print('Wrong Command')
            return 'Wrong Command'




