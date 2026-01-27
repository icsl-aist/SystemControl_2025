import matplotlib.pyplot as plt

def plot_set(ax, xlabel, ylabel, title=None):
    """
    matplotlibのAxesオブジェクト (ax) に、
    ラベル、グリッド、凡例などをまとめて設定する関数。
    """
    
    # 1. X軸とY軸のラベルを設定
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    
    # 2. タイトルが指定されていれば設定
    if title:
        ax.set_title(title)
    
    # 3. グリッド線（目盛り線）を表示
    ax.grid(True)
    
    # 4. 凡例（はんれい）が設定されている場合のみ表示する
    # (ax.plot(..., label='...')) のように label が指定されているかチェック
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(loc='best')
