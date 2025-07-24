from flask import Flask, render_template, request, send_file, redirect, url_for, flash, jsonify
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly
import json
from sniffer import capture_packets
from packet_analysis import analyze_packets

app = Flask(__name__)
app.secret_key = "packet_sniffer_secret"

CSV_FILE = "packet.csv"

@app.route('/')
def index():
    graphJSON = None
    packets = []

    if os.path.exists(CSV_FILE):
        try:
            df = pd.read_csv(CSV_FILE)

            if 'Protocol' in df.columns:
                protocol_counts = df['Protocol'].value_counts().head(5)
                fig = px.bar(
                    x=protocol_counts.index,
                    y=protocol_counts.values,
                    labels={'x': 'Protocol', 'y': 'Count'},
                    title='Top 5 Protocols',
                    color=protocol_counts.index
                )
                graphJSON = json.dumps({"data": fig.data, "layout": fig.layout}, cls=plotly.utils.PlotlyJSONEncoder)


            packets = df.tail(20).to_dict(orient='records')  # show latest 20 packets

        except Exception as e:
            flash(f"⚠️ Error loading packet data: {e}", "danger")

    return render_template('index.html', graphJSON=graphJSON, packets=packets)

@app.route('/start-sniff', methods=['POST'])
def start_sniff():
    try:
        packet_count = int(request.form.get("packet_count", 20))
        packets = capture_packets(packet_count=packet_count)

        # Count protocol occurrences
        proto_count = {}
        for pkt in packets:
            proto = pkt["Protocol"]
            proto_count[proto] = proto_count.get(proto, 0) + 1



        bar = go.Bar(x=list(proto_count.keys()), y=list(proto_count.values()))
        layout = go.Layout(title="Protocol Distribution", xaxis=dict(title="Protocol"), yaxis=dict(title="Count"))
        graphJSON = json.dumps({"data": [bar], "layout": layout}, default=str)

        flash(f"✅ Captured {len(packets)} packets successfully!", "success")
        return render_template("index.html", packets=packets, graphJSON=graphJSON)

    except Exception as e:
        flash(f"❌ Error during sniffing: {e}", "danger")
        return redirect(url_for("index"))

@app.route('/download-csv', methods=['GET'])
def download_csv():
    if os.path.exists(CSV_FILE):
        return send_file(CSV_FILE, as_attachment=True)
    else:
        flash("⚠️ CSV file not found. Please run the sniffer first.", "warning")
        return redirect(url_for('index'))

@app.route('/api/analyze', methods=['GET'])
def api_analyze():
    try:
        result = analyze_packets()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
