import numpy as np
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from module.experiments_comp.select_model import model_select_ver3



def experiment_hist_ver2():
    """
    複数のネットワークの次数分布ヒストグラムを同時に表示します。
    - ネットワークのサイズは共通
    - サイドバーでパラメータを選択、チェックボックスで生成
    - チェックボックス数とネットワーク数が一致しない場合は警告表示
    - ラベルにネットワーク名とパラメータを表示
    """
    st.header("次数分布")
    st.markdown(
        """
        - 複数のネットワークのヒストグラムを同時に表示します。
        - ネットワークのサイズは各ネットワークで共通です。
        - サイドバーでパラメータを選択し、チェックボックス☑を入れてください。
        - 用意するネットワークの個数とチェックボックスの数が同じ場合にのみヒストグラムが表示されます。
        """
    )
    
    st.divider()

    # サイドバーで設定
    network_count = st.sidebar.slider(
        "用意するネットワークの数", 1, 5, 1, key='n_m'
    )
 
    
    col1,col2=st.columns([3,2])
    with col1:
        network_size = st.number_input(
        "各ネットワークのサイズ", 10, 3000, 500, step=10, key='n_s'
        )

    with col2:
        st.write("")

    networks = []
    labels = []
    max_degree = 0
    abbr_map = {
        "random network": "RN",
        "watts-strogatz model": "WS",
        "Barabasi-Albert model": "BA",
        "Holme-Kim model":"HK",
        "ex random walk": "exRW"
    }
    
    

    # モデル選択と生成
    for i in range(network_count):
        # model_selectで生成
        G = model_select_ver3(N=network_size, index=i)
        if G is not None:
            networks.append(G)
            # モデル名と略称取得
            full_name = st.session_state.get(f"{i}_model", "Unknown")
            abbr = abbr_map.get(full_name, full_name)

            # パラメータ取得
            if full_name == "random network":
                p = st.session_state.get(f"{i}_p", None)
                params = f"p={p:.2f}" if p is not None else ""
            elif full_name == "watts-strogatz model":
                k = st.session_state.get(f"{i}_k", None)
                p = st.session_state.get(f"{i}_ws_p", None)
                params = f"K={k}, p={p:.2f}" if (k is not None and p is not None) else ""
            elif full_name == "Barabasi-Albert model":
                m = st.session_state.get(f"{i}_ba_m", None)
                params = f"m={m}" if m is not None else ""
            elif full_name == "Holme-Kim model":
                m = st.session_state.get(f"{i}_rw_m", None)
                p = st.session_state.get(f"{i}_rw_p", None)
                params = f"m={m}, p={p:.2f}" if (m is not None and p is not None) else ""                
            elif full_name == "ex random walk":
                p = st.session_state.get(f"{i}_srw_p", None)
                l = st.session_state.get(f"{i}_srw_l", None)
                params = f"p={p:.2f}" if p is not None else ""
            else:
                params = ""

            # ラベル作成
            label = f"{abbr} ({params})" if params else abbr
            labels.append(label)

            # 最大次数更新
            degrees = [d for _, d in G.degree()]
            max_degree = max(max_degree, max(degrees))

    # チェック数と生成数の確認
    if len(networks) != network_count:
        st.warning("⚠️ すべてのネットワークが生成されていません。チェックボックスを確認してください。")
        return

    # ヒストグラム生成ボタン
    if st.button("次数分布を生成", key='gene_hist'):
        bins = range(0, max_degree + 6)
        fig, ax = plt.subplots(figsize=(8, 7))

        for G, label in zip(networks, labels):
            degrees = [d for _, d in G.degree()]
            hist, _ = np.histogram(degrees, bins=bins, density=True)
            ax.plot(bins[:-1], hist, label=label)

        ax.set_xlabel('Degree')
        ax.set_ylabel('frequency')
        ax.grid(True)
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        
        handles, legend_labels = ax.get_legend_handles_labels()
        if handles:  # 凡例対象がある場合のみ
            ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        
        st.pyplot(fig)
    return None

