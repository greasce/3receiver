accelerate = 0

def on_received_number(receivedNumber):
    global accelerate
    while receivedNumber > 0:
        accelerate += 1
    while receivedNumber < 0:
        accelerate += -1
radio.on_received_number(on_received_number)

def on_forever():
    global accelerate
    while accelerate > 0:
        accelerate = 1
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
            kitronik_motor_driver.MotorDirection.FORWARD,
            50)
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
            kitronik_motor_driver.MotorDirection.FORWARD,
            50)
    while accelerate < 0:
        accelerate = -1
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
            kitronik_motor_driver.MotorDirection.REVERSE,
            50)
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
            kitronik_motor_driver.MotorDirection.FORWARD,
            50)
    while accelerate == 0:
        kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR1)
        kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR2)
basic.forever(on_forever)

def on_forever2():
    radio.set_group(99)
basic.forever(on_forever2)
