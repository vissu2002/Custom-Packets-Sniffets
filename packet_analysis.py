import pandas as pd

def analyze_packets():
    try:
        df = pd.read_csv("packet.csv")

        top_src_ips = df['Source'].value_counts().head(5).to_dict()
        top_dst_ips = df['Destination'].value_counts().head(5).to_dict()
        top_protocols = df['Protocol'].value_counts().head(5).to_dict()

        return {
            "top_source_ips": top_src_ips,
            "top_destination_ips": top_dst_ips,
            "top_protocols": top_protocols
        }

    except FileNotFoundError:
        return {"error": "packet.csv not found."}
    except Exception as e:
        return {"error": str(e)}


