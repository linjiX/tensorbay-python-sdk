#!/usr/bin/env python3
#
# Copyright 2021 Graviti. Licensed under MIT License.
#
# pylint: disable=invalid-name

"""Dataloader of the Elpv dataset."""

import os

from ...dataset import Data, Dataset
from ...label import Classification

DATASET_NAME = "Elpv"


def Elpv(path: str) -> Dataset:
    """Dataloader of the Elpv dataset.

    Arguments:
        path: The root directory of the dataset.
            The file structure should be like::

                <path>
                    labels.csv
                    images/
                        cell0001.png
                        ...

    Returns:
        Loaded `Dataset` object.

    """
    root_path = os.path.abspath(os.path.expanduser(path))

    dataset = Dataset(DATASET_NAME)
    dataset.load_catalog(os.path.join(os.path.dirname(__file__), "catalog.json"))
    segment = dataset.create_segment()

    csv_path = os.path.join(root_path, "labels.csv")

    with open(csv_path) as csv_file:
        for row in csv_file:
            image_name, attributes, category = row.strip().split()
            dirname, basename = image_name.split("/")
            image_path = os.path.join(root_path, dirname, basename)
            data = Data(image_path)
            data.label.classification = Classification(
                attributes={"defect probability": float(attributes)}, category=category
            )
            segment.append(data)
    return dataset
