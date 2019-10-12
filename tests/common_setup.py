# Copyright (c) 2019 NVIDIA Corporation
import unittest
import os
from tests.context import nemo


class NeMoUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        nemo.core.neural_factory.NeuralModuleFactory.reset_default_factory()
