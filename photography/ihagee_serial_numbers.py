import csv
import pathlib
import matplotlib.pyplot as plt


def read_data(filename):
    result = list()
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        next(reader)
        for line in reader:
            result.append(tuple(line))
    return result


def lower_upper(models_data):
    years = dict()
    for start, end, model, type_id, size, low, high in models_data:
        if len(start) > 0:
            year = int(start)
            sn0, sn1 = years.get(year, (0, 0))
            if len(low) > 0:
                low = int(low)
                if sn0 > 0 and low < sn0 or sn0 == 0:
                    years[year] = (low, sn1)
                    sn0 = low
                if low > sn1:
                    years[year] = (sn0, low)

        if len(end) > 0:
            year = int(end)
            sn0, sn1 = years.get(year, (0, 0))
            if len(high) > 0:
                high = int(high)
                if sn0 == 0:
                    sn0 = high
                if high > sn1:
                    years[year] = (sn0, high)
    return years


def plot_intervals(models_data):
    plt.figure(num=f"Ihagee serial numbers - intervals", figsize=(10, 6), tight_layout=True)
    for start, end, model, type_id, size, low, high in models_data:
        if len(start) > 0 and len(end) > 0 and len(low) > 0 and len(high) > 0:
            plt.plot((int(start), int(end)), (int(low), int(high)), "k.-")
    plt.xlabel("Production year")
    plt.ylabel("Serial number")
    axes = plt.gca()
    axes.xaxis.set_major_formatter(plt.FormatStrFormatter("%d"))
    axes.yaxis.set_major_formatter(plt.FormatStrFormatter("%d"))


def plot_bounds(sn_bounds):
    production_years = sorted(sn_bounds.keys())
    plt.figure(num=f"Ihagee serial numbers - bounds", figsize=(10, 6), tight_layout=True)
    for yr in production_years:
        plt.plot((yr, yr), sn_bounds[yr], "k.-")
    plt.xlabel("Production year")
    plt.ylabel("Serial number")
    axes = plt.gca()
    axes.xaxis.set_major_formatter(plt.FormatStrFormatter("%d"))
    axes.yaxis.set_major_formatter(plt.FormatStrFormatter("%d"))


if __name__ == "__main__":
    p = pathlib.Path(".") / "data" / "Ihagee.csv"
    data = read_data(p)
    bounds = lower_upper(data)
    plot_bounds(bounds)
    plot_intervals(data)
    for b in sorted(bounds.keys()):
        print(b, bounds[b])
    plt.show()

