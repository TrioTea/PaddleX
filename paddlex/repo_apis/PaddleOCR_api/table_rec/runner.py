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
from ..text_rec.runner import TextRecRunner
from ...base.utils.subprocess import CompletedProcess


class TableRecRunner(TextRecRunner):
    """ Table Recognition Runner """

    def predict(self, config_path: str, cli_args: list,
                device: str) -> CompletedProcess:
        """run predicting using dynamic mode

        Args:
            config_path (str): the config file path used to predict.
            cli_args (list): the additional parameters.
            device (str): unused.

        Returns:
            CompletedProcess: the result of predicting subprocess execution.
        """
        cmd = [self.python, 'tools/infer_table.py', '-c', config_path]
        return self.run_cmd(cmd, switch_wdir=True, echo=True, silent=False)

    def infer(self, config_path: str, cli_args: list,
              device: str) -> CompletedProcess:
        """run predicting using inference model

        Args:
            config_path (str): the path of config file used to predict.
            cli_args (list): the additional parameters.
            device (str): unused.

        Returns:
            CompletedProcess: the result of infering subprocess execution.
        """
        cmd = [self.python, 'ppstructure/table/predict_structure.py', *cli_args]
        return self.run_cmd(cmd, switch_wdir=True, echo=True, silent=False)