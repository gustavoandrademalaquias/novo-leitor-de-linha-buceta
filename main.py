# 0: preto
# 1: cor

'''

motorA = robotbit.Motors.M1A
motorB = robotbit.Motors.M1B

def on_forever():
    robotbit.motor_run(motorA, 150)
    robotbit.motor_run(motorB, 150)
    basic.pause(2500)
    robotbit.motor_run(motorA, 0)
    robotbit.motor_run(motorB, 0)
    basic.pause(2500)
basic.forever(on_forever)


'''

motor_esquerda = robotbit.Motors.M1A
motor_direita = robotbit.Motors.M1B
max_speed = 200
normal_speed = 150

def verificar():
    leitor_esquerda = pins.digital_read_pin(DigitalPin.P1)
    leitor_direita = pins.digital_read_pin(DigitalPin.P2)

    basic.clear_screen()
    basic.show_string(str(leitor_esquerda) + str(leitor_direita))

    return leitor_esquerda, leitor_direita



def on_forever():
    esquerda, direita = verificar()

    if esquerda == 1:
        #detectou linha na esquerda
        #parar motor direito pra esteira ir p esquerda
        robotbit.motor_run(
            motor_direita,
            max_speed
        )
        robotbit.motor_run(
            motor_esquerda,
            0
        )
        
    if direita == 1:
        robotbit.motor_run(
            motor_esquerda,
            max_speed
        )
        robotbit.motor_run(
            motor_direita,
            0
        )
        
    if esquerda == 0 and direita == 0:
        robotbit.motor_run(
            motor_direita,
            normal_speed
        )
        robotbit.motor_run(
            motor_esquerda,
            normal_speed
        )
'''
    if esquerda == 1 and direita == 1:
        robotbit.motor_run(
            motor_direita,
            -normal_speed
        )
        robotbit.motor_run(
            motor_esquerda,
            -normal_speed
        )
 '''       

basic.forever(on_forever)