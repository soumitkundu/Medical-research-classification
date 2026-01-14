# Medical Research Classification

Small project for classifying medical research documents using machine learning.

## Contents
- `data/` — raw and processed datasets
- `src/` — model and training code
- `models/` — saved model checkpoints

## Setup

Create a virtual environment and install dependencies:

```bash
python -m venv venv
.\\venv\\Scripts\\activate
pip install -r requirements.txt
```

## Usage

Run training or inference scripts in `src/`. Example:

```bash
python src/train.py --config configs/train.yaml
```

## Contributing

Please open issues or pull requests. Follow code style and add tests where appropriate.

## License

This project is available under the MIT License. See `LICENSE` for details.
