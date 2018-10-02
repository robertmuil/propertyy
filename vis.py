import matplotlib.pyplot as pp
import seaborn


def plot_transactions(df, by='postcode', n_groups=10):
    fig = pp.figure();
    ax = pp.subplot()

    for grp in df[by].value_counts()[0:n_groups].index:
        print(grp)
        print(df[df[by]==grp].shape)
        df[df[by] == grp].plot.line(ax=ax, y='price_paid', x='deed_date', marker='x', label=grp)