# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2024 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
Author: PaddlePaddle Authors
"""
import os
import yaml

from ..ts_base.config import BaseTSConfig
from ....utils.misc import abspath


class TSClassifyConfig(BaseTSConfig):
    """ TS Classify Config """

    def update_dataset(self, dataset_dir: str, dataset_type: str=None):
        """
        upadte the dataset

        Args:
            dataset_dir (str): dataset root path
            dataset_type (str, optional): type to set for dataset. Default='TSDataset'
        """
        if dataset_type is None:
            dataset_type = 'TSCLSDataset'
        dataset_dir = abspath(dataset_dir)
        ds_cfg = self._make_custom_dataset_config(dataset_dir)
        self.update(ds_cfg)

    def update_basic_info(self, info_params: dict):
        """
        update basic info including time_col, freq, target_cols.

        Args:
            info_params (dict): upadte basic info

        Raises:
            TypeError: if info_params is not dict, raising TypeError
        """
        if isinstance(info_params, dict):
            self.update({'info_params': info_params})
        else:
            raise TypeError("`info_params` must be a dict.")

    def _make_custom_dataset_config(self, dataset_root_path: str):
        """construct the dataset config that meets the format requirements

        Args:
            dataset_root_path (str): the root directory of dataset.

        Returns:
            dict: the dataset config.
        """
        ds_cfg = {
            'dataset': {
                'name': 'TSCLSDataset',
                'dataset_root': dataset_root_path,
                'train_path': os.path.join(dataset_root_path, 'train.csv'),
                'val_path': os.path.join(dataset_root_path, 'val.csv'),
            },
        }

        return ds_cfg