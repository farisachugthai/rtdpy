import matplotlib.pyplot as plt
import rtdpy
for pe in [100, 1000]:
    a = rtdpy.AD_hi_peclet(tau=1, peclet=pe, dt=.01, time_end=3)
    plt.plot(a.time, a.exitage, label=f"peclet={pe}")
plt.xlabel('Time')
plt.ylabel('Exit Age Function')
plt.legend()
plt.show()
