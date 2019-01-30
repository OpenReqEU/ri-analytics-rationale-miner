"""
Copyright (C) 2017-2018 Zijad Kurtanovic <kurtanovic@informatik.uni-hamburg.de>

This file is part of URMiner and subject to the terms and conditions defined in
file 'LICENSE.txt', which is part of this source code package.
"""


import logging

from RationalyticsFramework.classifier.ml.configs.classifier_configs_feature import F_TEXT
from RationalyticsFramework.classifier.data.preprocessors.preprocessor_basic import TextPreprocessor
from URMiner.classifier_ur.data.data_provider_factory import URTruthsetHandlerFactory
from URMiner.classifier_ur.ml.classifier import AURClassifierConfig

class URSentenceClassifierConfig(AURClassifierConfig):
    __th = URTruthsetHandlerFactory.ur_sentence()

    def __init__(self):
        super().__init__(self.__th)

    def init_granularity_spec_features(self):
        pass


class URBaselineSentenceClassifierConfig(URSentenceClassifierConfig):
    # def __init__(self):
    #     super().__init__()

    def _activate_features(self):
        logging.debug("activate feature cfg..")

        # activate text-ngram feature id for body-text
        f_text_BODY = self.get_body_fid(F_TEXT)
        self._activate_feature_id(f_text_BODY)

        # update preprocessor parameter for text-ngram feature for body-text
        self.update_feature_preprocessor_params(f_text_BODY, {TextPreprocessor.PARAM_NOPUNCT: True,
                                                            TextPreprocessor.PARAM_NOSTOPS: True,
                                                            TextPreprocessor.PARAM_DOLEMMATIZE: True})


