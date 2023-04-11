

class GPIO_Handler:
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
