let accelerate = 0
radio.onReceivedNumber(function (receivedNumber) {
    while (receivedNumber > 0) {
        accelerate += 1
    }
    while (receivedNumber < 0) {
        accelerate += -1
    }
})
basic.forever(function () {
    while (accelerate > 0) {
        accelerate = 1
        kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor1, kitronik_motor_driver.MotorDirection.Forward, 50)
        kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor2, kitronik_motor_driver.MotorDirection.Forward, 50)
    }
    while (accelerate < 0) {
        accelerate = -1
        kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor1, kitronik_motor_driver.MotorDirection.Reverse, 50)
        kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor2, kitronik_motor_driver.MotorDirection.Forward, 50)
    }
    while (accelerate == 0) {
        kitronik_motor_driver.motorOff(kitronik_motor_driver.Motors.Motor1)
        kitronik_motor_driver.motorOff(kitronik_motor_driver.Motors.Motor2)
    }
})
basic.forever(function () {
    radio.setGroup(99)
})
