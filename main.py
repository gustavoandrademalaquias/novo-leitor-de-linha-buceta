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
    # verificar() == 1 significa que detectou a linha preta (ausência de luz), caso contrário, 0 significa qualquer cor.
    esquerda, direita = verificar()

    if esquerda == 1:
        # sensor esquerdo passou na linha
        robotbit.motor_run(motor_direita, max_speed)
        robotbit.motor_run(motor_esquerda, 0)
    elif direita == 1:
        #sensor direito passou na linha
        robotbit.motor_run(motor_esquerda, max_speed)
        robotbit.motor_run(motor_direita, 0)
    else:
        #sensores ok
        robotbit.motor_run(motor_direita, normal_speed)
        robotbit.motor_run(motor_esquerda, normal_speed)

    basic.pause(100)

basic.forever(on_forever)
