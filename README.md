# 6-DOF Robot Arm Web Controller

A real-time 3D robotic manipulator simulator built with Flask + Three.js.

## Setup & Run

```bash
pip install flask
python app.py
```

Then open your browser at: http://localhost:5000

## Features

- **6 Degrees of Freedom**: Full control over each joint independently
- **Real-time 3D visualization**: Interactive Three.js renderer
- **Orbit camera**: Click + drag to rotate, scroll to zoom
- **End effector position**: Live XYZ coordinate readout
- **Random pose generator**: Jump to a random configuration
- **Reset**: Return all joints to home position
- **REST API**: Backend stores joint state at `/api/joints`

## Joints

| Joint | DOF Type       | Range       |
|-------|---------------|-------------|
| J1    | Base Rotation  | ±180°      |
| J2    | Shoulder Pitch | ±90°       |
| J3    | Elbow Pitch    | ±135°      |
| J4    | Wrist Roll     | ±180°      |
| J5    | Wrist Pitch    | ±90°       |
| J6    | EE Spin        | ±360°      |

## API Endpoints

- `GET /api/joints` — Get current joint angles
- `POST /api/joints` — Set joint angles (JSON body)
- `POST /api/reset` — Reset all joints to zero
