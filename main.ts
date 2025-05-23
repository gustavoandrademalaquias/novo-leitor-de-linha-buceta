//  0: preto
//  1: cor
/** 

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



 */
let motor_esquerda = robotbit.Motors.M1A
let motor_direita = robotbit.Motors.M1B
let max_speed = 200
let normal_speed = 150
function verificar(): number[] {
    let leitor_esquerda = pins.digitalReadPin(DigitalPin.P1)
    let leitor_direita = pins.digitalReadPin(DigitalPin.P2)
    basic.clearScreen()
    basic.showString("" + leitor_esquerda + ("" + leitor_direita))
    return [leitor_esquerda, leitor_direita]
}

/** 
    if esquerda == 1 and direita == 1:
        robotbit.motor_run(
            motor_direita,
            -normal_speed
        )
        robotbit.motor_run(
            motor_esquerda,
            -normal_speed
        )
 
 */
basic.forever(function on_forever() {
    let [esquerda, direita] = verificar()
    if (esquerda == 1) {
        // detectou linha na esquerda
        // parar motor direito pra esteira ir p esquerda
        robotbit.MotorRun(motor_direita, max_speed)
        robotbit.MotorRun(motor_esquerda, 0)
    }
    
    if (direita == 1) {
        robotbit.MotorRun(motor_esquerda, max_speed)
        robotbit.MotorRun(motor_direita, 0)
    }
    
    if (esquerda == 0 && direita == 0) {
        robotbit.MotorRun(motor_direita, normal_speed)
        robotbit.MotorRun(motor_esquerda, normal_speed)
    }
    
})
