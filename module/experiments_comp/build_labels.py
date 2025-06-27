
def build_labels(session_state, network_count):

    abbr_map = {
            "random(erdős-Rényi) model":"eR_RN",
            "random(gilbert) model":"G_RN",
            "watts-strogatz model":"WS",
            "Barabasi-Albert model":"BA",
            "Holme-Kim model":"HK",
            "ex random walk model":"ex_RW",
        }
    
    param_config = {
            "random(erdős-Rényi) model": [
                ("er_m",   "m",  "{}")
            ],        
        
            "random(gilbert) model": [
                ("gil_p",   "p",  "{:.2f}")
            ],
            "watts-strogatz model": [
                ("ws_k",    "K", "{}"),
                ("ws_p", "p", "{:.2f}")
            ],
            "Barabasi-Albert model": [
                ("ba_m", "m", "{}")
            ],
            "Holme-Kim model": [
                ("hk_m", "m", "{}"),
                ("hk_p", "p", "{:.2f}")
            ],
            "ex random walk model": [
                ("srw_p", "p", "{:.2f}")
            ]
        }
    
    labels = []

    for i in range(network_count):
        # 「i_model」のキーからモデル名（フルネーム）を取得
        full_name = session_state.get(f"{i}_model", "Unknown")

        # ─略称を取得。無ければ full_name を略称として使う
        abbr = abbr_map.get(full_name, full_name)

        # param_config から、そのモデルに紐づくパラメータ設定リストを取得
        configs = param_config.get(full_name, [])

        # 各パラメータ定義(サフィックス, 表示名, フォーマット)ごとに
        # session_state から値を取り出し、文字列化してリストに追加
        params_list = []
        for suffix, param_name, fmt in configs:
            val = session_state.get(f"{i}_{suffix}", None)
            if val is not None:
                params_list.append(f"{param_name}={fmt.format(val)}")

        # カンマ区切りでまとめる
        params = ", ".join(params_list)

        # パラメータがあれば "略称 (パラメータ)"、なければ略称だけ
        if params:
            label = f"{abbr} ({params})"
        else:
            label = abbr

        labels.append(label)

    return labels