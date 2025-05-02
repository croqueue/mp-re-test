from machine import Pin
from utime import sleep, sleep_ms
from rotary_irq_rp2 import RotaryIRQ


pin = Pin("LED", Pin.OUT)
rotary_encoder = RotaryIRQ(
    15,     # clock pin
    14,     # data pin
    min_val=0,
    max_val=19,
    incr=1,
    reverse=False,
    range_mode=RotaryIRQ.RANGE_WRAP, # RANGE_UNBOUNDED and RANGE_BOUNDED
    pull_up=False,
    half_step=False,
    invert=False    
)

def poll_encoder():
    print(f'encoder value: {rotary_encoder.value()}')


rotary_encoder.add_listener(poll_encoder)

while True:
    try:
        print('still going...')
    except KeyboardInterrupt:
        rotary_encoder.remove_listener(poll_encoder)
        break

    sleep_ms(1024)

print('i guess thats it?')

# print("LED starts flashing...")
# while True:
#     try:
#         pin.toggle()
#         sleep(1) # sleep 1sec
#     except KeyboardInterrupt:
#         break
# pin.off()
# print("Finished.")
