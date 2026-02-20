from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

joint_angles = {
    'j1': 0,  # Base rotation
    'j2': 0,  # Shoulder
    'j3': 0,  # Elbow
    'j4': 0,  # Wrist roll
    'j5': 0,  # Wrist pitch
    'j6': 0,  # End effector rotation
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/joints', methods=['GET'])
def get_joints():
    return jsonify(joint_angles)

@app.route('/api/joints', methods=['POST'])
def set_joints():
    data = request.json
    for key, value in data.items():
        if key in joint_angles:
            joint_angles[key] = float(value)
    return jsonify({'status': 'ok', 'joints': joint_angles})

@app.route('/api/reset', methods=['POST'])
def reset_joints():
    for key in joint_angles:
        joint_angles[key] = 0
    return jsonify({'status': 'ok', 'joints': joint_angles})

if __name__ == '__main__':
    app.run(debug=True, port=5000)