import argparse
import matplotlib.pyplot as plt

DEF_P = 0.7 # Default max contentration
DEF_X0 = 0.10 # Default initial condition
DEF_ST = 0.001 # Default Step size
K = 0.04

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-P", "--concentration",
                        help="Max concentration")
    parser.add_argument("-x", "--init",
                        help="Initial concentration")
    parser.add_argument("-s", "--step", help="Step")

    args = parser.parse_args()

    P = float(args.concentration) if args.concentration is not None else DEF_P
    x0 = float(args.init) if args.init is not None else DEF_X0
    h = float(args.step) if args.step is not None else DEF_ST

    x_axis, y_axis = range(10000), [x0]
    for i in range(9999):
        x_prev = y_axis[-1]
        x = h * K * (P - x_prev) + x_prev
        y_axis.append(x)

    plt.plot(y_axis)
    plt.title('Graphic')
    plt.show()
