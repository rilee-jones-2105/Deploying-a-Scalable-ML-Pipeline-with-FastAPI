import numpy as np
import pytest

from ml.model import (
    train_model,
    inference,
    compute_model_metrics,
)


def test_train_model():
    """Test that the model trains successfully and returns a trained model."""

    X_train = np.array([
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5],
    ])

    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)

    assert model is not None
    assert hasattr(model, "predict")


def test_inference():
    """Test that inference returns valid binary predictions."""

    X_train = np.array([
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5],
    ])

    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)

    X_test = np.array([
        [1, 2],
        [4, 5],
    ])

    predictions = inference(model, X_test)

    assert len(predictions) == 2
    assert set(predictions).issubset({0, 1})


def test_model_metrics():
    """Test that precision, recall, and F1 are calculated correctly."""

    y_true = np.array([0, 0, 1, 1])
    predictions = np.array([0, 1, 1, 1])

    precision, recall, fbeta = compute_model_metrics(
        y_true, predictions
    )

    assert precision == pytest.approx(0.6667, abs=0.001)
    assert recall == pytest.approx(1.0)
    assert fbeta == pytest.approx(0.8)
