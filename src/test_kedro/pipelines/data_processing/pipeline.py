"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.6
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_cars


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_cars,
                inputs="cars",
                outputs="preprocessed_cars",
                name="preprocess_cars_node",
            ),
        ]
    )
