#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tests for Louvain embedding"""
import unittest

import numpy as np

from sknetwork.data.test_graphs import test_graph, test_bigraph
from sknetwork.embedding import LouvainEmbedding


class TestLouvainEmbedding(unittest.TestCase):

    def test_predict(self):
        louvain = LouvainEmbedding()
        louvain.fit(test_graph())
        self.assertEqual(louvain.embedding_.shape[0], 10)
        louvain.fit(test_graph(), force_bipartite=True)
        self.assertEqual(louvain.embedding_.shape[0], 10)

        for method in ['remove', 'merge', 'keep']:
            louvain = LouvainEmbedding(isolated_nodes=method)
            louvain.fit(test_graph())
            embedding_vector = louvain.predict(np.array([1, 0, 0, 0, 1, 1, 0, 0, 0, 1]))
            self.assertEqual(embedding_vector.shape[0], 1)

        for method in ['remove', 'merge', 'keep']:
            bilouvain = LouvainEmbedding(isolated_nodes=method)
            bilouvain.fit(test_bigraph())
            embedding_vector = bilouvain.predict(np.array([1, 0, 0, 0, 1, 1, 0, 1]))
            self.assertEqual(embedding_vector.shape[0], 1)


