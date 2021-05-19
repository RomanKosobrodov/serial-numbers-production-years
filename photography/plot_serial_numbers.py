from photography.serial_numbers import SERIAL_NUMBERS
import matplotlib.pyplot as plt
import numpy as np
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot serial numbers vs. production years")
    parser.add_argument("manufacturer", help="Manufacturer", type=str)
    args = parser.parse_args()
    m = args.manufacturer
    sn_tuple = SERIAL_NUMBERS[m.upper()]
    sn = np.array(sn_tuple)

    plt.figure(num=f"{m} serial numbers", figsize=(10, 6), tight_layout=True)
    if sn.shape[1] == 3:
        for year, start, end in sn:
            plt.plot((year, year), (start, end), "k-")
    else:
        plt.plot(sn[:, 0], sn[:, 1], "k.-")
    plt.xlabel("Production year")
    plt.ylabel("Serial number")
    axes = plt.gca()
    axes.xaxis.set_major_formatter(plt.FormatStrFormatter("%d"))
    axes.yaxis.set_major_formatter(plt.FormatStrFormatter("%d"))
    plt.show()


