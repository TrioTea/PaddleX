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

from ...base.utils.arg import CLIArgument
from ...base.utils.subprocess import CompletedProcess
from ....utils.misc import abspath
from ..text_rec.model import TextRecModel


class TextDetModel(TextRecModel):
    """ Text Detection Model """

    def infer(self,
              model_dir: str,
              input_path: str,
              device: str='gpu',
              save_dir: str=None,
              **kwargs) -> CompletedProcess:
        """predict image using infernece model

        Args:
            model_dir (str): the directory path of inference model files that would use to predict.
            input_path (str): the path of image that would be predict.
            device (str, optional): the running device. Defaults to 'gpu'.
            save_dir (str, optional): the directory path to save output. Defaults to None.

        Returns:
            CompletedProcess: the result of infering subprocess execution.
        """
        config = self.config.copy()
        cli_args = []

        model_dir = abspath(model_dir)
        cli_args.append(CLIArgument('--det_model_dir', model_dir))

        input_path = abspath(input_path)
        cli_args.append(CLIArgument('--image_dir', input_path))

        device_type, _ = self.runner.parse_device(device)
        cli_args.append(CLIArgument('--use_gpu', str(device_type == 'gpu')))

        if save_dir is not None:
            save_dir = abspath(save_dir)
        else:
            # `save_dir` is None
            save_dir = abspath(os.path.join('output', 'infer'))
        cli_args.append(CLIArgument('--draw_img_save_dir', save_dir))

        model_type = config._get_model_type()
        cli_args.append(CLIArgument('--det_algorithm', model_type))

        self._assert_empty_kwargs(kwargs)

        with self._create_new_config_file() as config_path:
            config.dump(config_path)
            return self.runner.infer(config_path, cli_args, device)